"""
RAG 链模块 - 检索增强生成核心逻辑
"""
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage

from config import settings
from rag.vector_store import vector_store_manager
from services.mock_service import mock_service


class RAGChain:
    """RAG 链管理器"""
    
    def __init__(self):
        self._llm = None
        self._qa_chain = None
        self._chat_chain = None
    
    def _get_llm(self):
        """获取大模型实例"""
        if self._llm is None:
            self._llm = ChatOpenAI(
                model=settings.ARK_MODEL,
                openai_api_key=settings.ARK_API_KEY,
                openai_api_base=settings.ARK_BASE_URL,
                temperature=0.7,
                max_tokens=2048,
                request_timeout=60,
                streaming=False
            )
            print(f"✅ 大模型初始化完成: {settings.ARK_MODEL}")
        return self._llm
    
    def _format_docs(self, docs):
        """格式化检索到的文档"""
        if not docs:
            return "暂无参考资料，请基于你的专业知识回答。"
        return "\n\n".join([
            f"【文档 {i+1}】\n标题: {doc.metadata.get('title', '未知')}\n来源: {doc.metadata.get('source', '未知')}\n\n{doc.page_content}"
            for i, doc in enumerate(docs)
        ])
    
    def _safe_retrieve(self, query: str, k: int = 5):
        """安全检索，失败时返回空列表"""
        try:
            results = vector_store_manager.similarity_search(query, k=k)
            return results
        except Exception as e:
            print(f"⚠️  向量库检索失败，使用通用知识生成: {e}")
            return []
    
    def get_qa_chain(self):
        """获取问答链"""
        if self._qa_chain is None:
            llm = self._get_llm()
            
            # 问答 Prompt
            qa_prompt = ChatPromptTemplate.from_messages([
                ("system", """你是火山引擎的资深解决方案专家，精通火山引擎所有产品和行业解决方案。

请根据以下检索到的参考资料，回答用户的问题。

【要求】
1. 回答要专业、准确、有深度
2. 如果参考资料中有相关内容，请基于资料回答
3. 如果资料中没有相关内容，可以基于你的知识回答
4. 回答中要自然地融入火山引擎的产品和方案
5. 结构清晰，重点突出

【参考资料】
{context}
"""),
                ("human", "{question}")
            ])
            
            # 构建链（使用安全检索）
            self._qa_chain = (
                {
                    "context": lambda q: self._format_docs(self._safe_retrieve(q, k=5)),
                    "question": RunnablePassthrough()
                }
                | qa_prompt
                | llm
                | StrOutputParser()
            )
        
        return self._qa_chain
    
    def get_chat_chain(self):
        """获取对话链（支持多轮）"""
        if self._chat_chain is None:
            llm = self._get_llm()
            
            # 对话 Prompt
            chat_prompt = ChatPromptTemplate.from_messages([
                ("system", """你是一名{identity}领域的资深AI销售助手。

你的身份是一名{identity}，精通你所在领域的产品、方案、行业痛点和销售话术。
请完全站在{identity}的角度回答用户的问题。

你的职责是：
1. 解答用户关于你所在行业产品、方案、技术的问题
2. 帮助用户分析业务痛点，推荐合适的解决方案
3. 提供专业的销售建议和话术指导
4. 帮助用户提升销售效率和成单率

【风格要求】
- 专业、自信、有亲和力
- 善于引导用户需求
- 用数据和案例说话
- 自然地突出你所在行业的产品和方案优势

【参考资料】
{context}

请基于参考资料和对话历史回答用户的问题。
"""),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}")
            ])
            
            # 检索器
            retriever = vector_store_manager._get_vector_store().as_retriever(
                search_kwargs={"k": 5}
            )
            
            # 构建链（使用安全检索）
            self._chat_chain = (
                {
                    "context": lambda x: self._format_docs(
                        self._safe_retrieve(x["question"], k=5)
                    ),
                    "question": lambda x: x["question"],
                    "history": lambda x: x.get("history", []),
                    "identity": lambda x: x.get("identity", "云与AI销售")
                }
                | chat_prompt
                | llm
                | StrOutputParser()
            )
        
        return self._chat_chain
    
    def query(self, question: str) -> str:
        """单次问答"""
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式问答")
            return mock_service.query(question)
        
        chain = self.get_qa_chain()
        return chain.invoke(question)
    
    def chat(self, question: str, history: Optional[List] = None, identity: str = "云与AI销售") -> str:
        """多轮对话"""
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式对话")
            return mock_service.chat(question, history)
        
        if history is None:
            history = []
        
        # 转换历史消息格式
        formatted_history = []
        for msg in history:
            if msg.get("role") == "user":
                formatted_history.append(HumanMessage(content=msg["content"]))
            elif msg.get("role") == "assistant":
                formatted_history.append(AIMessage(content=msg["content"]))
        
        chain = self.get_chat_chain()
        return chain.invoke({
            "question": question,
            "history": formatted_history,
            "identity": identity
        })
    
    def chat_stream(self, question: str, history: Optional[List] = None, identity: str = "云与AI销售"):
        """流式多轮对话"""
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式流式对话")
            mock_reply = mock_service.chat(question, history)
            # 模拟逐字输出
            for char in mock_reply:
                yield char
            return
        
        if history is None:
            history = []
        
        # 转换历史消息格式
        formatted_history = []
        for msg in history:
            if msg.get("role") == "user":
                formatted_history.append(HumanMessage(content=msg["content"]))
            elif msg.get("role") == "assistant":
                formatted_history.append(AIMessage(content=msg["content"]))
        
        chain = self.get_chat_chain()
        for chunk in chain.stream({
            "question": question,
            "history": formatted_history,
            "identity": identity
        }):
            yield chunk


# 全局单例
rag_chain = RAGChain()

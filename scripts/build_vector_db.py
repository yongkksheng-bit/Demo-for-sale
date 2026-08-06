"""
构建向量知识库
将爬取的文档处理后存入向量库
"""
import os
import json
import sys
from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from config import settings
from rag.vector_store import vector_store_manager


def load_documents(raw_dir: str = "./data/raw") -> List[Document]:
    """加载原始文档"""
    documents = []
    
    # 遍历所有 json 文件
    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            if not file.endswith(".json"):
                continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # 支持单个文档和文档列表
                if isinstance(data, list):
                    docs = data
                else:
                    docs = [data]
                
                for doc_data in docs:
                    if not doc_data.get("content"):
                        continue
                    
                    doc = Document(
                        page_content=doc_data["content"],
                        metadata={
                            "title": doc_data.get("title", "未知标题"),
                            "source": doc_data.get("url", doc_data.get("source", "未知来源")),
                            "category": doc_data.get("category", "未分类"),
                        }
                    )
                    documents.append(doc)
                    
            except Exception as e:
                print(f"⚠️ 加载文件失败 {filepath}: {e}")
    
    print(f"📄 加载了 {len(documents)} 个文档")
    return documents


def split_documents(documents: List[Document]) -> List[Document]:
    """文档分块"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
    )
    
    splits = text_splitter.split_documents(documents)
    print(f"✂️  分块后共 {len(splits)} 个片段")
    return splits


def build_vector_db():
    """构建向量库"""
    print("🚀 开始构建向量知识库...")
    
    # 1. 加载文档
    documents = load_documents()
    if not documents:
        print("❌ 没有找到文档，请先运行爬虫")
        return
    
    # 2. 文档分块
    splits = split_documents(documents)
    
    # 3. 初始化向量库
    vector_store_manager.initialize()
    
    # 4. 清空旧数据
    try:
        count = vector_store_manager.get_collection_count()
        if count > 0:
            print(f"🗑️  清空旧向量库（{count} 条）")
            vector_store_manager.clear_collection()
    except:
        pass
    
    # 5. 添加到向量库
    vector_store_manager.add_documents(splits)
    
    # 6. 验证
    count = vector_store_manager.get_collection_count()
    print(f"\n✅ 向量库构建完成！")
    print(f"   总片段数: {count}")
    print(f"   保存位置: {settings.VECTOR_DB_PATH}")
    
    # 测试检索
    print("\n🧪 测试检索...")
    results = vector_store_manager.similarity_search("大模型解决方案", k=3)
    print(f"   检索到 {len(results)} 个结果:")
    for i, doc in enumerate(results):
        print(f"   {i+1}. {doc.metadata['title']} - {doc.page_content[:50]}...")


def main():
    build_vector_db()


if __name__ == "__main__":
    main()

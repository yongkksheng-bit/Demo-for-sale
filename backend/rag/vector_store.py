"""
向量库管理模块
"""
import os
from typing import List, Optional
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from config import settings


class VectorStoreManager:
    """向量库管理器"""
    
    def __init__(self):
        self._embeddings = None
        self._vector_store = None
        self._initialized = False
    
    def _get_embeddings(self):
        """获取向量化模型（使用火山方舟API）"""
        if self._embeddings is None:
            print(f"📥 初始化向量化模型: {settings.EMBEDDING_MODEL}")
            self._embeddings = OpenAIEmbeddings(
                model=settings.EMBEDDING_MODEL,
                openai_api_key=settings.ARK_API_KEY,
                openai_api_base=settings.ARK_BASE_URL,
            )
            print("✅ 向量化模型初始化完成")
        return self._embeddings
    
    def _get_vector_store(self):
        """获取向量库实例"""
        if self._vector_store is None:
            embeddings = self._get_embeddings()
            
            # 确保目录存在
            os.makedirs(settings.VECTOR_DB_PATH, exist_ok=True)
            
            self._vector_store = Chroma(
                collection_name=settings.VECTOR_COLLECTION_NAME,
                embedding_function=embeddings,
                persist_directory=settings.VECTOR_DB_PATH
            )
            print(f"✅ 向量库初始化完成: {settings.VECTOR_DB_PATH}")
        return self._vector_store
    
    def initialize(self):
        """初始化向量库"""
        if not self._initialized:
            self._get_vector_store()
            self._initialized = True
    
    def add_documents(self, documents: List[Document]):
        """添加文档到向量库"""
        if not documents:
            return 0
        
        vector_store = self._get_vector_store()
        print(f"📝 正在添加 {len(documents)} 个文档到向量库...")
        
        # 分批添加，避免一次性太多
        batch_size = 50
        total_added = 0
        
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            vector_store.add_documents(batch)
            total_added += len(batch)
            print(f"  已添加 {total_added}/{len(documents)}")
        
        print(f"✅ 文档添加完成，共 {total_added} 个")
        return total_added
    
    def similarity_search(self, query: str, k: int = 5, filter: Optional[dict] = None):
        """相似度检索"""
        vector_store = self._get_vector_store()
        results = vector_store.similarity_search(
            query,
            k=k,
            filter=filter
        )
        return results
    
    def similarity_search_with_score(self, query: str, k: int = 5, filter: Optional[dict] = None):
        """带分数的相似度检索"""
        vector_store = self._get_vector_store()
        results = vector_store.similarity_search_with_score(
            query,
            k=k,
            filter=filter
        )
        return results
    
    def get_collection_count(self):
        """获取集合中文档数量"""
        vector_store = self._get_vector_store()
        return vector_store._collection.count()
    
    def clear_collection(self):
        """清空集合"""
        vector_store = self._get_vector_store()
        vector_store.delete_collection()
        self._vector_store = None
        print("🗑️ 向量库已清空")


# 全局单例
vector_store_manager = VectorStoreManager()

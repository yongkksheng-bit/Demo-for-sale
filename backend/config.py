"""
应用配置模块
"""
import os
from dotenv import load_dotenv

# 加载项目根目录的 .env 文件
_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
load_dotenv(_env_path)


class Settings:
    """应用配置"""
    
    # 火山方舟 API 配置
    ARK_API_KEY: str = os.getenv("ARK_API_KEY", "")
    ARK_BASE_URL: str = os.getenv("ARK_BASE_URL", "https://ark.cn-beijing.volces.com/api/plan/v3")
    ARK_MODEL: str = os.getenv("ARK_MODEL", "ark-code-latest")
    
    # 向量化模型配置
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-zh-v1.5")
    
    # 向量库配置
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "../data/vector_db")
    VECTOR_COLLECTION_NAME: str = os.getenv("VECTOR_COLLECTION_NAME", "volcengine_solutions")
    
    # 应用配置
    APP_NAME: str = os.getenv("APP_NAME", "火山引擎智能方案顾问")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    USE_MOCK: bool = os.getenv("USE_MOCK", "false").lower() == "true"
    
    # 前端配置
    FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "*")


settings = Settings()

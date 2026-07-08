"""
config.py — 统一配置
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Dify 配置
    DIFY_API_BASE = os.getenv("DIFY_API_BASE", "http://localhost/v1")
    DIFY_API_KEY = os.getenv("DIFY_API_KEY", "")

    # 服务配置
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "9000"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "60"))


config = Config()
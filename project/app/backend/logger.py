"""日志模块 - 同时输出到控制台和 app.log 文件"""
import logging
import os
from logging.handlers import RotatingFileHandler
from config import config

# 日志文件路径
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(LOG_DIR, "app.log")

def setup_logger() -> logging.Logger:
    """初始化日志配置"""
    logger = logging.getLogger("app")
    logger.setLevel(getattr(logging, config.LOG_LEVEL))

    if logger.handlers:
        return logger

    # 格式
    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # 控制台输出
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)

    # 文件输出（最大 5MB，保留 3 个备份）
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
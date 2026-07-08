"""会话管理模块 - 存储用户与 AI 的对话上下文"""
from typing import Dict

class ConversationStore:
    """会话存储 - 内存版本（生产环境建议使用 Redis）"""

    def __init__(self):
        self._store: Dict[str, str] = {}

    def get(self, user_id: str) -> str:
        """获取用户的会话 ID"""
        return self._store.get(user_id, "")

    def set(self, user_id: str, conversation_id: str) -> None:
        """保存用户的会话 ID"""
        if conversation_id:
            self._store[user_id] = conversation_id

    def clear(self, user_id: str) -> None:
        """清除用户的会话"""
        self._store.pop(user_id, None)

# 全局单例
conversation_store = ConversationStore()
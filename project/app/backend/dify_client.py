"""
dify_client.py — Dify API 客户端
"""
import requests
from logger import logger
from config import config


class DifyClient:
    """Dify 聊天客户端"""

    def chat(self, query: str, user_id: str, conv_id: str = ""):
        """
        发送消息给 Dify，返回 (回复内容, 新会话ID)
        """
        try:
            resp = requests.post(
                f"{config.DIFY_API_BASE.rstrip('/')}/chat-messages",
                json={
                    "inputs": {},
                    "query": query,
                    "response_mode": "blocking",
                    "user": user_id,
                    "conversation_id": conv_id or ""
                },
                headers={
                    "Authorization": f"Bearer {config.DIFY_API_KEY}",
                    "Content-Type": "application/json"
                },
                timeout=config.REQUEST_TIMEOUT
            )
            resp.raise_for_status()
            data = resp.json()
            answer = data.get("answer", "抱歉，AI 没有返回内容。")
            new_conv_id = data.get("conversation_id", "")
            return answer, new_conv_id

        except requests.exceptions.RequestException as e:
            logger.error(f"请求 Dify 失败: {e}")
            return f"请求失败: {str(e)}", ""
        except Exception as e:
            logger.error(f"Dify 异常: {e}")
            return f"服务器异常: {str(e)}", ""


dify_client = DifyClient()
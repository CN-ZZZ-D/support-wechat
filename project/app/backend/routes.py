"""路由模块 - 定义所有 HTTP 接口"""
import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse

from conversation import conversation_store
from dify_client import dify_client
from logger import logger

router = APIRouter()

# 修复后（正确的）
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")

@router.get("/", response_class=HTMLResponse)
async def home():
    """首页 - 返回聊天界面"""
    html_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>前端页面未找到</h1>"

@router.get("/static/{file_name}")
async def static_file(file_name: str):
    """静态资源访问"""
    file_path = os.path.join(FRONTEND_DIR, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

@router.post("/chat")
async def chat(request: Request):
    """聊天接口"""
    body = await request.json()
    query = body.get("query", "").strip()
    user_id = body.get("user_id", "anonymous")

    if not query:
        return {"answer": "请输入内容"}

    # 获取历史会话
    conv_id = conversation_store.get(user_id)

    # 调用 Dify
    answer, new_conv_id = dify_client.chat(query, user_id, conv_id)

    # 保存新会话
    if new_conv_id:
        conversation_store.set(user_id, new_conv_id)

    return {"answer": answer}

@router.post("/clear")
async def clear_conversation(request: Request):
    """清除会话接口"""
    body = await request.json()
    user_id = body.get("user_id", "anonymous")
    conversation_store.clear(user_id)
    return {"status": "ok", "message": "会话已清除"}
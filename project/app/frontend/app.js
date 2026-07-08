const messagesDiv = document.getElementById('messages');
const input = document.getElementById('input');
const sendBtn = document.getElementById('sendBtn');
const userId = 'test-user-' + Math.random().toString(36).substr(2, 9);

function addMessage(role, content, time) {
    const div = document.createElement('div');
    div.className = 'message ' + role;
    div.innerHTML = `
        <div class="message-content">${escapeHtml(content)}</div>
        <div class="message-time">${time || new Date().toLocaleTimeString()}</div>
    `;
    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

async function send() {
    const text = input.value.trim();
    if (!text) return;

    addMessage('user', text);
    input.value = '';
    sendBtn.disabled = true;
    sendBtn.textContent = '发送中...';

    try {
        const resp = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: text, user_id: userId })
        });
        const data = await resp.json();
        addMessage('assistant', data.answer || '抱歉，没有收到回复');
    } catch (e) {
        addMessage('assistant', '请求失败: ' + e.message);
    } finally {
        sendBtn.disabled = false;
        sendBtn.textContent = '发送';
        input.focus();
    }
}

async function clearConv() {
    if (!confirm('确定要清除当前会话吗？')) return;
    try {
        await fetch('/clear', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        messagesDiv.innerHTML = '';
        addMessage('assistant', '会话已清除，可以开始新的对话');
    } catch (e) {
        alert('清除失败: ' + e.message);
    }
}
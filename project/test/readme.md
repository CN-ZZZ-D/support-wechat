# 测试目录

## 目录结构

```
test/
  backend/       ← 后端测试（与 app/backend 对应）
  frontend/      ← 前端测试（与 app/frontend 对应）
```

## uv 环境初始化

本目录有独立的 uv 虚拟环境，专门用于跑测试。

### 初始化步骤

```powershell
# 进入 test 目录
cd test

# 使用 uv 初始化项目（如尚未初始化）
uv init

# 安装测试依赖（根据需要添加）
uv add pytest

# 激活虚拟环境
.venv\Scripts\activate
```

### 运行测试

```powershell
# 运行所有测试
uv run pytest

# 运行指定目录的测试
uv run pytest backend/
```

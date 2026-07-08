# 全局注意事项

> 每次新建会话时，请让 AI 先读取此文件以了解全局注意事项。

## 环境注意事项

- **PowerShell**：注意 UTF-8 编码问题，如有乱码可尝试设置 `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`
- **路径分隔符**：Windows 使用 `\`，但在代码和配置中建议统一使用 `/`

## 项目规范

- 各功能部件（backend/frontend）自己管理环境，不共享虚拟环境
- test/ 目录有独立的 uv 环境，专门用于跑测试
- 代码改动遵循 `skills/编码要求.md` 中的规范（如有）

## 当前进度

- 当前阶段：01-初始化项目
- 当前 day：day01
- 下一步：用户填写 `docs/想法.md` 和 `docs/环境.md`

## 快速导航

- 项目总览：[readme.md](../readme.md)
- 想法文档：[docs/想法.md](../docs/想法.md)
- 环境文档：[docs/环境.md](../docs/环境.md)
- 方案文档：[docs/方案.md](../docs/方案.md)

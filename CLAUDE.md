# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

"零到全栈"课程学习项目（模块 4.5+）。**前端 Next.js 在 `frontend/`，后端 FastAPI 在它的子目录 `frontend/backend/`**（不是平级目录，别找错）。

网页上的所有文案/内容集中在 `frontend/data/site.js`（数据与界面分离）：组件只负责渲染，`site.js` 提供默认值；后端接口返回后覆盖默认值。

## 每日总结工作流（必须遵守）

每完成一段有意义的工作（修完 bug、跑通功能、学完一课、解决一个困惑），收尾时把**新学到的内容**追加到日记文件：

- **触发条件**：当我说总结上述内容(或者类似的话)的时候
- **路径**：`D:\LL的精神世界\LL的小世界\03_daily\YYYY-MM-DD.md`（按当天日期）
- **硬性要求**：**只做加法**——绝不覆盖、修改该文件已有内容，一律在末尾追加；追加前用 `---` 分隔
- **每节结构**（按这个顺序写）：
  1. **我的问题**：当时想干什么、卡在哪
  2. **根因 / 解释**：为什么（讲清原理，不要流水账）
  3. **我的决策**：最后怎么处理的；如果跟推荐做法不同，标注一下当时的考量
  4. **可复用的命令 / 结论**：下次能直接抄的那种
- **语气**：写给未来的自己看的笔记——具体、可复现，别写场面话

## 常用命令

**前端**（在 `frontend/` 下）：
```bash
npm install
npm run dev       # http://localhost:3000
npm run build
```

**后端**（在 `frontend/backend/` 下）：
```bash
source .venv/Scripts/activate        # 激活 venv（Git Bash）
uv pip install -r requirements.txt   # 装依赖
fastapi dev                          # http://localhost:8000（或 uvicorn main:app --reload）
```

**联调**：后端 8000 + 前端 3000 同时跑；前端用 `.env.local` 里的 `NEXT_PUBLIC_API_BASE_URL=http://localhost:8000` 连后端。

## venv 注意（最容易踩的坑）

- 后端 venv 由 **uv 管理**（`frontend/backend/.venv`，Python 3.11），**里面没有 pip**。
- 装包：`uv pip install <包名>`，装完**手动加一行**到 `frontend/backend/requirements.txt`（pip/uv 都不会自动更新它）。
- **不要用 `pip`**：即使激活了 venv，`pip` 也会落到系统 Python（E:\python，3.13）——因为 uv venv 不带 pip，PATH 会漏出去。判断命令指向：`which python` / `which pip`。
- 解释器固定为 `frontend/backend/.venv/Scripts/python.exe`，已在 `frontend/.vscode/settings.json` 和 `.vscode/settings.json` 配置。Pylance 报"无法解析导入"时先确认解释器选对 + `Developer: Reload Window`。
- **根目录 `2026/requirements.txt` 是过时副本**，以后端 `frontend/backend/requirements.txt` 为准。

## 架构

**前后端数据流**：
- `GET /api/profile`：主页数据。`HomeView` 进页面时 `useEffect` fetch，失败则保留 `site.js` 默认值（页面不崩）。
- `POST /api/analyze`：文字分析。`InputCard` 发请求，结果经父组件 `TextLabView` 的 state（状态提升）传给 `ResultCard`。后端目前是占位实现，`pinyin` 字段写着"（模块 6 再说）"。

**路由与组件**（Next.js 15 App Router，React 19）：
- `app/` 文件夹即路由：`page.jsx`（/）→ HomeView，`text-lab/page.jsx`（/text-lab）→ TextLabView；`layout.jsx` 是全站外壳并 import 8 个 CSS。
- 交互组件是 client 组件（`"use client"`）：Nav、InputCard、ResultCard、AnimatedCardGrid、TextLabView、HomeView。
- 设计系统在 `css/`（variables/reset/layout/hero/cards/nav/lab/responsive）。

**后端 CORS**：`main.py` 只放行 `http://localhost:3000`。改了前端端口或加新前端来源，要同步改这里。

## 约定

- 改前端文案只动 `data/site.js`，组件代码不用碰。
- 新增 Python 依赖：装进 venv + 手动同步 `frontend/backend/requirements.txt`。

# Python Basics｜Examiner Victoria AI 产品原型练习

这个仓库用于记录我围绕 **Examiner Victoria｜AI IELTS Speaking Coach** 补齐 Python、API、前端接口联调与产品原型能力的学习过程。

它不是算法刷题仓库，也不是把自己包装成成熟后端 / 全栈开发者的项目仓库。  
它的目标是：用可运行的小练习，逐步理解一个 AI 产品原型从题库、用户输入、接口请求、后端判断、响应结构，到前端状态和反馈展示的基本链路。

---

## 1. 学习定位

我的主线方向是：

- AI 产品原型
- AI 工具产品
- AI 交互设计
- Agent / Vibe Coding 产品实践
- 可运行 Demo 的需求拆解与迭代

这个仓库对应的能力重点不是“写复杂算法”，而是：

- 看懂并修改基础 Python 代码
- 理解题库、练习记录、接口契约等数据结构
- 理解 API（Application Programming Interface，应用程序接口）请求与响应
- 理解 JSON（JavaScript Object Notation，轻量级数据交换格式）在前后端之间的作用
- 用 FastAPI 搭建基础后端接口
- 用 HTML（HyperText Markup Language，超文本标记语言）和 JavaScript 的 `fetch` 完成前端调用后端
- 将原始接口返回结果，逐步转化为用户可理解的产品化反馈界面

---

## 2. 与 Examiner Victoria 的关系

Examiner Victoria 是一个 AI 雅思口语陪练产品原型。  
这个仓库是它的技术底座练习仓库，主要服务于以下产品链路：

```text
题库数据
  ↓
用户看到题目
  ↓
用户输入回答
  ↓
前端提交请求
  ↓
后端接收并判断
  ↓
返回 score / feedback / next_action
  ↓
前端展示页面状态和反馈卡片
```

当前练习重点对应 Examiner Victoria 中的这些能力：

- 题库结构化
- 用户回答校验
- 练习记录保存
- API 请求体和响应体设计
- FastAPI 后端接口
- Pydantic 请求模型与响应结构
- 前端 fetch 请求
- loading / error / success 页面状态
- 反馈卡片产品化展示

---

## 3. 当前学习进度

| Day | 文件 | 学习主题 | 对产品原型的意义 |
|---|---|---|---|
| Day 01 | `day01_variables.py` | 变量与产品状态 | 理解当前题目、用户回答、分数、反馈等状态如何被保存 |
| Day 02 | `day02_strings_prompt.py` | 字符串与 Prompt | 理解如何拼接题目、回答和反馈要求 |
| Day 03 | `day03_lists_questions.py` | 列表与题库 | 用列表保存多道题，理解题库的基础结构 |
| Day 04 | `day04_dict_question.py` | 字典与单道题结构 | 用 `part`、`topic`、`text` 描述一张题卡 |
| Day 05 | `day05_if_else_input.py` | if / else 与用户输入判断 | 判断空回答、短回答和有效回答 |
| Day 06 | `day06_loops_questions.py` | 循环与题库遍历 | 批量读取题库，并按条件筛选题目 |
| Day 07 | `day07_functions_flow.py` | 函数与产品流程封装 | 把展示题目、校验回答、生成 Prompt 等动作封装成函数 |
| Day 08 | `day08_file_records.py` | 文件读写与练习记录 | 将练习结果保存到本地文本文件 |
| Day 09 | `day09_json_records.py` | JSON 结构化练习记录 | 用结构化数据保存题目、回答、反馈和分数 |
| Day 10 | `day10_error_safe_read.py` | 异常处理与文件安全读取 | 防止文件不存在或 JSON 格式损坏导致程序崩溃 |
| Day 11 | `day11_api_contract.py` | API 请求与前后端接口 | 理解 request body 和 response body 的接口契约 |
| Day 12 | `day12_fastapi_routes.py` | FastAPI 基础：路由与接口 | 启动本地后端服务，创建基础接口 |
| Day 13 | `day13_pydantic_schema.py` | Pydantic 请求模型与响应结构 | 用模型规范接口输入和输出 |
| Day 14 | `day14_api_backend.py` / `day14_frontend_fetch.html` | 前端调用后端接口 | 用前端页面提交回答，并接收后端返回 |
| Day 15 | `day15_frontend_states.html` | 前端页面状态 | 区分 idle、loading、success、error 等页面状态 |
| Day 16 | `day16_frontend_validation.html` | 前端输入校验 | 在提交前判断空回答和短回答，减少无效请求 |
| Day 17 | `day17_feedback_cards.html` | 产品化反馈卡片 | 将原始 JSON 返回结果展示为更接近真实产品的反馈卡片 |

---

## 4. 当前文件说明

```text
python_basics/
├── README.md
├── .gitignore
├── day01_variables.py
├── day02_strings_prompt.py
├── day03_lists_questions.py
├── day04_dict_question.py
├── day05_if_else_input.py
├── day06_loops_questions.py
├── day07_functions_flow.py
├── day08_file_records.py
├── day09_json_records.py
├── day10_error_safe_read.py
├── day11_api_contract.py
├── day12_fastapi_routes.py
├── day13_pydantic_schema.py
├── day14_api_backend.py
├── day14_frontend_fetch.html
├── day15_frontend_states.html
├── day16_frontend_validation.html
├── day17_feedback_cards.html
├── practice_record.txt
└── practice_records.json
```

---

## 5. 运行方式

### 5.1 运行普通 Python 练习

在 VS Code Terminal 或 PowerShell 中进入项目目录：

```powershell
cd D:\Software\Python\python_basics
```

运行某一天的 Python 文件：

```powershell
python day01_variables.py
```

例如：

```powershell
python day09_json_records.py
```

---

### 5.2 安装 FastAPI 和 Uvicorn

FastAPI 是 Python 的 Web API 框架。  
Uvicorn 是运行 FastAPI 应用的本地服务器。

```powershell
python -m pip install fastapi uvicorn
```

---

### 5.3 启动后端 API 服务

以 Day 14 的后端接口为例：

```powershell
cd D:\Software\Python\python_basics
python -m uvicorn day14_api_backend:app --reload
```

成功后可以打开：

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/api/health
http://127.0.0.1:8000/docs
```

---

### 5.4 打开前端 HTML 页面

可以直接双击打开这些文件：

```text
day14_frontend_fetch.html
day15_frontend_states.html
day16_frontend_validation.html
day17_feedback_cards.html
```

注意：  
如果前端页面需要调用后端接口，必须先保持 Uvicorn 后端服务运行。

---

## 6. Git / GitHub 使用方式

这个文件夹已经初始化为 Git 本地仓库，并连接到 GitHub 远程仓库。

日常流程：

```text
修改代码
  ↓
保存文件
  ↓
在 VS Code Source Control 中 Stage
  ↓
Commit
  ↓
Sync / Push 到 GitHub
```

也可以使用终端：

```powershell
git status
git add .
git commit -m "Add Python basics practice Day 18"
git push
```

概念区分：

```text
Git = 本地版本控制工具
GitHub = 远程代码托管平台
Commit = 在本地保存一次版本记录
Push = 把本地版本上传到 GitHub
```

---

## 7. 后续学习计划

接下来不急着学复杂框架，先继续围绕 Examiner Victoria 的产品功能链路补齐基础。

| 后续 Day | 计划主题 | 学习目标 |
|---|---|---|
| Day 18 | 前端样式基础：CSS 卡片、间距与布局 | 让反馈卡片更像真实产品界面 |
| Day 19 | 题库数据接入：从数组 / JSON 读取题目 | 让页面不只展示固定题目 |
| Day 20 | 下一题逻辑：next_question 与练习流程 | 理解从一道题进入下一道题的状态切换 |
| Day 21 | 浏览器本地存储：localStorage | 保存用户练习记录和页面状态 |
| Day 22 | 后端文件拆分与项目结构 | 从单文件练习过渡到更清晰的项目结构 |
| Day 23 | 前后端联调小 MVP | 整合题目展示、回答提交、反馈展示 |
| Day 24 | 错误处理与接口兜底 | 处理后端未启动、输入异常、接口返回异常 |
| Day 25 | 项目说明与作品集整理 | 把练习沉淀成可放进作品集的技术说明 |

React、Vite、Electron、LangChain、Agent 框架等内容可以后置。  
当前优先级仍然是：先把 Python、API、JSON、FastAPI、前端请求、页面状态这些基础链路讲清楚、跑通、能复述。

---

## 8. 面试中可以如何描述这个仓库

可以这样说：

> 这个仓库是我围绕 Examiner Victoria 这个 AI 雅思口语陪练项目补齐技术底座的学习记录。它不是算法刷题仓库，而是按真实 AI 产品原型链路来练习：从题库结构、用户回答校验、JSON 练习记录，到 FastAPI 接口、Pydantic 请求模型、前端 fetch 联调、页面状态和反馈卡片展示。我的目标是能更好地和 AI Coding Agent 协作，理解产品功能背后的数据结构和接口逻辑，并能独立做出可运行的 AI 产品 MVP。

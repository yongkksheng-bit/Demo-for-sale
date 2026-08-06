# 火山引擎智能方案顾问 🚀

> AI 驱动的销售方案生成引擎，30秒生成一份专业级解决方案建议书

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688)
![LangChain](https://img.shields.io/badge/LangChain-0.3-FF6B6B)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3-38B2AC)

## ✨ 项目简介

火山引擎智能方案顾问是一个面向销售场景的 AI 工具，基于火山方舟大模型，能够根据行业和业务场景，一键生成专业的解决方案建议书。

**核心价值：**
- ⚡ **效率提升 10 倍**：从几小时缩短到几十秒
- 🎯 **专业精准**：基于火山引擎官方产品体系，内容专业可靠
- 🎨 **开箱即用**：精美 UI，一键部署，立即可用

## 🎯 核心功能

### 1. 智能方案生成
- 支持 **8 大行业** × **5 大场景**，覆盖零售、金融、制造、汽车、教育、医疗、文旅、政企
- 一键生成完整的解决方案建议书，包含行业分析、方案架构、产品组合、实施路径、ROI 估算
- 支持定制化需求，灵活调整方案

### 2. 智能对话顾问
- 7×24 小时 AI 销售顾问，解答产品、方案、技术问题
- 支持多轮对话，上下文理解
- 专业的销售话术，自然引导客户需求

### 3. 销售工具箱
- **销售话术生成**：根据行业和场景，生成专业的销售拜访话术
- **异议处理助手**：针对客户常见异议，生成专业的应对话术
- 更多工具开发中...

## 🛠️ 技术栈

### 后端
- **FastAPI** - 高性能 Python Web 框架
- **LangChain** - LLM 应用开发框架
- **Chroma** - 本地向量数据库（RAG 检索增强）
- **Pydantic** - 数据验证
- **Uvicorn** - ASGI 服务器

### 前端
- **Tailwind CSS** - 原子化 CSS 框架
- **原生 JavaScript** - 无框架依赖，轻量高效
- **Marked.js** - Markdown 渲染
- **Font Awesome** - 图标库

### AI 能力
- **火山方舟大模型** - 字节跳动自研大模型（Doubao 系列）
- **RAG 检索增强生成** - 基于知识库的精准回答
- **支持向量化模型** - 可选，用于知识库检索

## 📸 功能截图

### 首页
![首页](docs/screenshots/home.png)

### 方案生成
![方案生成](docs/screenshots/solution.png)

### 智能对话
![智能对话](docs/screenshots/chat.png)

### 销售工具箱
![销售工具箱](docs/screenshots/tools.png)

## 🚀 快速开始

### 环境要求
- Python 3.10+
- 火山方舟 API Key（[免费注册](https://www.volcengine.com/product/ark)）

### 1. 克隆项目
```bash
git clone https://github.com/your-username/volcengine-solution-consultant.git
cd volcengine-solution-consultant
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
复制 `.env.example` 为 `.env`，并填写你的 API Key：
```bash
cp .env.example .env
```

编辑 `.env` 文件：
```env
# 火山方舟 API 配置
ARK_API_KEY=your-api-key-here
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/plan/v3
ARK_MODEL=ark-code-latest

# 应用配置
APP_NAME=火山引擎智能方案顾问
APP_VERSION=1.0.0
DEBUG=false

# Mock 模式（不需要 API Key 也能演示）
USE_MOCK=false
```

### 4. 启动后端
```bash
cd backend
python main.py
```

后端将在 `http://localhost:8000` 启动。

### 5. 打开前端
直接用浏览器打开 `frontend/index.html` 即可。

或者使用任意静态文件服务器：
```bash
cd frontend
python -m http.server 8080
```

然后访问 `http://localhost:8080`。

## 📁 项目结构

```
volcengine-solution-consultant/
├── backend/                    # 后端代码
│   ├── main.py                 # FastAPI 主入口
│   ├── config.py               # 配置管理
│   ├── rag/                    # RAG 检索增强模块
│   │   ├── vector_store.py     # 向量库管理
│   │   └── chain.py            # RAG 链
│   ├── services/               # 业务服务层
│   │   ├── solution_service.py # 方案生成服务
│   │   └── mock_service.py     # Mock 服务（演示用）
│   └── models/                 # 数据模型
│       └── schemas.py          # Pydantic 模型
├── frontend/                   # 前端代码
│   ├── index.html              # 主页面
│   └── app.js                  # 前端逻辑
├── data/                       # 数据目录
│   ├── raw/                    # 原始数据
│   └── vector_db/              # 向量数据库
├── scripts/                    # 工具脚本
│   ├── crawl_volcengine.py     # 官网爬虫
│   └── build_vector_db.py      # 向量库构建
├── docs/                       # 文档
│   └── screenshots/            # 截图
├── requirements.txt            # Python 依赖
├── .env.example                # 环境变量模板
└── README.md                   # 项目说明
```

## 🧠 RAG 知识库

本项目支持 RAG（检索增强生成），可以基于火山引擎官方文档生成更准确的方案。

### 构建知识库
1. 运行爬虫抓取火山引擎官网文档：
```bash
python scripts/crawl_volcengine.py
```

2. 构建向量数据库：
```bash
python scripts/build_vector_db.py
```

> 注意：需要向量化模型支持。Agent Plan 套餐暂不支持向量化模型，可升级套餐或使用其他向量化服务。

## 🐳 Docker 部署

### 使用 Docker Compose 一键部署
```bash
docker-compose up -d
```

### 手动构建
```bash
# 构建后端镜像
cd backend
docker build -t solution-consultant-backend .

# 运行
docker run -p 8000:8000 --env-file .env solution-consultant-backend
```

## 🔮 未来规划

- [ ] **流式输出** - 支持方案生成的流式输出，边生成边显示
- [ ] **方案历史** - 保存生成历史，支持查看和管理
- [ ] **导出功能** - 支持导出为 PDF、Word 等格式
- [ ] **更多工具** - 增加竞品对比、ROI 计算器等销售工具
- [ ] **用户系统** - 支持多用户、团队协作
- [ ] **移动端适配** - 优化手机端体验
- [ ] **插件系统** - 支持第三方插件扩展

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- [火山引擎](https://www.volcengine.com/) - 提供强大的云服务和 AI 能力
- [LangChain](https://www.langchain.com/) - 优秀的 LLM 应用开发框架
- [FastAPI](https://fastapi.tiangolo.com/) - 高性能 Python Web 框架
- [Tailwind CSS](https://tailwindcss.com/) - 优雅的 CSS 框架

---

**如果这个项目对你有帮助，欢迎点个 Star ⭐ 支持一下！**

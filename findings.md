# 研究发现与知识库

## 火山引擎产品体系
*(待补充)*

## 行业解决方案
*(待补充)*

## 技术选型决策

### 大模型 API
- **选择**: 火山方舟 Agent Plan Small 套餐
- **原因**: 
  - 用户已购买，直接可用
  - 面试时说"用火山引擎做的火山引擎销售工具"，叠buff
  - 兼容 OpenAI 接口协议，迁移成本低
  - Base URL: https://ark.cn-beijing.volces.com/api/plan/v3

### RAG 框架
- **选择**: LangChain + Chroma
- **原因**:
  - LangChain 生态成熟，文档多
  - Chroma 是本地向量库，零部署，适合快速原型
  - vibe coding 速度快

### 后端框架
- **选择**: FastAPI
- **原因**:
  - 性能好，异步支持
  - 自动生成 API 文档
  - Python 生态，和 RAG 模块无缝衔接

### 前端方案
- **选择**: 纯 HTML + Tailwind CSS + 原生 JS
- **原因**:
  - 可以做得很漂亮，面试展示效果好
  - 无需构建工具，直接打开就能用
  - 部署简单，静态文件即可
  - Vercel/Netlify 一键部署

## 面试展示策略
1. 简历里放在线 Demo 链接 + GitHub 链接
2. 面试时现场 demo，输入一个行业，30秒生成方案
3. 讲解技术架构和设计思路
4. 延伸讨论：如果给火山引擎销售团队用，还可以加什么功能

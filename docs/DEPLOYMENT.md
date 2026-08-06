# 部署指南 🚀

> 如何将火山引擎智能方案顾问部署到线上

## 📋 目录
- [本地 Docker 部署](#本地-docker-部署)
- [前端部署到 Vercel](#前端部署到-vercel)
- [后端部署到 Render](#后端部署到-render)
- [环境变量配置](#环境变量配置)
- [常见问题](#常见问题)

---

## 🐳 本地 Docker 部署

### 前置要求
- Docker 已安装并运行
- docker-compose 已安装

### 快速启动

1. **克隆项目**
```bash
git clone https://github.com/yongksheng-bit/Demo-for-sale.git
cd Demo-for-sale
```

2. **配置环境变量**
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API Key
```

3. **一键启动**
```bash
docker-compose up -d
```

4. **访问应用**
- 前端：http://localhost
- 后端：http://localhost:8000
- API 文档：http://localhost:8000/docs

5. **停止服务**
```bash
docker-compose down
```

---

## 🌐 前端部署到 Vercel（推荐）

### 为什么选 Vercel？
- ✅ 完全免费（个人项目）
- ✅ 自动 HTTPS
- ✅ 全球 CDN 加速
- ✅ 推送代码自动部署
- ✅ 1 分钟搞定

### 部署步骤

#### 方法一：GitHub 集成（推荐）

1. **注册 Vercel 账号**
   - 访问 https://vercel.com
   - 用 GitHub 账号登录

2. **导入项目**
   - 点击 "Add New" → "Project"
   - 选择你的 GitHub 仓库
   - 点击 "Import"

3. **配置项目**
   - **Framework Preset**: 选 `Other`
   - **Root Directory**: 填 `frontend`
   - **Build Command**: 留空（纯静态文件）
   - **Output Directory**: 留空或填 `.`

4. **修改前端 API 地址**
   - 把 `frontend/app.js` 里的 `API_BASE_URL` 改成你的后端地址
   - 例如：`const API_BASE_URL = 'https://your-backend.onrender.com/api/v1'`

5. **部署**
   - 点击 "Deploy"
   - 等待 1-2 分钟
   - 部署完成后会给你一个域名，如 `your-app.vercel.app`

#### 方法二：手动上传

1. 把 `frontend` 文件夹打包
2. 直接拖到 Vercel 仪表盘
3. 完成！

---

## ⚙️ 后端部署到 Render（推荐）

### 为什么选 Render？
- ✅ 免费额度够用（演示足够）
- ✅ 支持 Docker 部署
- ✅ 自动 HTTPS
- ✅ 推送代码自动部署

### 部署步骤

#### 方法一：Docker 部署（推荐）

1. **注册 Render 账号**
   - 访问 https://render.com
   - 用 GitHub 账号登录

2. **创建 Web Service**
   - 点击 "New" → "Web Service"
   - 选择你的 GitHub 仓库
   - 点击 "Connect"

3. **配置服务**
   - **Name**: 随便起，如 `volcengine-solution-backend`
   - **Region**: 选离你近的，如 `Singapore`
   - **Branch**: `main`
   - **Runtime**: 选 `Docker`
   - **Dockerfile Path**: `backend/Dockerfile`
   - **Instance Type**: 选 `Free`（免费额度）

4. **配置环境变量**
   点击 "Advanced" → "Add Environment Variable"，添加：
   ```
   ARK_API_KEY=你的火山方舟API Key
   ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/plan/v3
   ARK_MODEL=ark-code-latest
   USE_MOCK=false
   DEBUG=false
   ```

5. **部署**
   - 点击 "Create Web Service"
   - 等待 5-10 分钟（第一次构建比较慢）
   - 部署完成后会给你一个域名，如 `your-app.onrender.com`

#### 注意事项
- ⚠️ 免费版 15 分钟无请求会休眠，第一次访问会慢一点（几秒钟）
- ⚠️ 免费版每月有 750 小时额度，个人演示完全够用
- 💡 可以用监控工具定时请求，防止休眠

---

## 🔑 环境变量配置

### 必需变量
| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `ARK_API_KEY` | 火山方舟 API Key | `ark-xxxxx` |
| `ARK_BASE_URL` | API 地址 | `https://ark.cn-beijing.volces.com/api/plan/v3` |
| `ARK_MODEL` | 模型名称 | `ark-code-latest` |

### 可选变量
| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `USE_MOCK` | 是否使用 Mock 模式 | `false` |
| `DEBUG` | 是否开启调试模式 | `false` |
| `EMBEDDING_MODEL` | 向量化模型 | `doubao-embedding` |
| `VECTOR_DB_PATH` | 向量库路径 | `../data/vector_db` |

---

## ❓ 常见问题

### Q: 部署后前端连不上后端？
A: 检查以下几点：
1. 前端的 `API_BASE_URL` 是否改成了后端的线上地址
2. 后端是否启动成功（看 Render 日志）
3. 后端端口是否正确（8000）
4. 有没有跨域问题（CORS 已经默认允许所有来源）

### Q: 生成很慢怎么办？
A: 
1. 免费版服务器性能有限，这是正常的
2. 可以升级到付费版，速度会快很多
3. 演示的时候可以先用 Mock 模式，秒出结果

### Q: API Key 会不会泄露？
A: 
- Render 的环境变量是安全的，不会暴露
- 不要把 API Key 写在前端代码里
- 不要把 .env 文件提交到 GitHub

### Q: 能不能用阿里云/腾讯云服务器？
A: 当然可以！
1. 买一台云服务器（1核2G 足够）
2. 安装 Docker
3. 用 docker-compose 一键部署
4. 配置域名和 HTTPS

---

## 📊 成本估算

### 免费方案（推荐演示用）
- 前端：Vercel 免费版 - ¥0
- 后端：Render 免费版 - ¥0
- 大模型：火山方舟免费额度 - ¥0
- **总计：¥0/月**

### 低成本方案（长期使用）
- 前端：Vercel 免费版 - ¥0
- 后端：Render 入门版 - $7/月（约 ¥50/月）
- 大模型：火山方舟按量付费 - 看使用量
- **总计：约 ¥50-100/月**

---

## 🎯 部署检查清单

部署完成后，检查以下内容：

- [ ] 前端页面能正常打开
- [ ] 后端健康检查接口正常（/health）
- [ ] 方案生成功能正常
- [ ] 智能对话功能正常
- [ ] 销售工具箱功能正常
- [ ] HTTPS 正常（地址栏有小锁）
- [ ] 移动端显示正常
- [ ] API Key 没有泄露

---

## 🆘 获取帮助

如果部署遇到问题：
1. 看 Render/Vercel 的日志
2. 检查环境变量是否正确
3. 本地 Docker 先跑通，再部署到线上
4. 搜索错误信息

祝你部署顺利！🎉

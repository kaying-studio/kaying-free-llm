# 每日免费大模型网站

基于 GitHub Actions 定时构建的免费大模型聚合网站，每日自动获取并展示 OpenRouter、硅基智能、智谱 AI 等提供商的免费模型。

## 功能特性

- 🕐 **定时更新**: 每日 5 点自动获取最新免费模型
- 🔍 **智能搜索**: 支持按模型名称搜索
- 🏷️ **分类筛选**: 按提供商筛选模型
- 📊 **统计展示**: 实时显示各提供商模型数量
- 📱 **响应式设计**: 支持移动端和桌面端
- 🎨 **友好界面**: 现代化 UI 设计

## 项目结构

```
kaying-free-llm/
├── .github/workflows/
│   └── fetch-models.yml    # GitHub Actions 工作流
├── data/
│   └── free_models.json    # 模型数据文件（自动生成）
├── fetch_models.py          # 模型获取脚本
├── index.html              # 网站主页
├── requirements.txt        # Python 依赖
├── .env.example           # 环境变量模板
└── README.md              # 项目说明
```

## 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd kaying-free-llm
```

### 2. 配置 API 密钥

复制环境变量模板并填入你的 API 密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入以下 API 密钥：

- **OpenRouter API Key**: 从 https://openrouter.ai/keys 获取
- **SiliconFlow API Key**: 从 https://cloud.siliconflow.cn/ 获取
- **Zhipu AI API Key**: 从 https://open.bigmodel.cn/ 获取

### 3. 本地运行

安装依赖并运行脚本：

```bash
pip install -r requirements.txt
python fetch_models.py
```

然后在浏览器中打开 `index.html` 查看结果。

### 4. GitHub 部署

1. 将项目推送到 GitHub 仓库
2. 在仓库设置中添加以下 Secrets：
   - `OPENROUTER_API_KEY`
   - `SILICONFLOW_API_KEY`
   - `ZHIPU_API_KEY`
3. GitHub Actions 将自动在每日 5 点运行

## 支持的提供商

### OpenRouter
- API 文档: https://openrouter.ai/docs
- 免费模型: 通过 pricing 字段识别免费模型

### 硅基智能 (SiliconFlow)
- API 文档: https://docs.siliconflow.cn/
- 免费模型: 通过模型名称中的关键字识别

### 智谱 AI (Zhipu AI)
- API 文档: https://open.bigmodel.cn/dev/api
- 免费模型: GLM-4-Flash 等免费模型

## 数据格式

模型数据以 JSON 格式存储在 `data/free_models.json`：

```json
{
  "updated_at": "2024-01-01T00:00:00",
  "total_count": 50,
  "models": [
    {
      "provider": "OpenRouter",
      "id": "model-id",
      "name": "Model Name",
      "description": "Model description",
      "context_length": 4096,
      "pricing": {
        "prompt": "0",
        "completion": "0"
      }
    }
  ]
}
```

## 技术栈

- **后端**: Python 3.11, Requests
- **前端**: HTML5, Tailwind CSS, JavaScript (ES6+)
- **CI/CD**: GitHub Actions
- **部署**: GitHub Pages

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 发起 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请提交 Issue 或联系开发者。

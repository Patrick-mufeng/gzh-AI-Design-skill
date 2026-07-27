# gzh-AI-Design · 公众号 AI 排版引擎

> 输入 Markdown → AI 自动设计主题 → 生成公众号兼容 HTML → 手机框预览 → 一键复制到公众号 / 推送到草稿箱

**纯知识驱动，不依赖任何后端服务。**

---

## 特性

- **📝 Markdown → 公众号 HTML** — AI 自动将文章转为微信兼容的排版
- **🎨 6 套设计语言** — 极简蓝 / 暖纸墨 / 暗夜青 / 森语绿 / 绯红编 / 墨金雅，每篇文章独一无二
- **🤖 AI 全原创模式** — 不套预设，AI 根据文章内容自主设计整套视觉方案
- **📱 手机框预览** — 双击 output-preview.html 即可在模拟手机中预览排版效果
- **📋 一键复制到公众号** — 点击即复制富文本，公众号后台 Ctrl+V 粘贴
- **📐 宽度切换** — 375 / 390 / 414 px 三种手机宽度对比
- **🔄 迭代编辑** — 排版后不满意，直接对 AI 说"标题颜色改深"，无需重新生成
- **🚀 微信 API 推送** — 配置凭证后自动推送到公众号草稿箱（可选）
- **✅ 自动校验** — 生成后跑 `validate_gzh_html.py` 确保合规

---

## 使用方式

### 方式一：AI 编码助手（Claude Code / Cursor / Codex / ZCode）

将 `gzh-AI-Design-skill/` 放入项目目录，对 AI 说：

```
帮我排版：今天写了一篇关于……的文章……
或：排版 + 推送 一条龙搞定
```

### 方式二：通用对话型 AI（ChatGPT / Kimi / 豆包 / Gemini）

直接复制核心规则作为 prompt 前缀。

### 方式三：纯手动（不需要 AI）

用 Markdown 写好文章，参考规范自行编写公众号兼容 HTML。

---

## 命令速查

| 你说 | 做什么 |
|------|--------|
| "帮我排版" / "排版" / "AI排版" / "公众号排版" | Markdown → 发布 HTML |
| "推送" / "推到公众号" | 推送到公众号草稿箱（需微信凭证） |
| "一条龙" | 排版 + 推送 全自动 |
| "标题颜色改深" / "间距太大" | 增量修改已生成的排版 |

---

## 凭证配置（推送功能）

在项目 `.env` 中添加：

```
WECHAT_APPID=wx1234567890
WECHAT_APPSECRET=your-secret
WECHAT_AUTHOR=你的作者名    # 可选
```

获取方式：公众号后台 → 设置与开发 → 基本配置

**未配置不影响排版使用**——推送时自动降级为手动复制粘贴模式。

---

## 文件结构

```
gzh-AI-Design-skill/
├── SKILL.md                              ← 排版 + 推送工作流
├── template-预览.html                     ← 输出预览模板
├── references/                           ← 设计规范
│   ├── spec-01-tags.md                   ← 标签规则
│   ├── spec-02-css.md                    ← CSS 白名单
│   ├── spec-03-components.md             ← 组件配方
│   ├── spec-04-design.md                 ← 色彩系统
│   ├── theme-index.md                    ← 主题索引
│   └── theme-*.md                        ← 6套主题设计语言
├── scripts/
│   ├── validate_gzh_html.py              ← 合规校验
│   └── wechat_push.py                    ← 微信推送
├── examples/
│   └── example-source.md                 ← 示例
└── output/                               ← 生成结果
```

---

## 技术细节

- **零依赖** — 纯 HTML / CSS / JavaScript（校验/推送脚本仅用 Python 标准库）
- **微信公众号深度兼容** — 基于真实公众号文章源码逆向分析的规则集
- **`<span leaf="">` 包裹** — 所有中文文字使用 `leaf=""` 属性保证粘贴后样式完整保留
- **文件协议兼容** — 所有页面均在 `file://` 下工作，无需 HTTP 服务器

---

## 协议

MIT License

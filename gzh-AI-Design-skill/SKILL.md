---
name: gzh-AI-Design-skill
description: "公众号文章 AI 排版 + 推送引擎。输入 Markdown → AI 设计主题 → 生成公众号 HTML → 内置预览 → 推送到公众号草稿箱。6套设计语言+AI全原创模式，每篇文章独一无二。支持微信API推送(需凭证)或手动复制。触发词：帮我排版/排版/AI排版/公众号排版/format/推送/push/推到公众号。"
argument-hint: [article-text or file-path] [— theme: <name>]
allowed-tools: Bash(*), Read, Write, Edit, Glob
---

# gzh-AI-Design · 公众号 AI 排版引擎

你是公众号排版设计师。输入 Markdown 文章 → 分析调性 → 设计主题 → 按规范生成 HTML → 输出预览 → 推送到公众号草稿箱。

**本 skill 自包含——设计规范、主题设计语言、校验脚本、推送脚本全部在 skill 目录内。**

---

## 文件结构

```
gzh-AI-Design-skill/
├── SKILL.md                              ← 本文件（排版 + 推送工作流）
├── template-预览.html                     ← 输出预览模板
├── references/                           ← 设计规范（AI 排版依据）
│   ├── spec-01-tags.md                   ← 标签规则与强制CSS
│   ├── spec-02-css.md                    ← CSS属性完整白名单
│   ├── spec-03-components.md             ← 布局模式与组件配方
│   ├── spec-04-design.md                 ← 色彩系统与设计指南
│   ├── theme-index.md                    ← 6套主题索引
│   ├── theme-{minimal-blue|warm-paper|night-cyan|forest-green|crimson-editorial|ink-gold}.md
│   └── common-components.md              ← 通用组件参考
├── scripts/
│   ├── validate_gzh_html.py              ← HTML合规校验（生成后必跑）
│   └── wechat_push.py                    ← 微信API推送脚本
├── examples/
│   └── example-source.md                 ← 示例 Markdown 输入
└── output/                               ← AI 生成结果目录
```

---

## 工作流总览

```
用户: "帮我排版" / "排版" + 文章
  ↓
Phase 0: 读取文章 + 分析调性
  ↓
Phase 1: 主题选择（A预设 / B自定义 / C AI全原创）
  ↓
Phase 2: 前置阅读 — 强制逐文件读取 4 个设计规范
  ↓
Phase 3: 原创设计 → 生成 HTML
  ↓
Phase 4: 生成预览页 + 脚本校验 + 交付
  ↓
用户: "推送" / "推到公众号"
  ↓
推送工作流（API推送 或 手动复制）
```

### 命令路由

| 用户说 | 执行 |
|--------|------|
| "帮我排版" / "排版" / "AI排版" / "公众号排版" / "format" | Phase 0→4（排版全流程） |
| "推送" / "push" / "推到公众号" / "推送到公众号" | 推送工作流 |
| "一条龙" / "全流程" / "排完就推" | Phase 0→4 + 推送（排版+推送串联） |

---

## 排版工作流

### Phase 0 · 读取 + 内容分析

1. 用户给文件路径 → 读文件；直接粘贴文本 → 直接用；都没给 → 问"文章在哪？"
2. **分析文章内容**（这是后续设计决策的基础）：
   - 判定文章类型：教程/盘点/观点/访谈/数据/随笔/案例
   - 感知文章情绪：冷静分析/激情论证/温暖叙事/权威报告/轻松分享
   - 识别结构特征：是否有代码块、是否有大量数据、是否有金句/引用、图片密度

### Phase 1 · 排版方式选择

```
🎨 排版方式：

A. 预设主题 — 6 套精选设计语言可选
B. 自己描述 — 你来描述想要的排版风格
C. AI 全原创 — 不套预设，AI 根据文章内容自主设计整套视觉方案

选 A / B / C？
```

#### A. 预设主题

**必须先读取 `references/theme-index.md`**，按以下策略推荐：

1. 根据 Phase 0 分析的文章类型/情绪，从 6 套主题中选最契合的 1 个标"推荐"+ 2 个备选
2. 展示给用户一步确认：

```
🎨 选择设计语言：

1. 极简蓝（推荐）— 克制·理性·呼吸感，适合技术教程
2. 暖纸墨 — 温度·杂志感·细线分隔，适合深度观点
3. 暗夜青 — 科技·终端美学，适合数据报告
4. 森语绿 — 自然·侘寂·大留白，适合随笔
5. 绯红编 — 编辑风骨·红白张力，适合作品评测
6. 墨金雅 — 墨色·金饰·经典比例，适合人物特稿

选 1-6？
```

**题材→主题契合参考**（`theme-index.md` 的权威映射）：

| 题材 | 推荐主题 | 理由 |
|------|---------|------|
| 技术教程 / 工具测评 / 知识整理 | 极简蓝 | 克制理性，蓝色锚点引导阅读路径 |
| 观点分析 / 深度思考 / 人文 | 暖纸墨 | 杂志翻阅感，细线分隔营造阅读节奏 |
| 开发技术 / 数据报告 / 产品深潜 | 暗夜青 | 终端美学，数据在暗底上更有冲击力 |
| 随笔 / 生活方式 / 个人反思 | 森语绿 | 大留白给文字呼吸空间 |
| 深度评测 / 行业分析 / 案例复盘 | 绯红编 | 编辑风骨，结构感强化论证逻辑 |
| 人物访谈 / 品牌叙事 / 高端内容 | 墨金雅 | 墨色金饰，经典比例提升内容重量 |

**全自动模式**（用户说"直接排 / 一键 / 不用问"）→ 不提问，自动选默认主题（极简蓝），交付时说明选择理由。

#### B. 自己描述

```
💬 说说你想要的排版感觉：
（例："浅米色底，深咖色字，像读纸书" / "白色底但标题用大红色，段落间距大一点"）
```

收到描述后，AI 自行定义设计变量（主色/底色/气质/节奏），仍需：
- 遵守微信公众号兼容性规则（标签白名单、CSS 安全清单）
- 遵守正文默认参数（字号 14px、行高 1.85）
- 给出设计理念一句话

#### C. AI 全原创设计

**不套任何预设主题**，AI 根据文章内容自主设计整套视觉方案：

1. **分析文章基因**：文章类型 + 情绪调性 + 内容特征（代码多？数据多？金句多？）
2. **定义设计变量**：自选主色/底色/气质关键词/节奏策略
3. **设计每个组件**：从零创作，不参考预设主题
4. **硬约束**（不可突破）：
   - 遵守微信公众号兼容性规则（标签白名单、CSS 安全清单）
   - 遵守正文默认参数（字号 14px、行高 1.85）
   - 所有中文文字 `<span leaf="">` 包裹
   - 颜色对比度 ≥ 4.5:1
5. **软约束**（可突破但需有理由）：60-30-10 配色比例、主色出现 ≤5 处
6. **交付时**：给这套临时方案命名（如"冰岛蓝调"），说明设计理念。用户满意可建议登记为常驻主题

---

### Phase 2 · 前置阅读（强制，逐文件依次读取）

> ⚠️ **以下 4 个规范文件是生成合规 HTML 的唯一规则来源。你必须完整读取每个文件，读完一个再读下一个。不可并行读取，不可跳读。**

```
按顺序依次读取：

1. references/spec-01-tags.md     — 标签规则与强制 CSS
2. references/spec-02-css.md      — CSS 属性完整白名单
3. references/spec-03-components.md — 布局模式与组件配方
4. references/spec-04-design.md   — 色彩系统与设计指南
```

#### 自检：确认已完整读取（读完 4 个文件后必做）

```
📋 设计规范阅读自检：

spec-01-tags.md  ✅ 已读
  → 7 个可用标签：section / p / span / strong / em / img / br
  → 强制属性：box-sizing:border-box + max-width:100%!important
  → <span leaf=""> 包裹铁律已确认

spec-02-css.md   ✅ 已读
  → 5 个最危险的禁用 CSS：position:absolute / animation / calc() / var() / @media
  → flex 是主力布局，grid 仅用于 SVG 绝对定位

spec-03-components.md ✅ 已读
  → 4 种安全布局模式：Flex行/列/左右分栏/Grid叠加
  → 15 个组件模板 + 3 种代码块变体已过目

spec-04-design.md ✅ 已读
  → 颜色值格式：仅 #hex / rgb() / rgba()
  → Do's 清单 8 条 + Don'ts 清单 10 条已确认
  → 头部卡片 4 必须项 + 尾部卡片 3 必须项已确认
```

**如果任何一项无法确认，说明没有完整读取——回到对应文件重新读。**

---

### Phase 3 · 原创设计 → 生成 HTML

> ⚠️ **核心思路**：这是**设计创作**而非模板填充。AI 理解设计语言后，为当前文章进行独一无二的排版设计。
>
> **开始前必读**：
> 1. **选 A（预设主题）** → 读取对应 `references/theme-{标识}.md`（设计变量+设计原则+组件设计模式+设计策略），同时读取 `references/common-components.md`
> 2. **选 B（自己描述）** → 读取 `references/common-components.md`，设计变量从用户描述推导
> 3. **选 C（AI 全原创）** → 读取 `references/common-components.md`，设计变量完全自主定义

#### 设计流程

```
读设计语言 → 理解气质内核
      ↓
分析文章结构 → 识别设计机会（哪里需要锚点/哪里需要节奏打断/哪里需要呼吸）
      ↓
设计每个组件 → 根据文章内容原创形态（组件设计模式是灵感，不是模板）
      ↓
按文章骨架装配 → 全局容器 + 头部卡 + 章节序列 + 尾部卡
      ↓
逐段标注关键词下划线 → 每段 1-3 处
      ↓
检查视觉节奏 → 锚点≤5处 / 段落疏密有致 / 无连续长段落
```

#### 关键设计决策

| 决策点 | 依据 | 自由度 |
|--------|------|--------|
| 代码块深色/浅色 | 主题底色深浅 → 暗底用深色代码块，亮底可用浅色 | 自由选择 |
| 章节标题形态 | 主题设计模式 + 章节数量 → 多章节可用编号卡片，少章节可用左竖条 | 自由演绎 |
| 引用块风格 | 主题气质 + 引用内容长度 → 长引用用左竖条，短金句可居中大字 | 自由选择 |
| 分割线样式 | 主题气质 → 极简用点、温暖用线、科技用符号 | 自由创造 |
| 首段处理 | 文章类型 → 故事型可首字放大，教程型直接进入 | 自由决定 |
| 图片圆角/阴影 | 主题气质 → 圆角 4-12px 范围，阴影 0-8px 深度 | 微调范围 |

#### 微信公众号兼容性规则（核心摘要，设计时对照检查）

##### 标签白名单（仅 7 个）

| 标签 | 用途 | 铁律 |
|------|------|------|
| `<section>` | 唯一块级容器 | 替代 div |
| `<p>` | 段落 | `margin:0px` 强制 |
| `<span>` | 行内文字 | 必须 `<span leaf="">` |
| `<strong>` | 加粗 | |
| `<em>` | 斜体 | |
| `<br>` | 换行 | `<br/>` |
| `<img>` | 图片 | `draggable="false"` |

禁用：div / h1-h6 / table / ul / ol / a / style / link

##### 每条元素必带

```css
box-sizing: border-box;
max-width: 100% !important;
```

##### 正文默认参数

```
字号:14px  行高:1.85  段落间距:8px  letter-spacing:0.3px
```

##### `<span leaf="">` 强制包裹（核心铁律）

**所有含中文的文字节点必须用 `<span leaf="">文字</span>` 包裹**，否则粘贴到公众号编辑器后文字样式会大面积丢失。

```
✅ <p style="font-size:14px"><span leaf="">正文内容</span></p>
❌ <p style="font-size:14px">正文内容</p>
```

##### 平台铁律（不可突破）

- 所有中文文字节点 `<span leaf="">文字</span>` 包裹
- 仅用 `<section>/<p>/<span>/<strong>/<em>/<img>/<br>`
- 禁 `<div>/<h1~h6>/<style>/<table>/<a>`
- 所有 CSS 内联，`box-sizing:border-box;` + `max-width:100%!important;` 每个元素必带
- 正文 14px / 行高 1.85 / 段落间距 8px
- position/float/grid/animation/@media/var()/calc() 禁用

#### 输出文件

保存到 `output/{标题}_{日期}/output.html`

结构：全局容器 `<section>` 包裹全文 + 头部信息卡 + 正文（章节标题+段落+引用+代码+图片）+ 尾部互动卡

---

### Phase 4 · 生成预览 + 校验 + 交付

#### 4.1 生成 output-preview.html

1. 读取 `template-预览.html`，获取自包含预览页的 HTML 骨架
2. 将 Phase 3 生成的 `output.html` 完整内容注入到预览页的 `<script id="article-data" type="text/x-template">` 标签内
3. 保存到 `output/{标题}_{日期}/output-preview.html`

> 注意：如果 HTML 内容中包含 `</script>` 字符串，需替换为 `<\/script>` 防止提前闭合。

#### 4.2 脚本校验（强制）

**必须运行校验脚本**，ERROR 清零才算完成：

```bash
python scripts/validate_gzh_html.py "output/{标题}_{日期}/output.html"
```

| 检查项 | 级别 | 说明 |
|--------|------|------|
| `<style>` / `<script>` / `<div>` / `<link>` 标签 | ERROR | 会被公众号过滤 |
| `class` / `id` 属性 | ERROR | 会被剥离 |
| `position:fixed/absolute/sticky` / `float` | ERROR | 不被支持 |
| `display:grid` / `@media` / `@keyframes` | ERROR | 不被支持 |
| CSS 变量 `var(--x)` | ERROR | 不被支持 |
| `<span leaf="">` 包裹率 | ERROR/WARNING | 中文文本未被包裹 → 粘贴后样式丢失 |
| 半角标点 / 英文引号 | WARNING | 应改为中文全角 |

**失败处理**：ERROR → 回到 Phase 3 修复 → 重新生成 → 重新校验；WARNING 同样修复到 0 再交付。

#### 4.3 自检清单

重读 output.html 补充验证：

- [ ] 文件存在，字节 > 1000
- [ ] 无 `<div>`、`<h1~h6>`、`<style>` 标签
- [ ] 所有样式内联
- [ ] 所有中文文字节点已 `<span leaf="">` 包裹

#### 4.4 交付与预览

保存完成后，立即用命令打开预览页：

- **Windows**: `start output\\{标题}_{日期}\\output-preview.html`
- **macOS**: `open output/{标题}_{日期}/output-preview.html`
- **Linux**: `xdg-open output/{标题}_{日期}/output-preview.html`

```
✅ 排版完成：output/{标题}_{日期}/
  ├── output.html           ← 公众号粘贴用
  └── output-preview.html   ← 手机预览 + 一键复制

手机框内可直接预览效果：
  · 切换宽度 375/390/414 看不同机型效果
  · 点击「📋 复制到公众号」→ 公众号后台 Ctrl+V
  · 拖拽 .html 文件即可加载
```

### 迭代编辑模式

用户对已生成的 HTML 提出修改时（如"标题颜色改深"、"正文间距太大"），**不重新走全套工作流**——直接：

1. 用 Read 打开 `output/` 下对应的 `output.html`
2. 定位需要修改的元素（按用户描述匹配内容/样式）
3. 直接用 Edit 修改相关内联样式
4. 告知用户："已更新，刷新预览页即可见"

**判断标准**：修改范围 ≤ 3 处样式调整 → 增量编辑。修改涉及整体主题或结构调整 → 重新生成。

---

## 推送工作流

> 通过微信公众号 API 将排版后的文章推送到草稿箱。只入草稿箱，不自动群发。
>
> **无凭证时自动降级为手动复制模式**。

### Phase P0 · 检查凭证

检查项目根目录 `.env` 文件是否存在且配置了微信凭证：

```bash
grep -E "^WECHAT_APPID=|^WECHAT_APPSECRET=" .env 2>/dev/null || echo "MISSING"
```

**已配置** → 进入 Phase P1。

**未配置或 .env 不存在** → 进入凭证引导流程：

---

#### 凭证引导（.env 不存在或未配置时执行）

**Step 1: 创建 .env 文件**

```bash
touch .env
```

然后用 Write 写入空模板：

```
WECHAT_APPID=
WECHAT_APPSECRET=
WECHAT_AUTHOR=
```

**Step 2: 引导用户获取凭证**

```
🔑 配置微信公众号推送需要以下信息：

第一步：获取 AppID 和 AppSecret
  1. 登录公众号后台 → https://mp.weixin.qq.com
  2. 左侧菜单 → 设置与开发 → 基本配置
  3. 复制「开发者ID(AppID)」
  4. 点击「开发者密码(AppSecret)」→ 生成并复制
     （AppSecret 只在生成时显示一次，请妥善保存）

第二步：配置 IP 白名单（必须！否则推送会报 40164 错误）
  1. 同一页面 → 「IP 白名单」
  2. 点击「添加」

现在我来帮你查公网 IP：

```bash
curl -s https://ip.sb
```

拿到 IP 后展示给用户：
  3. 将 IP 填入白名单：{查询到的IP}
  4. 提示：这是你当前的公网 IP，如果网络环境变化（如换 WiFi），需重新添加

第三步：填入 .env
  把获取到的值填入项目根目录的 .env 文件：
    WECHAT_APPID=wx1234567890
    WECHAT_APPSECRET=你的32位密钥
    WECHAT_AUTHOR=你的作者名

填好后告诉我，我来确认配置是否正确。
```

**Step 3: 验证配置**

用户填好后，重新运行检查命令：

```bash
grep -E "^WECHAT_APPID=|^WECHAT_APPSECRET=" .env
```

- 两行都有值且 AppID 以 `wx` 开头 → 进入 Phase P1
- 仍是空值 → 提示用户填好后重试，不阻塞（可先手动复制粘贴）

---

**快速参考（已配置但用户忘记来源）**：

| 项目 | 地址 | 做什么 |
|------|------|--------|
| 公众号后台 | https://mp.weixin.qq.com | 设置与开发 → 基本配置 |
| AppID | 基本配置页直接显示 | 以 `wx` 开头的字符串 |
| AppSecret | 点击「生成」后显示一次 | 32 位十六进制密钥 |
| IP 白名单 | 基本配置页 → IP 白名单 | 添加你服务器的公网 IP |
| 查公网 IP | https://ip.sb | 浏览器打开即可看到

### Phase P1 · 确认推送

```
📤 推送到公众号草稿箱

文章：{title}
作者：{WECHAT_AUTHOR 或未设置}
封面：{如有 cover/cover-combined.png}

将推送到公众号草稿箱，不会自动群发。确认？(Y/n)
```

### Phase P2 · 执行推送

```bash
python scripts/wechat_push.py "output/{标题}_{日期}"
```

#### 脚本内部流程

```
① 从 .env 读取 WECHAT_APPID + WECHAT_APPSECRET + WECHAT_AUTHOR
② 从 output.html 读取正文内容
③ 上传正文图片到微信 CDN → 替换本地路径
④ 上传封面（如有 cover/cover-combined.png）为永久素材 → media_id
⑤ POST draft/add → 创建草稿 → 返回 media_id
```

#### 成功输出

```
✅ 推送成功

草稿 media_id：{media_id}
请前往公众号后台 → 草稿箱 查看和群发。
```

#### 失败处理

| 错误码 | 常见原因 | 解决 |
|--------|---------|------|
| 40013 / 40125 | AppID/AppSecret 错误 | 检查 .env 配置 |
| 40164 | IP 未加白名单 | 公众号后台 → 基本配置 → IP白名单 |
| 45166 | HTML 格式不兼容 | 检查 output.html 标签，重新跑 validate_gzh_html.py |
| 网络错误 | 代理/防火墙 | 自动重试 1 次，仍失败提示手动操作 |

**推送失败不阻塞**——用户仍可通过 `output-preview.html` 手动复制粘贴到公众号后台。

### Phase P3 · 自检

| # | 目标 | 验证 |
|---|------|------|
| 1 | 凭证 | WECHAT_APPID + WECHAT_APPSECRET 非空 |
| 2 | 推送结果 | 脚本 stdout 含 `"success": true` + media_id 非空 |
| 3 | 手动模式 | 已提示用户手动操作步骤 |

---

## 核心纪律

1. **先读设计规范再动手**——生成前必须依次读完 4 个 spec 文件
2. **设计创作 > 模板填充**——主题文件提供设计原则和灵感参考，AI 根据每篇文章内容原创演绎
3. **只用 7 个标签**——`<section>/<p>/<span>/<strong>/<em>/<img>/<br>`，其余禁用
4. **所有中文文字节点用 `<span leaf="">文字</span>` 包裹**——否则粘贴后样式大面积丢失
5. **所有 CSS 内联**——无 `<style>` 标签
6. **每个元素必带 `box-sizing:border-box;` + `max-width:100%!important;`**
7. **margin 清零**——所有 `<p>` 设 `margin:0`，段落间用 `margin-bottom:8px`
8. **字号 14px 起**——公众号最小可读字号，行高 1.85
9. **必须跑 `validate_gzh_html.py` 校验**——ERROR 清零才交付
10. **每篇文章排版必须不同**——即使同主题，不同文章应有不同的视觉演绎
11. **推送只入草稿箱**——不自动群发，用户在公众号后台确认后手动发布
12. **凭证缺失不阻塞**——提示手动操作，降级为复制粘贴模式

---

## 升级指南

本 skill 的升级路径：

- **新增主题** → 1) 创建设计语言文件 `references/theme-{标识}.md`（五章节结构：设计变量/设计原则与气质/组件设计模式/文章类型→设计策略/设计决策指南）；2) 在 `references/theme-index.md` 登记；3) 在本文 Phase 1.A 中追加
- **更新设计规范** → 直接替换 `references/spec-*.md` 对应文件
- **新增组件配方** → 更新 `references/spec-03-components.md`
- **推送功能** → `scripts/wechat_push.py` 纯标准库，可直接修改

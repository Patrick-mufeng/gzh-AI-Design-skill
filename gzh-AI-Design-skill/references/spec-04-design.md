> 本文件是微信公众号 HTML 排版规范的 **第 4/4 部分：色彩系统与设计指南**。完整规范由 4 个文件组成，必须依次全部读完。其他部分：spec-01-tags.md / spec-02-css.md / spec-03-components.md
## 第六部分：色彩系统

### 6.1 颜色值格式

```
✅ #hex      — #ffffff, #333, #e5e7eb
✅ rgb()     — rgb(247, 247, 247), rgb(0, 0, 0)
✅ rgba()    — rgba(0, 0, 0, 0.1), rgba(255, 255, 255, 0.93)
❌ hsl()     — 不支持
❌ oklch()   — 不支持
❌ color()   — 不支持
```

### 6.2 推荐的语义色板

```yaml
主题色 (primary):    用于按钮、重点标记、活跃状态
强调色 (accent):     用于加粗文字、引用、步骤编号
背景色 (surface):    文章底色
次背景 (surface2):   卡片底色
边框色 (border):     分割线、卡片描边
正文色 (ink):        主要文字
弱色 (mute):         副文字、标签
```

### 6.3 九套示例主题

#### 🌸 可爱手帐
```
primary: #ff9aa2    accent: #e88a7a
surface: #fffefb    s2: #fffef9    s3: #fff5f5
border: #f0e8d8     ink: #4a3830
mute: #c0b0a0       body: #5a4e42
```

#### 💳 Stripe 金融
```
primary: #533afd    accent: #ff00d4
surface: #ffffff    s2: #f6f9fc    s3: #fff5f7
border: #e6ebf0     ink: #0d253d
mute: #7a8a9a       body: #3c4257
```

#### ⬛ Vercel 极客
```
primary: #171717    accent: #50e3c2
surface: #ffffff    s2: #fafafa    s3: #f5f5f5
border: #ebebeb     ink: #171717
mute: #888888       body: #4d4d4d
```

#### 🍎 Apple 极简
```
primary: #0066cc    accent: #0066cc
surface: #ffffff    s2: #f5f5f7    s3: #fafafc
border: #e0e0e0     ink: #1d1d1f
mute: #7a7a7a       body: #1d1d1f
```

#### 🖌 新中式水墨
```
primary: #8b4513    accent: #8b4513
surface: #fbf9f6    s2: #f8f5ef
border: rgba(139,69,19,0.12)  ink: #2c1f0e
mute: #b0a090       body: #3a3631
```

#### 💜 赛博霓虹
```
primary: #00c8ff    accent: #ff00ff
surface: #0c0c14    s2: rgba(0,200,255,0.04)  s3: rgba(255,0,255,0.04)
border: rgba(0,200,255,0.1)  ink: #e0f0ff
mute: #5a6a8a       body: #b8c4d4
```

#### 🍃 日系侘寂
```
primary: #5a6842    accent: #a0b088
surface: #fafbf8    s2: #f5f6f1    s3: rgba(160,176,136,0.1)
border: #e0e4da     ink: #3a4832
mute: #a0a898       body: #4a5048
```

#### 📰 报刊社论
```
primary: #c44       accent: #c44
surface: #fefcf7    s2: #faf7f0    s3: rgba(204,68,68,0.03)
border: #d0c8b8     ink: #2a2218
mute: #999          body: #2a2218
```

#### ⬜ 极简黑白
```
primary: #000       accent: #000
surface: #ffffff    s2: #fafafa    s3: #f0f0f0
border: #e0e0e0     ink: #1a1a1a
mute: #888          body: #1a1a1a
```

---

## 第七部分：排版尺度

### 7.1 字号层级（基准 14px）

| 层级 | 字号 | 用途 |
|------|------|------|
| 文章标题 | 21-24px | 文首大标题 |
| 章节标题 | 15-17px | 一级分段标题 |
| 卡片标题 | 15px | 强调卡片标题 |
| **正文** | **14px** | **基准正文** |
| 引用文字 | 13-15px | 金句/引用 |
| 辅助说明 | 12-13px | 卡片正文、步骤描述 |
| 小标签 | 9-10px | 徽章、日期、编号 |
| 微型文字 | 9px | badge、label |

### 7.2 行高与字间距

| 场景 | line-height | letter-spacing |
|------|------------|----------------|
| 正文段落 | 1.85 | 0.3px |
| 标题 | 1.3-1.4 | 0.5-1px |
| 引用 | 1.8-1.9 | 0.5px |
| 标签/badge | — | 2px |

### 7.3 间距

| 层级 | margin | 用途 |
|------|--------|------|
| 章节间隔 | 32px 上 | 章节标题上方 |
| 卡片间隔 | 20-24px 上下 | 组件之间 |
| 段落间隔 | 8-10px 上下 | 正文段落 |
| 元素内边距 | 12-20px | 卡片、框内 |

---

## 第八部分：Do's 和 Don'ts

### ✅ 必须做

1. 每个元素写 `style="box-sizing:border-box;"`
2. 每个块级元素写 `max-width:100%!important;`
3. `<p>` 标签写 `margin:0px;padding:0px;`
4. **所有中文文字节点用 `<span leaf="">文字</span>` 包裹**（否则粘贴后样式丢失）
5. 所有 transform 带 4 个厂商前缀
6. 图片使用 `display:block;` 消除底部空隙
7. 容器之间用 `vertical-align:middle;` 或 `top` 对齐
8. flex 子元素写 `flex:0 0 auto;`

### ❌ 禁止做

1. 使用 `<div>` — 永远用 `<section>`
2. 使用 `<style>` 标签 — 100% 内联样式
3. 使用 `position:absolute/fixed/relative`
4. 使用 `animation` / `transition` / `@keyframes`
5. 使用 `vw` / `vh` / `rem` / `calc()` / `var()`
6. 使用外部 CSS 文件
7. transform 只写标准属性不写前缀
8. 图片不写 `display:block;` 导致底部有缝隙
9. 用 `<table>` 做布局 — 用 flex
10. **中文文字不加 `<span leaf="">` 包裹** — 粘贴后样式整片丢失

---

## 第九部分：文章完整结构模板

```html
<section style="width:100%;max-width:677px;background:transparent;padding:0 8px 24px;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;font-size:14px;line-height:1.85;color:#body;letter-spacing:0.3px;box-sizing:border-box;margin:0 auto">

  <!-- 文章头部 -->
  ... (见 5.1)

  <!-- 正文组件 -->
  ... (见第五部分)

  <!-- 尾部卡片 -->
  ... (见 12.2)

</section>
```

---

## 第十部分：暗黑模式与白天模式兼容

微信公众号文章在暗黑模式下会自动适配，但需要注意以下规则：

### 10.1 背景色规则（透明优先）

- **文章容器背景使用 `transparent` 或无背景** — 让微信的默认底色透出，白天模式自然白底，暗黑模式自动变深色
- **卡片底色使用 `rgba(0,0,0,0.03)` ~ `rgba(0,0,0,0.06)`** — 半透明在两种模式下都能看清层次
- **标签按钮和强调元素可使用主题色**
- **文字颜色使用深色 `#1a1a1a` / `#333` / `#555`** — 暗黑模式下自动转为浅色
- **渐变使用透明色停止点** — 如 `linear-gradient(to right, rgba(0,0,0,0.06), transparent)`

### 10.2 图片规则

- 图片不会被反色处理
- 文字截图在暗黑模式下保持原样
- 渐变背景使用 `linear-gradient` 设计卡片层次

### 10.3 注意事项

- 不使用 `@media (prefers-color-scheme: dark)` — 公众号自动处理
- 文字和背景对比度至少 4.5:1
- 白色卡片 + 浅灰文字 = 暗黑模式下也清晰

---

## 第十一部分：AI 内容处理权限

AI 在生成排版时可以适度修改文章内容：

### 11.1 允许的操作

- **提取金句**：从正文中提取最有冲击力的句子，做成引用块或大字居中展示
- **拆分段落**：将长段落拆为短段落，增强阅读节奏
- **添加小标题总结**：为章节添加一句话核心提炼
- **数据可视化**：将数据句包装为数字卡片组件
- **重组顺序**：在不改变逻辑的前提下优化叙事结构
- **浓缩开头**：将文章开头凝练为引人入胜的导语

### 11.2 禁止的操作

- 不得改变事实和数据
- 不得添加原文没有的观点
- 不得删除关键论据
- 不得改变文章立场和结论

### 11.3 原则

保持原意，增强表现力。让文章在公众号中更易读、更有节奏、更美观。

---

## 第十二部分：AI 自由设计头尾卡片

AI 应根据所选主题风格，自由设计文章头部和尾部卡片。

### 12.1 头部卡片（必须包含）

头部卡片应包含以下信息，但设计形式由 AI 根据主题自由发挥：

- 文章字数
- 预计阅读时间
- 话题标签（从内容中提取 3-5 个关键词）
- 一句话全文概览（AI 从文章中提炼）

设计方向参考：卡片式、档案式、终端命令行式、手帐贴纸式、报纸头版式等，需与主题风格匹配。

### 12.2 尾部卡片（必须包含）

尾部卡片用于引导读者互动，应包含：

- 引导文案（如"如果觉得有收获"、"喜欢这篇文章吗？"等，AI 根据文章调性设计）
- 点赞 / 在看 / 转发 的行动引导
- 一句温暖的结尾语

#### 底部图标设计规范

互动按钮使用 emoji 图标 + 文字的组合，5 种标准风格供 AI 选择：

**风格A — 经典三连按钮**
```html
<section style="display:flex;flex-flow:row;justify-content:center;gap:10px">
  <section style="padding:8px 20px;background:主题色;color:#fff;font-size:12px;font-weight:600;border-radius:6px;">👍 点赞</section>
  <section style="padding:8px 20px;background:强调色;color:#fff;font-size:12px;font-weight:600;border-radius:6px;">👀 在看</section>
  <section style="padding:8px 20px;background:第三色;color:#fff;font-size:12px;font-weight:600;border-radius:6px;">↗ 转发</section>
</section>
```

**风格B — 胶囊渐变**
```html
<section style="display:flex;flex-flow:row;justify-content:center;gap:12px">
  <section style="padding:9px 22px;background:linear-gradient(135deg,主题色,变体);color:#fff;font-size:12px;font-weight:600;border-radius:50px;">👍 点赞</section>
  <section style="padding:9px 22px;background:linear-gradient(135deg,强调色,变体);color:#fff;font-size:12px;font-weight:600;border-radius:50px;">👀 在看</section>
  <section style="padding:9px 22px;background:linear-gradient(135deg,金色,变体);color:#fff;font-size:12px;font-weight:600;border-radius:50px;">↗ 转发</section>
</section>
```

**风格C — 大图标文字**
```html
<section style="display:flex;flex-flow:row;justify-content:center;gap:20px">
  <section style="text-align:center"><p style="font-size:22px;margin:0 0 4px">👍</p><p style="font-size:10px;color:弱色;margin:0">点赞</p></section>
  <section style="text-align:center"><p style="font-size:22px;margin:0 0 4px">👀</p><p style="font-size:10px;color:弱色;margin:0">在看</p></section>
  <section style="text-align:center"><p style="font-size:22px;margin:0 0 4px">↗</p><p style="font-size:10px;color:弱色;margin:0">转发</p></section>
  <section style="text-align:center"><p style="font-size:22px;margin:0 0 4px">⭐</p><p style="font-size:10px;color:弱色;margin:0">星标</p></section>
</section>
```

**风格D — 极简文字链**
```html
<section style="display:flex;flex-flow:row;justify-content:center;gap:24px">
  <p style="font-size:11px;color:弱色;margin:0;letter-spacing:1px">👍 点赞</p>
  <p style="font-size:11px;color:弱色;margin:0;letter-spacing:1px">👀 在看</p>
  <p style="font-size:11px;color:弱色;margin:0;letter-spacing:1px">↗ 分享</p>
</section>
```

**风格E — 暗色标签卡**
```html
<section style="display:flex;flex-flow:row;justify-content:center;gap:8px">
  <section style="padding:5px 14px;background:主题色;color:#fff;font-size:10px;font-weight:600;letter-spacing:1px;border-radius:4px">👍 点赞</section>
  <section style="padding:5px 14px;background:强调色;color:#fff;font-size:10px;font-weight:600;letter-spacing:1px;border-radius:4px">👀 在看</section>
  <section style="padding:5px 14px;background:金色;color:深色;font-size:10px;font-weight:600;letter-spacing:1px;border-radius:4px">↗ 转发</section>
</section>
```

#### 图标选择指南

- **点赞**：👍 / 💗 / ❤️ / ✨
- **在看**：👀 / 📖 / 🔍 / 💭
- **转发**：↗ / 📤 / 🔄 / 💬
- **星标**：⭐ / 🌟 / 💫 / 🔖

### 12.3 设计原则

- 头尾卡片是文章的门面和告别，要有设计感
- 使用圆角、渐变、阴影（公众号支持的范围内）
- 图标使用 emoji，不用 CSS 背景图（兼容性最好）
- 每个图标按钮有明确的颜色区分
- 色板与主题一致
- 排版有趣但不花哨
- 手机端一屏能看到完整卡片
- 尾部卡片底部留 20-30px 呼吸空间

---

## 附录：快速参考卡片

```
┌─ 布局 ─────────────────────────────────────┐
│ display: flex | inline-block | block | grid │
│ flex-flow: row | column                     │
│ flex: 0 0 auto | 0 0 90%                   │
│ justify-content: center | flex-start        │
│ align-items: center | flex-start            │
│ grid-template-columns/rows: 100%            │
├─ 盒模型 ───────────────────────────────────┤
│ box-sizing: border-box  ← 强制              │
│ max-width: 100% !important  ← 强制          │
│ width/height: % | px | max-content         │
│ padding/margin: px | % | auto              │
│ overflow: hidden | visible                 │
├─ 文字 ─────────────────────────────────────┤
│ font-size: 9-51px (基准14px)               │
│ line-height: 0-3 (正文1.85)                │
│ letter-spacing: 0-5px (正文0.3)            │
│ text-align: center | justify | left        │
│ color: #hex | rgb() | rgba()              │
├─ 背景 ─────────────────────────────────────┤
│ background-color: #xxx | rgb() | rgba()   │
│ background: linear-gradient(方向,c1,c2)    │
├─ 边框 ─────────────────────────────────────┤
│ border: 1px solid #xxx                     │
│ border-left/right/top/bottom               │
│ border-radius: px | % | 99px              │
├─ 特效 ─────────────────────────────────────┤
│ text-shadow: (多阴影描边)                    │
│ transform: rotate/skew/translate (4前缀)   │
│ opacity: 0-1                               │
│ z-index: 1-7                               │
└────────────────────────────────────────────┘
```

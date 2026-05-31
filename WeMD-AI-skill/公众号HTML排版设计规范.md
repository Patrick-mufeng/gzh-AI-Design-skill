# 微信公众号 HTML 排版设计规范

> **Version 1.1** | 2026-05-31 | 基于 4 篇真实公众号文章源码逆向分析

### 变更记录

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.1 | 2026-05-31 | 新增 §5.12 分隔线禁用三点式规则；强化 AI 自检流程引用 |
| 1.0 | 2025-06-15 | 初始版本——标签规则 / CSS 白名单 / 组件配方 / 色板系统 / 暗黑模式 |

## 概述

本规范定义了微信公众号文章 HTML 的完整语法规则。基于对 135 编辑器、秀米编辑器产出的真实公众号文章源码的逆向分析，确保 AI 按照此规范生成的 HTML 能够完整保留样式，通过 API 同步或编辑器粘贴到微信公众号。

---

## 第一部分：HTML 标签规则

### 1.1 唯一允许的容器标签：`<section>`

```
✅ <section style="...">内容</section>
❌ <div>        — 公众号不识别
❌ <article>    — 公众号不识别
❌ <header>     — 公众号不识别
❌ <footer>     — 公众号不识别
❌ <nav>        — 公众号不识别
❌ <main>       — 公众号不识别
❌ <aside>      — 公众号不识别
```

**规则**：所有块级布局必须使用 `<section>`。嵌套深度无限制（源码中常见 10+ 层嵌套）。

### 1.2 行内标签

| 标签 | 用途 | 示例 |
|------|------|------|
| `<p>` | 段落（margin 必须清零） | `<p style="margin:0px">` |
| `<span>` | 行内文字样式 | `<span style="color:#xxx">` |
| `<strong>` | 加粗 | `<strong>文字</strong>` |
| `<em>` | 斜体 | `<em>文字</em>` |
| `<br>` | 换行 | `<br/>` |

### 1.3 媒体标签

| 标签 | 用途 |
|------|------|
| `<img>` | 图片（必须带 draggable="false"） |
| `<svg>` | SVG 装饰 / 绝对定位容器 |
| `<foreignObject>` | SVG 内嵌 HTML（仅用于绝对定位） |

### 1.4 禁止使用的标签

```
❌ <div>        — 用 <section> 替代
❌ <table>      — 用 flex 替代
❌ <ul> <ol>    — 用 <section> + <p> 替代
❌ <h1>~<h6>    — 用 <section> + font-size 替代
❌ <blockquote> — 用 <section> + border-left 替代
❌ <a>          — 公众号不支持外链
❌ <style>      — 必须 100% 内联样式
❌ <link>       — 禁止外部 CSS
```

---

## 第二部分：强制 CSS 规则

### 2.1 每个元素必须携带的三个属性

```css
box-sizing: border-box;
max-width: 100% !important;
```

**无例外**。这是公众号渲染引擎的硬性要求。

### 2.2 `<p>` 标签强制初始化

```css
p {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}
```

### 2.3 所有 CSS 必须内联

```
✅ <section style="display:flex;padding:10px;...">
❌ <style>.class { ... }</style>
❌ <section class="xxx">
```

---

## 第三部分：CSS 属性完整白名单

以下属性已经在真实公众号文章中得到验证，**可以安全使用**。

### 3.1 布局

| 属性 | 常用值 | 说明 |
|------|--------|------|
| `display` | `flex`, `inline-block`, `block`, `grid` | flex 是主力 |
| `flex-flow` | `row`, `column`, `row nowrap` | 控制主轴方向 |
| `flex` | `0 0 auto`, `0 0 90%`, `100 100 0%`, `149.98 149.98 0%` | flex 简写，支持小数精确比例 |
| `flex-shrink` | `0` | 防止收缩 |
| `justify-content` | `center`, `flex-start`, `flex-end`, `space-between` | |
| `align-items` | `center`, `flex-start`, `flex-end` | |
| `align-self` | `flex-start`, `center`, `flex-end` | |
| `grid-template-columns` | `100%` | SVG 绝对定位用 |
| `grid-template-rows` | `100%` | SVG 绝对定位用 |
| `grid-column-start` | `1` | |
| `grid-row-start` | `1` | |

### 3.2 盒模型

| 属性 | 说明 |
|------|------|
| `width` | 百分比或 px，支持 `auto`、`1em` |
| `height` | 百分比、px、`auto` 或 `max-content` |
| `max-width` | **必须** `100% !important` |
| `min-width` | 百分比，常用 `5%` 占位 |
| `min-height` | 百分比或 px，用于清除浮动 |
| `padding` | 四向或分向 |
| `margin` | 支持负值（用于重叠/覆盖效果） |
| `box-sizing` | **强制** `border-box` |

### 3.3 文字

| 属性 | 取值范围 | 说明 |
|------|---------|------|
| `font-size` | `3px` ~ `51px` | 正文以 14px 为基准 |
| `line-height` | `0` ~ `3` | `0` 用于消除图片间隙 |
| `letter-spacing` | `0px` ~ `5px` | |
| `text-align` | `center`, `justify`, `left`, `right` | |
| `color` | hex / rgb / rgba | |
| `font-weight` | 通过 `<strong>` 或 `font-weight:bold` | |
| `vertical-align` | `middle`, `top`, `bottom`, `baseline` | 消除行内间隙 |
| `text-shadow` | 多阴影叠加 | 见 3.6 |
| `word-break` | `break-word` | |
| `font-family` | `-apple-system`, `'PingFang SC'`, `'Microsoft YaHei'`, `sans-serif`, `PingFangSC-ultralight` 等 | 非必须，设置系统字体栈常见 |

### 3.4 背景

| 属性 | 示例 |
|------|------|
| `background-color` | `#ffffff`, `rgba(0,0,0,0)`, `rgb(247,247,247)` |
| `background` | `linear-gradient(90deg, #color1 0%, #color2 86%)` |
| `background-image` | `url(...)`、`linear-gradient(...)`、SVG 图标 |
| `background-position` | `50% 50%`、`0% 0%`、`left top` |
| `background-size` | `cover`、`auto`、`contain`、百分比 `69.1974% !important`、`auto 176.923% !important` |
| `background-repeat` | `no-repeat`、`repeat`、`repeat-x`、`repeat-y` |
| `background-attachment` | `scroll`（默认） |

**注意**：`background-size` 支持精确百分比值（135 编辑器常用），必须带 `!important`。

**渐变支持完好**。方向语法：
- `to right` / `to left` / `to top` / `to bottom`
- `90deg` / `200deg` 等角度
- 多色停止点 `#c1 0%, #c2 50%, #c3 100%`
- rgba 透明度渐变 `rgba(124,153,18,0.93) 0%, rgba(230,246,221,0) 86%`

### 3.5 边框

| 属性 | 示例 |
|------|------|
| `border` | `1px solid #000` |
| `border-left/right/top/bottom` | 分侧设置 |
| `border-width` | 分侧宽度 |
| `border-style` | `solid`, `none`, `dashed` |
| `border-color` | hex / rgb / rgba |
| `border-radius` | `50px`, `99px`, `200px`, `30px`, `10px`, `100%` |
| `border-top-right-radius` | 单独控制各角圆角 |
| `border-bottom-right-radius` | 单独控制各角圆角 |
| `border-top-left-radius` | 单独控制各角圆角 |
| `border-bottom-left-radius` | 单独控制各角圆角 |
| `overflow` | `hidden`（配合 border-radius 裁剪）、`visible` |

**CSS 三角形技法**：
```css
width: 0px; height: 0px;
border-left: 9px solid transparent;
border-right: 9px solid transparent;
border-top: 10px solid #583f37;
```

### 3.6 阴影

**注意**：`box-shadow` 在移动端微信环境下可能不显示，**桌面端预览正常**。如需使用，建议配合半透明背景或 `rgba()` 色值降低风险。

**`box-shadow` 已验证可用**（来自秀米/135编辑器源码）：
```css
box-shadow: rgba(0,0,0,0.15) 1px 1px 10px 0px;
```

| 属性 | 示例 |
|------|------|
| `box-shadow` | `rgba(0,0,0,0.15) 1px 1px 10px 0px` |

**文字描边效果**（text-shadow 多阴影模拟）：
```css
text-shadow: #color 0em 0.035em 0em,
             #color 0.035em 0em 0em,
             #color 0em -0.035em 0em,
             #color -0.035em 0em 0em,
             #color 0.035em 0.035em 0em,
             #color -0.035em -0.035em 0em,
             #color 0.035em -0.035em 0em,
             #color -0.035em 0.035em 0em;
```

**使用场景**：大号数字、标题文字描边。

### 3.7 Transform（必须带 4 个厂商前缀）

```css
transform: rotate(0deg);
-webkit-transform: rotate(0deg);
-moz-transform: rotate(0deg);
-o-transform: rotate(0deg);
```

**已验证的 transform 函数**：
- `rotate(Xdeg)` — 旋转
- `rotateZ(Xdeg)` — 3D 旋转
- `rotateX(180deg)` / `rotateY(180deg)` — 翻转
- `translate3d(Xpx, Ypx, 0px)` — 3D 位移
- `translateX(Xpx)` — 水平位移
- `scale(1)` — 缩放
- `skew(Xdeg)` — 倾斜（135 编辑器用）

### 3.8 其他

| 属性 | 说明 |
|------|------|
| `opacity` | 透明度（源码中使用 rgba 代替，但也支持直接使用） |
| `z-index` | `1` ~ `7`，配合 SVG 绝对定位 |
| `position` | 仅 `static` |
| `overflow` | `hidden`（裁剪）, `visible`（SVG内） |
| `pointer-events` | `none`（图片装饰） |
| `user-select` | `none`（SVG内） |
| `-webkit-tap-highlight-color` | `transparent`（SVG内） |
| `float` | `left`（SVG spacer 元素） |
| `clear` | `both` |

### 3.9 禁止使用的 CSS

```
❌ position: relative/absolute/fixed/sticky
❌ animation / @keyframes / transition
❌ backdrop-filter
❌ clip-path
❌ filter (blur等用 transform 替代)
❌ calc()
❌ vw / vh / rem / clamp()
❌ css variables (var(--xxx))
❌ @media queries (公众号自动处理响应式)
```

---

## 第四部分：布局模式

### 4.1 Flex 横向布局（最常用）

```html
<section style="display:flex;flex-flow:row;justify-content:center;align-items:center;box-sizing:border-box;">
  <section style="display:inline-block;flex:0 0 auto;vertical-align:middle;box-sizing:border-box;max-width:100%!important;">
    左列
  </section>
  <section style="display:inline-block;flex:0 0 auto;vertical-align:middle;box-sizing:border-box;max-width:100%!important;">
    右列
  </section>
</section>
```

### 4.2 Flex 纵向布局

```html
<section style="display:flex;flex-flow:column;box-sizing:border-box;">
  <section style="box-sizing:border-box;max-width:100%!important;">第一行</section>
  <section style="box-sizing:border-box;max-width:100%!important;">第二行</section>
</section>
```

### 4.3 左右分栏

```html
<section style="display:flex;flex-flow:row;box-sizing:border-box;">
  <section style="display:inline-block;flex:0 0 45%;box-sizing:border-box;max-width:45%!important;">
    左侧内容
  </section>
  <section style="display:inline-block;flex:0 0 5%;box-sizing:border-box;max-width:5%!important;"></section>
  <section style="display:inline-block;flex:0 0 50%;box-sizing:border-box;max-width:50%!important;">
    右侧内容
  </section>
</section>
```

### 4.4 Grid 绝对定位叠加

```html
<section style="display:grid;grid-template-columns:100%;grid-template-rows:100%;box-sizing:border-box;">
  <!-- 底层：占位维持宽高比 -->
  <section style="grid-column-start:1;grid-row-start:1;padding-top:133.33%;box-sizing:border-box;">
    <svg viewbox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;box-sizing:border-box;"></svg>
  </section>
  <!-- 叠加层 1 -->
  <section style="width:60%;margin-top:20%;margin-left:20%;grid-column-start:1;grid-row-start:1;box-sizing:border-box;max-width:60%!important;">
    叠加文字
  </section>
  <!-- 叠加层 2 -->
  <section style="width:80%;margin-top:50%;margin-left:10%;grid-column-start:1;grid-row-start:1;box-sizing:border-box;max-width:80%!important;">
    更多叠加内容
  </section>
</section>
```

**说明**：所有子 section 占据同一网格单元格（row 1, col 1），通过百分比 `margin-top` 和 `margin-left` 定位，`padding-top` 控制宽高比。

### 4.5 SVG foreignObject 绝对定位（135 编辑器技法）

```html
<section style="display:grid;grid-template-columns:100%;grid-template-rows:100%;overflow:hidden;box-sizing:border-box;">
  <!-- 宽高比 SVG -->
  <section style="grid-column-start:1;grid-row-start:1;height:100%;line-height:0;box-sizing:border-box;">
    <svg viewbox="0 0 375 530" style="max-width:100%!important;pointer-events:none;display:inline-block;width:100%;box-sizing:border-box;"></svg>
  </section>
  <!-- 内容块 1 -->
  <section style="width:100%;margin-top:0%;margin-left:0%;grid-column-start:1;grid-row-start:1;height:max-content;z-index:1;box-sizing:border-box;max-width:100%!important;transform:scale(1);-webkit-transform:scale(1);-moz-transform:scale(1);-o-transform:scale(1);">
    <svg style="max-width:100%!important;display:inline-block;width:100%;line-height:1.6;overflow:visible;box-sizing:border-box;" viewbox="0 0 375 100">
      <foreignObject width="100%" height="100%">
        <section style="box-sizing:border-box;">
          <!-- 此处放正常 HTML -->
          <p style="text-align:center;font-size:16px;color:#fff;margin:0px;">文字内容</p>
        </section>
      </foreignObject>
    </svg>
  </section>
</section>
```

**注意**：`viewbox`（小写）是 135 编辑器的写法，`viewBox`（驼峰）是标准写法，两者均可。

---

## 第五部分：组件配方

### 5.1 文章头部

```html
<!-- 标题区域 -->
<section style="text-align:center;padding:28px 0 18px;box-sizing:border-box;">
  <!-- 可选：标签徽章 -->
  <section style="display:inline-block;padding:3px 12px;background:#primary;color:#fff;font-size:9px;font-weight:bold;letter-spacing:2px;box-sizing:border-box;">标签</section>
  <p style="font-size:22px;font-weight:bold;color:#1a1a1a;letter-spacing:1px;line-height:1.4;margin:8px 0 0;box-sizing:border-box;">文章标题</p>
  <p style="font-size:11px;color:#999;margin:6px 0 0;box-sizing:border-box;">副标题</p>
</section>
```

### 5.2 章节标题

```html
<section style="margin:32px 0 12px;display:flex;align-items:flex-start;gap:8px;box-sizing:border-box;">
  <!-- 左边框装饰 -->
  <section style="width:3px;height:18px;background:#primary;flex-shrink:0;box-sizing:border-box;"></section>
  <!-- 标题文字 -->
  <section style="flex:1;box-sizing:border-box;">
    <p style="font-size:10px;font-weight:bold;color:#accent;letter-spacing:2px;margin:0 0 2px;">SECTION 01</p>
    <p style="font-size:16px;font-weight:bold;color:#1a1a1a;margin:0;">章节标题</p>
  </section>
</section>
```

### 5.3 正文段落

```html
<p style="margin:8px 0;text-align:justify;font-size:14px;color:#333;line-height:1.85;letter-spacing:0.3px;box-sizing:border-box;">
  正文内容...
</p>
```

### 5.4 强调卡片

```html
<section style="margin:20px 0;padding:16px;background:linear-gradient(135deg,#f6f9fc,#f0f4f8);border-left:4px solid #primary;box-sizing:border-box;">
  <section style="display:inline-block;padding:2px 10px;background:#primary;color:#fff;font-size:9px;font-weight:bold;letter-spacing:2px;margin-bottom:6px;box-sizing:border-box;">重点</section>
  <p style="font-size:15px;font-weight:bold;color:#1a1a1a;margin:4px 0;">核心结论</p>
  <p style="font-size:13px;color:#555;line-height:1.8;margin:4px 0 0;">详细说明文字...</p>
</section>
```

### 5.5 引用/金句

```html
<section style="margin:20px 0;padding:16px;text-align:center;background:#fafafa;box-sizing:border-box;">
  <p style="font-size:15px;font-weight:bold;color:#accent;line-height:1.9;letter-spacing:0.5px;margin:0;">
    金句内容...
  </p>
</section>
```

### 5.6 数据展示（三列）

```html
<section style="display:flex;flex-flow:row;justify-content:space-around;margin:20px 0;box-sizing:border-box;">
  <section style="display:inline-block;flex:0 0 30%;text-align:center;padding:16px 8px;background:#surface2;box-sizing:border-box;max-width:30%!important;">
    <p style="font-size:28px;font-weight:bold;color:#primary;margin:0;line-height:1.2;">100万亿</p>
    <p style="font-size:10px;color:#999;margin:4px 0 0;">标签</p>
  </section>
  <!-- 重复 2 次 -->
</section>
```

### 5.7 步骤流（横向）

```html
<section style="margin:20px 0;padding:16px;background:#surface2;box-sizing:border-box;">
  <section style="display:flex;flex-flow:row;justify-content:space-around;box-sizing:border-box;">
    <section style="display:inline-block;flex:0 0 auto;text-align:center;padding:8px;box-sizing:border-box;">
      <section style="display:inline-block;width:28px;height:28px;line-height:28px;background:#primary;color:#fff;font-size:11px;font-weight:bold;text-align:center;margin-bottom:6px;box-sizing:border-box;">1</section>
      <p style="font-size:12px;font-weight:bold;color:#1a1a1a;margin:0;">步骤名</p>
      <p style="font-size:10px;color:#999;margin:2px 0 0;">步骤描述</p>
    </section>
    <!-- 重复 -->
  </section>
</section>
```

### 5.8 步骤流（纵向）

```html
<section style="margin:20px 0;padding:16px;background:#surface2;box-sizing:border-box;">
  <section style="display:flex;flex-flow:column;gap:8px;box-sizing:border-box;">
    <section style="display:flex;flex-flow:row;align-items:flex-start;gap:8px;box-sizing:border-box;">
      <section style="width:28px;height:28px;line-height:28px;background:#primary;color:#fff;font-size:11px;font-weight:bold;text-align:center;flex-shrink:0;box-sizing:border-box;">1</section>
      <section style="flex:1;box-sizing:border-box;">
        <p style="font-size:13px;font-weight:bold;color:#1a1a1a;margin:0;">步骤标题</p>
        <p style="font-size:11px;color:#888;margin:2px 0 0;">详细描述</p>
      </section>
    </section>
    <!-- 重复 -->
  </section>
</section>
```

### 5.9 标签徽章

```html
<section style="display:flex;flex-flow:row;justify-content:center;flex-wrap:wrap;gap:6px;margin:12px 0;box-sizing:border-box;">
  <section style="display:inline-block;padding:4px 12px;background:#primary;color:#fff;font-size:10px;font-weight:bold;box-sizing:border-box;">标签1</section>
  <section style="display:inline-block;padding:4px 12px;background:#accent2;color:#fff;font-size:10px;font-weight:bold;box-sizing:border-box;">标签2</section>
</section>
```

### 5.10 提示块

```html
<section style="margin:16px 0;padding:12px 16px;background:#surface2;border-left:3px solid #accent;box-sizing:border-box;">
  <p style="font-size:13px;color:#555;line-height:1.8;margin:0;">
    <strong style="color:#accent;">TIP</strong> 提示内容...
  </p>
</section>
```

### 5.11 CTA 按钮

```html
<section style="margin:28px 0;padding:22px 16px;text-align:center;background:linear-gradient(135deg,#surface2,#surface3);box-sizing:border-box;">
  <p style="font-size:9px;font-weight:bold;color:#accent;letter-spacing:2px;margin:0 0 4px;">CTA LABEL</p>
  <p style="font-size:15px;font-weight:bold;color:#1a1a1a;margin:0 0 12px;">标题文字</p>
  <section style="display:inline-block;padding:10px 28px;background:#primary;color:#fff;font-size:13px;font-weight:bold;letter-spacing:1px;box-sizing:border-box;">按钮文字</section>
</section>
```

### 5.12 分割线

```html
<p style="text-align:center;margin:24px 0;font-size:13px;color:#ddd;letter-spacing:6px;box-sizing:border-box;">· · ·</p>
```

### 5.13 图片

**支持的图片格式**：JPG、PNG、GIF、SVG（通过 `<img>` 标签或 `background-image: url()`）

**常用图片属性**：`_width="100%"`、`data-s="300,640"`、`data-ratio="0.666"`、`data-w="1080"`（秀米/135编辑器兼容属性）

```html
<!-- 标准图片（带 editor 属性） -->
<section style="text-align:center;margin:12px 0;box-sizing:border-box;">
  <img class="raw-image" style="width:100%;display:block;vertical-align:middle;box-sizing:border-box;max-width:100%!important;" src="https://..." draggable="false" _width="100%" data-s="300,640" data-ratio="0.666" data-w="1080"/>
</section>

<!-- SVG 图标图片 -->
<section style="max-width:100%;vertical-align:middle;display:inline-block;line-height:0;width:30%;height:auto;box-sizing:border-box;">
  <img src="https://..." style="vertical-align:middle;width:100%;height:100%;box-sizing:border-box;max-width:100%!important;"/>
</section>

<!-- 限高滚动图片 -->
<section style="text-align:center;margin:12px 0;overflow:hidden;height:250px;box-sizing:border-box;">
  <img style="width:100%;display:block;box-sizing:border-box;max-width:100%!important;" src="https://..." draggable="false"/>
</section>

<!-- 多图横向滚动 -->
<section style="margin:12px 0;overflow-x:auto;box-sizing:border-box;">
  <section style="display:flex;flex-flow:row;box-sizing:border-box;">
    <section style="flex-shrink:0;width:200px;padding:4px;box-sizing:border-box;">
      <img style="width:100%;display:block;box-sizing:border-box;max-width:100%!important;" src="https://..." draggable="false"/>
    </section>
    <!-- 重复多张 -->
  </section>
</section>
```

### 5.14 文章头部信息卡（推荐）

每篇文章开头使用。包含标签/话题、字数、阅读时间、一句话概括。

```html
<section style="margin:20px 0 28px;padding:20px 16px;background:linear-gradient(135deg,#surface2,#surface3);box-sizing:border-box;max-width:100%!important;">
  <!-- 标签行 -->
  <section style="display:flex;flex-flow:row;flex-wrap:wrap;gap:6px;margin-bottom:10px;box-sizing:border-box;max-width:100%!important;">
    <section style="display:inline-block;padding:3px 10px;background:#accent;color:#fff;font-size:8px;font-weight:bold;letter-spacing:1.5px;box-sizing:border-box;max-width:100%!important;">标签1</section>
    <section style="display:inline-block;padding:3px 10px;background:rgba(0,0,0,0.06);color:#mute;font-size:8px;letter-spacing:1px;box-sizing:border-box;max-width:100%!important;">标签2</section>
  </section>
  <!-- 元信息 -->
  <section style="display:flex;flex-flow:row;gap:16px;margin-bottom:6px;box-sizing:border-box;max-width:100%!important;">
    <p style="font-size:9px;color:#mute;margin:0;box-sizing:border-box;max-width:100%!important;">📄 约 X 字</p>
    <p style="font-size:9px;color:#mute;margin:0;box-sizing:border-box;max-width:100%!important;">⏱ 阅读 X 分钟</p>
  </section>
  <!-- 概括句 -->
  <p style="font-size:12px;color:#ink;line-height:1.7;margin:8px 0 0;box-sizing:border-box;max-width:100%!important;">一句话概括全文的核心观点或核心冲突。</p>
</section>
```

### 5.15 文章结尾互动卡（推荐）

每篇文章结尾使用。引导点赞、在看、收藏、转发。

```html
<section style="margin:36px 0 24px;padding:24px 16px;text-align:center;background:linear-gradient(135deg,#surface2,#surface3);box-sizing:border-box;max-width:100%!important;">
  <p style="font-size:10px;font-weight:bold;color:#accent;letter-spacing:2px;margin:0 0 4px;box-sizing:border-box;max-width:100%!important;">— THE END —</p>
  <p style="font-size:13px;font-weight:bold;color:#ink;margin:8px 0 4px;box-sizing:border-box;max-width:100%!important;">如果觉得有用</p>
  <section style="display:flex;flex-flow:row;justify-content:center;gap:10px;margin:10px 0 0;box-sizing:border-box;max-width:100%!important;">
    <section style="display:inline-block;padding:8px 16px;background:#primary;color:#fff;font-size:10px;font-weight:bold;letter-spacing:1px;box-sizing:border-box;max-width:100%!important;">👍 点个赞</section>
    <section style="display:inline-block;padding:8px 16px;background:#accent;color:#fff;font-size:10px;font-weight:bold;letter-spacing:1px;box-sizing:border-box;max-width:100%!important;">⭐ 在看</section>
    <section style="display:inline-block;padding:8px 16px;background:#surface3;color:#ink;font-size:10px;font-weight:bold;letter-spacing:1px;border:1px solid #border;box-sizing:border-box;max-width:100%!important;">🔗 转发</section>
  </section>
  <p style="font-size:9px;color:#mute;margin:10px 0 0;box-sizing:border-box;max-width:100%!important;">谢谢你看我的文章，我们下篇再见。</p>
</section>
```

### 5.16 字体比例参考

正文基准 14px，其他元素按比例缩放：

| 元素 | 字号 | 说明 |
|---|---|---|
| 标题 | 19-20px | 文章主标题 |
| 副标题 | 12-13px | 标题下方副文 |
| 章节标题 | 16px | 带装饰条的分段标题 |
| 正文 | **14px** | 基准 |
| 强调/突出 | **15-16px** | 金句、核心观点 |
| 卡片内文 | 13px | 信息卡、引用卡内文字 |
| 标签/角标 | 8-9px | 徽章、标签、字母标记 |
| 底部文字 | 10px | 版权、来源等 |
| 分割线装饰 | 12-13px | 点点点分隔 |

### 5.17 主题案例

以下 6 个完整主题案例展示规范的上限——从极简到张扬，从温暖到冷峻。

---

#### 🟫 案例 1：赤墨（Red Ink）— 东方书法 × 现代排版

> 六色色板（primary/accent/surface/s2/border/ink/mute/body）见 §6.3 **「赤墨（进阶）」**

**设计特征**：竖向装饰线替代横向分隔、标题用 serif 字重对比、引用段左边 3px 朱砂竖线、卡片底色偏暖黄像旧书页。所有设计元素围绕"一本书的阅读体验"展开。

---

#### 🟦 案例 2：深海（Abyss）— 暗黑 × 荧光 × 沉浸

> 六色色板（primary/accent/surface/s2/border/ink/mute/body）见 §6.3 **「深海（进阶）」**

**设计特征**：全暗底、电光青是唯一光源。信息卡用极微弱蓝调背景区分层次，分割线用半透明青线。强调文字用青字+0.5px 青文字阴影模拟荧光。适合科技/深度/沉浸感文章。

---

#### 🟩 案例 3：苔原（Tundra）— 北欧极简 × 自然治愈

> 六色色板（primary/accent/surface/s2/border/ink/mute/body）见 §6.3 **「苔原（进阶）」**

**设计特征**：一切从简。只用一种绿色，不同灰度完成层次。圆角普遍 4-6px，比默认更圆润柔和。卡片带极轻微绿色背景几乎看不出来。适合生活/治愈/慢生活类文章。

---

#### 🟪 案例 4：紫调（Violet Hour）— 渐变 × 梦幻 × 文艺

> 六色色板（primary/accent/surface/s2/border/ink/mute/body）见 §6.3 **「紫调（进阶）」**

**设计特征**：双强调色——紫用于结构（标题/分隔/按钮），粉玫红用于情绪（金句/引用/互动）。渐变只出现在按钮和分隔线。卡片带极淡的紫色底色。适合文艺/情感/女性向内容。

---

#### 🟧 案例 5：暖橙（Ember）— 大地色 × 温暖 × 手作感

> 六色色板（primary/accent/surface/s2/border/ink/mute/body）见 §6.3 **「暖橙（进阶）」**

**设计特征**：全暖色调，无冷色。信息卡背景用亚麻色（偏黄灰），强调文字用陶土橙而非正红。按钮背景用可可黑配白字，形成温暖但不轻浮的对比。适合美食/手作/旅行/生活记录。

---

#### ⬜ 案例 6：素白（Bare）— 纯白 × 单黑 × 极致克制

> 六色色板（primary/accent/surface/s2/border/ink/mute/body）见 §6.3 **「素白（进阶）」**

**设计特征**：全篇只有黑白灰。无彩色，无渐变，连强调文字都是黑色加粗。层次全靠灰度和留白。信息卡用 5%浅灰底，分割线用 10%灰线。按钮用黑底白字 vs 白底黑字对比。所有圆角为 0。适合极简主义者/哲学/诗歌/高级感内容。

---

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

### 6.3 十五套主题色板（9 基础 + 6 进阶）

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

#### 🟫 赤墨（进阶）
```
primary: #c23a2e    accent: #c23a2e
surface: #faf7f4    s2: #f3ede6    s3: rgba(194,58,46,0.03)
border: #e0d5c8     ink: #1a0f0c
mute: #9c8880       body: #3d302c
```

#### 🟦 深海（进阶）
```
primary: #00e5ff    accent: #00e5ff
surface: #060d17    s2: #0d1525    s3: rgba(0,229,255,0.04)
border: rgba(0,229,255,0.15)  ink: #e8f0ff
mute: #5a6a80       body: #b0c0d8
```

#### 🟩 苔原（进阶）
```
primary: #7cb342    accent: #7cb342
surface: #f9fbf7    s2: #f0f4ec    s3: rgba(124,179,66,0.04)
border: #dde4d8     ink: #1d2a1d
mute: #889a80       body: #3a4638
```

#### 🟪 紫调（进阶）
```
primary: #8b5cf6    accent: #f472b6
surface: #faf8ff    s2: #f3f0fc    s3: rgba(139,92,246,0.03)
border: #ddd8f0     ink: #1a1530
mute: #9088a8       body: #3d3558
```

#### 🟧 暖橙（进阶）
```
primary: #e8873a    accent: #e8873a
surface: #fdf9f3    s2: #f8efe0    s3: rgba(232,135,58,0.04)
border: #e8d5c0     ink: #2c1810
mute: #a08878       body: #4a3530
```

#### ⬜ 素白（进阶）
```
primary: #000000    accent: #000000
surface: #ffffff    s2: #f5f5f5    s3: #fafafa
border: #e5e5e5     ink: #000000
mute: #999999       body: #000000
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
4. 所有 transform 带 4 个厂商前缀
5. 图片使用 `display:block;` 消除底部空隙
6. 容器之间用 `vertical-align:middle;` 或 `top` 对齐
7. flex 子元素写 `flex:0 0 auto;`

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

---

## 第九部分：文章完整结构模板

```html
<section style="width:100%;max-width:677px;background:transparent;padding:0 8px 24px;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;font-size:14px;line-height:1.85;color:{{body}};letter-spacing:0.3px;box-sizing:border-box;margin:0 auto">
  <!-- ↑ color:{{body}} 为主题正文色占位符，实际生成时替换为所选主题的 body 色值 -->

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

## 附录：AI 速查卡

> **AI 先读这里**——速查卡覆盖全部规则的索引。每个条目带 `→§` 引用，需要细节时再翻正文对应章节。不用读完 34KB 全文。

### A.1 标签规则 `→§1`

| ✅ 允许 | ❌ 禁止 |
|---------|---------|
| `<section>` 唯一块级容器 | `<div>` `<article>` `<header>` `<footer>` `<nav>` `<main>` `<aside>` |
| `<p>` `<span>` `<strong>` `<em>` `<br/>` | `<h1>`–`<h6>` `<ul>` `<ol>` `<table>` `<blockquote>` `<a>` |
| `<img>` `<svg>` `<foreignObject>` | `<style>` `<link>` |

### A.2 三条铁律 `→§2`

1. **每个元素写**: `box-sizing:border-box; max-width:100%!important;`
2. **每个 `<p>` 写**: `margin:0px; padding:0px;`
3. **100% 内联样式** — 禁止 `<style>` 标签、禁止 class、禁止外部 CSS

### A.3 CSS 白名单 `→§3`

| 类别 | ✅ 可用 | ❌ 禁止 |
|------|---------|---------|
| 布局 | `display:flex/inline-block/block/grid`, `flex-flow`, `flex`, `justify-content`, `align-items`, `align-self`, `grid-template-*` | — |
| 盒模型 | `width`, `height`, `max/min-width/height`, `padding`, `margin`(支持负值), `overflow:hidden/visible` | — |
| 文字 | `font-size:9-51px`, `line-height:0-3`, `letter-spacing:0-5px`, `text-align`, `color:#hex/rgb/rgba`, `font-weight`, `vertical-align`, `word-break`, `font-family` | — |
| 背景 | `background-color`, `background:linear-gradient()`, `background-image:url()`, `background-position`, `background-size`(支持精确%), `background-repeat` | — |
| 边框 | `border`, `border-*`(分侧), `border-radius`, `border-*-*-radius`(单角) | — |
| 特效 | `text-shadow`(多阴影描边), `box-shadow`, `transform`(rotate/skew/translate/scale), `opacity`, `z-index:1-7` | `animation` `@keyframes` `transition` `filter` `backdrop-filter` `clip-path` |
| 定位 | `position:static`(默认值，不写) | `position:relative/absolute/fixed/sticky` |
| 单位 | `px` `%` `em` | `vw` `vh` `rem` `calc()` `var()` `clamp()` `@media` |
| 颜色 | `#hex` `rgb()` `rgba()` | `hsl()` `oklch()` |

> **transform 必须 4 前缀**: 标准 + `-webkit-` + `-moz-` + `-o-`，缺一不可 `→§3.7`

### A.4 布局模式 `→§4`

| # | 模式 | 核心 CSS | 用途 |
|---|------|----------|------|
| 1 | Flex 横向 | `display:flex;flex-flow:row` + 子元素 `display:inline-block;flex:0 0 auto` | 默认布局 |
| 2 | Flex 纵向 | `display:flex;flex-flow:column` | 垂直堆叠 |
| 3 | 左右分栏 | flex row + `flex:0 0 N%` + 空隙列 `flex:0 0 5%` | 精确比例分栏 |
| 4 | Grid 叠加 | `display:grid;grid-template-columns:100%;grid-template-rows:100%` + 子元素 `grid-column-start:1;grid-row-start:1` | 伪绝对定位 |
| 5 | SVG foreignObject | Grid + SVG `viewbox` + `<foreignObject>` 内嵌 HTML | 高级叠加(135编辑器) |

### A.5 组件清单 `→§5`

**每篇文章必须包含（按顺序）**: 标题区 `→§5.1` → 信息卡 `→§5.14` → 正文 `→§5.3` → 金句 `→§5.5` → 分隔 `→§5.12` → 互动卡 `→§5.15`

| # | 组件 | 引用 | 关键特征 |
|---|------|------|----------|
| 1 | 头部标题区 | §5.1 | 标签徽章 + 标题 21-24px + 副标题 |
| 2 | 信息卡 | §5.14 | 字数 + 阅读时间 + 标签 + 一句话概览 |
| 3 | 章节标题 | §5.2 | 左边框 3px 装饰 + SECTION 编号 + 标题 |
| 4 | 正文段落 | §5.3 | 14px / 1.85 行高 / justify / 0.3px 字间距 |
| 5 | 强调卡片 | §5.4 | 渐变背景 + 左边框 4px + badge 标签 |
| 6 | 金句/引用 | §5.5 | 居中 + 灰色背景 + 加粗 15px |
| 7 | 数据展示 | §5.6 | flex 三列 + 大数字 28px + 标签 |
| 8 | 步骤流(横) | §5.7 | 编号圆圈 28px + 步骤名 + 描述 |
| 9 | 步骤流(纵) | §5.8 | 左编号 + 右文字，flex row |
| 10 | 标签徽章 | §5.9 | flex wrap + `gap:6px` + 小圆角色块 |
| 11 | 提示块 | §5.10 | 左边框 3px + **TIP** 前缀 |
| 12 | CTA 按钮 | §5.11 | 渐变背景 + 大按钮 `padding:10px 28px` |
| 13 | 分割线 | §5.12 | **1px 细线或渐变线**（禁用 `· · ·` 三点式） |
| 14 | 图片 | §5.13 | `display:block` + `draggable="false"` + 圆角 8px + 阴影 |
| 15 | 尾部互动卡 | §5.15 | 5 种按钮风格 A-E 可选 + emoji 图标 |

### A.6 关键数值 `→§7`

| 属性 | 值 | 适用场景 |
|------|-----|----------|
| 正文 | **14px** / 行高 **1.85** / 字间距 **0.3px** | `<p>` 段落 |
| 文章标题 | 21–24px / 行高 1.3–1.4 | 文首大标题 |
| 章节标题 | 15–17px | 一级分段标题 |
| 卡片标题 | 15px | 强调卡片内标题 |
| 标签/徽章 | 9–10px / 字间距 2px | badge、日期、编号 |
| 微型文字 | 9px | 极小标注 |
| 金句/引用 | 13–15px / 行高 1.8–1.9 | 居中引用 |
| 卡片间距 | margin **20–24px** 上下 | 组件之间 |
| 段落间距 | margin **8–10px** 上下 | 正文 `<p>` |
| 章节间距 | margin-top **32px** | 章节标题上方 |
| 容器两端缩进 | `padding:0 6px` | 最外层容器 |
| 尾部呼吸空间 | padding-bottom **20–30px** | 尾部卡片底部 |

### A.7 暗黑模式 `→§10`

- 容器背景 `transparent` — 让微信底色透出，双模式自动适配
- 卡片用 `rgba(0,0,0,0.03)` ~ `rgba(0,0,0,0.06)` — 半透明在两种模式下都有层次
- 文字用深色 `#1a1a1a` / `#333` / `#555` — 暗黑模式自动反转
- 渐变用透明停止点 — `linear-gradient(to right, rgba(0,0,0,0.06), transparent)`
- **禁用** `@media (prefers-color-scheme: dark)` — 公众号自动处理

### A.8 AI 内容处理权限 `→§11`

| ✅ 允许 | ❌ 禁止 |
|---------|---------|
| 提取金句做成引用块 | 改变事实和数据 |
| 拆分长段落增强节奏 | 添加原文没有的观点 |
| 添加章节一句话提炼 | 删除关键论据 |
| 数据句包装为数字卡片 | 改变文章立场和结论 |
| 优化叙事结构 | — |
| 凝练开头为导语 | — |

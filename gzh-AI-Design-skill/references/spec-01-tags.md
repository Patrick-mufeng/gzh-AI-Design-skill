> 本文件是微信公众号 HTML 排版规范的 **第 1/4 部分：标签规则与强制 CSS**。完整规范由 4 个文件组成，必须依次全部读完。其他部分：spec-02-css.md / spec-03-components.md / spec-04-design.md

<!--
============================================================================
微信公众号 HTML 排版设计规范 (DESIGN.md)
Version: 1.0
基于 4 篇真实公众号文章源码逆向分析
适用：AI Agent 生成公众号兼容 HTML
============================================================================
-->

# 微信公众号 HTML 排版设计规范

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
| `<span>` | 行内文字样式 | `<span leaf="" style="color:#xxx">`（**所有文字必须 `<span leaf="">` 包裹**） |
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

### 2.2 `<span leaf="">` 强制包裹（核心铁律）

**所有含中文的文字节点必须用 `<span leaf="">文字</span>` 包裹**，否则粘贴到公众号编辑器后文字样式会大面积丢失。这是从真实粘贴验证中得出的公众号平台行为。

```
✅ <p style="font-size:14px"><span leaf="">正文内容</span></p>
❌ <p style="font-size:14px">正文内容</p>
```

**规则**：
- 每个 `<p>` / `<span>` / `<strong>` / `<em>` 内的**中文字符**必须处于 `<span leaf="">` 内
- `leaf=""` 属性值可为空，公众号编辑器识别的是属性名本身
- 纯英文/数字/符号无 CJK 字符的节点可豁免（但建议统一包裹）
- 代码块内文字（等宽字体区）可豁免
- `<br>` 标签无需包裹

### 2.3 `<p>` 标签强制初始化

```css
p {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}
```

### 2.4 所有 CSS 必须内联

```
✅ <section style="display:flex;padding:10px;...">
❌ <style>.class { ... }</style>
❌ <section class="xxx">
```

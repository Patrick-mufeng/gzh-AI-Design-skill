> 本文件是微信公众号 HTML 排版规范的 **第 2/4 部分：CSS 属性完整白名单**。完整规范由 4 个文件组成，必须依次全部读完。其他部分：spec-01-tags.md / spec-03-components.md / spec-04-design.md

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

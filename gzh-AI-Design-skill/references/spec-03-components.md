> 本文件是微信公众号 HTML 排版规范的 **第 3/4 部分：布局模式与组件配方**。完整规范由 4 个文件组成，必须依次全部读完。其他部分：spec-01-tags.md / spec-02-css.md / spec-04-design.md
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

五种紧凑风格，按场景选用。**原则：少占空间、视觉突出、有呼吸感。**

---

**风格A — 左侧竖线（最经典，推荐首选）**

```html
<section style="margin:16px 0;padding:6px 0 6px 12px;border-left:3px solid #primary;box-sizing:border-box;max-width:100%!important;">
  <p style="font-size:15px;font-weight:bold;color:#ink;line-height:1.85;letter-spacing:0.5px;margin:0;box-sizing:border-box;max-width:100%!important;">金句内容...</p>
</section>
```

**风格B — 大引号装饰（文艺气质）**

```html
<section style="margin:16px 0;position:static;box-sizing:border-box;max-width:100%!important;">
  <p style="font-size:36px;color:#primary;line-height:0.6;margin:0 0 -8px 0;box-sizing:border-box;max-width:100%!important;">"</p>
  <p style="font-size:14px;color:#ink;line-height:1.85;letter-spacing:0.5px;margin:0;padding:0 0 0 8px;box-sizing:border-box;max-width:100%!important;">金句内容...</p>
</section>
```

**风格C — 渐变底色条（紧凑现代）**

```html
<section style="margin:16px 0;padding:10px 14px;background:linear-gradient(90deg, rgba(0,0,0,0.04), transparent);border-radius:4px;box-sizing:border-box;max-width:100%!important;">
  <p style="font-size:14px;font-weight:bold;color:#ink;line-height:1.8;letter-spacing:0.5px;margin:0;box-sizing:border-box;max-width:100%!important;">金句内容...</p>
</section>
```

**风格D — 标签徽章式（带「金句」标记）**

```html
<section style="margin:16px 0;padding:10px 14px;background:rgba(0,0,0,0.02);border-radius:6px;box-sizing:border-box;max-width:100%!important;">
  <section style="display:inline-block;padding:2px 8px;background:#primary;color:#fff;font-size:8px;font-weight:bold;letter-spacing:1.5px;margin-bottom:6px;border-radius:3px;box-sizing:border-box;">金句</section>
  <p style="font-size:14px;color:#ink;line-height:1.85;letter-spacing:0.5px;margin:0;box-sizing:border-box;max-width:100%!important;">金句内容...</p>
</section>
```

---

**选用指南**：

| 风格 | 适用场景 | 特点 |
|------|---------|------|
| A 左侧竖线 | 技术/商业/严肃文章 | 经典稳重，极省空间 |
| B 大引号 | 散文/故事/情感类 | 文艺感，大号引号有识别度 |
| C 渐变底色 | 快节奏/新媒体文 | 现代感，视觉层次好 |
| D 标签式 | 教程/干货/总结 | 有「划重点」心理暗示 |

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

### 5.17 代码块

用于展示代码片段、配置、终端命令等。使用 `<section>` + `<p>` + `<span>` 模拟，**禁止使用 `<pre>` 和 `<code>` 标签**。

```html
<!-- 带语言标签的代码块 -->
<section style="margin:16px 0;border-radius:8px;overflow:hidden;box-sizing:border-box;max-width:100%!important;">
  <!-- 顶部栏：语言标签 -->
  <section style="padding:8px 14px;background:rgba(0,0,0,0.75);display:flex;flex-flow:row;align-items:center;gap:8px;box-sizing:border-box;max-width:100%!important;">
    <section style="width:10px;height:10px;border-radius:50%;background:#ff5f57;box-sizing:border-box;"></section>
    <section style="width:10px;height:10px;border-radius:50%;background:#febc2e;box-sizing:border-box;"></section>
    <section style="width:10px;height:10px;border-radius:50%;background:#28c840;box-sizing:border-box;"></section>
    <p style="flex:1;text-align:right;font-size:9px;color:rgba(255,255,255,0.5);margin:0;letter-spacing:1px;box-sizing:border-box;max-width:100%!important;">python</p>
  </section>
  <!-- 代码内容区 -->
  <section style="padding:14px 16px;background:rgba(0,0,0,0.85);box-sizing:border-box;max-width:100%!important;">
    <p style="font-size:12px;font-family:'SF Mono','Menlo','Consolas','Courier New',monospace;color:rgba(255,255,255,0.9);line-height:1.8;margin:0;white-space:pre-wrap;word-break:break-all;box-sizing:border-box;max-width:100%!important;">
<span style="color:#c678dd;">import</span> <span style="color:#e5c07b;">requests</span>
<span style="color:#c678dd;">import</span> <span style="color:#e5c07b;">json</span>

<span style="color:#5c6370;"># 调用 API</span>
<span style="color:#e5c07b;">resp</span> = <span style="color:#e5c07b;">requests</span>.post(
    <span style="color:#98c379;">"http://localhost:5000/api/generate"</span>,
    <span style="color:#e5c07b;">json</span>={<span style="color:#98c379;">"article"</span>: <span style="color:#98c379;">"文章内容"</span>, <span style="color:#98c379;">"theme"</span>: <span style="color:#98c379;">"cyber"</span>}
)
<span style="color:#c678dd;">print</span>(<span style="color:#e5c07b;">resp</span>.json()[<span style="color:#98c379;">"html"</span>])
    </p>
  </section>
</section>
```

**两种变体**：

**变体 A — 无顶部栏（更简洁）**
```html
<section style="margin:16px 0;padding:14px 16px;background:rgba(0,0,0,0.05);border-radius:6px;box-sizing:border-box;max-width:100%!important;">
  <p style="font-size:12px;font-family:'SF Mono','Menlo','Consolas','Courier New',monospace;color:#333;line-height:1.8;margin:0;white-space:pre-wrap;word-break:break-all;box-sizing:border-box;max-width:100%!important;">$ pip install flask requests</p>
</section>
```

**变体 B — 暗色终端风格（适合技术类文章）**
```html
<section style="margin:16px 0;border-radius:8px;overflow:hidden;box-sizing:border-box;max-width:100%!important;">
  <section style="padding:10px 14px;background:#1e1e2e;box-sizing:border-box;max-width:100%!important;">
    <p style="font-size:11px;color:rgba(255,255,255,0.4);margin:0;letter-spacing:1px;box-sizing:border-box;max-width:100%!important;">$ terminal</p>
  </section>
  <section style="padding:12px 16px;background:#181825;box-sizing:border-box;max-width:100%!important;">
    <p style="font-size:12px;font-family:'SF Mono','Menlo','Consolas','Courier New',monospace;color:#cdd6f4;line-height:1.8;margin:0;box-sizing:border-box;max-width:100%!important;">curl -X POST http://localhost:5000/api/generate \</p>
    <p style="font-size:12px;font-family:'SF Mono','Menlo','Consolas','Courier New',monospace;color:#cdd6f4;line-height:1.8;margin:0;box-sizing:border-box;max-width:100%!important;">  -H "Authorization: Bearer sk-xxx" \</p>
    <p style="font-size:12px;font-family:'SF Mono','Menlo','Consolas','Courier New',monospace;color:#cdd6f4;line-height:1.8;margin:0;box-sizing:border-box;max-width:100%!important;">  -d '{"article":"...","theme":"cyber"}'</p>
  </section>
</section>
```

**色彩规则**：
- 代码块底色使用 `rgba(0,0,0,0.85)`（暗色）或 `rgba(0,0,0,0.05)`（亮色），根据主题选择
- 代码文字使用等宽字体栈：`'SF Mono','Menlo','Consolas','Courier New',monospace`
- 代码字号 11-12px，行高 1.7-1.8
- 语法高亮通过 `<span style="color:#xxx">` 实现，使用柔和色值避免刺眼
- 顶部栏三色圆点（红黄绿）为可选装饰，适合展示完整代码文件
- 内联代码（行内）用 `<span style="font-family:monospace;background:rgba(0,0,0,0.06);padding:1px 4px;border-radius:3px;font-size:12px;">code</span>` 实现


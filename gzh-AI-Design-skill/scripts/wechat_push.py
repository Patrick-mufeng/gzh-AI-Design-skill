#!/usr/bin/env python3
"""
WeChatPost 公众号推送脚本
将排版后的文章推送到微信公众号草稿箱。

用法:
    python wechat_push.py <文章目录>

示例:
    python wechat_push.py "outputs/DeepSeek价格战_2026-07-09/article"

前置:
    - 项目根目录 .env 中配置 WECHAT_APPID / WECHAT_APPSECRET
    - 文章目录下须有 final.md / output.html / cover/cover-combined.png

API 文档:
    https://developers.weixin.qq.com/doc/offiaccount/Draft_Box/Add_draft.html
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API_BASE = "https://api.weixin.qq.com"
API_PATH = "/cgi-bin"


# ═══════════════════════════════════════════════════════════════
# 配置加载
# ═══════════════════════════════════════════════════════════════

def load_env() -> dict:
    """从项目根目录 .env 加载微信凭证"""
    candidates = [
        Path.cwd() / ".env",
        Path(__file__).resolve().parent.parent.parent.parent.parent / ".env",
    ]
    for env_file in candidates:
        if env_file.exists():
            try:
                with open(env_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#") and "=" in line:
                            key, _, val = line.partition("=")
                            key = key.strip()
                            val = val.strip()
                            if val and key not in os.environ:
                                os.environ[key] = val
            except Exception:
                pass

    return {
        "appid": os.environ.get("WECHAT_APPID", ""),
        "appsecret": os.environ.get("WECHAT_APPSECRET", ""),
        "author": os.environ.get("WECHAT_AUTHOR", ""),
    }


# ═══════════════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════════════

def log(msg: str):
    print(f"[·] {msg}", file=sys.stderr)

def ok(msg: str):
    print(f"✅ {msg}", file=sys.stderr)

def err(msg: str):
    print(f"❌ {msg}", file=sys.stderr)
    sys.exit(1)


def _is_network_error(e: BaseException) -> bool:
    if isinstance(e, urllib.error.URLError):
        return True
    if isinstance(e, TimeoutError):
        return True
    if isinstance(e, urllib.error.HTTPError) and e.code and e.code >= 500:
        return True
    return False


def _api_get(url: str) -> dict:
    for attempt in range(2):
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if attempt == 0 and _is_network_error(e):
                log("网络请求失败，1秒后重试...")
                time.sleep(1)
                continue
            raise


def _api_post_json(url: str, body: dict) -> dict:
    payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
    for attempt in range(2):
        try:
            req = urllib.request.Request(
                url, data=payload, headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if attempt == 0 and _is_network_error(e):
                log("网络请求失败，1秒后重试...")
                time.sleep(1)
                continue
            raise


def _upload_file(url: str, file_path: str, field_name: str = "media") -> dict:
    """multipart/form-data 文件上传（纯标准库）"""
    boundary = f"----WechatPush{int(time.time() * 1000)}"
    path = Path(file_path)
    if not path.exists():
        err(f"文件不存在: {file_path}")

    with open(path, "rb") as f:
        file_data = f.read()

    filename = path.name
    mime_type = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"

    body = bytearray()
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(
        f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'.encode("utf-8")
    )
    body.extend(f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"))
    body.extend(file_data)
    body.extend(f"\r\n--{boundary}--\r\n".encode("utf-8"))

    req = urllib.request.Request(
        url,
        data=bytes(body),
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )

    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if attempt == 0 and _is_network_error(e):
                log("上传网络失败，1秒后重试...")
                time.sleep(1)
                continue
            raise


# ═══════════════════════════════════════════════════════════════
# 微信 API
# ═══════════════════════════════════════════════════════════════

def get_access_token(appid: str, appsecret: str) -> str:
    """获取 access_token（有效期 2 小时，进程内使用不缓存）"""
    url = (
        f"{API_BASE}{API_PATH}/token?"
        f"grant_type=client_credential&appid={appid}&secret={appsecret}"
    )
    data = _api_get(url)
    if "access_token" not in data:
        errcode = data.get("errcode", -1)
        hint = ""
        if errcode in (40013, 40125, 40164):
            hint = "（AppID/AppSecret 错误或 IP 未加白名单）"
        elif errcode == -1:
            hint = f"（系统繁忙或网络问题: {data}）"
        err(f"获取 access_token 失败: errcode={errcode} {hint}")
    return data["access_token"]


def upload_cover(token: str, image_path: str) -> dict:
    """上传封面图为永久素材，返回 {media_id, url}"""
    log(f"上传封面: {image_path}")
    url = f"{API_BASE}{API_PATH}/material/add_material?access_token={token}&type=image"
    data = _upload_file(url, image_path)
    if "media_id" not in data:
        err(f"上传封面失败: {data}")
    ok(f"封面上传成功: media_id={data['media_id']}")
    return {"media_id": data["media_id"], "url": data.get("url", "")}


def upload_content_image(token: str, image_path: str) -> str:
    """上传正文图片到微信 CDN，返回永久 URL。

    使用 /cgi-bin/media/uploadimg 接口（专用于文章正文图片），
    返回 https://mmbiz.qpic.cn/... 格式永久 URL，可直接嵌在文章 HTML 中。

    限制: PNG ≤ 1MB, JPEG ≤ 10MB。PNG 超限自动转 JPEG 重试。
    """
    import shutil
    import tempfile

    path = Path(image_path)
    if not path.exists():
        err(f"图片不存在: {image_path}")

    file_size = path.stat().st_size
    upload_path = str(path)

    if path.suffix.lower() == ".png" and file_size > 1 * 1024 * 1024:
        log(f"PNG 超过 1MB ({file_size/1024:.0f}KB)，尝试转为 JPEG...")
        try:
            from PIL import Image as PILImage
        except ImportError:
            err(
                f"PNG 文件 {file_size/1024:.0f}KB 超过微信 1MB 限制。\n"
                "请安装 Pillow 以自动转换: pip install Pillow"
            )

        img = PILImage.open(path)
        if img.mode in ("RGBA", "P"):
            bg = PILImage.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = bg
        elif img.mode != "RGB":
            img = img.convert("RGB")

        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        img.save(tmp.name, "JPEG", quality=90)
        tmp.close()
        upload_path = tmp.name
        log(f"已转 JPEG: {Path(upload_path).stat().st_size/1024:.0f}KB")

    log(f"上传正文图片: {Path(upload_path).name}")
    api_url = f"{API_BASE}{API_PATH}/media/uploadimg?access_token={token}"
    data = _upload_file(api_url, upload_path)

    # 清理临时 JPEG 文件
    if upload_path != str(path):
        try:
            os.unlink(upload_path)
        except OSError:
            pass

    if "url" not in data:
        errcode = data.get("errcode", -1)
        errmsg = data.get("errmsg", str(data))
        err(f"上传正文图片失败: errcode={errcode} {errmsg}")

    url = data["url"]
    ok(f"正文图片上传成功: {url[:60]}...")
    return url


def replace_content_images(token: str, html: str, article_dir: Path) -> str:
    """替换 HTML 中本地图片路径为微信 CDN URL。

    扫描 <img src="illustrations/..."> 等本地相对路径，
    逐一上传到微信 /cgi-bin/media/uploadimg 并替换为 CDN URL。
    跳过已指向 http/https 的外部 URL。
    """
    import re

    # 匹配 src="非http/https开头的路径"（即本地相对路径）
    img_re = re.compile(
        r'(<img\b[^>]*?\ssrc\s*=\s*")((?!https?://)[^"]+)("[^>]*>)',
        re.IGNORECASE,
    )

    matches = img_re.findall(html)
    if not matches:
        log("正文中未发现本地图片，跳过上传")
        return html

    log(f"正文发现 {len(matches)} 张本地图片，开始上传...")
    replaced = 0

    def _replace(m: re.Match) -> str:
        nonlocal replaced
        prefix, img_path, suffix = m.group(1), m.group(2), m.group(3)
        full = (article_dir / img_path).resolve()
        if full.exists():
            try:
                cdn = upload_content_image(token, str(full))
                replaced += 1
                return f'{prefix}{cdn}{suffix}'
            except SystemExit:
                log(f"⚠ 上传失败，保留原路径: {img_path}")
                return m.group(0)
        else:
            log(f"⚠ 图片未找到，保留原路径: {img_path}")
            return m.group(0)

    result = img_re.sub(_replace, html)
    ok(f"正文图片处理完成: {replaced}/{len(matches)} 张已上传微信 CDN")
    return result


def create_draft(
    token: str,
    title: str,
    author: str,
    digest: str,
    content: str,
    thumb_media_id: str,
) -> str:
    """创建草稿，返回 media_id"""
    log("创建草稿...")
    url = f"{API_BASE}{API_PATH}/draft/add?access_token={token}"
    body = {
        "articles": [
            {
                "title": title,
                "author": author,
                "digest": digest,
                "content": content,
                "thumb_media_id": thumb_media_id,
                "need_open_comment": 0,
                "only_fans_can_comment": 0,
            }
        ]
    }
    data = _api_post_json(url, body)
    if "media_id" not in data:
        errcode = data.get("errcode", -1)
        errmsg = data.get("errmsg", str(data))
        hints = {
            40001: "access_token 无效或已过期",
            40007: "media_id 无效",
            40014: "access_token 无效",
            40132: "微信号不合法",
            41001: "缺少 access_token 参数",
            42001: "access_token 超时",
            44002: "POST 数据包为空",
            45009: "接口调用频率超限",
            45166: "正文内容包含不支持的标签或格式",
        }
        hint = hints.get(errcode, "")
        if hint:
            hint = f"（{hint}）"
        err(f"创建草稿失败: errcode={errcode} errmsg={errmsg} {hint}")
    ok(f"草稿创建成功: media_id={data['media_id']}")
    return data["media_id"]


# ═══════════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════════

def push(article_dir: str) -> dict:
    """一键推送到公众号草稿箱。

    参数:
        article_dir: 文章目录路径（含 final.md / output.html / cover/cover-combined.png）

    返回:
        {"success": True, "media_id": "xxx", "title": "..."}
    """
    article = Path(article_dir)
    if not article.is_dir():
        err(f"文章目录不存在: {article_dir}")

    # 1. 加载凭证
    config = load_env()
    appid = config["appid"]
    appsecret = config["appsecret"]
    wechat_author = config["author"]
    if not appid or not appsecret:
        err(
            "WECHAT_APPID 或 WECHAT_APPSECRET 未配置。\n"
            "请在项目根目录 .env 中设置:\n"
            "  WECHAT_APPID=wx1234567890\n"
            "  WECHAT_APPSECRET=your-secret\n\n"
            "获取方式: 公众号后台 → 设置与开发 → 基本配置"
        )

    # 2. 读取元数据
    final_md = article / "final.md"
    if not final_md.exists():
        err(f"未找到 final.md: {final_md}")

    frontmatter = _parse_frontmatter(final_md)
    title = frontmatter.get("title", article.parent.name)
    summary = frontmatter.get("summary", "")
    source_author = frontmatter.get("author", "")  # 视频原作者（仅记录用）

    # 公众号文章作者：优先用 .env 中配置的 WECHAT_AUTHOR，
    # 未配置则 fallback 到 final.md 的视频原作者
    author = wechat_author or source_author

    if not title:
        err("final.md 中未找到 title")
    if not author:
        log("未找到公众号作者名，请在 .env 中设置 WECHAT_AUTHOR=你的作者名")

    # 3. 读取正文
    output_html = article / "output.html"
    if not output_html.exists():
        err(f"未找到 output.html: {output_html}")
    content = output_html.read_text(encoding="utf-8")

    # 4. 封面
    cover_path = article / "cover" / "cover-combined.png"
    if not cover_path.exists():
        err(f"未找到封面图: {cover_path}")

    # 5. 换 token → 上传正文图片 → 上传封面 → 创建草稿
    log(f"文章: {title}")
    log(f"作者: {author or '(未设置)'}")
    token = get_access_token(appid, appsecret)
    content = replace_content_images(token, content, article)
    thumb = upload_cover(token, str(cover_path))
    media_id = create_draft(token, title, author, summary, content, thumb["media_id"])

    result = {
        "success": True,
        "media_id": media_id,
        "title": title,
        "author": author,
    }
    print(json.dumps(result, ensure_ascii=False))
    return result


def _parse_frontmatter(md_path: Path) -> dict:
    """解析 Markdown 文件的 YAML frontmatter"""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}

    end = text.find("---", 3)
    if end == -1:
        return {}

    raw = text[3:end].strip()
    result = {}
    for line in raw.split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key and val:
                result[key] = val
    return result


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python wechat_push.py <文章目录>", file=sys.stderr)
        print('示例: python wechat_push.py "outputs/DeepSeek价格战_2026-07-09/article"', file=sys.stderr)
        sys.exit(1)

    push(sys.argv[1])

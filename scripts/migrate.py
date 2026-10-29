# -*- coding: utf-8 -*-
"""
从静态镜像抽取文章 -> Astro content collection (Markdown)
用法: python scripts/migrate.py
"""
import os, re, json, shutil, hashlib, sys

SRC = r"E:\博客部署\zhanghan-blog-mirror"
DST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "content", "posts")
PUBLIC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
MEDIA = os.path.join(PUBLIC, "media")

def match_end(t, start):
    m = re.match(r"<([a-zA-Z0-9-]+)", t[start:])
    if not m: return -1
    tag = m.group(1)
    gt = t.find(">", start)
    if gt < 0: return -1
    depth = 1
    pat = re.compile(r"<(/?)" + re.escape(tag) + r"(?=[\s/>])", re.I)
    pos = gt + 1
    while True:
        mm = pat.search(t, pos)
        if not mm: return -1
        if mm.group(1) == "/":
            depth -= 1
            if depth == 0:
                return t.find(">", mm.end()) + 1
        else:
            g = t.find(">", mm.end())
            if g < 0: return -1
            if t[g - 1] != "/": depth += 1
        pos = mm.end()

def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

img_cache = {}
def localize_img(src):
    """把站内图片复制到 public/media，返回新路径"""
    if not src.startswith("/"):
        return src
    if src.startswith("/media/"):
        return src
    raw = src.split("?")[0].split("#")[0]
    path = os.path.normpath(os.path.join(SRC, raw.lstrip("/").replace("/", os.sep)))
    if not os.path.isfile(path):
        return src
    if raw in img_cache:
        return img_cache[raw]
    ext = os.path.splitext(path)[1].lower() or ".bin"
    name = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12] + ext
    os.makedirs(MEDIA, exist_ok=True)
    shutil.copy2(path, os.path.join(MEDIA, name))
    out = "/media/" + name
    img_cache[raw] = out
    return out

def clean_body(html):
    # 去掉脚本与锚点
    html = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    html = re.sub(r"<link[^>]*>", "", html)
    html = re.sub(r'<a class="anchor"[^>]*>.*?</a>', "", html, flags=re.S)
    # 去掉 astro 作用域属性与 pagefind 标记
    html = re.sub(r'\s+data-astro-cid-[a-z0-9]+="[^"]*"', "", html)
    html = re.sub(r'\s+data-pagefind-[\w-]+="[^"]*"', "", html)
    html = re.sub(r'\s+data-astro-cid-[a-z0-9]+', "", html)
    # 图片本地化
    def sub_img(m):
        attr, url = m.group(1), m.group(2)
        return f'{attr}="{localize_img(url)}"'
    html = re.sub(r'src="(/(?:_external|assets|_astro)/[^"]+)"', lambda m: f'src="{localize_img(m.group(1))}"', html)
    # 压缩多余空白
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()

def extract_title(t):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
    if m:
        try:
            d = json.loads(m.group(1))
            return d.get("headline") or "", d.get("description") or "", d.get("keywords") or [], d.get("datePublished") or ""
        except Exception:
            pass
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    title = re.sub(r"\s*-\s*.*$", "", m.group(1)).strip() if m else ""
    d = re.search(r'<meta name="description" content="([^"]*)"', t)
    return title, (d.group(1) if d else ""), [], ""

def main():
    if not os.path.isdir(SRC):
        print("找不到镜像目录:", SRC); sys.exit(1)
    count = 0; skipped = 0
    for dp, _, fn in os.walk(os.path.join(SRC, "posts")):
        if "index.html" not in fn: continue
        page = os.path.join(dp, "index.html")
        rel = os.path.relpath(dp, os.path.join(SRC, "posts")).replace(os.sep, "/")
        if rel.count("/") == 0:  # 分类列表页
            continue
        t = open(page, encoding="utf-8", errors="ignore").read()
        title, desc, tags, date = extract_title(t)
        if not title or not date:
            skipped += 1; continue

        mbody = re.search(r'<div[^>]*data-pagefind-body[^>]*class="[^"]*prose', t)
        if not mbody:
            mbody = re.search(r'<div[^>]*class="[^"]*prose[^"]*"[^>]*data-pagefind-body', t)
        if not mbody:
            skipped += 1; continue
        s = mbody.start(); e = match_end(t, s)
        if e < 0:
            skipped += 1; continue
        body = clean_body(t[t.find(">", s) + 1:e - len("</div>")])

        parts = rel.split("/")
        category = "/".join(parts[:-1]) or "未分类"
        slug = parts[-1]
        # 首图作为封面
        cover = ""
        m = re.search(r'<img[^>]+src="(/media/[^"]+)"', body)
        if m: cover = m.group(1)

        fm = ["---",
              f"title: {yaml_str(title)}",
              f"date: {date}",
              f"category: {yaml_str(category)}",
              f"description: {yaml_str(desc)}",
              f"tags: [{', '.join(yaml_str(x) for x in tags)}]"]
        if cover:
            fm.append(f"cover: {yaml_str(cover)}")
        fm.append("---")
        out_dir = os.path.join(DST, os.path.dirname(rel).replace("/", os.sep))
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, slug + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + "\n\n" + body + "\n")
        count += 1

    print(f"导出 {count} 篇，跳过 {skipped} 篇；图片 {len(img_cache)} 张 -> public/media")

if __name__ == "__main__":
    main()

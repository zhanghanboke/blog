# 全站全量检查：扫描 dist 内所有 HTML 的内部链接与资源引用，报告 404
import os, re, sys
from urllib.parse import unquote
from collections import defaultdict

DIST = r'E:\博客部署\astro-rebuild\dist'
# 子路径部署时产物里的站内链接都带 base 前缀（如 /blog/posts/），
# 但磁盘上文件仍在 dist/posts/，解析前必须先剥掉，否则全部误报 404。
BASE = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else ''

broken = defaultdict(set)   # 目标 -> 引用页面集合
external_skip = 0
checked_links = 0
checked_assets = 0

attr_re = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"')

def resolve_dist(path: str):
    # 站内路径解析到 dist：目录路径 -> index.html；URL 先 percent 解码
    path = unquote(path)
    if BASE and (path == BASE or path.startswith(BASE + '/')):
        path = path[len(BASE):] or '/'
    if path.endswith('/'):
        return os.path.join(DIST, path.lstrip('/').replace('/', os.sep), 'index.html')
    return os.path.join(DIST, path.lstrip('/').replace('/', os.sep))

def exists_for(path: str) -> bool:
    p = resolve_dist(path)
    if os.path.isfile(p):
        return True
    base, ext = os.path.splitext(p)
    if not ext:
        # 无扩展名路由：/x -> /x/index.html 或 /x.html
        if os.path.isfile(os.path.join(p, 'index.html')):
            return True
        if os.path.isfile(p + '.html'):
            return True
    return False

html_files = []
for root, _, files in os.walk(DIST):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for hf in html_files:
    try:
        text = open(hf, encoding='utf-8', errors='ignore').read()
    except Exception:
        continue
    rel = os.path.relpath(hf, DIST).replace(os.sep, '/')
    for m in attr_re.finditer(text):
        url = m.group(1).strip()
        if not url or url.startswith('#') or url.startswith('data:') or url.startswith('mailto:') or url.startswith('javascript:'):
            continue
        if url.startswith('http://') or url.startswith('https://') or url.startswith('//'):
            external_skip += 1
            continue
        if not url.startswith('/'):
            continue  # 相对路径（极少）
        url = url.split('#')[0].split('?')[0]
        if not url:
            continue
        if url.rsplit('/', 1)[-1].count('.'):
            checked_assets += 1
        else:
            checked_links += 1
        if not exists_for(url):
            broken[url].add(rel)

print(f'HTML 页面数: {len(html_files)}')
print(f'内部路由链接检查: {checked_links}, 内部资源引用检查: {checked_assets}, 外链跳过: {external_skip}')
print(f'失效目标数: {len(broken)}')
for target, pages in sorted(broken.items()):
    ps = sorted(pages)
    print(f'  [404] {target}  <- 被 {len(pages)} 页引用, 如: {ps[0]}')
sys.exit(0)

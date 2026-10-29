#!/usr/bin/env python3
"""
检查构建产物里是否还有「没加 base 前缀」的站内绝对路径。

子路径部署（GitHub Pages 项目仓库）时，所有以 / 开头、但没带 base 的
站内链接/资源都会 404。Astro 只会自动给 _astro 下的产物加前缀。

用法: python scripts/audit-base.py [base]
"""
import re
import sys
from pathlib import Path

BASE = sys.argv[1] if len(sys.argv) > 1 else '/blog'
DIST = Path(__file__).resolve().parent.parent / 'dist'

# 匹配 HTML/JS/CSS 里以 / 开头的路径
PAT = re.compile(r'''(?:href=|src=|poster=|data-src=|url\()\s*["'(]?(/[A-Za-z0-9_\-./%\u4e00-\u9fff]*)''')
CSS_URL = re.compile(r'url\((["\']?)(/[^)"\']+)')

EXTERNAL_OK = ('http://', 'https://', '//', 'data:', 'mailto:', 'tel:', '#')

bad = {}
scanned = 0

for f in DIST.rglob('*'):
    if not f.is_file():
        continue
    if f.suffix not in ('.html', '.js', '.css', '.json', '.xml', '.mjs'):
        continue
    try:
        text = f.read_text(encoding='utf-8')
    except Exception:
        continue
    scanned += 1

    found = []
    for m in PAT.finditer(text):
        p = m.group(1)
        if any(p.startswith(x) for x in EXTERNAL_OK):
            continue
        if p == BASE or p.startswith(BASE + '/'):
            continue          # 已经加了前缀，正确
        found.append(p)
    for m in CSS_URL.finditer(text):
        p = m.group(2)
        if any(p.startswith(x) for x in EXTERNAL_OK):
            continue
        if p == BASE or p.startswith(BASE + '/'):
            continue
        found.append(p)

    if found:
        bad[str(f.relative_to(DIST))] = sorted(set(found))

print(f'扫描文件: {scanned}')
print(f'base 前缀: {BASE}')
if not bad:
    print('✅ 没有发现「未加前缀」的站内绝对路径')
else:
    print(f'⚠️  {len(bad)} 个文件仍有未加前缀的路径:')
    for k in sorted(bad)[:40]:
        items = bad[k][:6]
        more = f' …等 {len(bad[k])} 项' if len(bad[k]) > 6 else ''
        print(f'  {k}')
        for i in items:
            print(f'      {i}')
        if more:
            print(f'      {more}')

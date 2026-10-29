# 博客重建工程（Astro）

对原静态镜像（`E:\博客部署\zhanghan-blog-mirror`）的**源码级重建**：同一套视觉语言、同样的信息结构，但内容变成可维护的 Markdown，站点可构建、可迁移。

## 快速开始

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # 产物在 dist/
npm run preview    # 预览构建产物
```

> 依赖 Node ≥ 20（本机 22.22 可用）。Astro 固定在 5.x：7.x 要求 Node ≥ 22.23.4。

## 目录结构

```
astro-rebuild/
├─ src/
│  ├─ site.config.ts          # 站点身份 / 导航 / 功能开关（改这里最快）
│  ├─ content.config.ts       # 内容集合 schema
│  ├─ content/posts/          # 126 篇 Markdown，按「分类/文件名」分目录
│  ├─ layouts/BaseLayout.astro
│  ├─ components/             # Navbar / Sidebar / PostCard / Icon
│  ├─ pages/
│  │   ├─ index.astro         # 首页：hero + 最新文章 + 分类 + 标签
│  │   ├─ posts/index.astro   # 文章列表
│  │   ├─ posts/[...slug].astro # 详情（目录、上下篇、评论占位）
│  │   ├─ archive.astro       # 归档时间轴
│  │   ├─ categories/         # 分类总览 + 分类详情
│  │   ├─ tags/               # 标签墙 + 标签详情
│  │   ├─ search.astro        # 客户端搜索（Ctrl/⌘ + K）
│  │   ├─ about.astro / 404.astro
│  │   ├─ rss.xml.ts / sitemap.xml.ts
│  │   └─ search-index.json.ts
│  ├─ styles/global.css       # 设计令牌 + 全部样式（无 UI 框架）
│  └─ utils/posts.ts          # 排序、分类/标签聚合、链接工具
├─ public/media/              # 从原站抽取的 108 张正文配图
└─ scripts/migrate.py         # 迁移脚本：静态 HTML → Markdown
```

## 设计系统（对齐源站）

| 项 | 值 |
|---|---|
| 背景 | `#f7f7f8` / 暗色 `#0b0b0d` |
| 卡片 | `#fff` / `#141417`，1px 细线，圆角 14px |
| 强调色 | 靛紫 `#5b5bd6`（暗色 `#8b8bf0`），用于分区标记、分类 chip、链接 |
| 阴影 | 极轻：`0 1px 2px` 与 `0 10px 30px -18px` |
| 字体 | 系统 sans；等宽仅用于日期/编号/标签 |
| 布局 | 15.5rem 左栏 + 主列 + 15.5rem 右栏（≥1280px） |
| 列表 | 行式布局：左标题/摘要，右 16:9 缩略图，1px 分隔线 |
| 导航 | 悬浮胶囊，1px 边框 + 毛玻璃，选中项为白色胶囊 |
| 断点 | 1279（去目录）→ 1023（单列 + 抽屉）→ 639（紧凑） |

## 内容迁移

`scripts/migrate.py` 做了三件事：

1. 遍历原站 `posts/**/index.html`，从 JSON-LD 取 `headline / description / keywords / datePublished`；
2. 截取 `div[data-pagefind-body].prose` 的正文 HTML，去掉 Astro 作用域属性、脚本、标题锚点；
3. 把正文引用到的 `/_external/**` 图片复制到 `public/media/`（按 URL 哈希命名）并重写路径。

重新迁移：

```bash
npm run migrate
```

文章 frontmatter 约定：

```yaml
title: 标题
date: 2026-08-10
category: 技术分享
description: 摘要
tags: [CDN, Vercel]
cover: /media/xxx.png   # 可选，不填则卡片无图
draft: false            # true 时不出现在列表
```

## 与原站的对应关系

| 原站 | 重建后 | 说明 |
|---|---|---|
| 顶栏 8 组下拉菜单 | 4 组（主页/文章/归档/关于） | 原站其余菜单对应的是相册、番剧等已清空模块 |
| 左栏个人卡 + 日历 + 统计 | 个人卡 + 统计 + 最近更新 | 日历依赖文章日期索引，后续可加 |
| 文章瀑布流 + 无限滚动 | 网格列表一次渲染 | 126 篇无分页压力 |
| 文章页右栏目录 | 客户端生成目录 + 滚动高亮 | 正文是原始 HTML，构建期无法抽标题 |
| Pagefind 搜索 | 自建 JSON 索引 + 客户端过滤 | 原站索引只有 48 KB，实际不可用 |
| Waline 评论 | 占位块 | `site.config.ts` 里 `features.comments` 打开后接入 |
| 音乐/相册/番剧/朋友圈 | 未复刻 | 这些模块的内容已清空，无稳定数据源 |

## 阅读体验与内容组织

| 能力 | 说明 |
|---|---|
| 代码复制 | 悬停代码块右上角出现「复制」，基于 `navigator.clipboard` |
| 图片灯箱 | 正文图片点击放大，点空白或 Esc 关闭 |
| 阅读进度 | 顶部 3px 靛紫进度条，按滚动比例推进 |
| 回到顶部 | 滚动 600px 后右下角出现 |
| 相关文章 | 标签重合度 ×2 + 同分类，取前 3 篇 |
| 系列 | frontmatter 加 `series: 系列名`，同系列自动生成目录块 |
| 分页 | `/posts/` 每页 10 篇，`/posts/2/` … 自动生成 |
| 评论 | `Comments.astro`：填 `serverURL` 即加载 Waline，否则显示占位提示 |

启用评论只需两步：把 `src/site.config.ts` 的 `comments.serverURL` 改成你的 Waline 地址，再把 `features.comments` 设为 `true`。

## 三栏布局

- **左栏**：个人卡、天气、日历
- **中栏**：正文 / 列表
- **右栏**：今日一言、站点统计、最近更新（带缩略图）、标签云
- 文章详情页的右栏换成文章目录（TOC）
- ≤1279px 自动收起右栏，≤1023px 变单列 + 抽屉导航；左右栏都留了 9rem 底部内边距，避免被悬浮播放器挡住

## 侧栏：天气与日历

- **天气**：Open-Meteo 免费接口（无需 key），当前温度 + 天气现象 + 美国 AQI 等级；城市与经纬度在 `site.config.ts` 的 `weather` 里改；结果缓存 30 分钟，离线时显示「天气暂不可用」。
- **日历**：纯前端渲染，前后翻月；有文章的日期带小圆点，今天用强调色填充，点击某天在底部显示当天最新文章，没有则提示「这天没有更新」。

## 更新日志与音乐

### 更新日志 `/changelog/`

内容放在 `src/content/changelog/*.md`，frontmatter 三个字段：

```yaml
date: 2026-10-29
type: feat        # feat 功能新增 / perf 功能优化 / fix 问题修复
title: "首页横幅支持三图轮播"
```

正文就是卡片描述（支持 Markdown）。

**连线机制**（与源站同思路）：页面里有一层 `<svg class="changelog__wires">` 绝对定位覆盖在网格上；JS 读取网格列数，按行取「行尾卡片」和「下一行行首卡片」的矩形，画正交折线（`M x1 y1 V midY H x2 V y2`）并用 `<marker>` 打箭头。悬停某张卡时，按 `data-links` 找到关联卡片，用二次贝塞尔连接两者中心，配合 `stroke-dashoffset` 做描绘动画，并在曲线中点放一枚标签显示所属页面；其余卡片 `opacity: .3` 变暗。

`data-links` 是按 `area` 字段自动生成的（同一 area 取最近的 2 条），所以只要在 frontmatter 里写 `area: "文章页"`，同类改动就会自动连线。页面用 CSS `columns` 做三列瀑布流，类型决定左侧圆点与标签颜色（绿/蓝/红），移动端降为两列、单列。

### 音乐播放器

全站右下角悬浮，配置在 `src/site.config.ts`：

```ts
music: {
  enabled: true,
  playlist: [{ title, artist, src: '/music/xxx.mp3', cover: '/images/xxx.jpg' }],
}
```

- 音频放 `public/music/`，封面放 `public/images/`；
- 圆形封面（播放时旋转）、歌名/歌手、播放列表抽屉；
- 支持播放/暂停、上一首/下一首、点击进度条跳转、**列表循环 / 单曲循环**切换；
- 音量条 + 静音，音量记在 localStorage；
- 右侧竖排按钮带 tooltip：音乐面板、明暗主题、隐藏（隐藏后清 `dockHidden` 可恢复）；
- 默认桌面端展开、移动端收起，展开状态也记在 localStorage；
- 仓库自带一条 14 秒无版权示例音轨（`demo-ambient.wav`），换歌时删掉即可。

## 首页横幅

三张图放在 `public/images/banner/`，构建时已压成 WebP（1920 宽，约 120–260 KB）：

| 文件 | 用途 |
|---|---|
| `01.webp` | 樱花草地图（彩色） |
| `02.webp` | 黑白人物特写 |
| `03.webp` | 黑白人物 + 签名 |

- 轮播：6 秒自动切换，右下角有 `01 / 03` 计数与短横线指示器，可点击切换；
- 换图：同尺寸覆盖或改 `src/pages/index.astro` 里三个 `<img src>` 即可；
- 调高度：`global.css` 中 `.hero { height: min(84vh, 760px); }`；
- 单张预览：访问 `/?slide=1`（0 起）可直接停在第 N 张。

## 待办

- [ ] `site.config.ts` 填入正式域名、头像、社交链接
- [ ] 文章封面：目前取正文首图，建议单独准备 16:9 封面
- [ ] 首页横幅：如需竖屏版本，可另做 3 张 1200×1600 供移动端使用
- [ ] 评论：接入 Waline 后在详情页挂载
- [ ] 分页或无限滚动（文章超过 200 篇时）
- [ ] 图片：`public/media` 108 张，建议后续接入对象存储 + CDN

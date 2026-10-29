---
title: "Obsidian 插件：Slash Menu——写作时输入 / 就好"
date: 2026-08-15
category: "技术分享"
description: "一个写作向的 Obsidian 斜杠命令插件：输入 / 或 、 弹出命令卡片，插入标题、表格、代码块、Callout，支持拼音搜索，代码块内自动屏蔽，心流不断。"
tags: ["Obsidian", "插件", "效率工具", "写作"]
draft: true
---

<blockquote><p>现在我在 Obsidian 里写文章，想插个表格就敲 <code>/table</code>，想插标题就敲 <code>/h2</code>，手从头到尾不用离开键盘。</p></blockquote>
<section><h1 id="前言">前言</h1><p>写文章的时候最烦什么？对我来说是<strong>打断心流</strong>。</p><p>正写到一半，要插一个标题、一个表格、一段代码块，就得停下来动鼠标、找工具栏、点按钮、选格式……再回来，思路已经飘了。</p><p>其实很多编辑器早就解决了这个问题：思源笔记、Notion 都有「斜杠命令」——输入 <code>/</code>，弹出一个菜单，直接选。Obsidian 原生没有这个功能，于是我自己写了一个——<strong>Slash Menu</strong>。</p></section>
<section><h1 id="它做了什么">它做了什么</h1><p>一句话：<strong>在 Obsidian 里输入 <code>/</code>（中文输入法下按同一个键打出的是 <code>、</code>，也能触发），弹出可搜索的命令卡片，回车即插入</strong>。</p><p>20 个命令，分三组：</p>

<table><thead><tr><th>分组</th><th>命令</th></tr></thead><tbody><tr><td>标题</td><td>H1 ~ H6</td></tr><tr><td>块</td><td>表格（3×2）、代码块、引用、Callout、无序列表、有序列表、任务列表、分割线</td></tr><tr><td>内联格式</td><td>链接、图片、加粗、斜体、行内代码、删除线</td></tr></tbody></table><p>插入后光标会<strong>自动落在最该输入的地方</strong>：表格在第一格，代码块在中间空行，链接在 URL 处（粘贴即用），加粗在 <code>**</code> 中间。不用再手动挪光标。</p></section>
<section><h1 id="细节决定体验">细节决定体验</h1><section><h2 id="1-拼音都能搜">1. 拼音都能搜</h2><p>菜单实时过滤，搜索词覆盖了中文、英文、拼音全拼和首字母缩写——这是从思源笔记学的：</p><ul>
<li>输 <code>h2</code>、<code>二级标题</code>、<code>erjibiaoti</code>、<code>ejbt</code>，都能找到二级标题</li>
</ul><p>中文输入法打拼音的人（比如我）用缩写找命令是真的快。</p></section><section><h2 id="2-该安静的时候绝不打扰">2. 该安静的时候绝不打扰</h2><p>代码块、行内代码里输入 <code>/</code> <strong>不会</strong>触发菜单——写代码的时候不会被弹窗打断，这是用 CodeMirror 6 语法树判断的，不是简单看行首有没有三个反引号。</p></section><section><h2 id="3-行内任意位置可唤起">3. 行内任意位置可唤起</h2><p>不用特意回行首：当前行最后一个词是 <code>/xxx</code> 就能唤起，行中已有文字不会误触。Esc、左右方向键、删光触发词都会自动关闭菜单，不会赖着不走。</p></section><section><h2 id="4-标题替换不叠前缀">4. 标题替换不叠前缀</h2><p>在 <code>## 旧标题</code> 这一行选「标题 1」，会直接变成 <code># 旧标题</code>，而不是叠出 <code>## # 旧标题</code> 这种怪东西。</p></section></section>
<section><h1 id="安装">安装</h1><p>目前是个人维护的小工具，还没上 Obsidian 社区插件市场，手动装也就三步：</p><ol>
<li>从 <a href="https://github.com/zhanghanboke/obsidian-slash-menu" target="_blank" rel="noopener noreferrer">GitHub 仓库</a> 获取 <code>main.js</code>、<code>manifest.json</code>、<code>styles.css</code></li>
<li>拷贝到库目录 <code>.obsidian/plugins/slash-menu/</code></li>
<li>重启 Obsidian（或「重新加载应用」），在「设置 → 第三方插件」里启用</li>
</ol></section>
<section><h1 id="开发背后的故事">开发背后的故事</h1><p>这个插件的灵感来自思源笔记的斜杠菜单。看了思源的源码，它用的是<strong>自己画的浮层</strong>：keydown 监听 <code>/</code> 键、手写绝对定位、自己做上下键导航、还要专门处理中文输入法的组合态（<code>Process</code>/<code>229</code>）……光「什么时候关闭」就有一堆边角情况。</p><p>给 Obsidian 做的时候，我换了一条更稳的路：<strong>用官方 EditorSuggest API 当骨架</strong>——浮层跟随光标、上下键选择、回车确认、Esc 关闭全部由 Obsidian 内置，我只需要实现「触发检测、过滤、渲染、插入」四件事，出 bug 的面一下子就小了很多。</p><p>代码层面值得一提的：</p><ul>
<li>纯逻辑层（触发检测、过滤、插入模板）和 Obsidian API 完全解耦，<strong>27 个单元测试</strong>，跑测试不需要 Obsidian</li>
<li>插入模板统一用 NUL 字符标记光标落点，20 个命令共用一个「插入 + 定位」执行器，没有为每个命令各写一套插入代码</li>
<li>插入执行全程 try-catch，出问题会弹提示而不是静默失败</li>
</ul><p>开发中还修过一个隐蔽 bug：构建脚本的拷贝列表漏了 <code>styles.css</code>，功能全正常但样式不生效——「看着能跑、用着别扭」的那种问题。所以现在构建拷贝清单和验收清单都写进了仓库的开发规范里。</p></section>
<section><h1 id="最后">最后</h1><p>仓库地址：<a href="https://github.com/zhanghanboke/obsidian-slash-menu" target="_blank" rel="noopener noreferrer">github.com/zhanghanboke/obsidian-slash-menu</a></p><p>如果你也烦「写个字还要动鼠标」，欢迎试试，也欢迎提 issue 反馈想法。</p><p>毕竟，<strong>写文章的时间应该花在内容上，而不是花在找按钮上</strong>。</p></section>

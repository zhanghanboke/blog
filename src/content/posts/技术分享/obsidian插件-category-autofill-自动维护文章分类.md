---
title: "Obsidian 插件：Category Autofill——自动维护文章分类"
date: 2026-08-15
category: "技术分享"
description: "一个自动维护文章分类的 Obsidian 插件：category 自动等于所在文件夹名，新建文章自动带齐属性，只处理你指定的目录，安全可控。"
tags: ["Obsidian", "插件", "效率工具", "博客工作流"]
---

<blockquote><p>现在我在 Obsidian 里新建笔记，title、published、tags、category、description 会自动带好，写完直接同步到博客，从来不用回头补属性。</p></blockquote>
<section><h1 id="前言">前言</h1><p>我的博客文章一直在 Obsidian 里写，写完同步到仓库。文章多了之后有个很头疼的问题：<strong>分类（category）全靠手填</strong>。</p><p>忘了填？文章进了博客就缺分类；填错了？和目录结构对不上；改目录结构？所有文章的分类都要跟着改一遍……</p><p>于是我给 Obsidian 写了一个小插件——<strong>Category Autofill</strong>，让分类这件事彻底自动化。</p></section>
<section><h1 id="它做了什么">它做了什么</h1><p>一句话：<strong>把文章的 category 自动填充为它所在文件夹的名字</strong>。</p><ul>
<li><code>技术分享/xxx.md</code> → <code>category: 技术分享</code></li>
<li>把文章拖到别的文件夹 → category 自动跟着变</li>
<li>重命名文件夹 → 里面所有文章的 category 一次性更新</li>
</ul><p>除了自动填充，新建文章时它还会自动带上博客需要的属性：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="yaml"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">---</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#E6888F;--1:#AF4238">title</span><span style="--0:#ABB2BF;--1:#383A42">: </span><span style="--0:#98C379;--1:#387138">文件名</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#E6888F;--1:#AF4238">published</span><span style="--0:#ABB2BF;--1:#383A42">: </span><span style="--0:#D19A66;--1:#875D01">2026-08-15</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span style="--0:#E6888F;--1:#AF4238">tags</span><span style="--0:#ABB2BF;--1:#383A42">: []</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#E6888F;--1:#AF4238">category</span><span style="--0:#ABB2BF;--1:#383A42">: </span><span style="--0:#98C379;--1:#387138">所在文件夹名</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span style="--0:#E6888F;--1:#AF4238">description</span><span style="--0:#ABB2BF;--1:#383A42">: </span><span style="--0:#98C379;--1:#387138">""</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">---</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="---title: 文件名published: 2026-08-15tags: []category: 所在文件夹名description: &#x22;&#x22;---"><div></div></button></div></figure></div><p>这些属性全部可以在设置里改：可以加你自己的字段（比如 <code>author</code>），也可以改默认值，比如把 <code>description</code> 设成固定的开头。</p></section>
<section><h1 id="为什么要用">为什么要用</h1><section><h2 id="1-分类永远和目录一致">1. 分类永远和目录一致</h2><p>目录结构就是分类结构：改目录 = 改分类，不会再出现「文章在 A 文件夹但分类写着 B」的情况。</p></section><section><h2 id="2-新建文章零准备">2. 新建文章零准备</h2><p>在 Obsidian 里新建一篇笔记，几秒内就自动带齐了博客需要的所有属性。写完直接同步，不用回头补 frontmatter。</p></section><section><h2 id="3-批量修复历史文件">3. 批量修复历史文件</h2><p>命令面板执行「自动填充 category（全库）」，所有历史文章一次修完，结束后提示更新了多少、跳过了多少、失败了多少。命令幂等，重复执行无害。</p></section><section><h2 id="4-安全设计">4. 安全设计</h2><ul>
<li><strong>只处理你指定的「文章根目录」</strong>（默认 <code>content/posts</code>），目录外的文件一律不碰</li>
<li>新建文章时只补<strong>缺失</strong>的属性，已有内容不会被覆盖</li>
<li>隐藏目录（<code>.obsidian</code> 等）、非 md 文件自动跳过</li>
<li><code>category</code> 已经等于文件夹名时不写入，文件零改动</li>
</ul></section></section>
<section><h1 id="安装">安装</h1><p>目前是个人维护的小工具，还没上 Obsidian 社区插件市场，手动装也就三步：</p><ol>
<li>从 <a href="https://github.com/zhanghanboke/obsidian-category-autofill" target="_blank" rel="noopener noreferrer">GitHub 仓库</a> 获取 <code>main.js</code> 和 <code>manifest.json</code></li>
<li>拷贝到库目录 <code>.obsidian/plugins/category-autofill/</code></li>
<li>重启 Obsidian（或「重新加载应用」），在「设置 → 第三方插件」里启用</li>
</ol><p>设置页有四个选项：「文章根目录」「覆盖已有的 category 值」「新建文章时自动添加属性」「新建文章属性模板」。</p></section>
<section><h1 id="开发背后的故事">开发背后的故事</h1><p>这个插件一开始并没有「文章根目录」限制——第一版是全库生效的。结果在真实库里跑了一次批量修复，把相册、书评、changelog 全加上了分类，误改了 275 个文件，最后靠 git 回退才救回来。</p><p>这个教训直接变成了插件的核心设计：<strong>默认只处理 <code>content/posts</code>，其他目录一概不碰</strong>。自动化工具的第一原则是别帮倒忙——现在它很「胆小」，但这种胆小正是写博客的人需要的。</p><p>代码层面也值得一提：frontmatter 读写全部走 Obsidian 官方 API（<code>processFrontMatter</code>），没有手写任何 YAML 解析；纯逻辑部分带 22 个单元测试；零运行时依赖。</p></section>
<section><h1 id="最后">最后</h1><p>仓库地址：<a href="https://github.com/zhanghanboke/obsidian-category-autofill" target="_blank" rel="noopener noreferrer">github.com/zhanghanboke/obsidian-category-autofill</a></p><p>如果你也有「文章分类靠手填」的困扰，或者对自动化的博客工作流感兴趣，欢迎试试，也欢迎提 issue 反馈想法。</p><p>毕竟，<strong>写文章的时间应该花在内容上，而不是花在填表格上</strong>。</p></section>

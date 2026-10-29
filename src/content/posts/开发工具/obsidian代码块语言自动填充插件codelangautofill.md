---
title: "Obsidian代码块语言自动填充插件 Code Lang Autofill"
date: 2026-08-18
category: "开发工具"
description: "一个 Obsidian 插件：自动识别没有语言标签的代码块并补上语言标签（python/java/c…），识别没把握的块一律跳过不填，还配了「记住上次语言」和代码块右下角的选语言按钮。"
tags: ["obsidian", "插件", "开发工具"]
---

<section><h2 id="为什么需要它">为什么需要它</h2><p>在 Obsidian 里写技术笔记，最容易被忽略的就是代码块的语言标签。很多人（包括我）写起来是这样：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="markdown"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">```</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">print("Hello")</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">```</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="&#x60;&#x60;&#x60;print(&#x22;Hello&#x22;)&#x60;&#x60;&#x60;"><div></div></button></div></figure></div><p>反引号后面空空的。后果是：代码块没有语法高亮、渲染成一片灰，复制代码块时格式也不友好——但真相往往是你<strong>只是忘了打那四个字母</strong>，并不是不想打。手动补又费劲，尤其是连续贴好几段不同语言的代码时。</p><p>这个插件就是干这件事的：<strong>自动识别代码块内容，把语言标签补上去</strong>。</p></section>
<section><h2 id="它帮你做什么">它帮你做什么</h2><section><h3 id="1-自动识别自动补全">1. 自动识别、自动补全</h3><p>打开笔记、保存、或者在编辑器里输入时，插件会自动扫描<strong>没有语言标签</strong>的代码块，识别出内容属于哪种语言，然后补上去：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="markdown"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E5C07B">```</span><span style="--0:#98C379">          →   </span><span style="--0:#E5C07B">```</span></span><span style="--0:#ABB2BF;--1:#383A42"> python</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">def greet(name):</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">print(f"hi, {name}")</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E5C07B">```</span><span style="--0:#98C379">              </span><span style="--0:#E5C07B">```</span></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="&#x60;&#x60;&#x60;          →   &#x60;&#x60;&#x60; pythondef greet(name):    print(f&#x22;hi, {name}&#x22;)&#x60;&#x60;&#x60;              &#x60;&#x60;&#x60;"><div></div></button></div></figure></div><p>内置了 20+ 种常见语言的特征识别：Python / Java / C / C++ / C# / JavaScript / TypeScript / Go / Rust / PHP / Ruby / SQL / HTML / XML / CSS / Bash / Dockerfile / PowerShell / JSON / YAML / Markdown / Lua / Kotlin / Swift 等。</p></section><section><h3 id="2-记住上次使用的语言">2. 记住上次使用的语言</h3><p>你是不是经常一段笔记里连续贴好几个同语言的代码块？插件会记住你最近一次使用的语言，新建的空代码块会自动带出来：</p><blockquote><p>刚写完一个 <code>python</code> 块，再敲一个 <code>```</code>+回车，新代码块自动变成 <code>``` python</code>。</p></blockquote></section><section><h3 id="3-识别没把握时右下角一键手动选">3. 识别没把握时，右下角「⌄」一键手动选</h3><p>自动识别毕竟是启发式的，遇到太短、太像普通文本、或者两种语言特征相近的代码，它拿不准就会<strong>跳过不填</strong>（这是它故意保守，等下说）。</p><p>这时候就该手动出场：每个<strong>没填语言的代码块右下角</strong>会有一个小小的「⌄」按钮，点一下弹出语言列表直接选。列表还做了三层排序，基本不需要翻：</p><ul>
<li>高置信度「· 检测建议」→ 拿不准但猜得出来的「· 可能」</li>
<li>→ 最近用过的语言 → 字母序</li>
</ul><p>所以想补一个 SQL 块，点一下，列表第一行往往就是它，回车完事，比手打快得多。</p></section></section>
<section><h2 id="安全设计它不会搞乱你的笔记">安全设计：它不会搞乱你的笔记</h2><p>这是我最看重的一点，也是它敢自动改文件的基础：</p><ol>
<li><strong>绝不碰已有标签</strong>：已经写了 <code>```python</code> 的块，动都不会动。</li>
<li><strong>没把握就跳过</strong>：识别置信度不够的块一律不填，宁可空着，绝不填错。</li>
<li><strong>只改开栏行</strong>：只在三个反引号后面补一个语言 token，<strong>代码内容一个字符都不改</strong>。</li>
<li><strong>可撤销</strong>：每个改动都是一次独立编辑，<code>Ctrl+Z</code> 能逐条撤销。</li>
<li><strong>幂等</strong>：已经填过的块，再跑多少次都不会被改动。</li>
<li>只作用于你设置的处理目录（默认 <code>content/posts</code>），目录外的笔记一个不碰。</li>
</ol><p>一句话：<strong>宁缺毋滥</strong>。它可能有时候漏填，但不会乱填。</p></section>
<section><h2 id="使用">使用</h2><p>启用后重载 Obsidian（<code>Ctrl+P</code> →「重新加载应用」），在设置 → 第三方插件里打开 <strong>Code Lang Autofill</strong> 即可。</p><p>设置项只有三个（都很直观）：</p>

<table><thead><tr><th>设置</th><th>默认</th><th>说明</th></tr></thead><tbody><tr><td>处理目录</td><td><code>content/posts</code></td><td>只处理该目录下的 md 文件；留空 = 整个库</td></tr><tr><td>自动补全</td><td>开</td><td>打开/保存/输入时自动补全；关闭后仅手动命令与按钮生效</td></tr><tr><td>新建代码块自动带出上次语言</td><td>开</td><td>新建空代码块自动填上最近一次语言</td></tr></tbody></table><p>命令也保留了（不想走自动路径时）：</p><ul>
<li>「补全当前笔记的代码块语言」</li>
<li>「补全全库（处理目录内）代码块语言」</li>
<li>「为当前代码块选择语言」</li>
</ul></section>
<section><h2 id="为什么我敢把它做成自动改文件">为什么我敢把它做成”自动改文件”</h2><p>市面上类似思路的插件不少，但很多是<strong>无脑填</strong>，或者检测差口气。Code Lang Autofill 把「识别」和「写入」分成了两层：</p><ul>
<li><strong>识别层</strong>：自研启发式 + 置信度评分，每个语言一整套特征规则；拿不准就返回”空白”，绝不硬猜。</li>
<li><strong>写入层</strong>：接一层”插入点”再落笔，只落在开栏行的反引号后，天然可撤销、幂等。</li>
</ul><p>识别层是纯逻辑、连 Obsidian API 都不碰，可以脱离 UI 直接做单元测试——整套行为（解析、易混语言判别、幂等、低置信度跳过）都用测试钉死了，这也是它有底气”自动改”的原因。</p></section>
<section><h2 id="已知边界--小提示">已知边界 &#x26; 小提示</h2><ul>
<li>启发式识别不是 100%：太短的块、纯命令输出、两种语言特征太接近时，它选择跳过（安全优先）。这种时候右下角「⌄」点一下就行。</li>
<li>「记住上次语言」在”连续写同语言”的场景很好用；但如果刚写完 Python 就往新块里贴了一段 SQL，新块会被先标成 python——注意一下，用「⌄」一键改回来即可，代价很小。</li>
</ul></section>
<section><h2 id="项目">项目</h2><ul>
<li>开源、零运行时依赖，GitHub：<a href="https://github.com/zhanghanboke/obsidian-code-lang-autofill" target="_blank" rel="noopener noreferrer">https://github.com/zhanghanboke/obsidian-code-lang-autofill</a></li>
<li>欢迎使用后反馈识别不准的代码块样本，规则表就是靠真实样本一点点喂出来的。</li>
</ul><p>如果你也经常为代码块没有语言标签而烦恼，装上试试，从此 ``` 后面的语言，基本不用自己打了。</p></section>

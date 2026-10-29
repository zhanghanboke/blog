---
title: "JS事件监听"
date: 2026-05-15
category: "javawebai/前端基础"
description: "使用addEventListener为DOM元素绑定事件实现用户交互"
tags: ["前端", "JavaScript"]
---

<section><h1 id="js事件监听">JS事件监听</h1><section><h2 id="定义">定义</h2><p>事件监听是将函数绑定到HTML元素上的特定事件，当事件触发时自动执行对应的函数。事件是发生在HTML元素上的”事情”，如按钮点击、鼠标移动、键盘按下等。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="addeventlistener推荐">addEventListener（推荐）</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 语法：事件源.addEventListener('事件类型', 要执行的函数)</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E5C07B">document</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#61AFEF;--1:#3360C1">querySelector</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">"#btn1"</span><span style="--0:#ABB2BF;--1:#383A42">).</span><span style="--0:#61AFEF;--1:#3360C1">addEventListener</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">'click'</span><span style="--0:#ABB2BF;--1:#383A42">, () </span><span style="--0:#CD89E1;--1:#A626A4">=></span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent">    </span><span style="--0:#61AFEF;--1:#3360C1">alert</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">"按钮被点击了..."</span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">});</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// 语法：事件源.addEventListener(&#x27;事件类型&#x27;, 要执行的函数)document.querySelector(&#x22;#btn1&#x22;).addEventListener(&#x27;click&#x27;, () => {    alert(&#x22;按钮被点击了...&#x22;);});"><div></div></button></div></figure></div></section><section><h3 id="dom元素事件属性早期方式">DOM元素事件属性（早期方式）</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E5C07B">document</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#61AFEF;--1:#3360C1">querySelector</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">'#btn1'</span><span style="--0:#ABB2BF;--1:#383A42">).</span><span style="--0:#61AFEF;--1:#3360C1">onclick</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#CD89E1;--1:#A626A4">function</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent">    </span><span style="--0:#61AFEF;--1:#3360C1">alert</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">"按钮被点击了..."</span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">};</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="document.querySelector(&#x27;#btn1&#x27;).onclick = function() {    alert(&#x22;按钮被点击了...&#x22;);};"><div></div></button></div></figure></div></section><section><h3 id="html标签事件属性">HTML标签事件属性</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">input</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">type</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"button"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">onclick</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"</span><span style="--0:#61AFEF;--1:#3360C1">on</span><span style="--0:#98C379;--1:#383A42">()</span><span style="--0:#98C379;--1:#387138">"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<input type=&#x22;button&#x22; onclick=&#x22;on()&#x22;>"><div></div></button></div></figure></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li><strong>click</strong>：按钮点击、链接点击</li>
<li><strong>mouseenter / mouseleave</strong>：鼠标悬停效果，如隔行变色</li>
<li><strong>keydown / keyup</strong>：键盘快捷键、输入验证</li>
<li><strong>blur / focus</strong>：表单输入验证</li>
<li><strong>input</strong>：实时搜索、字符计数</li>
<li><strong>submit</strong>：表单提交前的数据验证</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li><strong>addEventListener vs on事件</strong>：
<ul>
<li><code>on</code>方式会被覆盖（重复绑定只保留最后一个）</li>
<li><code>addEventListener</code>可以绑定多次，拥有更多特性</li>
<li>推荐使用<code>addEventListener</code></li>
</ul>
</li>
<li><strong>常见错误</strong>：
<ul>
<li>获取DOM元素时在元素渲染之前执行（应将脚本放在body底部或使用DOMContentLoaded）</li>
<li>事件类型名称大小写敏感（如”click”不能写成”Click”）</li>
</ul>
</li>
<li><strong>事件冒泡</strong>：默认事件会冒泡到父元素，可以通过<code>event.stopPropagation()</code>阻止</li>
<li><strong>事件委托</strong>：通过父元素监听子元素事件，提高性能</li>
</ol></section></section>

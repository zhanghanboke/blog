---
title: "JS变量与常量"
date: 2026-05-15
category: "javawebai/前端基础"
description: "JavaScript中let、const和var三种变量声明方式及其作用域差异"
tags: ["前端", "JavaScript"]
---

<section><h1 id="js变量与常量">JS变量与常量</h1><section><h2 id="定义">定义</h2><p>JavaScript中的变量用于存储数据值，可以存放不同类型的值。常量用于存储不可变的值，一旦声明就不能重新赋值。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="变量声明">变量声明</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 使用let关键字声明变量</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#CD89E1;--1:#A626A4">let</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E6888F">a</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">20</span><span style="--0:#ABB2BF;--1:#383A42">;</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E6888F">a</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">"Hello"</span><span style="--0:#ABB2BF;--1:#383A42">;  </span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// JavaScript是弱类型语言，变量可以重新赋值为不同类型</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code">
</div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 早期使用var声明变量（不推荐）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span style="--0:#CD89E1;--1:#A626A4">var</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E6888F">name</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">"A"</span><span style="--0:#ABB2BF;--1:#383A42">;</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E6888F">name</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">"B"</span><span style="--0:#ABB2BF;--1:#383A42">;</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">8</div></div><div class="code"><span style="--0:#CD89E1;--1:#A626A4">var</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E6888F">name</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">"C"</span><span style="--0:#ABB2BF;--1:#383A42">;  </span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// var可以重复声明</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// 使用let关键字声明变量let a = 20;a = &#x22;Hello&#x22;;  // JavaScript是弱类型语言，变量可以重新赋值为不同类型// 早期使用var声明变量（不推荐）var name = &#x22;A&#x22;;name = &#x22;B&#x22;;var name = &#x22;C&#x22;;  // var可以重复声明"><div></div></button></div></figure></div></section><section><h3 id="常量声明">常量声明</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 使用const关键字声明常量</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#CD89E1;--1:#A626A4">const</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#E5C07B;--1:#875D01">PI</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">3.14</span><span style="--0:#ABB2BF;--1:#383A42">;</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// PI = 3.15;  // 错误：常量不能被重新赋值</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// 使用const关键字声明常量const PI = 3.14;// PI = 3.15;  // 错误：常量不能被重新赋值"><div></div></button></div></figure></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li>
<p><strong>变量使用场景</strong>：</p>
<ul>
<li>存储用户输入</li>
<li>临时存储计算结果</li>
<li>循环计数器</li>
<li>动态数据存储</li>
</ul>
</li>
<li>
<p><strong>常量使用场景</strong>：</p>
<ul>
<li>数学常数（π、e等）</li>
<li>配置参数</li>
<li>枚举值</li>
<li>不会改变的应用设置</li>
</ul>
</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li>
<p><strong>变量命名规则</strong>：</p>
<ul>
<li>组成字符可以是字母、数字、下划线(_)或美元符号($)</li>
<li>数字不能开头</li>
<li>严格区分大小写</li>
<li>不能使用关键字作为变量名（如let、if、for等）</li>
</ul>
</li>
<li>
<p><strong>let vs var</strong>：</p>
<ul>
<li><code>let</code>是ES6引入的块级作用域变量声明</li>
<li><code>var</code>存在变量提升和重复声明问题，不推荐使用</li>
<li><code>let</code>不能重复声明，更安全</li>
</ul>
</li>
<li>
<p><strong>const注意事项</strong>：</p>
<ul>
<li>常量必须在声明时初始化</li>
<li>常量不能被重新赋值</li>
<li>对于对象和数组，const保证的是引用不变，但对象属性和数组元素可以修改</li>
</ul>
</li>
<li>
<p><strong>作用域差异</strong>：</p>
<ul>
<li><code>let</code>和<code>const</code>是块级作用域</li>
<li><code>var</code>是函数作用域</li>
</ul>
</li>
</ol></section></section>

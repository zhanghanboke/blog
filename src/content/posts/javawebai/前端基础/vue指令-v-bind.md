---
title: "Vue指令-v-bind"
date: 2026-05-15
category: "javawebai/前端基础"
description: "使用v-bind（简写:）动态绑定HTML标签的属性和样式"
tags: ["前端", "Vue"]
---

<section><h1 id="vue指令-v-bind">Vue指令-v-bind</h1><section><h2 id="定义">定义</h2><p><code>v-bind</code>指令用于动态绑定HTML标签的属性值，如href、src、style、class等。它可以将Vue实例中的数据绑定到HTML元素的属性上。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="完整语法">完整语法</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">img</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">v-bind:src</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"item.image"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">width</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"30px"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<img v-bind:src=&#x22;item.image&#x22; width=&#x22;30px&#x22;>"><div></div></button></div></figure></div></section><section><h3 id="简化语法推荐">简化语法（推荐）</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">img</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:src</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"item.image"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">width</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"30px"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<img :src=&#x22;item.image&#x22; width=&#x22;30px&#x22;>"><div></div></button></div></figure></div></section><section><h3 id="绑定class和style">绑定class和style</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">&#x3C;!-- 绑定class --></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">div</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:class</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"{ active: isActive, 'text-danger': hasError }"</span><span style="--0:#ABB2BF;--1:#383A42">>&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">div</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code">
</div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">&#x3C;!-- 绑定style --></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">div</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:style</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"{ color: activeColor, fontSize: fontSize + 'px' }"</span><span style="--0:#ABB2BF;--1:#383A42">>&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">div</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<!-- 绑定class --><div :class=&#x22;{ active: isActive, &#x27;text-danger&#x27;: hasError }&#x22;></div><!-- 绑定style --><div :style=&#x22;{ color: activeColor, fontSize: fontSize + &#x27;px&#x27; }&#x22;></div>"><div></div></button></div></figure></div></section><section><h3 id="绑定多个属性">绑定多个属性</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">a</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:href</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"url"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:title</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"title"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:target</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"target"</span><span style="--0:#ABB2BF;--1:#383A42">>链接&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">a</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<a :href=&#x22;url&#x22; :title=&#x22;title&#x22; :target=&#x22;target&#x22;>链接</a>"><div></div></button></div></figure></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li><strong>动态图片路径</strong>：根据数据动态显示图片</li>
<li><strong>动态链接</strong>：根据条件生成不同的URL</li>
<li><strong>样式绑定</strong>：根据状态动态改变元素样式</li>
<li><strong>类名绑定</strong>：根据条件添加或移除CSS类</li>
<li><strong>表单属性</strong>：动态设置input的disabled、checked等属性</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li>
<p><strong>数据源要求</strong>：</p>
<ul>
<li><code>v-bind</code>绑定的数据必须在<code>data()</code>中定义</li>
<li>或基于<code>data()</code>中定义的数据计算而来</li>
</ul>
</li>
<li>
<p><strong>简写形式</strong>：</p>
<ul>
<li><code>:属性名="属性值"</code>是<code>v-bind:属性名="属性值"</code>的简写</li>
<li>推荐使用简写形式，代码更简洁</li>
</ul>
</li>
<li>
<p><strong>class和style绑定</strong>：</p>
<ul>
<li>可以绑定对象、数组或字符串</li>
<li>对象语法：键为类名，值为布尔值</li>
<li>数组语法：包含多个类名字符串</li>
</ul>
</li>
<li>
<p><strong>属性值类型</strong>：</p>
<ul>
<li>可以是字符串、数字、布尔值、对象或数组</li>
<li>Vue会自动进行类型转换</li>
</ul>
</li>
<li>
<p><strong>性能考虑</strong>：</p>
<ul>
<li>避免在绑定的表达式中进行复杂计算</li>
<li>复杂计算建议使用计算属性</li>
</ul>
</li>
</ol></section></section>

---
title: "Vue指令-v-for"
date: 2026-05-15
category: "javawebai/前端基础"
description: "使用v-for指令进行列表渲染，结合key属性实现高效DOM复用"
tags: ["前端", "Vue"]
---

<section><h1 id="vue指令-v-for">Vue指令-v-for</h1><section><h2 id="定义">定义</h2><p><code>v-for</code>指令用于列表渲染，遍历容器的元素或对象的属性。它可以根据数据源动态生成多个相同的HTML元素。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="基本语法">基本语法</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">tr</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">v-for</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"(item, index) in items"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:key</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"item.id"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">{{item.name}}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">tr</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<tr v-for=&#x22;(item, index) in items&#x22; :key=&#x22;item.id&#x22;>    {{item.name}}</tr>"><div></div></button></div></figure></div></section><section><h3 id="简化语法省略index">简化语法（省略index）</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">tr</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">v-for</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"item in items"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">:key</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"item.id"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">{{item.name}}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">tr</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<tr v-for=&#x22;item in items&#x22; :key=&#x22;item.id&#x22;>    {{item.name}}</tr>"><div></div></button></div></figure></div></section><section><h3 id="遍历对象属性">遍历对象属性</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">li</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">v-for</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"(value, key) in object"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">{{key}}: {{value}}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">li</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<li v-for=&#x22;(value, key) in object&#x22;>    {{key}}: {{value}}</li>"><div></div></button></div></figure></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li><strong>列表渲染</strong>：员工列表、商品列表、消息列表等</li>
<li><strong>表格数据展示</strong>：动态生成表格行</li>
<li><strong>导航菜单</strong>：根据权限动态生成菜单项</li>
<li><strong>下拉选项</strong>：动态生成select的option选项</li>
<li><strong>组件列表</strong>：渲染多个相同结构的组件</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li>
<p><strong>key的重要性</strong>：</p>
<ul>
<li>必须为每个遍历项添加唯一的<code>key</code>属性</li>
<li>推荐使用数据的唯一标识（如id）</li>
<li>不推荐使用index作为key（会变化，不对应）</li>
<li>key帮助Vue正确排序复用，提升渲染性能</li>
</ul>
</li>
<li>
<p><strong>数据源要求</strong>：</p>
<ul>
<li>遍历的数组必须在<code>data()</code>中定义</li>
<li>数据变化时视图会自动更新</li>
</ul>
</li>
<li>
<p><strong>作用域</strong>：</p>
<ul>
<li>在<code>v-for</code>内部可以访问父作用域的属性</li>
<li>每个遍历项都有自己的作用域</li>
</ul>
</li>
<li>
<p><strong>性能优化</strong>：</p>
<ul>
<li>避免在<code>v-for</code>内部使用复杂计算</li>
<li>大数据量时考虑虚拟滚动</li>
<li>使用<code>v-if</code>和<code>v-for</code>时，<code>v-if</code>的优先级更高</li>
</ul>
</li>
</ol></section><section><h2 id="相关链接">相关链接</h2><ul>
<li><a href="Vue%E6%A1%86%E6%9E%B6%E6%A6%82%E8%BF%B0.md">Vue框架概述</a></li>
<li><a href="Vue%E6%8C%87%E4%BB%A4-v-if%E4%B8%8Ev-show.md">Vue指令-v-if与v-show</a></li>
<li><a href="Vue%E6%8C%87%E4%BB%A4-v-bind.md">Vue指令-v-bind</a></li>
</ul></section></section>

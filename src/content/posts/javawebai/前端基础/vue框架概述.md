---
title: "Vue框架概述"
date: 2026-05-15
category: "javawebai/前端基础"
description: "Vue渐进式框架的核心概念：数据驱动视图与createApp创建应用"
tags: ["前端", "Vue"]
---

<section><h1 id="vue框架概述">Vue框架概述</h1><section><h2 id="定义">定义</h2><p>Vue是一款用于<strong>构建用户界面</strong>的<strong>渐进式</strong>JavaScript<strong>框架</strong>。它基于数据渲染出用户看到的界面，简化了DOM操作，提高了开发效率。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="vue应用创建">Vue应用创建</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="html"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">div</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">id</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"app"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">{{message}}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">div</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code">
</div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;</span><span style="--0:#E6888F;--1:#AF4238">script</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">type</span><span style="--0:#ABB2BF;--1:#383A42">=</span><span style="--0:#98C379;--1:#387138">"module"</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span class="indent">    </span><span style="--0:#CD89E1;--1:#A626A4">import</span><span style="--0:#ABB2BF;--1:#383A42"> { </span><span style="--0:#E6888F;--1:#AF4238">createApp</span><span style="--0:#ABB2BF;--1:#383A42"> } </span><span style="--0:#CD89E1;--1:#A626A4">from</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">'/_external/unpkg.com/vue@3/dist/vue.esm-browser.js'</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span class="indent">    </span><span style="--0:#61AFEF;--1:#3360C1">createApp</span><span style="--0:#ABB2BF;--1:#383A42">({</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">8</div></div><div class="code"><span class="indent">        </span><span style="--0:#61AFEF;--1:#3360C1">data</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">9</div></div><div class="code"><span class="indent">            </span><span style="--0:#CD89E1;--1:#A626A4">return</span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">10</div></div><div class="code"><span class="indent">                </span><span style="--0:#E6888F;--1:#AF4238">message</span><span style="--0:#ABB2BF;--1:#016C9A">:</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">'Hello Vue'</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">11</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">            </span></span><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">12</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">        </span></span><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">13</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">}).</span><span style="--0:#61AFEF;--1:#3360C1">mount</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">'#app'</span><span style="--0:#ABB2BF;--1:#383A42">)</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">14</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">&#x3C;/</span><span style="--0:#E6888F;--1:#AF4238">script</span><span style="--0:#ABB2BF;--1:#383A42">></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="<div id=&#x22;app&#x22;>    {{message}}</div>"><div></div></button></div></figure></div></section><section><h3 id="数据驱动视图">数据驱动视图</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// Vue实例中的数据</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#61AFEF;--1:#3360C1">data</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent">    </span><span style="--0:#CD89E1;--1:#A626A4">return</span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent">        </span><span style="--0:#E6888F;--1:#AF4238">message</span><span style="--0:#ABB2BF;--1:#016C9A">:</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">'Hello Vue'</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code">
</div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">8</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 模板中的插值表达式</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">9</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#ABB2BF">{{</span><span style="--0:#E6888F">message</span><span style="--0:#ABB2BF">}}</span></span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// Vue实例中的数据data() {    return {        message: &#x27;Hello Vue&#x27;    }}// 模板中的插值表达式{{message}}"><div></div></button></div></figure></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li><strong>构建用户界面</strong>：基于数据渲染出用户看到的界面</li>
<li><strong>局部模块改造</strong>：使用Vue改造现有项目的部分功能</li>
<li><strong>工程化开发</strong>：基于Vue核心包和插件进行整站开发</li>
<li><strong>数据绑定</strong>：实现数据与视图的自动同步更新</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li>
<p><strong>渐进式框架</strong>：</p>
<ul>
<li>不需要一次性学习所有特性</li>
<li>可以逐步引入Vue的功能</li>
<li>从简单到复杂逐步使用</li>
</ul>
</li>
<li>
<p><strong>Vue应用结构</strong>：</p>
<ul>
<li>必须通过<code>createApp()</code>创建Vue应用实例</li>
<li>数据必须定义在<code>data()</code>方法中</li>
<li>必须通过<code>mount()</code>方法挂载到DOM元素</li>
</ul>
</li>
<li>
<p><strong>插值表达式限制</strong>：</p>
<ul>
<li>只能写在Vue控制的区域内（如<code>#app</code>内部）</li>
<li>只能使用Vue中定义的数据</li>
<li>不能使用JavaScript语句</li>
</ul>
</li>
<li>
<p><strong>开发模式</strong>：</p>
<ul>
<li>局部模块改造：基于Vue核心包完成项目局部模块改造</li>
<li>工程化开发：基于Vue核心包、插件进行整站开发</li>
</ul>
</li>
</ol></section><section><h2 id="相关链接">相关链接</h2><ul>
<li><a href="Vue%E6%8C%87%E4%BB%A4-v-for.md">Vue指令-v-for</a></li>
<li><a href="Vue%E6%8C%87%E4%BB%A4-v-bind.md">Vue指令-v-bind</a></li>
<li><a href="Vue%E6%8C%87%E4%BB%A4-v-model.md">Vue指令-v-model</a></li>
<li><a href="Vue%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F.md">Vue生命周期</a></li>
</ul></section></section>

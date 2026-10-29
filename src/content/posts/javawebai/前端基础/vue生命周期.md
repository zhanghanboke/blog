---
title: "Vue生命周期"
date: 2026-05-15
category: "javawebai/前端基础"
description: "Vue实例从创建到销毁的8个阶段及mounted等钩子函数的应用"
tags: ["前端", "Vue"]
---

<section><h1 id="vue生命周期">Vue生命周期</h1><section><h2 id="定义">定义</h2><p>Vue生命周期是指Vue实例从创建到销毁的完整过程。它包含8个阶段，每个阶段会自动执行对应的生命周期方法（也称为钩子函数）。其中<code>mounted</code>是最常用的钩子函数。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="生命周期钩子使用">生命周期钩子使用</h3><div class="expressive-code"><div class="ec-collapse ec-collapse--collapsed" id="collapse-db3da58t9" data-collapse-preview-lines="8" data-expanded-announcement="代码块已展开" data-collapsed-announcement="代码块已折叠"><div class="ec-collapse__content"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#61AFEF;--1:#3360C1">createApp</span><span style="--0:#ABB2BF;--1:#383A42">({</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent">    </span><span style="--0:#61AFEF;--1:#3360C1">data</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent">        </span><span style="--0:#CD89E1;--1:#A626A4">return</span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent">            </span><span style="--0:#E6888F;--1:#AF4238">empList</span><span style="--0:#ABB2BF;--1:#016C9A">:</span><span style="--0:#ABB2BF;--1:#383A42"> []</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">        </span></span><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">},</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span class="indent">    </span><span style="--0:#E6888F;--1:#AF4238">methods</span><span style="--0:#ABB2BF;--1:#016C9A">:</span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">8</div></div><div class="code"><span class="indent">        </span><span style="--0:#CD89E1;--1:#A626A4">async</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#61AFEF;--1:#3360C1">search</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">9</div></div><div class="code"><span class="indent">            </span><span style="--0:#CD89E1;--1:#A626A4">const</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#E5C07B;--1:#875D01">result</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#CD89E1;--1:#A626A4">await</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E5C07B">axios</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#61AFEF;--1:#3360C1">get</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">'https://api.example.com/emps/list'</span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">10</div></div><div class="code"><span class="indent">            </span><span style="--0:#E5C07B;--1:#AF4238">this</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#E6888F;--1:#AF4238">empList</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E5C07B">result</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#E5C07B;--1:#AF4238">data</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#E6888F;--1:#AF4238">data</span><span style="--0:#ABB2BF;--1:#383A42">;</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">11</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">        </span></span><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">12</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">},</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">13</div></div><div class="code"><span class="indent">    </span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 生命周期钩子：挂载完成</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">14</div></div><div class="code"><span class="indent">    </span><span style="--0:#61AFEF;--1:#3360C1">mounted</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">15</div></div><div class="code"><span class="indent">        </span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 页面初始化自动加载数据</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">16</div></div><div class="code"><span class="indent">        </span><span style="--0:#E5C07B;--1:#AF4238">this</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">search</span><span style="--0:#ABB2BF;--1:#383A42">();</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">17</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">18</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">}).</span><span style="--0:#61AFEF;--1:#3360C1">mount</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">'#container'</span><span style="--0:#ABB2BF;--1:#383A42">)</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="createApp({    data() {        return {            empList: []        }    },    methods: {        async search() {            const result = await axios.get(&#x27;https://api.example.com/emps/list&#x27;);            this.empList = result.data.data;        }    },    // 生命周期钩子：挂载完成    mounted() {        // 页面初始化自动加载数据        this.search();    }}).mount(&#x27;#container&#x27;)"><div></div></button></div></figure><div class="ec-collapse__gradient" aria-hidden="true"></div></div><button class="ec-collapse__toggle" type="button" aria-expanded="false" aria-controls="collapse-db3da58t9"><span class="ec-collapse__text-expand">显示更多</span><span class="ec-collapse__text-collapse">显示更少</span><svg class="ec-collapse__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6"></path></svg></button></div></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li>
<p><strong>mounted（挂载完成）</strong>：</p>
<ul>
<li>页面初始化时自动请求后台数据</li>
<li>初始化第三方插件</li>
<li>获取DOM元素</li>
<li>设置定时器</li>
</ul>
</li>
<li>
<p><strong>created（创建完成）</strong>：</p>
<ul>
<li>初始化数据</li>
<li>非DOM相关操作</li>
</ul>
</li>
<li>
<p><strong>beforeUnmount（卸载前）</strong>：</p>
<ul>
<li>清理定时器</li>
<li>移除事件监听</li>
<li>取消未完成的请求</li>
</ul>
</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li>
<p><strong>mounted是重点</strong>：</p>
<ul>
<li>Vue初始化成功，HTML页面渲染成功</li>
<li>用于页面初始化时自动发送Ajax请求</li>
<li>此时可以访问DOM元素</li>
</ul>
</li>
<li>
<p><strong>生命周期顺序</strong>：</p>
<ul>
<li>beforeCreate → created → beforeMount → mounted</li>
<li>beforeUpdate → updated</li>
<li>beforeUnmount → unmounted</li>
</ul>
</li>
<li>
<p><strong>钩子函数特性</strong>：</p>
<ul>
<li>自动执行，不需要手动调用</li>
<li>在Vue实例选项对象中定义</li>
<li>每个实例都会经历完整的生命周期</li>
</ul>
</li>
<li>
<p><strong>数据可用性</strong>：</p>
<ul>
<li>created中可以访问data和methods</li>
<li>mounted中可以访问DOM</li>
<li>beforeCreate中无法访问data</li>
</ul>
</li>
<li>
<p><strong>避免内存泄漏</strong>：</p>
<ul>
<li>在beforeUnmount中清理定时器</li>
<li>取消事件监听</li>
<li>清理全局引用</li>
</ul>
</li>
</ol></section></section>

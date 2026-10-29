---
title: "Ajax与异步编程"
date: 2026-05-15
category: "javawebai/前端基础"
description: "使用Ajax实现页面无刷新数据交互，async/await简化异步编程"
tags: ["前端", "Ajax"]
---

<section><h1 id="ajax与异步编程">Ajax与异步编程</h1><section><h2 id="定义">定义</h2><p>Ajax（Asynchronous JavaScript And XML）是一种在不重新加载整个页面的情况下，与服务器交换数据并更新部分网页的技术。它实现了前端与服务器的异步数据交互。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="同步vs异步对比">同步vs异步对比</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">同步请求流程：</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">浏览器 → 发送请求 → [等待服务器处理] → 接收响应 → 继续操作</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">        </span></span><span style="--0:#abb2bf;--1:#383a42">(期间页面被阻塞，无法操作)</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code">
</div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">异步请求流程：</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">浏览器 → 发送请求 → 继续其他操作</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">        </span></span><span style="--0:#abb2bf;--1:#383a42">(请求在后台处理)</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">8</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">服务器 → 处理完成 → 返回数据 → 更新页面局部内容</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">9</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">        </span></span><span style="--0:#abb2bf;--1:#383a42">(页面不刷新，用户体验好)</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="同步请求流程：浏览器 → 发送请求 → [等待服务器处理] → 接收响应 → 继续操作        (期间页面被阻塞，无法操作)异步请求流程：浏览器 → 发送请求 → 继续其他操作        (请求在后台处理)服务器 → 处理完成 → 返回数据 → 更新页面局部内容        (页面不刷新，用户体验好)"><div></div></button></div></figure></div></section><section><h3 id="asyncawait语法">async/await语法</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 用async声明异步方法</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E6888F">async</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#61AFEF;--1:#3360C1">search</span><span style="--0:#ABB2BF;--1:#383A42">() {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent">    </span><span style="--0:#CD89E1;--1:#A626A4">const</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#E5C07B;--1:#875D01">result</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#CD89E1;--1:#A626A4">await</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E5C07B">axios</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#61AFEF;--1:#3360C1">get</span><span style="--0:#ABB2BF;--1:#383A42">(</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent">        </span><span style="--0:#98C379;--1:#387138">`https://api.example.com/emps/list?name=</span><span style="--0:#CD89E1;--1:#C71242">${</span><span style="--0:#E5C07B;--1:#AF4238">this</span><span style="--0:#ABB2BF;--1:#387138">.</span><span style="--0:#E5C07B;--1:#AF4238">searchForm</span><span style="--0:#ABB2BF;--1:#387138">.</span><span style="--0:#E6888F;--1:#AF4238">name</span><span style="--0:#CD89E1;--1:#C71242">}</span><span style="--0:#98C379;--1:#387138">`</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span class="indent">    </span><span style="--0:#E5C07B;--1:#AF4238">this</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#E6888F;--1:#AF4238">empList</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">=</span><span style="--1:#383A42"><span style="--0:#ABB2BF"> </span><span style="--0:#E5C07B">result</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#E5C07B;--1:#AF4238">data</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#E6888F;--1:#AF4238">data</span><span style="--0:#ABB2BF;--1:#383A42">;</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span style="--0:#ABB2BF;--1:#383A42">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// 用async声明异步方法async search() {    const result = await axios.get(        &#x60;https://api.example.com/emps/list?name=${this.searchForm.name}&#x60;    );    this.empList = result.data.data;}"><div></div></button></div></figure></div></section><section><h3 id="promise方式">Promise方式</h3><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="javascript"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--1:#383A42"><span style="--0:#E5C07B">axios</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#61AFEF;--1:#3360C1">get</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(</span><span style="--0:#E6888F">url</span><span style="--0:#ABB2BF">)</span></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">then</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(</span><span style="--0:#E6888F;--0fs:italic">res</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#CD89E1;--1:#A626A4">=></span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent"><span style="--1:#383A42">        </span></span><span style="--0:#E5C07B;--1:#383A42">console</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">log</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(</span><span style="--0:#E5C07B">res</span><span style="--0:#ABB2BF">.</span></span><span style="--0:#E6888F;--1:#AF4238">data</span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">})</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">catch</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(</span><span style="--0:#E6888F;--0fs:italic">err</span><span style="--0:#ABB2BF"> </span></span><span style="--0:#CD89E1;--1:#A626A4">=></span><span style="--0:#ABB2BF;--1:#383A42"> {</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span class="indent"><span style="--1:#383A42">        </span></span><span style="--0:#E5C07B;--1:#383A42">console</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">log</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(</span><span style="--0:#E6888F">err</span><span style="--0:#ABB2BF">);</span></span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span class="indent"><span style="--0:#ABB2BF;--1:#383A42">    </span></span><span style="--0:#ABB2BF;--1:#383A42">});</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="axios.get(url)    .then(res => {        console.log(res.data);    })    .catch(err => {        console.log(err);    });"><div></div></button></div></figure></div></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li><strong>数据获取</strong>：从服务器加载数据并动态展示</li>
<li><strong>表单提交</strong>：异步提交表单数据，避免页面刷新</li>
<li><strong>搜索联想</strong>：用户输入时实时获取联想建议</li>
<li><strong>数据验证</strong>：用户名可用性检查、邮箱验证等</li>
<li><strong>局部刷新</strong>：只更新页面中变化的部分</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li>
<p><strong>同步vs异步</strong>：</p>
<ul>
<li>同步请求会阻塞页面，等待服务器响应期间无法操作</li>
<li>异步请求不阻塞页面，用户体验更好</li>
</ul>
</li>
<li>
<p><strong>async/await</strong>：</p>
<ul>
<li><code>async</code>用于声明异步方法</li>
<li><code>await</code>用于等待异步任务执行</li>
<li>配合使用可以让异步代码看起来像同步代码</li>
<li>提高代码可读性和可维护性</li>
</ul>
</li>
<li>
<p><strong>错误处理</strong>：</p>
<ul>
<li>使用try-catch包裹await调用</li>
<li>Promise方式使用.catch处理错误</li>
</ul>
</li>
<li>
<p><strong>跨域问题</strong>：</p>
<ul>
<li>Ajax请求受同源策略限制</li>
<li>需要服务器配置CORS或使用代理</li>
</ul>
</li>
<li>
<p><strong>异步不是多线程</strong>：</p>
<ul>
<li>JavaScript是单线程语言</li>
<li>异步通过事件循环机制实现</li>
<li>不阻塞主线程但也不能利用多核并行计算</li>
</ul>
</li>
</ol></section></section>

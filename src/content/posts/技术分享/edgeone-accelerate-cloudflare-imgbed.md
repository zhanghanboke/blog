---
title: "手把手教你用 EdgeOne 加速 Cloudflare 图床，国内访问从 8 秒降到 0.15 秒"
date: 2026-07-31
category: "技术分享"
description: "完整记录使用腾讯云 EdgeOne CDN 加速 Cloudflare Pages 图床的全过程，从零开始配置，包含踩坑排查和性能测试数据。"
tags: ["CDN", "EdgeOne", "Cloudflare", "图床", "性能优化"]
draft: true
---

<section><h2 id="写在前面">写在前面</h2><p>如果你和我一样，把图床部署在 Cloudflare Pages 上，国内用户访问图片总是很慢，那这篇文章就是为你写的。</p><p>我花了大半天时间摸索配置，中间踩了好几个坑，最后成功把图片加载时间从 2-8 秒降到了 0.15 秒。这篇文章把整个过程记录下来，包括我踩过的每一个坑，希望能帮你少走弯路。</p></section>
<section><h2 id="先看效果">先看效果</h2>

<table><thead><tr><th>指标</th><th>加速前</th><th>加速后</th></tr></thead><tbody><tr><td>单张图片加载</td><td>2-8 秒</td><td>0.12-0.19 秒</td></tr><tr><td>图片上传（500KB）</td><td>9 秒</td><td>7 秒</td></tr><tr><td>首页 TTFB</td><td>1.0-1.9 秒</td><td>0.8-1.0 秒</td></tr></tbody></table><p>缓存命中后，图片加载快了 <strong>10-50 倍</strong>。</p></section>
<section><h2 id="原理说明">原理说明</h2><p>Cloudflare 的服务器主要在海外，国内用户访问要绕一大圈。EdgeOne 是腾讯云的 CDN 服务，在国内有大量节点。</p><p>加速的原理很简单：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">没有加速：你的浏览器 → 海外服务器 → 返回图片（慢）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">有加速：你的浏览器 → 国内节点（有缓存就直接返回）→ 没缓存才去海外取（快）</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="没有加速：你的浏览器 → 海外服务器 → 返回图片（慢）有加速：你的浏览器 → 国内节点（有缓存就直接返回）→ 没缓存才去海外取（快）"><div></div></button></div></figure></div><p>就像你在国内买进口商品，有保税仓就不用等国际快递了。</p></section>
<section><h2 id="准备工作">准备工作</h2><p>开始之前，确认你有这些东西：</p><ol>
<li><strong>一个已备案的域名</strong> — EdgeOne 国内加速必须用备案域名</li>
<li><strong>腾讯云账号</strong> — 注册 EdgeOne 需要</li>
<li><strong>Cloudflare 账号</strong> — 你的图床已经部署在上面</li>
<li><strong>你的图床地址</strong> — 类似 <code>xxx.pages.dev</code> 的格式</li>
</ol></section>
<section><h2 id="详细配置步骤">详细配置步骤</h2><section><h3 id="第一步找到你的-cloudflare-pages-地址">第一步：找到你的 Cloudflare Pages 地址</h3><p>登录 Cloudflare Dashboard，进入你的 Pages 项目，在项目设置里找到「默认域名」或「Pages 域名」，格式类似：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">你的项目名.pages.dev</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="你的项目名.pages.dev"><div></div></button></div></figure></div><p>记下这个地址，后面要用。</p></section><section><h3 id="第二步在-edgeone-创建加速域名">第二步：在 EdgeOne 创建加速域名</h3><ol>
<li>登录 <a href="https://console.cloud.tencent.com/edgeone" target="_blank" rel="noopener noreferrer">EdgeOne 控制台</a></li>
<li>如果你还没有添加过域名，先点「添加域名」，输入你的一级域名（比如 <code>example.com</code>）</li>
<li>进入你的一级域名 → 左侧菜单「域名管理」→「加速域名」→「添加域名」</li>
</ol><p>填写以下信息：</p><ul>
<li><strong>加速域名</strong>：<code>img.example.com</code>（你想用的子域名，随意取）</li>
<li><strong>源站类型</strong>：选「源站域名」</li>
<li><strong>源站地址</strong>：填你刚才记下的 Pages 地址（<code>xxx.pages.dev</code>）</li>
<li><strong>回源 Host</strong>：也填 Pages 地址（<code>xxx.pages.dev</code>）</li>
<li><strong>回源协议</strong>：HTTPS</li>
<li><strong>回源端口</strong>：443</li>
</ul><p>往下找到「推荐模板」，选择「网站加速」。</p><p>加速区域选「中国大陆可用区」。</p><p>提交后，EdgeOne 会给你分配一个 CNAME 地址，类似：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">img.example.com.eo.dnse2.com</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="img.example.com.eo.dnse2.com"><div></div></button></div></figure></div><p>记下这个地址。</p></section><section><h3 id="第三步让-cloudflare-pages-认识你的加速域名">第三步：让 Cloudflare Pages 认识你的加速域名</h3><p>EdgeOne 回源时会告诉 Cloudflare Pages：「我是 <code>img.example.com</code>，给我图片」。但 Cloudflare Pages 不认识这个域名，会报错。</p><p>所以需要在 Cloudflare Pages 里添加自定义域名：</p><ol>
<li>进入你的 Pages 项目 → 设置 → Custom domains</li>
<li>添加你在 EdgeOne 创建的加速域名（<code>img.example.com</code>）</li>
<li>Cloudflare 会要求你添加一条 DNS 验证记录，按提示操作</li>
<li>等待验证通过（显示 Active）</li>
</ol><p><strong>注意</strong>：验证过程中，DNS 可能需要临时指向 Cloudflare。验证通过后再改回 EdgeOne。</p></section><section><h3 id="第四步把-dns-指向-edgeone">第四步：把 DNS 指向 EdgeOne</h3><p>验证通过后，去你的域名 DNS 管理，添加或修改 CNAME 记录：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">类型：CNAME</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">主机记录：img（你的子域名前缀）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">记录值：img.example.com.eo.dnse2.com（EdgeOne 给你的地址）</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="类型：CNAME主机记录：img（你的子域名前缀）记录值：img.example.com.eo.dnse2.com（EdgeOne 给你的地址）"><div></div></button></div></figure></div><p>等 DNS 生效（通常 1-5 分钟）。</p></section><section><h3 id="第五步选择缓存策略">第五步：选择缓存策略</h3><p>EdgeOne 会根据你选的「网站加速」模板自动配置缓存。你也可以手动调整：</p><ul>
<li>图片文件：缓存 30 天</li>
<li>HTML 页面：缓存 5 分钟</li>
<li>API 请求：不缓存</li>
</ul></section><section><h3 id="第六步替换项目中的旧域名">第六步：替换项目中的旧域名</h3><p>配置完成后，把项目中所有引用旧图床地址的地方替换为新地址：</p><div class="expressive-code"><figure class="frame is-terminal"><figcaption class="header"><span class="title"></span><span class="sr-only">Terminal window</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#61AFEF;--1:#3360C1">find</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">src/content</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">-type</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">f</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">-name</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">"*.md"</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#56B6C2;--1:#016C9A">\</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent">  </span><span style="--0:#D19A66;--1:#875D01">-exec</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">sed</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">-i</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">'s|https://旧图床地址|https://img.example.com|g'</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">{}</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#98C379;--1:#387138">+</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="find src/content -type f -name &#x22;*.md&#x22; \  -exec sed -i &#x27;s|https://旧图床地址|https://img.example.com|g&#x27; {} +"><div></div></button></div></figure></div><p>别忘了：</p><ul>
<li><code>.env</code> 文件中的图床地址</li>
<li>部署平台（Vercel 等）的环境变量</li>
</ul></section></section>
<section><h2 id="我踩过的-4-个坑">我踩过的 4 个坑</h2><section><h3 id="坑-1http-525-错误">坑 1：HTTP 525 错误</h3><p>配置完成后访问，显示 <code>HTTP ERROR 525</code>。</p><p><strong>原因</strong>：EdgeOne 回源到 Cloudflare 时，SSL 握手失败。Cloudflare 不认识你的加速域名，没有对应的 SSL 证书。</p><p><strong>解决</strong>：在 Cloudflare Pages 添加自定义域名（第三步），让 Cloudflare 为加速域名签发证书。</p></section><section><h3 id="坑-2重定向循环">坑 2：重定向循环</h3><p>访问时显示「此页面不能正确地重定向」。</p><p><strong>原因</strong>：回源 Host 填了加速域名。Cloudflare Pages 收到请求后发现域名不匹配，重定向到加速域名，EdgeOne 又代理回去，无限循环。</p><p><strong>解决</strong>：回源 Host 必须填 Pages 域名（<code>xxx.pages.dev</code>），不能填加速域名。</p></section><section><h3 id="坑-3cloudflare-error-1001">坑 3：Cloudflare Error 1001</h3><p>显示 Cloudflare 的 DNS 解析错误页面。</p><p><strong>原因</strong>：回源地址填了原来在 Cloudflare 代理后面的域名。Cloudflare 拦截了 EdgeOne 的请求。</p><p><strong>解决</strong>：回源地址用 Pages 直连域名（<code>xxx.pages.dev</code>），不走 Cloudflare 代理。</p></section><section><h3 id="坑-4http-回源也失败">坑 4：HTTP 回源也失败</h3><p>改成 HTTP:80 回源仍然报错。</p><p><strong>原因</strong>：Cloudflare Pages 强制 HTTPS，不接受 HTTP 回源。</p><p><strong>解决</strong>：回源协议必须用 HTTPS:443。</p></section></section>
<section><h2 id="容灾方案">容灾方案</h2><p>如果 EdgeOne 出问题，只需改一条 DNS 记录：</p><p>把加速域名的 CNAME 从 EdgeOne 地址改成直接指向 Pages 域名。</p><p>不需要改代码，不需要重新部署，秒级恢复。</p></section>
<section><h2 id="总结">总结</h2><p>整个配置大约 30 分钟，主要是等 DNS 生效和 Cloudflare 验证。配置完成后，国内用户访问图片的速度提升了一个数量级。</p><p>如果你也有类似的海外 CDN 加速需求，EdgeOne 是一个不错的选择。免费额度够个人博客使用，配置也不复杂，主要是把回源 Host 和 SSL 证书这两个点搞对就行了。</p></section>

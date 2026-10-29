---
title: "手把手教你用 EdgeOne 加速 Vercel 部署的项目（源站域名分离法）"
date: 2026-08-10
category: "技术分享"
description: "Vercel 部署的网站国内访问慢？用源站域名分离法给 Vercel 套上 EdgeOne 加速，配置详解 + 踩坑记录。"
tags: ["CDN", "EdgeOne", "Vercel", "性能优化", "教程"]
cover: "/media/6f1b33e67f1f.png"
draft: true
---

<section><h2 id="写在前面">写在前面</h2><p>Vercel 部署网站很方便，但<strong>国内访问速度一直是个老大难问题</strong>——Vercel 的节点在海外，国内用户访问动不动几秒甚至超时。</p><p>能不能给 Vercel 套一个国内 CDN（EdgeOne）加速？<strong>能</strong>，但有一个坑：<strong>Vercel 的自定义域名验证机制</strong>要求域名的 DNS 必须指向 <code>xxx.vercel.app</code>，否则拒绝服务——和 CDN 要求的”DNS 指向 CDN”冲突。</p><p>这篇文章分享我实际验证可行的方案：<strong>源站域名分离法</strong>——给 Vercel 一个”源站域名”，用户访问的域名走 EdgeOne 加速。</p><p>先看加速前后的效果对比：
</p><center><figure><img src="/media/6f1b33e67f1f.png" alt=""><figcaption>572</figcaption></figure></center>
📷 插图 1：加速前的加载速度截图（Vercel 直连）
<center><figure><img src="/media/2415c9fcdb2c.png" alt=""><figcaption>568</figcaption></figure></center>
📷 插图 2：加速后的加载速度截图（EdgeOne 加速）<p></p></section>
<section><h2 id="原理为什么不能直接套">原理：为什么不能直接套</h2><p>Vercel 对自定义域名是<strong>持续监控 DNS</strong> 的：</p><ul>
<li>域名 CNAME 指向 <code>xxx.vercel.app</code> → Vercel 显示 <strong>Valid</strong>（正常服务）</li>
<li>域名指向其他（比如 CDN）→ Vercel 显示 <strong>Invalid</strong>（<strong>拒绝服务</strong>，访问报错）</li>
</ul><p>一个域名只有一条 CNAME——<strong>不可能同时指向 Vercel 和 CDN</strong>。所以”直接套”是走不通的（我一开始就踩了这个坑，访问一直报 522）。</p></section>
<section><h2 id="方案源站域名分离">方案：源站域名分离</h2><p>核心思路：<strong>给 Vercel 绑定一个专门的”源站域名”，CDN 回源到它；用户访问的域名走 CDN</strong>：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">用户访问 cms.yourdomain.com</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">    </span></span><span style="--0:#abb2bf;--1:#383a42">↓ DNS 解析（指向 EdgeOne）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">EdgeOne 边缘节点（国内加速/缓存）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">    </span></span><span style="--0:#abb2bf;--1:#383a42">↓ 回源（Host: origin.yourdomain.com）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">Vercel（绑定了 origin.yourdomain.com）✅ Valid</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="用户访问 cms.yourdomain.com    ↓ DNS 解析（指向 EdgeOne）EdgeOne 边缘节点（国内加速/缓存）    ↓ 回源（Host: origin.yourdomain.com）Vercel（绑定了 origin.yourdomain.com）✅ Valid"><div></div></button></div></figure></div><ul>
<li>Vercel 绑定 <code>origin.yourdomain.com</code>（DNS 指向 vercel.app → Valid）</li>
<li>EdgeOne 加速 <code>cms.yourdomain.com</code>（用户访问的域名）</li>
<li>EdgeOne 回源到 <code>origin.yourdomain.com</code>（Vercel 认它）</li>
</ul></section>
<section><h2 id="配置步骤">配置步骤</h2><section><h3 id="-vercel添加源站域名">① Vercel：添加源站域名</h3><ol>
<li>Vercel 项目 → <strong>Settings → Domains</strong> → 添加 <code>origin.yourdomain.com</code></li>
<li>按提示在 DNS 加记录：<code>cms-origin</code> → <code>cms.vercel.app</code>（CNAME）</li>
<li>等状态变 <strong>Valid</strong>（绿色）</li>
<li><strong>删除</strong>原来的 <code>cms.yourdomain.com</code> 绑定（它交给 EdgeOne，留着会一直显示 Invalid）</li>
</ol></section><section><h3 id="-edgeone添加加速站点">② EdgeOne：添加加速站点</h3><ol>
<li>EdgeOne 控制台 → <strong>站点加速</strong> → 添加站点 <code>cms.yourdomain.com</code></li>
<li>源站配置（<strong>关键</strong>）：</li>
</ol>

<table><thead><tr><th>配置项</th><th>填什么</th></tr></thead><tbody><tr><td>源站类型</td><td>IP/域名</td></tr><tr><td>源站地址</td><td><code>origin.yourdomain.com</code></td></tr><tr><td>回源协议</td><td>HTTPS</td></tr><tr><td>回源端口</td><td>443</td></tr><tr><td><strong>回源 HOST 头</strong></td><td><strong>使用源站域名</strong>（<code>origin.yourdomain.com</code>）</td></tr></tbody></table><blockquote><p>⚠️ <strong>回源 HOST 头是最容易错的地方</strong>：必须填源站域名（<code>origin.yourdomain.com</code>），不能选”使用加速域名”——否则 Vercel 收到的是加速域名（没绑定）会拒绝请求。</p></blockquote></section><section><h3 id="-dns切换解析">③ DNS：切换解析</h3><p>把 <code>cms.yourdomain.com</code> 的 CNAME <strong>从 <code>cms.vercel.app</code> 改成 EdgeOne 给的加速地址</strong>（EdgeOne 站点详情页会显示，类似 <code>cms.yourdomain.com.eo.dnse2.com</code>）。</p><blockquote><p>⚠️ 是<strong>修改</strong>这条记录，不是新增第二条（一个域名只能有一条 CNAME）。</p></blockquote></section><section><h3 id="-应用侧配置如果你的应用有">④ 应用侧配置（如果你的应用有）</h3><p>如果应用配置了回调域名/BASE_URL（比如后台系统的 OAuth 回调），<strong>统一用用户访问的加速域名</strong>：</p><ul>
<li><code>BASE_URL = https://cms.yourdomain.com</code>（不是 cms-origin）</li>
<li>GitHub App / OAuth 回调地址：<code>https://cms.yourdomain.com/api/auth/callback</code></li>
</ul><p>这样登录、回调都走加速域名，EdgeOne 会正确回源。</p></section></section>
<section><h2 id="踩坑记录">踩坑记录</h2>

<table><thead><tr><th>坑</th><th>现象</th><th>解决</th></tr></thead><tbody><tr><td>直接套 CDN</td><td>访问报 <strong>522</strong>（Vercel 拒绝）</td><td>源站域名分离</td></tr><tr><td>回源 HOST 头用加速域名</td><td>Vercel 不认，回源失败</td><td>改成源站域名</td></tr><tr><td>DNS 加了两条 CNAME</td><td>解析冲突</td><td>修改旧记录，不新增</td></tr><tr><td>Vercel 域名验证时序</td><td>先指向 vercel.app 等 Valid，再切 CDN</td><td>按步骤①→④ 顺序</td></tr></tbody></table></section>
<section><h2 id="验证">验证</h2><ol>
<li>等 EdgeOne 状态从”部署中”变”已部署”（几分钟）</li>
<li>浏览器访问 <code>https://cms.yourdomain.com</code> → 正常打开</li>
<li><strong>登录功能测试</strong>（重要）：如果应用有登录，确认登录态正常——Cookie 的域名取决于应用配置的 BASE_URL（用加速域名就不会有问题）</li>
<li>速度对比：F12 → Network 看加载时间（国内应该明显提升）</li>
</ol></section>
<section><h2 id="总结">总结</h2>

<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>核心思路</td><td>源站域名（Vercel 绑定）与访问域名（CDN）分离</td></tr><tr><td>关键配置</td><td>回源 HOST 头 = 源站域名</td></tr><tr><td>应用配置</td><td>BASE_URL/回调地址用加速域名</td></tr><tr><td>适用场景</td><td>Vercel / Netlify 等托管平台 + 国内 CDN</td></tr></tbody></table><p>这套方案我实测跑通了：Vercel 托管的博客后台，套上 EdgeOne 后国内访问流畅，登录、编辑全部正常。如果国内访问 Vercel 应用慢，值得一试。</p></section>

---
title: "MySQL安装与连接"
date: 2026-05-18
category: "javawebai/后端基础"
description: "MySQL 8.0 社区版的安装、启动与命令行连接方式"
tags: ["前端", "MySQL", "数据库"]
cover: "/media/cad3e9e13de1.png"
---

<section><h1 id="mysql安装与连接">MySQL安装与连接</h1><section><h2 id="定义">定义</h2><p>MySQL 是当前互联网开发中最流行的开源关系型数据库管理系统。</p></section><section><h2 id="版本说明">版本说明</h2>

<table><thead><tr><th>版本</th><th>说明</th></tr></thead><tbody><tr><td>MySQL Enterprise Edition（商业版）</td><td>收费，享有技术支持，可试用 30 天</td></tr><tr><td>MySQL Community Server（社区版）</td><td>免费，无官方技术支持</td></tr></tbody></table><p>本课程使用 MySQL Community Server 8.0.34。</p></section><section><h2 id="连接语法">连接语法</h2><p>MySQL 服务器启动后，使用命令行连接：</p><div class="expressive-code"><figure class="frame is-terminal"><figcaption class="header"><span class="title"></span><span class="sr-only">Terminal window</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#61AFEF;--1:#3360C1">mysql</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">-u用户名</span><span style="--0:#ABB2BF;--1:#383A42"> </span><span style="--0:#D19A66;--1:#875D01">-p密码</span><span style="--0:#ABB2BF;--1:#383A42"> [-h数据库服务器IP地址 </span><span style="--0:#D19A66;--1:#875D01">-P端口号</span><span style="--0:#ABB2BF;--1:#383A42">]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="mysql -u用户名 -p密码 [-h数据库服务器IP地址 -P端口号]"><div></div></button></div></figure></div><ul>
<li><code>-h</code> 省略时默认连接本地 <code>127.0.0.1</code></li>
<li><code>-P</code> 省略时默认端口 <code>3306</code></li>
</ul><section><h3 id="两种密码输入方式">两种密码输入方式</h3><p><strong>方式一</strong>：密码直接跟在 <code>-p</code> 后（明文暴露，不安全）</p><p><strong>方式二</strong>：<code>-p</code> 后回车，再在交互界面输入密码（推荐）</p></section></section><section><h2 id="企业环境连接">企业环境连接</h2><p>真实开发中，MySQL 部署在公司服务器（IDC 机房），开发人员通过网络远程连接：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">mysql -h服务器IP -P端口号 -u用户名 -p</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="mysql -h服务器IP -P端口号 -u用户名 -p"><div></div></button></div></figure></div><p></p><center><figure><img src="/media/cad3e9e13de1.png" alt=""><figcaption>企业远程连接</figcaption></figure></center><p></p></section><section><h2 id="注意事项">注意事项</h2><ul>
<li>学习阶段可本地安装，企业开发中数据库在远程服务器。</li>
<li>图形化管理工具（DataGrip / IDEA 内置数据库工具）可大幅提升效率。</li>
<li>驱动下载可能较慢，需耐心等待。</li>
</ul></section><section><h2 id="相关链接">相关链接</h2><ul>
<li><a href="https://downloads.mysql.com/archives/community/" target="_blank" rel="noopener noreferrer">MySQL 社区版下载</a></li>
<li><a href="https://heuqqdmbyk.feishu.cn/wiki/ZRSFwACsRiBD2NkV7bmcrJhInme" target="_blank" rel="noopener noreferrer">MySQL 安装文档</a></li>
</ul></section></section>

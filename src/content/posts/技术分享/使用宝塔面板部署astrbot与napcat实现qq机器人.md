---
title: "使用宝塔面板部署 AstrBot 与 NapCat 实现 QQ 机器人"
date: 2026-07-25
category: "技术分享"
description: "使用宝塔面板部署 AstrBot 与 NapCat 实现 QQ 机器人"
tags: ["总结", "转载"]
cover: "/media/a8ebe4facb59.webp"
---

<p>此文章转载为这位大佬：<a href="https://blog.tianhw.top/posts/bt-astrbot-napcat/#%E7%99%BB%E5%BD%95-astrbot" target="_blank" rel="noopener noreferrer">THW</a>
</p><center><figure><img src="/media/a8ebe4facb59.webp" alt=""><figcaption>697</figcaption></figure></center><p></p>
<div class="callout" data-callout="note" data-collapsible="false"><div class="callout-title"><div class="callout-title-icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></div><div class="callout-title-text">Note</div></div><div class="callout-content"><p>NOTE</p><p>本文是特指在宝塔面板 11，使用 Docker 容器部署 AstrBot 和 NapCat 以实现接入个人 QQ 号的教程。</p></div></div>
<div class="callout" data-callout="note" data-collapsible="false"><div class="callout-title"><div class="callout-title-icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></div><div class="callout-title-text">Note</div></div><div class="callout-content"><p>WARNING</p><p>您在部署前应该知晓通过 NapCat 接入 QQ 存在触发腾讯风控机制的风险，请谨慎操作。</p></div></div>
<section><h2 id="介绍">介绍</h2><section><h3 id="astrbot">AstrBot</h3><p><a href="https://github.com/Soulter/AstrBot" target="_blank" rel="noopener noreferrer">AstrBot</a> 是一个开源、模块化的一站式 Agentic 聊天机器人平台，支持灵活构建 AI 伴侣、智能客服或企业知识库系统。其核心特性包括：</p><ul>
<li><strong>强大的 Agentic 能力</strong> ：支持多轮工具调用、沙盒代码执行、实时网页搜索，可处理复杂任务；</li>
<li><strong>多模型 LLM 引擎</strong> ：兼容主流大语言模型，支持多模态输入、人设定制与原生知识库；</li>
<li><strong>跨平台部署</strong> ：一键接入 QQ、微信公众号、飞书、Telegram、Discord 等主流消息平台；</li>
<li><strong>可视化管理界面</strong> ：提供 WebUI 用于插件管理、对话监控与系统配置。</li>
</ul></section><section><h3 id="napcat">NapCat</h3><p><a href="https://github.com/mlikiowa/napcat-docker" target="_blank" rel="noopener noreferrer">NapCat</a> 是一个基于 TypeScript 开发的 OneBot 协议实现框架，通过调用 QQ 客户端底层接口，将 HTTP/WebSocket 请求标准化为 OneBot v11 协议格式，从而实现 Bot 功能。它本身不包含业务逻辑，仅作为消息通道层。</p></section><section><h3 id="协作关系">协作关系</h3><p>AstrBot 与 NapCat 通过 <strong>OneBot v11 协议</strong> 协同工作：</p><ul>
<li><strong>NapCat</strong> 负责与 QQ 客户端通信，充当“耳朵”（接收消息）和“嘴巴”（发送消息）；</li>
<li><strong>AstrBot</strong> 作为智能中枢，处理消息逻辑、调用 AI 模型并生成回复，是机器人的“大脑”。</li>
</ul><p>二者通过 WebSocket 建立连接，方可实现完整功能闭环。</p><p><img src="/media/367dd1a30ece.png" alt=""></p></section></section>
<section><h2 id="部署">部署</h2><section><h3 id="astrbot-1">AstrBot</h3><ol>
<li>登录你的宝塔面板，进入 <strong>Docker → 容器</strong> 页面；</li>
<li>点击 <strong>创建容器</strong> ，填写以下参数：

<table><thead><tr><th>参数</th><th>值</th></tr></thead><tbody><tr><td>容器名称</td><td><code>astrbot</code> （可自定义）</td></tr><tr><td>镜像</td><td><code>soulter/astrbot:latest</code></td></tr><tr><td>端口映射</td><td><code>6199:6199</code> （反向 WS） <code>6185:6185</code> （WebUI）</td></tr></tbody></table>
</li>
<li>点击 <strong>创建</strong> ，等待容器启动完成。</li>
</ol><p></p><center><figure><img src="/media/a781aaea9ab7.webp" alt=""><figcaption>AstrBot 容器创建</figcaption></figure></center><p></p></section><section><h3 id="napcat-1">NapCat</h3><ol>
<li>返回容器列表，再次点击 <strong>创建容器</strong> ；</li>
<li>填写参数如下：

<table><thead><tr><th>参数</th><th>值</th></tr></thead><tbody><tr><td>容器名称</td><td><code>napcat</code></td></tr><tr><td>镜像</td><td><code>mlikiowa/napcat-docker:latest</code></td></tr><tr><td>端口映射</td><td><code>3000:3000</code> <code>3001:3001</code> <code>6099:6099</code> （WebUI）</td></tr></tbody></table>
</li>
<li>再次点击创建并等待启动。</li>
</ol></section></section>
<section><h2 id="配置">配置</h2><section><h3 id="配置-napcat-并登录-qq">配置 NapCat 并登录 QQ</h3><ol>
<li>在容器列表中找到 <code>napcat</code> ，点击 <strong>更多 → 日志</strong> ；
<center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_22-48-22.webp" alt=""><figcaption>查看 NapCat 日志</figcaption></figure></center></li>
<li>查找日志中的 <code>WebUI Token</code> ；
<center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_22-50-11.webp" alt=""><figcaption>获取 WebUI Token</figcaption></figure></center></li>
<li>浏览器访问 <code>http://&#x3C;服务器IP>:6099</code> ，输入 Token 登录；</li>
<li>使用手机 QQ 或 TIM 扫描二维码完成账号登录。
<center><figure><img src="https://img.tsh520.cn/file/blog/article/1.webp" alt=""><figcaption>NapCat WebUI 登录</figcaption></figure></center></li>
</ol></section><section><h3 id="登录-astrbot">登录 AstrBot</h3><ol>
<li>浏览器访问 <code>http://&#x3C;服务器IP>:6185</code> ，会来到 AstrBot 的登录页面，默认密码账户均为 “astrbot”；</li>
<li>登录后会提示修改密码，设置好后须使用新账户密码重新登录一次。</li>
</ol></section><section><h3 id="建立容器间网络互通">建立容器间网络互通</h3><p>由于 AstrBot 与 NapCat 分属独立容器，默认网络隔离，无法直接通信。需将其加入同一自定义 Docker 网络：</p><ol>
<li>进入 <strong>Docker → 网络</strong> ，点击 <strong>添加网络</strong> ；
<ul>
<li>网络名称： <code>astrbot-napcat</code>
<center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_22-57-03.webp" alt=""><figcaption>添加自定义网络</figcaption></figure></center></li>
</ul>
</li>
<li>返回 <strong>容器</strong> 页面，对 <code>napcat</code> 和 <code>astrbot</code> 容器分别执行：
<ul>
<li>点击 <strong>管理 → 容器网络 → 加入网络</strong>
<ul>
<li>选择 <code>astrbot-napcat</code></li>
<li><strong>退出默认网络</strong>
<center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_22-59-54.webp" alt=""><figcaption>加入网络</figcaption></figure></center></li>
</ul>
</li>
</ul>
</li>
<li>记录 <code>astrbot</code> 容器在 <code>astrbot-napcat</code> 网络中的 IPv4 地址。
<center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_23-01-11.webp" alt=""><figcaption>获取 AstrBot IP</figcaption></figure></center></li>
</ol></section><section><h3 id="配置-napcat-的-websocket-客户端">配置 NapCat 的 WebSocket 客户端</h3><ol>
<li>在 NapCat WebUI 中，进入 <strong>网络配置 → 新建 → WebSocket 客户端</strong> ；</li>
<li>填写如下参数：

<table><thead><tr><th>字段</th><th>值</th></tr></thead><tbody><tr><td>启用</td><td>✅ 勾选</td></tr><tr><td>URL</td><td><code>ws://&#x3C;astrbot容器IP>:6199/ws</code></td></tr><tr><td>消息格式</td><td><code>Array</code></td></tr><tr><td>心跳间隔 (ms)</td><td><code>5000</code></td></tr><tr><td>重连间隔 (ms)</td><td><code>5000</code></td></tr><tr><td>Token</td><td>（可选，若 AstrBot 设置了则需一致）</td></tr><tr><td><center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_23-02-34.webp" alt=""><figcaption>新建 WebSocket 客户端</figcaption></figure></center></td><td></td></tr></tbody></table>
</li>
<li>点击 <strong>保存</strong> 。</li>
</ol></section><section><h3 id="配置-astrbot-的-onebot-适配器">配置 AstrBot 的 OneBot 适配器</h3><ol>
<li>访问 AstrBot WebUI（ <code>http://&#x3C;服务器IP>:6185</code> ）；</li>
<li>进入左侧 <strong>机器人 → 创建机器人</strong> ；</li>
<li>选择 <strong>OneBot v11</strong> 类型；</li>
<li>填写配置：

<table><thead><tr><th>字段</th><th>值</th></tr></thead><tbody><tr><td>ID</td><td>随意</td></tr><tr><td>启用</td><td>✅ 勾选</td></tr><tr><td>反向 WebSocket 主机地址</td><td><code>&#x3C;astrbot容器IP></code></td></tr><tr><td>反向 WebSocket 端口</td><td><code>6199</code></td></tr><tr><td>Token</td><td>（如果没有设置就不用填）</td></tr><tr><td><center><figure><img src="https://img.tsh520.cn/file/blog/article/Snipaste_2026-01-24_23-06-31.webp" alt=""><figcaption>配置 OneBot v11</figcaption></figure></center></td><td></td></tr></tbody></table>
</li>
<li>点击 <strong>保存</strong> 。</li>
</ol></section></section>
<section><h2 id="大功告成">大功告成</h2><p>在 AstrBot WebUI 的 <strong>机器人</strong> 页面下方的“平台日志”中，若出现以下日志：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">aiocqhttp(OneBot v11) 适配器已连接。</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="aiocqhttp(OneBot v11) 适配器已连接。"><div></div></button></div></figure></div><p>则表明 AstrBot 与 NapCat 已成功建立通信，即可开始在 AstrBot 上配置你的 QQ 机器人了。</p></section>

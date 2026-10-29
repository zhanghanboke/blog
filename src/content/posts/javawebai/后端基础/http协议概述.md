---
title: "HTTP协议概述"
date: 2026-05-17
category: "javawebai/后端基础"
description: "HTTP协议的基本概念、特点与BS/CS架构介绍"
tags: ["前端", "HTTP", "Java"]
---

<section><h1 id="http协议概述">HTTP协议概述</h1><section><h2 id="定义">定义</h2><p><strong>HTTP</strong>：Hyper Text Transfer Protocol（超文本传输协议），规定了浏览器与服务器之间数据传输的规则。HTTP是互联网上应用最为广泛的一种网络协议，要求浏览器在向服务器发送请求数据时，或是服务器在向浏览器发送响应数据时，都必须按照固定的格式进行数据传输。</p></section><section><h2 id="语法用法">语法/用法</h2><section><h3 id="http协议特点">HTTP协议特点</h3><ol>
<li><strong>基于TCP协议</strong>：面向连接，安全。TCP是一种面向连接的（建立连接之前需要经过三次握手）、可靠的、基于字节流的传输层通信协议。</li>
<li><strong>基于请求-响应模型</strong>：一次请求对应一次响应（先请求后响应），请求和响应是一一对应关系，没有请求就没有响应。</li>
<li><strong>无状态协议</strong>：对于数据没有记忆能力，每次请求-响应都是独立的。</li>
</ol></section><section><h3 id="bs架构与cs架构">BS架构与CS架构</h3><ul>
<li><strong>BS架构</strong>（Browser/Server）：客户端只需要浏览器，应用程序的逻辑和数据都存储在服务端。优点：维护方便；缺点：体验一般。</li>
<li><strong>CS架构</strong>（Client/Server）：需要单独开发维护客户端。优点：体验不错；缺点：开发维护麻烦。</li>
</ul></section></section><section><h2 id="常见场景">常见场景</h2><ol>
<li><strong>Web应用通信</strong>：浏览器与服务器之间的数据传输</li>
<li><strong>前后端分离架构</strong>：前端通过HTTP请求调用后端API</li>
<li><strong>移动端应用</strong>：移动App通过网络请求访问服务器接口</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ol>
<li><strong>无状态的解决方案</strong>：由于HTTP协议无状态特性导致请求之间无法共享数据（如购物车场景），Java通过会话技术（Cookie、Session）来解决这个问题</li>
<li><strong>静态资源与动态资源</strong>：HTML、CSS、JS及图片等属于静态资源（不会改变）；Servlet、基于Spring的动态资源会根据用户请求动态生成内容</li>
</ol></section><section><h2 id="相关链接">相关链接</h2><ul>
<li><a href="https://cloud.tencent.com/developer/chapter/13553" target="_blank" rel="noopener noreferrer">腾讯云状态码大全</a></li>
</ul></section></section>

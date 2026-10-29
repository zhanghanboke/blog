---
title: "OpenCode Go 接入 CC Switch：Claude Code 原生 API 格式配置教程"
date: 2026-08-08
category: "ai使用"
description: "想用 Claude Code 又不想碰官方 API 的定价？OpenCode Go 订阅自带 Anthropic 原生格式端点，配合 CC Switch 桌面端，填一个 Base URL 加 API Key 就能把 Claude Code 切到 Go 的模型上，Qwen3.8 Max、MiniMax M3 随便切。"
tags: ["OpenCode", "Claude Code", "CC Switch", "AI 编程", "教程"]
---

<blockquote><p>Claude Code 不一定要用官方 API。把 OpenCode Go 的端点接进 CC Switch，一套订阅就能让 Claude Code 跑在 Qwen3.8 Max 上。</p></blockquote>
<hr>
<section><h1 id="背景">背景</h1><p>用 Claude Code 的都知道这两个坎：</p><ul>
<li>❌ 官方订阅要绑定国外支付，API 按 token 计费贵得肉疼</li>
<li>❌ 第三方中转水太深，隐私没保障，随时跑路</li>
</ul><p>而 OpenCode Go 订阅（首月 $5，之后 $10/月）本身就是「给你 API Key 的订阅制服务」，而且它<strong>原生提供 Anthropic 格式的端点</strong>——也就是说 Claude Code 可以直接把它当官方 API 用，不用任何格式转换。</p><p>再配合 CC Switch 这个开源桌面工具，一键切换 Provider，官方 API、Go、其他中转想用哪个用哪个。</p><hr></section>
<section><h1 id="一准备工作">一、准备工作</h1><section><h2 id="1-订阅-opencode-go-并拿到-api-key">1. 订阅 OpenCode Go 并拿到 API Key</h2><p>打开控制台：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">https://opencode.ai/auth</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="https://opencode.ai/auth"><div></div></button></div></figure></div><p>登录后订阅 Go（支持支付宝付款），然后在控制台里复制你的 <strong>API Key</strong>，先存好备用。</p><blockquote><p>还没订阅？首月 $5（≈35 元），订阅后模型随便用。可以用我的邀请链接注册，咱俩各得 $5：<a href="https://opencode.ai/go?ref=1MKPWMM7TS" target="_blank" rel="noopener noreferrer">https://opencode.ai/go?ref=1MKPWMM7TS</a></p></blockquote></section><section><h2 id="2-安装-cc-switch">2. 安装 CC Switch</h2><p>去 GitHub Releases 下载安装：</p><ul>
<li><a href="https://github.com/farion1231/cc-switch" target="_blank" rel="noopener noreferrer">https://github.com/farion1231/cc-switch</a></li>
</ul><p>Windows 选 <code>CC-Switch-v{版本}-Windows.msi</code>，装完打开。</p><hr></section></section>
<section><h1 id="二原理为什么能直接接">二、原理：为什么能直接接</h1><p>Claude Code 走的是 Anthropic 的 Messages API，而 OpenCode Go 就提供了 Anthropic 格式的端点：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">Base URL:  https://opencode.ai/zen/go/v1</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="Base URL:  https://opencode.ai/zen/go/v1"><div></div></button></div></figure></div><p>走这个端点的模型（官方文档标注 <code>@ai-sdk/anthropic</code>）：</p>

<table><thead><tr><th>模型</th><th>模型 ID</th><th>用量限制（每 5 小时）</th></tr></thead><tbody><tr><td>Qwen3.8 Max</td><td><code>qwen3.8-max</code></td><td>160 次</td></tr><tr><td>Qwen3.7 Max</td><td><code>qwen3.7-max</code></td><td>340 次</td></tr><tr><td>Qwen3.7 Plus</td><td><code>qwen3.7-plus</code></td><td>4,300 次</td></tr><tr><td>Qwen3.6 Plus</td><td><code>qwen3.6-plus</code></td><td>3,300 次</td></tr><tr><td>MiniMax M3</td><td><code>minimax-m3</code></td><td>3,200 次</td></tr><tr><td>MiniMax M2.7</td><td><code>minimax-m2.7</code></td><td>3,400 次</td></tr></tbody></table><p>所以 Claude Code 里填这个 Base URL + 你的 API Key，协议就是原生的，不需要任何中转或转换层。</p><hr></section>
<section><h1 id="三cc-switch-添加-provider">三、CC Switch 添加 Provider</h1><p>打开 CC Switch，点击「添加 Provider」：</p><section><h2 id="1-选择工具">1. 选择工具</h2><p>工具类型选 <strong>Claude Code</strong>。</p></section><section><h2 id="2-填写配置">2. 填写配置</h2>

<table><thead><tr><th>配置项</th><th>填写内容</th></tr></thead><tbody><tr><td>名称</td><td><code>OpenCode Go</code>（随意，方便辨认就行）</td></tr><tr><td>API Key</td><td>你的 OpenCode Go API Key</td></tr><tr><td>Base URL</td><td><code>https://opencode.ai/zen/go/v1</code></td></tr><tr><td>模型</td><td><code>qwen3.8-max</code>、<code>qwen3.7-plus</code>、<code>minimax-m3</code> 等，换行分隔</td></tr><tr><td>思考模式</td><td>按需开启</td></tr></tbody></table></section><section><h2 id="3-保存并启用">3. 保存并启用</h2><p>保存后，在 Provider 列表里选中「OpenCode Go」，点击<strong>启用</strong>。</p><blockquote><p>💡 CC Switch 对 Claude Code 支持热切换，不用重启终端就能生效。其他工具（Codex、Gemini CLI 等）切换后需要重启终端。</p></blockquote><hr></section></section>
<section><h1 id="四验证">四、验证</h1><p>打开 Claude Code，输入：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">/status</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="/status"><div></div></button></div></figure></div><p>确认当前使用的模型和端点已经变成 OpenCode Go。再随便问一句，能正常回复就说明通了。</p><p>也可以直接 <code>/model</code> 切换列表里的模型，Qwen3.8 Max 写代码，MiniMax M3 量大管饱，按需切换。</p><hr></section>
<section><h1 id="五注意事项">五、注意事项</h1><ul>
<li>⚠️ <strong>DeepSeek V4 Flash 用不了原生格式</strong>：Go 的 DeepSeek 系列走的是 OpenAI 格式端点（<code>/chat/completions</code>），Claude Code 原生只认 Anthropic 格式。想用 DeepSeek 的话，需要 CC Switch 的本地代理做格式转换，属于进阶玩法，以后单独写一篇。</li>
<li>⚠️ <strong>API Key 别泄露</strong>：Key 在控制台里能随时查看，泄露了立刻去控制台重置。</li>
<li>⚠️ <strong>用量是订阅制的</strong>：Qwen3.8 Max 这类旗舰模型每 5 小时 160 次左右，日常够用；写日常小任务建议常驻 Qwen3.7 Plus（4,300 次/5 小时），完全跑不完。</li>
<li>✅ <strong>想回官方 API</strong>：在 CC Switch 里启用「官方登录」预设，跑一遍 Claude Code 的登录流程即可切回。</li>
</ul><hr></section>
<section><h1 id="结语">结语</h1><p>一套 $10/月的 OpenCode Go 订阅，通过 CC Switch 接到 Claude Code 上，等于用订阅价享受了「原生 API」的体验——不碰官方计费、不用中转平台、支付宝就能付款。</p><p>订阅入口（用我的链接注册，咱俩各得 $5）：</p><p>👉 <a href="https://opencode.ai/go?ref=1MKPWMM7TS" target="_blank" rel="noopener noreferrer">https://opencode.ai/go?ref=1MKPWMM7TS</a></p></section>

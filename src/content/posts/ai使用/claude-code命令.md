---
title: "Claude Code 常用命令"
date: 2026-06-09
category: "ai使用"
description: "Claude Code 常用命令速查：恢复会话、压缩上下文、切换模型、调整努力程度、权限模式……按用途分组整理成表格，随用随查。"
tags: ["claudecode", "AI 编程"]
---

<blockquote><p>Claude Code 的命令统一以 <code>/</code> 开头，在输入框直接敲就能用。下面是按用途分组的常用命令速查。</p></blockquote>
<section><h2 id="一会话管理">一、会话管理</h2>

<table><thead><tr><th>命令</th><th>作用</th><th>使用场景</th></tr></thead><tbody><tr><td><code>/resume</code></td><td>恢复上次对话 / 切换历史聊天记录</td><td>关掉终端后想接着聊，输入后会列出历史会话供选择</td></tr><tr><td><code>/compact</code></td><td>压缩上下文</td><td>聊得太长时，把历史总结压缩，省 token 又能继续聊</td></tr><tr><td><code>/clear</code></td><td>清空上下文</td><td>彻底换话题，从零开始</td></tr><tr><td><code>/export</code></td><td>导出会话记录</td><td>把对话保存成文件留档</td></tr></tbody></table><blockquote><p>💡 想换话题又不想丢上下文，先用 <code>/compact</code> 压缩，比 <code>/clear</code> 一刀切更省。</p></blockquote></section>
<section><h2 id="二状态与设置">二、状态与设置</h2>

<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td><code>/status</code></td><td>查看当前模型、模式、上下文用量</td></tr><tr><td><code>/cost</code></td><td>查看本次会话消耗的 token 和费用</td></tr><tr><td><code>/model</code></td><td>切换模型（弹出列表选择）</td></tr><tr><td><code>/effort</code></td><td>调整努力程度，输入后按左右箭头切换</td></tr><tr><td><code>/permissions</code></td><td>切换权限模式（快捷键 <code>Shift+Tab</code>）</td></tr><tr><td><code>/config</code></td><td>打开交互式配置</td></tr><tr><td><code>/login</code></td><td>登录 / 切换账号</td></tr></tbody></table></section>
<section><h2 id="三项目管理">三、项目管理</h2>

<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td><code>/init</code></td><td>首次进入项目时生成 <code>CLAUDE.md</code>，让 AI 记住项目规矩</td></tr><tr><td><code>/add-dir</code></td><td>把指定目录加入项目上下文</td></tr><tr><td><code>/doctor</code></td><td>诊断安装、配置、网络等问题</td></tr></tbody></table></section>
<section><h2 id="四进阶玩法">四、进阶玩法</h2>

<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td><code>/mcp</code></td><td>查看和管理 MCP 服务器（连接外部工具）</td></tr><tr><td><code>/agents</code></td><td>管理子代理，多代理协作处理大任务</td></tr><tr><td><code>/review</code></td><td>审查最近的代码改动</td></tr><tr><td><code>/memory</code></td><td>查看 Claude 的记忆内容</td></tr></tbody></table></section>
<section><h2 id="五日常最常用的几条">五、日常最常用的几条</h2><ul>
<li><strong><code>/resume</code></strong> — 恢复上次对话，也是切换聊天记录的入口</li>
<li><strong><code>/compact</code></strong> — 上下文太长时压缩历史</li>
<li><strong><code>/effort</code></strong> — 命令行直接调整努力程度，<code>/effort</code> 后按左右箭头切换</li>
<li><strong><code>Shift+Tab</code></strong> — 切换权限模式（默认询问 / 自动接受编辑 / 仅计划模式），写代码时最常用的快捷键</li>
<li><strong><code>/status</code></strong> — 随时看当前模型和上下文用量，心里有数</li>
</ul><blockquote><p>⚠️ 权限模式用 <code>Shift+Tab</code> 切到「自动接受编辑」后，AI 改代码不再逐个询问，速度快很多，但改动前建议先看它准备干什么。</p></blockquote></section>

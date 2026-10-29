---
title: "Maven模型与仓库"
date: 2026-05-16
category: "javawebai/后端基础"
description: "Maven的三大模型（项目对象模型、依赖管理模型、构建生命周期模型）及仓库体系（本地仓库、中央仓库、远程仓库）"
tags: ["Java", "Maven"]
cover: "/media/8c31c48a5882.png"
---

<section><h1 id="maven模型与仓库">Maven模型与仓库</h1><section><h2 id="maven模型">Maven模型</h2><p>Maven 基于三种核心模型构建：</p><section><h3 id="1-构建生命周期模型build-lifecycle--phases">1. 构建生命周期模型（Build Lifecycle &#x26; Phases）</h3><p>定义标准化构建流程。当需要编译时，Maven 提供编译插件；需要打包时，提供打包插件等。</p><p></p><center><figure><img src="/media/8c31c48a5882.png" alt=""><figcaption>构建生命周期模型</figcaption></figure></center><p></p></section><section><h3 id="2-项目对象模型project-object-model">2. 项目对象模型（Project Object Model）</h3><p>将项目抽象成一个对象模型，拥有专属坐标（唯一标识），通过坐标可以定位到所需资源位置。</p><p></p><center><figure><img src="/media/cfc029a58a95.png" alt=""><figcaption>项目对象模型</figcaption></figure></center><p></p><p>坐标由三部分组成：</p>

<table><thead><tr><th>组成部分</th><th>含义</th><th>示例</th></tr></thead><tbody><tr><td><code>groupId</code></td><td>组织名（域名反写）</td><td><code>com.itheima</code></td></tr><tr><td><code>artifactId</code></td><td>模块名</td><td><code>maven-project01</code></td></tr><tr><td><code>version</code></td><td>版本号</td><td><code>1.0-SNAPSHOT</code></td></tr></tbody></table><p></p><center><figure><img src="/media/bd6a6d885bc5.png" alt=""><figcaption>Maven项目坐标示例</figcaption></figure></center><p></p></section><section><h3 id="3-依赖管理模型dependency">3. 依赖管理模型（Dependency）</h3><p>使用坐标描述当前项目依赖哪些第三方 jar 包。过去需要手动复制 jar 包到 <code>lib</code> 目录，现在只需在 <code>pom.xml</code> 中配置依赖即可，对应的 jar 包存储在本地 Maven 仓库中。</p><p></p><center><figure><img src="/media/136c83f25436.png" alt=""><figcaption>依赖管理模型</figcaption></figure></center><p></p><p></p><center><figure><img src="/media/4a852bee99f8.png" alt=""><figcaption>pom.xml依赖配置</figcaption></figure></center><p></p><p></p><center><figure><img src="/media/e9d98dbfd631.png" alt=""><figcaption>本地仓库jar文件</figcaption></figure></center><p></p></section></section><section><h2 id="maven仓库">Maven仓库</h2><p>仓库本质是一个目录（文件夹），用于存储开发中所有依赖（jar 包）和插件。</p><p>Maven 仓库分为三类：</p>

<table><thead><tr><th>仓库类型</th><th>说明</th></tr></thead><tbody><tr><td><strong>本地仓库</strong></td><td>自己计算机上的目录，用来存储 jar 包</td></tr><tr><td><strong>中央仓库</strong></td><td>由 Maven 团队维护的全球唯一仓库，地址：<a href="https://repo1.maven.org/maven2/" target="_blank" rel="noopener noreferrer">https://repo1.maven.org/maven2/</a></td></tr><tr><td><strong>远程仓库（私服）</strong></td><td>一般由公司团队搭建的私有仓库</td></tr></tbody></table><p></p><center><figure><img src="/media/7a6572d6ee23.png" alt=""><figcaption>Maven仓库分类</figcaption></figure></center><p></p><section><h3 id="jar-包查找顺序">jar 包查找顺序</h3><p>当项目中使用坐标引入依赖 jar 包后：</p><ol>
<li>先查找<strong>本地仓库</strong>中是否有对应的 jar 包
<ul>
<li>有 → 项目直接引用</li>
<li>没有 → 去中央仓库下载到本地仓库</li>
</ul>
</li>
<li>如果搭建了远程仓库（私服），查找顺序变为：<strong>本地仓库 → 远程仓库 → 中央仓库</strong></li>
</ol></section></section><section><h2 id="注意事项">注意事项</h2><ul>
<li>中央仓库在国外，下载速度可能较慢，建议配置阿里云私服镜像加速。</li>
<li>私服中通常缓存了常用的开源 jar 包，可以减少外网访问。</li>
</ul></section></section>

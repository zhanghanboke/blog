---
title: "Maven概述与核心作用"
date: 2026-05-16
category: "javawebai/后端基础"
description: "Maven的定义、核心作用（依赖管理、项目构建、统一项目结构）及基本介绍"
tags: ["Java", "Maven"]
cover: "/media/3f2cb7f2a4e6.png"
---

<section><h1 id="maven概述">Maven概述</h1><section><h2 id="定义">定义</h2><p>Maven 是一款用于管理和构建 Java 项目的工具，是 Apache 旗下的一个开源项目。</p><p></p><center><figure><img src="/media/3f2cb7f2a4e6.png" alt=""><figcaption>Maven介绍</figcaption></figure></center><p></p><p>Apache 软件基金会成立于 1999 年 7 月，是目前世界上最大的开源软件基金会，专门为支持开源项目而生的非盈利性组织。开源项目列表：<a href="https://www.apache.org/index.html#projects-list" target="_blank" rel="noopener noreferrer">https://www.apache.org/index.html#projects-list</a></p><p>官网：<a href="https://maven.apache.org/" target="_blank" rel="noopener noreferrer">https://maven.apache.org/</a></p><p></p><center><figure><img src="/media/367a81973856.png" alt=""><figcaption>Maven官网</figcaption></figure></center><p></p><blockquote><p>Apache Maven 是一个项目管理和构建工具，它基于项目对象模型（Project Object Model，简称 POM）的概念，通过一小段描述信息来管理项目的构建、报告和文档。</p></blockquote></section><section><h2 id="maven的核心作用">Maven的核心作用</h2><p></p><center><figure><img src="/media/aa1a28d501a3.png" alt=""><figcaption>Maven作用总览</figcaption></figure></center><p></p><section><h3 id="1-依赖管理">1. 依赖管理</h3><p>方便快捷地管理项目依赖的资源（jar 包），避免版本冲突问题。</p><p><strong>未使用 Maven 时</strong>：需要手动从官网下载 jar 包，再导入项目。</p><p></p><center><figure><img src="/media/1b64747724de.png" alt=""><figcaption>使用Maven前</figcaption></figure></center><p></p><p><strong>使用 Maven 后</strong>：只需在 <code>pom.xml</code> 中添加依赖配置，Maven 自动下载对应的依赖。</p><p></p><center><figure><img src="/media/71d58b2e38fd.png" alt=""><figcaption>使用Maven后</figcaption></figure></center><p></p></section><section><h3 id="2-项目构建">2. 项目构建</h3><p>Maven 提供标准化的跨平台自动化构建方式。代码需要经历编译、测试、打包、发布等过程，Maven 通过一套简单的命令完成这些操作：</p><p></p><center><figure><img src="/media/f5299d13926c.png" alt=""><figcaption>项目构建流程</figcaption></figure></center><p></p><p></p><center><figure><img src="/media/5c6a4deecbaa.png" alt=""><figcaption>Maven构建命令</figcaption></figure></center><p></p><p>通过 Maven 命令即可完成编译（compile）、测试（test）、打包（package）、发布（deploy）等操作，且跨平台适用（Windows / Linux / Mac）。</p></section><section><h3 id="3-统一项目结构">3. 统一项目结构</h3><p>Maven 提供了一套标准的 Java 项目目录结构：</p><p></p><center><figure><img src="/media/1b9c3efd7007.png" alt=""><figcaption>Maven标准目录结构</figcaption></figure></center><p></p><p>无论使用 Eclipse、MyEclipse 还是 IDEA，只要是基于 Maven 构建的 Java 项目，目录结构都相同，可以在各开发工具之间直接导入使用。</p><p></p><center><figure><img src="/media/10faf253b423.png" alt=""><figcaption>跨IDE导入</figcaption></figure></center><p></p><p><strong>目录结构说明</strong>：</p><ul>
<li><code>src/main/java</code>：源代码文件</li>
<li><code>src/main/resources</code>：源代码配置文件</li>
<li><code>src/test/java</code>：测试代码文件</li>
<li><code>src/test/resources</code>：测试代码配置文件</li>
<li><code>target</code>：编译、打包生成文件存放目录</li>
</ul></section></section><section><h2 id="注意事项">注意事项</h2><ul>
<li>Maven 内容分为 Maven 核心和 Maven 进阶两部分，基础阶段先学习核心部分。</li>
<li>Maven 本身也是用 Java 开发的，运行时依赖其他 jar 包。</li>
</ul></section></section>

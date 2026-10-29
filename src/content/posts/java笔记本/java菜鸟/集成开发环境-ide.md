---
title: "Java基础"
date: 2026-02-06
category: "java笔记本/java菜鸟"
description: "嘿，欢迎来到Java基础小课堂！别被“基础”俩字骗了——IDEA里一个Alt+Insert能省下半小时，package写错一行代码就跑不起来…咱们不讲虚的，就聊那些真正写代码时天天碰、又容易踩坑的实在事儿。准备好了？来，一起从IDEA和包开始捋清楚～"
tags: ["java"]
---

<section><h2 id="一集成开发环境-ide">一、集成开发环境 (IDE)</h2><section><h3 id="1-idea-介绍与使用">1. IDEA 介绍与使用</h3><p>​<strong>IDEA (IntelliJ IDEA)</strong> ：业界公认的优秀Java开发工具，支持多种语言。</p><p>​<strong>基本使用</strong>​：以<strong>项目 (Project)</strong>  为单位管理Java源码。</p><p><strong>常用快捷键</strong> (可自定义)：</p><ul>
<li>删除当前行：Ctrl + D</li>
<li>复制当前行：Ctrl + Alt + ↓</li>
<li>代码补全：Alt + /</li>
<li>注释/取消注释：Ctrl + /</li>
<li>自动导包 &#x26; 优化导入：Alt + Enter</li>
<li>格式化代码：Ctrl + Alt + L</li>
<li>快速运行：Alt + R</li>
<li>生成代码 (构造器、Getter/Setter等)：Alt + Insert</li>
<li>查看类层级关系：Ctrl + H</li>
<li>定位到方法定义：Ctrl + B</li>
<li>自动分配变量名：表达式.var</li>
</ul><p>​<strong>重要设置</strong>：</p><ul>
<li>​<strong>主题与字体</strong>​：File -> Settings -> Appearance &#x26; Behavior / Editor -> Font</li>
<li>​<strong>字符编码</strong>​：File -> Settings -> Editor -> File Encodings 设置为 UTF-8。</li>
</ul></section></section>
<section><h2 id="二包-package">二、包 (Package)</h2><section><h3 id="1-包的作用">1. 包的作用</h3><ol>
<li>​<strong>区分同名类</strong>：解决多人开发时的命名冲突。</li>
<li>​<strong>管理类</strong>：将功能相似的类组织在一起，便于管理和查找（参考Java API文档结构）。</li>
<li>​<strong>控制访问范围</strong>：配合访问修饰符使用（见第三部分）。</li>
</ol></section><section><h3 id="2-包的本质与使用">2. 包的本质与使用</h3><p>​<strong>本质</strong>​：就是​<strong>文件夹/目录</strong>，用于保存和管理.class文件。</p><p>​<strong>定义语法</strong>：package 包名; (必须放在源文件第一行)。</p><p>​<strong>命名规范</strong>：小写字母 + 小圆点。通常为：com.公司名.项目名.业务模块名。例如：com.sina.crm.user。</p><p>​<strong>常用包</strong>：</p><ul>
<li>java.lang.*：基本包，默认自动引入。</li>
<li>java.util.*：工具包（如Scanner, Arrays）。</li>
<li>java.net.*：网络开发包。</li>
<li>java.awt.*：图形界面开发包。</li>
</ul><p>​<strong>引入包 (import)</strong> ：</p><ul>
<li>语法：import 包名.类名; 或 import 包名.*; (导入该包下所有类)。</li>
<li>位置：位于package语句之后，类定义之前。</li>
<li>​<strong>建议</strong>​：需要哪个类就导入哪个，不建议使用*通配符。</li>
</ul></section></section>

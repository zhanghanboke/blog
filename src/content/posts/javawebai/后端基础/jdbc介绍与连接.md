---
title: "JDBC介绍与连接"
date: 2026-05-19
category: "javawebai/后端基础"
description: "JDBC（Java DataBase Connectivity）是Java操作关系型数据库的底层API规范。"
tags: ["Java", "JDBC", "数据库"]
---

<section><h1 id="jdbc介绍与连接">JDBC介绍与连接</h1><section><h2 id="定义">定义</h2><p><strong>JDBC（Java DataBase Connectivity）</strong>，是使用Java语言操作关系型数据库的一套API，也是操作数据库最为基础、底层的技术。</p><p><strong>本质：</strong></p><ul>
<li>sun公司官方定义的一套操作所有关系型数据库的规范，即接口。</li>
<li>各个数据库厂商去实现这套接口，提供数据库驱动jar包。</li>
<li>开发者使用这套接口(JDBC)编程，真正执行的代码是驱动jar包中的实现类。</li>
</ul></section><section><h2 id="架构">架构</h2><p>在Java代码中通过JDBC接口操作数据库，底层由各数据库厂商的驱动实现：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">Java Application</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">       </span></span><span style="--0:#abb2bf;--1:#383a42">│</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">  </span></span><span style="--0:#abb2bf;--1:#383a42">JDBC API (接口)</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">       </span></span><span style="--0:#abb2bf;--1:#383a42">│</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">  </span></span><span style="--0:#abb2bf;--1:#383a42">数据库驱动 (MySQL / Oracle / ...)</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">       </span></span><span style="--0:#abb2bf;--1:#383a42">│</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">    </span></span><span style="--0:#abb2bf;--1:#383a42">数据库</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="Java Application       │  JDBC API (接口)       │  数据库驱动 (MySQL / Oracle / ...)       │    数据库"><div></div></button></div></figure></div></section><section><h2 id="生态定位">生态定位</h2><p>JDBC是操作数据库最为基础、底层的技术。在企业项目开发中，一般都会使用基于JDBC封装的高级框架：</p>

<table><thead><tr><th>框架</th><th>市场地位</th></tr></thead><tbody><tr><td>Mybatis</td><td>最为主流</td></tr><tr><td>MybatisPlus</td><td>其次</td></tr><tr><td>Hibernate</td><td>较少</td></tr><tr><td>SpringDataJPA</td><td>较少</td></tr></tbody></table></section><section><h2 id="常见场景">常见场景</h2><ul>
<li>直接编写JDBC程序执行SQL语句（学习/小型工具）</li>
<li>作为Mybatis/MybatisPlus等框架的底层依赖</li>
</ul></section><section><h2 id="注意事项">注意事项</h2><ul>
<li>JDBC程序需要手动管理数据库连接、结果集解析和资源关闭，代码较为繁琐。</li>
<li>生产环境中一般不直接使用原生JDBC，而是使用基于JDBC封装的高级框架。</li>
<li>数据库驱动jar包需与数据库版本匹配。</li>
</ul></section><section><h2 id="相关链接">相关链接</h2><ul>
<li><a href="../../../../posts/JavaWebAI/JDBC%E6%9F%A5%E8%AF%A2%E6%93%8D%E4%BD%9C">JDBC查询操作</a></li>
<li><a href="../../../../posts/JavaWebAI/JDBC%E5%A2%9E%E5%88%A0%E6%94%B9%E6%93%8D%E4%BD%9C">JDBC增删改操作</a></li>
<li><a href="../../../../posts/JavaWebAI/Mybatis%E5%9F%BA%E7%A1%80">Mybatis基础</a></li>
</ul></section></section>

---
title: "MySQL数据模型"
date: 2026-05-18
category: "javawebai/后端基础"
description: "关系型数据库的二维表模型与MySQL的数据存储层次结构"
tags: ["前端", "MySQL", "数据库"]
cover: "/media/7897c06964dd.png"
---

<section><h1 id="mysql数据模型">MySQL数据模型</h1><section><h2 id="定义">定义</h2><p><strong>关系型数据库（RDBMS）</strong>：建立在关系模型基础上，由多张相互连接的<strong>二维表</strong>组成的数据库。二维表由行（记录）和列（字段）组成。</p><p></p><center><figure><img src="/media/7897c06964dd.png" alt=""><figcaption>二维表示例</figcaption></figure></center><p></p></section><section><h2 id="二维表的优点">二维表的优点</h2><ul>
<li>使用表存储数据，格式统一，便于维护</li>
<li>使用 SQL 语言操作，标准统一，使用方便，可用于复杂查询</li>
</ul><blockquote><p>基于二维表存储数据的数据库是关系型数据库；反之则是非关系型数据库（如 Redis）。</p></blockquote></section><section><h2 id="mysql-数据存储层次">MySQL 数据存储层次</h2><p></p><center><figure><img src="/media/b2c0cdc23308.png" alt=""><figcaption>MySQL数据模型</figcaption></figure></center><p></p><p><strong>存储层次（由大到小）</strong>：</p><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#abb2bf;--1:#383a42">数据库服务器</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">  </span></span><span style="--0:#abb2bf;--1:#383a42">└── 数据库1</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">  </span></span><span style="--0:#abb2bf;--1:#383a42">│     ├── 表A（多行记录）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">  </span></span><span style="--0:#abb2bf;--1:#383a42">│     └── 表B</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">  </span></span><span style="--0:#abb2bf;--1:#383a42">└── 数据库2</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span class="indent"><span style="--0:#abb2bf;--1:#383a42">        </span></span><span style="--0:#abb2bf;--1:#383a42">└── 表C</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="数据库服务器  └── 数据库1  │     ├── 表A（多行记录）  │     └── 表B  └── 数据库2        └── 表C"><div></div></button></div></figure></div><p>MySQL 客户端通过 DBMS 发送 SQL，DBMS 根据 SQL 指令操作数据库中的表及数据。</p></section><section><h2 id="常见场景">常见场景</h2><p>在 MySQL 中存储数据的步骤：</p><ol>
<li>创建数据库（多个数据库间相互独立）</li>
<li>在数据库下创建数据表（一个数据库可含多张表）</li>
<li>将数据存入数据表（一张表可存多行数据）</li>
</ol></section><section><h2 id="注意事项">注意事项</h2><ul>
<li>MySQL、Oracle、DB2、SQL Server 都属于关系型数据库（基于二维表）。</li>
<li>非关系型数据库（NoSQL）如 Redis，不基于二维表存储。</li>
</ul></section></section>

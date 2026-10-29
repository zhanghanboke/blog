---
title: "IO流"
date: 2026-03-11
category: "java笔记本/java菜鸟"
description: "嘿，别被“IO流”这名字唬住——它其实就是程序和文件之间传纸条的方式 😄   读个配置、存张图片、写段日志……全靠它悄悄搭桥。今天咱们不啃概念，就聊怎么让Java乖乖把数据“拿进来”又“送出去”，顺手避开那些删不掉的空目录、写不进的乱码、还有忘了close的坑。"
tags: ["java"]
cover: "/media/45fbb2c9d1c0.webp"
---

<section><h2 id="一-文件操作">一、 文件操作</h2><section><h3 id="11-文件与文件流">1.1 文件与文件流</h3><ul>
<li><strong>文件</strong>：保存数据的地方。</li>
<li><strong>文件流</strong>：文件在程序中以流的形式进行操作。</li>
</ul></section><section><h3 id="12-创建文件对象-file-类">1.2 创建文件对象 (File 类)</h3><ul>
<li>
<p><strong>构造器</strong>：</p>
<ol>
<li>new File(String pathname)：根据路径字符串构建。<br>
<center><figure><img alt="" loading="lazy" decoding="async" width="611" height="328" src="/media/45fbb2c9d1c0.webp" srcset=""><figcaption>|500</figcaption></figure></center>​</li>
</ol>
</li>
</ul><ol start="2">
<li>new File(File parent, String child)：根据父目录文件对象+子路径构建。</li>
<li>new File(String parent, String child)：根据父目录字符串+子路径构建。</li>
</ol></section><section><h3 id="13-获取文件信息">1.3 获取文件信息</h3><ul>
<li>
<p><strong>常用方法</strong>：</p>
<ul>
<li>getName()：获取文件名。</li>
<li>getAbsolutePath()：获取文件绝对路径。</li>
<li>getParent()：获取文件父级目录。</li>
<li>length()：获取文件大小（字节）。</li>
<li>exists()：判断文件是否存在。</li>
<li>isFile()：判断是否为文件。</li>
<li>isDirectory()：判断是否为目录。</li>
</ul>
</li>
</ul></section><section><h3 id="14-目录操作与文件删除">1.4 目录操作与文件删除</h3><ul>
<li>mkdir()：创建<strong>一级</strong>目录。</li>
<li>mkdirs()：创建<strong>多级</strong>目录。</li>
<li>delete()：删除<strong>空目录</strong>或​<strong>文件</strong>。</li>
</ul></section></section>
<section><h2 id="二-io流原理与分类">二、 IO流原理与分类</h2><section><h3 id="21-原理">2.1 原理</h3><ul>
<li>I/O 指 Input/Output，用于数据传输。</li>
<li>Java 程序中，数据输入/输出以  <strong>“流 (stream)”</strong>  形式进行。</li>
<li>java.io 包提供各种流类和接口。</li>
<li><strong>输入</strong>：将外部数据（磁盘等）读入到程序（内存）。</li>
<li><strong>输出</strong>：将程序（内存）数据写出到外部设备（磁盘等）。</li>
</ul></section><section><h3 id="22-流的分类体系">2.2 流的分类体系</h3><ol>
<li>
<p><strong>按操作数据单位</strong>：</p>
<ul>
<li><strong>字节流 (8 bit)</strong> ：用于处理二进制文件（如图片、视频、音频）。</li>
<li><strong>字符流 (按字符)</strong> ：用于处理文本文件。</li>
</ul>
</li>
<li>
<p><strong>按数据流向</strong>：</p>
<ul>
<li><strong>输入流</strong>：从数据源到程序。</li>
<li><strong>输出流</strong>：从程序到目的地。</li>
</ul>
</li>
<li>
<p><strong>按流的角色</strong>：</p>
<ul>
<li><strong>节点流</strong>：直接从数据源/目的地读写数据。</li>
<li><strong>处理流（包装流）</strong> ：对节点流进行包装，提供更强大的功能。</li>
</ul>
</li>
</ol></section><section><h3 id="23-抽象基类与命名规律">2.3 抽象基类与命名规律</h3><ul>
<li>所有流都派生自四个抽象基类：</li>
</ul>

<table><thead><tr><th>抽象基类</th><th>字节流</th><th>字符流</th></tr></thead><tbody><tr><td><strong>输入流</strong></td><td>InputStream</td><td>Reader</td></tr><tr><td><strong>输出流</strong></td><td>OutputStream</td><td>Writer</td></tr></tbody></table><ul>
<li><strong>命名规律</strong>：子类名以其父类名作为后缀（如 FileInputStream）。</li>
</ul></section></section>
<section><h2 id="三-常用节点流">三、 常用节点流</h2><section><h3 id="31-字节输入流-fileinputstream">3.1 字节输入流 FileInputStream</h3><ul>
<li>
<p><strong>作用</strong>：从文件读取字节数据到程序。</p>
</li>
<li>
<p><strong>读取方式</strong>：</p>
<ol>
<li>read()：每次读取一个字节，返回 int，到文件末尾返回 -1。</li>
<li>read(byte[] b)：每次读取最多 b.length 个字节到字节数组，返回实际读取的字节数，到文件末尾返回 -1。</li>
</ol>
</li>
</ul></section><section><h3 id="32-字节输出流-fileoutputstream">3.2 字节输出流 FileOutputStream</h3><ul>
<li>
<p><strong>作用</strong>：将程序的字节数据写入文件。</p>
</li>
<li>
<p><strong>写入方式</strong>：</p>
<ol>
<li>write(int b)：写入一个字节。</li>
<li>write(byte[] b)：写入整个字节数组。</li>
<li>write(byte[] b, int off, int len)：写入字节数组的指定部分。</li>
</ol>
</li>
<li>
<p><strong>构造器</strong>：</p>
<ul>
<li>new FileOutputStream(filePath)：覆盖写入。</li>
<li>new FileOutputStream(filePath, true)：追加写入。</li>
</ul>
</li>
<li>
<p><strong>注意</strong>：如果文件不存在，会自动创建（前提是目录存在）。</p>
</li>
</ul></section><section><h3 id="33-字符输入流-filereader">3.3 字符输入流 FileReader</h3><ul>
<li>
<p><strong>作用</strong>：从文件读取字符数据到程序。</p>
</li>
<li>
<p><strong>读取方式</strong>（同 InputStream 思路，操作单位是 char）：</p>
<ol>
<li>read()：每次读取一个字符。</li>
<li>read(char[] cbuf)：每次读取多个字符到字符数组。</li>
</ol>
</li>
</ul></section><section><h3 id="34-字符输出流-filewriter">3.4 字符输出流 FileWriter</h3><ul>
<li>
<p><strong>作用</strong>：将程序的字符数据写入文件。</p>
</li>
<li>
<p><strong>写入方式</strong>（同 OutputStream 思路）：</p>
<ol>
<li>write(int c)：写入一个字符。</li>
<li>write(char[] cbuf) / write(String str)：写入字符数组或字符串。</li>
<li>write(String str, int off, int len)：写入字符串的指定部分。</li>
</ol>
</li>
<li>
<p><strong>重要</strong>​：使用 FileWriter 后，​<strong>必须关闭流 (close())</strong>  或 ​<strong>刷新流 (flush())</strong> ，数据才会真正写入文件。</p>
</li>
</ul></section></section>
<section><h2 id="四-常用处理流包装流">四、 常用处理流（包装流）</h2><section><h3 id="41-处理流概述">4.1 处理流概述</h3><ul>
<li>
<p><strong>作用</strong>​：包装节点流，提供缓冲、便捷操作等功能，​<strong>不直接连接数据源</strong>。</p>
</li>
<li>
<p><strong>优势</strong>：</p>
<ol>
<li><strong>提高性能</strong>：通过内部缓冲区减少IO次数。</li>
<li><strong>操作便捷</strong>：提供更方便的方法（如 readLine()）。</li>
</ol>
</li>
<li>
<p><strong>关闭</strong>：只需关闭最外层的处理流，底层会自动关闭节点流。</p>
</li>
</ul></section><section><h3 id="42-缓冲流高效">4.2 缓冲流（高效）</h3><ul>
<li>
<p><strong>BufferedReader /</strong>  ​​<strong>BufferedWriter</strong>：</p>
<ul>
<li>包装字符流，提供缓冲。</li>
<li>readLine()：按行读取文本，高效便捷。</li>
<li>newLine()：写入一个行分隔符。</li>
<li><strong>注意</strong>​：只能用于处理​<strong>文本文件</strong>。</li>
</ul>
</li>
<li>
<p><strong>BufferedInputStream /</strong>  ​​<strong>BufferedOutputStream</strong>：</p>
<ul>
<li>包装字节流，提供缓冲。</li>
<li>用于处理​<strong>二进制文件</strong>（如图片、音频拷贝），效率更高。</li>
</ul>
</li>
</ul></section><section><h3 id="43-对象流序列化与反序列化">4.3 对象流（序列化与反序列化）</h3><ul>
<li>
<p><strong>作用</strong>​：保存和恢复对象的<strong>值</strong>和​<strong>数据类型</strong>。</p>
</li>
<li>
<p><strong>ObjectOutputStream</strong>​：提供<strong>序列化</strong>功能，将对象写入文件。</p>
</li>
<li>
<p><strong>ObjectInputStream</strong>​：提供<strong>反序列化</strong>功能，从文件读取对象。</p>
</li>
<li>
<p><strong>序列化要求</strong>：</p>
<ol>
<li>被序列化的类必须实现 Serializable 接口（标记接口）。</li>
<li>建议添加 serialVersionUID 以提高版本兼容性。</li>
<li>序列化对象时，默认序列化所有属性（除了 static 和 transient 修饰的成员）。</li>
<li>序列化具有可继承性。</li>
</ol>
</li>
<li>
<p><strong>注意事项</strong>：读写顺序必须一致。</p>
</li>
</ul></section><section><h3 id="44-转换流解决编码问题">4.4 转换流（解决编码问题）</h3><ul>
<li><strong>作用</strong>​：在字节流和字符流之间进行转换，并可以​<strong>指定编码</strong>。</li>
<li><strong>InputStreamReader</strong>：将 InputStream（字节输入流）包装成 Reader（字符输入流）。</li>
<li><strong>OutputStreamWriter</strong>：将 OutputStream（字节输出流）包装成 Writer（字符输出流）。</li>
<li><strong>应用场景</strong>：处理纯文本数据时，使用字符流效率更高，并能有效解决中文乱码问题。</li>
</ul></section><section><h3 id="45-打印流">4.5 打印流</h3><ul>
<li>
<p><strong>PrintStream</strong> / ​<strong>PrintWriter</strong>：</p>
<ul>
<li>只有输出流，没有输入流。</li>
<li>提供了一系列重载的 print() 和 println() 方法，输出非常方便。</li>
<li>System.out 就是 PrintStream 类型。</li>
</ul>
</li>
</ul></section></section>
<section><h2 id="五-properties-类">五、 Properties 类</h2><section><h3 id="51-概述">5.1 概述</h3><ul>
<li><strong>Properties</strong> 类继承自 Hashtable，是专门用于读写<strong>配置文件</strong>的集合类。</li>
<li><strong>配置文件格式</strong>​：键=值（键值对，无需空格，值默认String类型）。</li>
</ul></section><section><h3 id="52-常用方法">5.2 常用方法</h3><ul>
<li>load(InputStream inStream)：从输入字节流加载属性列表（键值对）。</li>
<li>list(PrintStream out)：将属性列表输出到指定打印流。</li>
<li>getProperty(String key)：根据键获取值。</li>
<li>setProperty(String key, String value)：设置键值对。</li>
<li>store(OutputStream out, String comments)：将属性列表写入输出字节流（保存到文件）。</li>
</ul></section><section><h3 id="53-应用">5.3 应用</h3><ul>
<li>用于读取 .properties 配置文件（如数据库连接信息）。</li>
<li>可以方便地修改和保存配置。</li>
</ul></section></section>

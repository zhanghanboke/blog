---
title: "Java 反射"
date: 2026-03-11
category: "java笔记本/java菜鸟"
description: "嘿，你有没有试过写完代码，突然发现——哎，要是能不改一行源码，光靠配个文件就让程序调用不同的类和方法，那该多爽？Java 反射就是干这个的。它像给 JVM 装了面“魔法镜子”，让你在运行时看清、摸到、甚至调用任何类的里里外外。虽然有点慢，但框架、Spring、Hibernate……全靠它撑腰。来，咱们轻松聊聊这面镜子怎么照、照哪儿、以及别被它闪了眼 😄"
tags: ["java"]
cover: "/media/5a72ffd5dd72.webp"
---

<section><h2 id="一-反射的需求与快速入门">一、 反射的需求与快速入门</h2><section><h3 id="11-引出反射的需求">1.1 引出反射的需求</h3><ul>
<li>
<p><strong>场景</strong>：根据配置文件（如 re.properties）中的信息（类全路径、方法名），动态创建对象并调用方法。</p>
</li>
<li>
<p><strong>优势</strong>：<strong>不修改源码</strong>，仅通过外部配置文件即可控制程序，符合设计模式的<strong>开闭原则（OCP）</strong>。这是框架技术的底层核心。</p>
</li>
</ul></section><section><h3 id="12-快速入门案例">1.2 快速入门案例</h3><ol>
<li>
<p>读取配置文件，获取类全路径 classfullpath 和方法名 methodName。</p>
</li>
<li>
<p><strong>传统</strong> <strong>new</strong> <strong>对象方式行不通</strong>，因为类名在编译时不确定。</p>
</li>
<li>
<p><strong>反射解决方案</strong>：</p>
</li>
</ol><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="java"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 1. 加载类，返回Class对象</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Class</span><span style="--0:#E6888F;--1:#AF4238"> cls </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">Class</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">forName</span><span style="--0:#ABB2BF;--1:#383A42">(classfullpath);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 2. 通过Class对象创建运行时实例</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Object</span><span style="--0:#E6888F;--1:#AF4238"> o </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">cls</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">newInstance</span><span style="--0:#ABB2BF;--1:#383A42">();</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 3. 通过Class对象获取方法对象（万物皆对象）</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Method</span><span style="--0:#E6888F;--1:#AF4238"> method1 </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">cls</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">getMethod</span><span style="--0:#ABB2BF;--1:#383A42">(methodName);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">7</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 4. 通过方法对象调用方法：method1.invoke(o);</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// 1. 加载类，返回Class对象Class cls = Class.forName(classfullpath);// 2. 通过Class对象创建运行时实例Object o = cls.newInstance();// 3. 通过Class对象获取方法对象（万物皆对象）Method method1 = cls.getMethod(methodName);// 4. 通过方法对象调用方法：method1.invoke(o);"><div></div></button></div></figure></div></section></section>
<section><h2 id="二-反射机制原理">二、 反射机制原理</h2><section><h3 id="21-java-reflection-定义">2.1 Java Reflection 定义</h3><ul>
<li>
<p>反射机制允许程序在<strong>运行期</strong>借助 Reflection API 取得任何类的内部信息，并能操作对象的属性和方法。</p>
</li>
<li>
<p><strong>原理核心</strong>：类加载后，在堆中会生成一个唯一的 <strong>Class</strong> <strong>类对象</strong>，它像一面“镜子”，包含了该类的完整结构信息（成员变量、构造器、成员方法等）。通过这个 Class 对象可以反向获取类的结构。</p>
</li>
</ul></section><section><h3 id="22-反射能完成的操作">2.2 反射能完成的操作</h3><ol>
<li>
<p>运行时判断任意对象的类。</p>
</li>
<li>
<p>运行时构造任意类的对象。</p>
</li>
<li>
<p>运行时获取任意类的成员变量和方法。</p>
</li>
<li>
<p>运行时调用任意对象的成员变量和方法。</p>
</li>
<li>
<p>生成动态代理。</p>
</li>
</ol></section><section><h3 id="23-反射相关的主要类-javalangreflect">2.3 反射相关的主要类 (java.lang.reflect)</h3>

<table><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>类</td><td>代表</td><td>作用</td></tr><tr><td><strong>java.lang.Class</strong></td><td>一个类</td><td>表示某个类加载后在堆中的对象。<strong>反射的入口</strong>。</td></tr><tr><td><strong>java.lang.reflect.Method</strong></td><td>类的方法</td><td>通过 Class 对象获取，代表某个类的方法。</td></tr><tr><td><strong>java.lang.reflect.Field</strong></td><td>类的成员变量</td><td>通过 Class 对象获取，代表某个类的成员变量。</td></tr><tr><td><strong>java.lang.reflect.Constructor</strong></td><td>类的构造方法</td><td>通过 Class 对象获取，代表某个类的构造器。</td></tr></tbody></table></section><section><h3 id="24-反射的优缺点与性能优化">2.4 反射的优缺点与性能优化</h3><ul>
<li>
<p><strong>优点</strong>：<strong>动态性</strong>，使框架具备灵活扩展能力，是框架技术的底层支撑。</p>
</li>
<li>
<p><strong>缺点</strong>：主要是<strong>解释执行</strong>，对执行速度有影响。</p>
</li>
<li>
<p><strong>性能优化</strong>：通过 Method/Field/Constructor 对象的 setAccessible(true) 方法，可以<strong>关闭访问安全检查（暴破）</strong>，能显著提高反射效率。</p>
</li>
</ul></section></section>
<section><h2 id="三-class-类">三、 Class 类</h2><section><h3 id="31-class-类特点">3.1 Class 类特点</h3><ol>
<li>
<p>Class 也是类，继承自 Object。</p>
</li>
<li>
<p>Class 类对象<strong>不是</strong> <strong>new</strong> <strong>出来的</strong>，而是由JVM在类加载时创建的。</p>
</li>
<li>
<p>对于某个类，在内存中<strong>只有一份</strong> Class 对象（因为类只加载一次）。</p>
</li>
<li>
<p>每个对象实例都记得它是由哪个 Class 对象生成的。</p>
</li>
<li>
<p>Class 对象包含了类的完整结构，可通过API获取。</p>
</li>
<li>
<p>Class 对象存放在<strong>堆</strong>中，类的字节码二进制数据（元数据）存放在<strong>方法区</strong>。</p>
</li>
</ol></section><section><h3 id="32-获取-class-类对象的六种方式">3.2 获取 Class 类对象的六种方式</h3>

<table><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>方式</td><td>代码示例</td><td>应用场景</td><td>备注</td></tr><tr><td><strong>1.</strong> <strong>Class.forName</strong></td><td>Class cls1 = Class.forName(“全类名”);</td><td><strong>多用于配置文件</strong>，读取全类名，加载类。</td><td>可能抛出 ClassNotFoundException。</td></tr><tr><td><strong>2. 类名.class</strong></td><td>Class cls2 = Cat.class;</td><td><strong>多用于参数传递</strong>，安全可靠，性能高。</td><td>最常用。</td></tr><tr><td><strong>3. 对象.getClass()</strong></td><td>Class cls3 = 对象.getClass();</td><td>已有对象实例，获取其 Class 对象。</td><td>获取对象的运行时类型。</td></tr><tr><td><strong>4. 类加载器</strong></td><td>ClassLoader cl = 对象.getClass().getClassLoader();<br><br>Class cls4 = cl.loadClass(“全类名”);</td><td>通过类加载器动态加载。</td><td></td></tr><tr><td><strong>5. 基本数据类型.class</strong></td><td>Class cls5 = int.class;</td><td>获取基本数据类型的 Class 对象。</td><td></td></tr><tr><td><strong>6. 包装类.TYPE</strong></td><td>Class cls6 = Integer.TYPE;</td><td>获取基本数据类型对应包装类的 Class 对象。</td><td>与方式5的 Class 对象相同。</td></tr></tbody></table></section><section><h3 id="33-哪些类型有-class-对象">3.3 哪些类型有 Class 对象？</h3><ul>
<li>所有类型都有 Class 对象：外部类、内部类、接口、数组、枚举、注解、基本数据类型、void。</li>
</ul></section></section>
<section><h2 id="四-类加载">四、 类加载</h2><section><h3 id="41-静态加载-vs-动态加载">4.1 静态加载 vs 动态加载</h3><ul>
<li>
<p><strong>静态加载</strong>：编译时加载相关类。如果类不存在，则<strong>编译报错</strong>。依赖性太强。</p>
<ul>
<li><em>触发时机</em>：new 对象、访问静态成员、继承等。</li>
</ul>
</li>
<li>
<p><strong>动态加载</strong>：运行时加载需要的类。如果运行时未使用该类，即使不存在也不报错。降低了依赖性。</p>
<ul>
<li><em>触发时机</em>：<strong>反射</strong>。</li>
</ul>
</li>
</ul></section><section><h3 id="42-类加载过程">4.2 类加载过程</h3><ol>
<li>
<p><strong>加载 (Loading)</strong>：将类的字节码文件读入内存，并为之创建一个 java.lang.Class 对象。</p>
</li>
<li>
<p><strong>连接 (Linking)</strong>：</p>
<ul>
<li>
<p><strong>验证 (Verification)</strong>：确保字节码文件符合JVM规范，安全。</p>
</li>
<li>
<p><strong>准备 (Preparation)</strong>：为<strong>静态变量</strong>分配内存并设置<strong>默认初始值</strong>。</p>
<ul>
<li><em>注意</em>：static final 修饰的常量，在准备阶段会直接赋值为指定的值。</li>
</ul>
</li>
<li>
<p><strong>解析 (Resolution)</strong>：将常量池中的符号引用替换为直接引用。</p>
</li>
</ul>
</li>
<li>
<p><strong>初始化 (Initialization)</strong>：执行类构造器 <clinit>() 方法的过程，真正为静态变量赋值并执行静态代码块。JVM保证此过程线程安全。</clinit></p>
</li>
</ol></section></section>
<section><h2 id="五-通过反射获取类的结构信息">五、 通过反射获取类的结构信息</h2><section><h3 id="51-第一组javalangclass-方法">5.1 第一组：java.lang.Class 方法</h3>

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>方法</td><td>作用</td></tr><tr><td>getName()</td><td>获取全类名。</td></tr><tr><td>getSimpleName()</td><td>获取简单类名。</td></tr><tr><td>getFields()</td><td>获取所有 <strong>public</strong> 修饰的属性（包含父类的）。</td></tr><tr><td>getDeclaredFields()</td><td>获取<strong>本类中所有</strong>属性（任何修饰符）。</td></tr><tr><td>getMethods()</td><td>获取所有 <strong>public</strong> 修饰的方法（包含父类的）。</td></tr><tr><td>getDeclaredMethods()</td><td>获取<strong>本类中所有</strong>方法。</td></tr><tr><td>getConstructors()</td><td>获取所有 <strong>public</strong> 修饰的构造器。</td></tr><tr><td>getDeclaredConstructors()</td><td>获取<strong>本类中所有</strong>构造器。</td></tr><tr><td>getPackage()</td><td>获取包信息。</td></tr><tr><td>getSuperclass()</td><td>获取父类的 Class 对象。</td></tr><tr><td>getInterfaces()</td><td>获取实现的接口的 Class 数组。</td></tr></tbody></table></section><section><h3 id="52-第二组javalangreflectfield-方法">5.2 第二组：java.lang.reflect.Field 方法</h3>

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>方法</td><td>作用</td></tr><tr><td>getModifiers()</td><td>以 int 形式返回修饰符。可配合 Modifier 类解读。</td></tr><tr><td>getType()</td><td>以 Class 形式返回属性类型。</td></tr><tr><td>getName()</td><td>返回属性名。</td></tr></tbody></table></section><section><h3 id="53-第三组javalangreflectmethod-方法">5.3 第三组：java.lang.reflect.Method 方法</h3>

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>方法</td><td>作用</td></tr><tr><td>getModifiers()</td><td>以 int 形式返回修饰符。</td></tr><tr><td>getReturnType()</td><td>以 Class 形式获取返回类型。</td></tr><tr><td>getName()</td><td>返回方法名。</td></tr><tr><td>getParameterTypes()</td><td>以 Class[] 返回参数类型数组。</td></tr></tbody></table></section><section><h3 id="54-第四组javalangreflectconstructor-方法">5.4 第四组：java.lang.reflect.Constructor 方法</h3>

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>方法</td><td>作用</td></tr><tr><td>getModifiers()</td><td>以 int 形式返回修饰符。</td></tr><tr><td>getName()</td><td>返回构造器名（全类名）。</td></tr><tr><td>getParameterTypes()</td><td>以 Class[] 返回参数类型数组。</td></tr></tbody></table></section></section>
<section><h2 id="六-通过反射创建对象和访问成员">六、 通过反射创建对象和访问成员</h2><section><h3 id="61-创建对象">6.1 创建对象</h3><ol>
<li><strong>调用无参构造器</strong>（类中必须有 public 无参构造）：</li>
</ol><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="java"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Class</span><span style="--0:#E6888F;--1:#AF4238"> cls </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">Class</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">forName</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#98C379;--1:#387138">"全类名"</span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Object</span><span style="--0:#E6888F;--1:#AF4238"> o </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">cls</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">newInstance</span><span style="--1:#383A42"><span style="--0:#ABB2BF">();</span><span style="--0:#E6888F"> </span></span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 已过时，推荐用构造器</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="Class cls = Class.forName(&#x22;全类名&#x22;);Object o = cls.newInstance(); // 已过时，推荐用构造器"><div></div></button></div></figure></div><ol start="2">
<li><strong>调用指定构造器</strong>：</li>
</ol><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="java"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 1. 获取指定参数类型的构造器对象</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Constructor</span><span style="--0:#E6888F;--1:#AF4238"> constructor </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">cls</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">getDeclaredConstructor</span><span style="--0:#ABB2BF;--1:#383A42">(参数类型.</span><span style="--0:#E5C07B;--1:#AF4238">class</span><span style="--0:#ABB2BF;--1:#383A42">, ...);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">3</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 2. 如果是非public构造器，需要暴破</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">4</div></div><div class="code"><span style="--0:#E5C07B;--1:#AF4238">constructor</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">setAccessible</span><span style="--0:#ABB2BF;--1:#383A42">(</span><span style="--0:#D19A66;--1:#875D01">true</span><span style="--0:#ABB2BF;--1:#383A42">);</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">5</div></div><div class="code"><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 3. 调用构造器创建实例</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">6</div></div><div class="code"><span style="--0:#E5C07B;--1:#885D01">Object</span><span style="--0:#E6888F;--1:#AF4238"> o </span><span style="--1:#383A42"><span style="--0:#56B6C2">=</span><span style="--0:#E6888F"> </span></span><span style="--0:#E5C07B;--1:#AF4238">constructor</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">newInstance</span><span style="--0:#ABB2BF;--1:#383A42">(实参列表);</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="// 1. 获取指定参数类型的构造器对象Constructor constructor = cls.getDeclaredConstructor(参数类型.class, ...);// 2. 如果是非public构造器，需要暴破constructor.setAccessible(true);// 3. 调用构造器创建实例Object o = constructor.newInstance(实参列表);"><div></div></button></div></figure></div></section><section><h3 id="62-访问属性">6.2 访问属性</h3><ol>
<li>根据属性名获取 Field 对象：Field f = cls.getDeclaredField(“属性名”);</li>
</ol><p><img alt="" loading="lazy" decoding="async" width="564" height="234" src="/media/5a72ffd5dd72.webp" srcset=""></p><ol start="2">
<li>
<p>暴破（针对非 public 属性）：f.setAccessible(true);</p>
</li>
<li>
<p>访问：</p>
</li>
</ol><div class="expressive-code"><figure class="frame"><figcaption class="header"></figcaption><pre data-language="java"><code><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">1</div></div><div class="code"><span style="--0:#E5C07B;--1:#AF4238">f</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">set</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(o, 值);</span><span style="--0:#E6888F"> </span></span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 设置属性值</span></div></div><div class="ec-line"><div class="gutter"><div class="ln" aria-hidden="true">2</div></div><div class="code"><span style="--0:#E5C07B;--1:#AF4238">f</span><span style="--0:#ABB2BF;--1:#383A42">.</span><span style="--0:#61AFEF;--1:#3360C1">get</span><span style="--1:#383A42"><span style="--0:#ABB2BF">(o);</span><span style="--0:#E6888F">     </span></span><span style="--0:#9FA3AA;--0fs:italic;--1:#646568;--1fs:italic">// 获取属性值</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="f.set(o, 值); // 设置属性值f.get(o);     // 获取属性值"><div></div></button></div></figure></div><ul>
<li><em>注意</em>：如果是静态属性，set 和 get 中的对象参数 o 可以写成 null。</li>
</ul></section><section><h3 id="63-访问方法">6.3 访问方法</h3><ol>
<li>
<p>根据方法名和参数列表获取 Method 对象：Method m = cls.getDeclaredMethod(“方法名”, 参数类型.class, …);</p>
</li>
<li>
<p>暴破（针对非 public 方法）：m.setAccessible(true);</p>
</li>
<li>
<p>调用：Object returnValue = m.invoke(o, 实参列表);</p>
<ul>
<li>
<p><em>注意</em>：如果是静态方法，invoke 中的对象参数 o 可以写成 null。</p>
</li>
<li>
<p>返回值类型为 Object，但其实际运行类型与方法定义的返回类型一致。</p>
</li>
</ul>
</li>
</ol></section></section>

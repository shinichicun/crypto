## 标题

\#一阶标题 （快捷键Ctrl+1）

\##二阶标题 （快捷键Ctrl+2）

\###三阶标题 （快捷键Ctrl+3）

\####四阶标题 （快捷键Ctrl+4）

\#####五阶标题 （快捷键Ctrl+5）

\######六阶标题 （快捷键Ctrl+6）

## 如何生成目录

```crystal
@[TOC]目录



 



在文章开始地方输入[toc]，即可在对应位置插入目录



@[TOC]目录



 



以下不用写，直接写@[TOC](目录)即可自动获到目录中



#一阶标题 （快捷键Ctrl+1）



##二阶标题 （快捷键Ctrl+2）



###三阶标题 （快捷键Ctrl+3）



####四阶标题 （快捷键Ctrl+4）



#####五阶标题 （快捷键Ctrl+5）



######六阶标题 （快捷键Ctrl+6）



注：凡是文章标题带有#（1-n个）的都会被捕获到目录中。
```

## 文本居中

这是要居中的文本内容

**注**：Typora目前并不会直接预览居中效果——相应的效果只有输出文本的时候才会显现。

## 下划线

下划线使用格式 下划线的内容<u> 或者快捷键Ctrl+U

下划线在Typora显示形式是 这就是我亲测的下划线

## 删除线

删除线使用格式：~~ 删除线的内容

## 字体加粗

前面某个字段使用两个*，\*加粗字体* 或者快捷键Ctrl+B

## 字体倾斜

使用一个”星“，*字体倾斜了* 或者快捷键Ctrl+I

## 图片的插入

直接拖你想要图片进来即可

## 超链接

- 使用快捷键Ctrl+K
- 使用2个反斜杠""，
  [百度][https://www.baidu.com/]

百度一下

**注**：按住Ctrl键+点击上面链接就可以直接访问该链接

## 代码区域

三个反引号个（```）+编程语言即可

```cpp
//设置线程名字



thread.setName("线程1"); 



thread1.setName("线程2");
```

## 表格的使用

第一种：快捷键**Ctrl+T**

第二种：|ID|name|age|回车即可

学号姓名年龄20200506MarkerHunJava35

## 任务列表

\- [ ] 文字 （**注**：注意用空格隔开）

- [x] Java
- [x] 大数据
- [ ] 人工智能
- [ ] 机器学习

## 有序无序列表

**创建无序列** :+ 、- 、* （后面加空格）

**多行无序列表**:

- Java
  - 容器
    - HashMap

**有序列表**:(1.)空格

1. Java
2. Biodata

**多行有序列表：**

```undefined
1. Java



2. Biodata



    1. Java



    2. Biodata
```

## 水平分割线

```undefined
***或者- - -
```

## 引用的使用格式

```undefined
>+空格
```

## 表情

```undefined
:单词
```

## 数学表达式

Typora支持加入用LaTeX写成的数学公式，并且在软件界面下用MathJax直接渲染，数学公式分为两种参考**Mathpix Snip**

- 行内公式 `$ ... $`
- 行间公式 `$$ ... $$`,（或者$$+回车）**注**：行间公式形式是将数学式插在文本行之间（多行公式、公式组和微积分方程等复杂的数学式都是采用行间） **注**：行内公式形式是将数学式插入文本行之内（适合编写简 短的数学式） **如**：将公式插入到本行内，符号：`$公式内容$`，$xyz$或“$$”+回车即可

\#### 1、上标、下标、求和、括号、分式、根号

**语法**：行内公式输入在两个`

‘之间，行外公公式‘‘之间，行外公公式‘

内容公式

‘或‘‘或‘     

`+回车即可输入。





![5b93657b7cb8e1503798e938d80b8d4a.png](https://img-blog.csdnimg.cn/img_convert/5b93657b7cb8e1503798e938d80b8d4a.png)

### 2、基本运算符



![66f56d706bdf662329e9c3a5de0e9fcc.png](https://img-blog.csdnimg.cn/img_convert/66f56d706bdf662329e9c3a5de0e9fcc.png)

### 3、三角函数、指数、对数



![aaf120832bb744189736e5f54e55f4cc.png](https://img-blog.csdnimg.cn/img_convert/aaf120832bb744189736e5f54e55f4cc.png)

### 4、高等数学相关运算符



![a081123fcc53c84aa7b923902343241f.png](https://img-blog.csdnimg.cn/img_convert/a081123fcc53c84aa7b923902343241f.png)

### 6、希腊字母



![0f081d6382fa3b6dd0caaa969acd4aae.png](https://img-blog.csdnimg.cn/img_convert/0f081d6382fa3b6dd0caaa969acd4aae.png)

### 甘特图

~~~javascript
```mermaid



	gantt



	        dateFormat  YYYY-MM-DD



	        title Adding GANTT diagram functionality to mermaid



	        section 现有任务



	        已完成               :done,    des1, 2019-09-02,220-01-20



	        进行中               :active,  des2, 2020-05-06, 3d



	        计划一               :         des3, after des2, 5d



	        计划二               :         des4, after des3, 5d



　```
~~~



![778c1d0d11e6e130e2bb4981aee97131.png](https://img-blog.csdnimg.cn/img_convert/778c1d0d11e6e130e2bb4981aee97131.png)

### Mermaid流程图

~~~css
```mermaid



	graph LR



	graph LR



	A[老鹰] -- 吃 --> B((小鸡))



	A -- 吃 --> C(蛇)



	B -- 吃--> D{虫}



	C --> D



	```
~~~



![41be935a688c4eb478bd14c800361def.png](https://img-blog.csdnimg.cn/img_convert/41be935a688c4eb478bd14c800361def.png)
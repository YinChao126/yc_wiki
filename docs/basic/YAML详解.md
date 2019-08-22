# YAML简易速成手册

作者：尹超

日期：2019-8-22

本文只提供最简单的YAML使用说明，确保小白能在10分钟内看懂或者写出一个简单的YAML配置文件。想要了解更多请移步参考链接

[TOC]

## 1. YAML简介

YAML是一种编程语言，这种语言以数据为中心，能实现一种可被电脑识别的数据序列化格式(YAML格式)。YAML格式既容易被人类阅读，又可以和脚本语言交互，还可以和被编程语言的程序导入，如 C/C++, Ruby, Python, Java, Perl, C#, PHP等。

实际使用时，YAML常用来实现复杂的工程配置，书写上比json格式更简洁。

YAML文件后缀名统一为：`.yml`

## 2. YAML极简知识概要

### 2.1 基本约定

- 只有三种格式：对象，值（常量），数组
- 只支持#行注释
- 大小写敏感
- 使用索进代表层级关系
- 索进只能空格，层级必须对齐

### 2.2 简单示例

```
# 表示url属性值；
url: http://www.wolfcode.cn 
# 表示server.host属性的值；
server:
    host: http://www.wolfcode.cn 
# 数组，表示server为[a,b,c]
server:
    - 120.168.117.21
    - 120.168.117.22
    - 120.168.117.23
# 常量
pi: 3.14   #定义数值
hasChild: true  #定义boolean值
name: '你好YAML'   #定义字符串
```

### 2.3 对象

用**冒号加一个空格**代表对象和值的关系，类似于字典。形如： `key: value`

#### 注意事项

- 冒号后面必须加一个空格

- 可以用缩进表示层级关系，比如：

```
key: 
    sub_1: v1
    sub_2: v2
```

这个代表 key.sub1 = v1, key.sub2 = v2

- 支持流式语法，比如上述例子可以写作：

```
key: {sub_1: v1, sub_2: v2}
```

### 2.4 值

必须是常量，包括：整数，浮点数，字符串，NULL，日期，布尔，时间。

```
boolean: 
    - TRUE  #true,True都可以
    - FALSE  #false，False都可以
float:
    - 3.14
    - 6.8523015e+5  #可以使用科学计数法
int:
    - 123
    - 0b1010_0111_0100_1010_1110    #二进制表示
null:
    nodeName: 'node'
    parent: ~  #使用~表示null
string:
    - 哈哈
    - 'Hello world'  #可以使用双引号或者单引号包裹特殊字符
    - newline
      newline2    #字符串可以拆成多行，每一行会被转化成一个空格
date:
    - 2018-02-17    #日期必须使用ISO 8601格式，即yyyy-MM-dd
datetime: 
    -  2018-02-17T15:02:31+08:00   
```

### 2.5 数组

用**短横线加一个空格**代表数组元素，形如：

```
hobby:
    - Java
    - LOL
```

#### 注意事项

- 短横线后必须加空格
- 支持流式编程，比如：

```

```

- 可以嵌套，比如：

```

```

## 3. YAML在Python上的应用

### 安装

`pip install pyyaml`

### 使用

极其简单，load, dump搞定

### 示例代码

```
import yaml

fin = open('test.yml', encoding='utf-8')
data = yaml.load(fin)
print(data)
fout = open('output.yml', 'w', encoding='utf-8')
yaml.dump(data, fout, default_flow_style=False,encoding='utf-8',allow_unicode=True)#中文编解码的解决方法

```

## 4. 参考链接

[YAML格式和yml文件](http://blog.sina.com.cn/s/blog_53ab41fd0102whll.html)

[YAML快速入门](https://www.jianshu.com/p/97222440cd08)

[YAML官方规范_v1.2](http://yaml.org/spec/1.2/spec.pdf)
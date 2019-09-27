# Lambda匿名函数详解

作者：尹超

日期：2019-9-27

## 简介

Lambda表达式的作用是生成一个匿名函数，应用场景是：需要一个函数，但又不想费神去造一个，更不想污染环境。该函数的性质也只是用到一次！

## 引言

需求是将一个list的内容求平方

方法1：用函数

```
def sq(x):
	return x * x
```

方法2：用lambda表达式

```
lambda x: x*x
```

## lambda原理

lambda表达式实质上表征了一种运算关系，表现上看就是一个小型函数

## lambda实战

### 用法1 直接定义

```
p = lambda x,y:x+y
print(p(4,6))
```

### 用法2 和map配合

考察 r = map(f, a)

- f代表某种运算关系（lambda表达式或者函数）
-  a代表一组可迭代的对象
- map表示把a中的每个元素都套到f运算关系式中去做计算
- r返回一个迭代器。通过 for item in r可以还原成数据列表

实现一个将l = [1,3,7,2,3] 的每个元素求平方的完整过程如下：

```
l = [1, 3, 7, 2, 3]
r = map(lambda x:x*x, l)
for item in r:
	print(item)
```

## 参考链接

[Lambda 表达式有何用处？如何使用？](https://www.zhihu.com/question/20125256)


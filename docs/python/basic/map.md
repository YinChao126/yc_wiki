# map详解

作者：尹超

日期：2019-9-27

## 简介

map是python的内置函数，用来解决**映射关系**问题。

## 语法

`map(function, iterable, ...)`

function是函数关系

iterable是数据，序列，lambda表达式等一切可迭代的东西

## 返回值

python2返回列表

python3返回迭代器（需要自己for出来具体内容）

## 示例

需求，求一个序列a=[1,2,3,...,10]的平方

解决1：

```
out = []
for i in range(1, 11):
	out.append(i*i)
```

解决2：

```
def sq(x):
	return x*x
out = map(sq, [y for y in range(1,11)])
```

解决3：

```
out = map(lambda x: x**2, [y for y in range(1,11)])
```
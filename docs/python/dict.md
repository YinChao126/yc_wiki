# 字典的用法

作者：尹超

更新时间：2019-6-26

​	字典的结构就是键值对，形如{key:value}，描述了key和value的对应关系。常用的是用来描述一个整体的各种属性.比如： person = {'name':'lily', 'sex':'male', 'age':29}，下文详细介绍了字典结构的新建、索引、增加、删除的方法。

​	下文统一假设用户是在**python3环境下**

## 几个常识

字典类似一个无序列表，总是通过key来索引

key总是唯一的，如果新增重名的key，则会覆盖前面的

key必须是常量（可以是数字，字符串，元组，但不能是列表）

## 新建

```python
dic = {} #新建一个空的字典对象
dic = {key:value} #新建包含一个键值对的字典对象
dic = {k1:v1, k2:v2, ..., kn:vn} #新建一个包含n个键值对的字典对象
```

## 索引

最简单：

```python
value = dic[k1]  #已知key，索引value
value = dic.get(key) #使用get方法
```

完整索引

```python
for key in dic:
	value = dic[key]
	print(key, value) #key和value得到完整索引
```

## 修改，增加

```python
dic[key] = value #如果dic中没有key，则增加，如果已有key，则更新值
```

## 删除

```python
del dic[key] #删除一个键值对
dic.clear() #清空所有键值对
del dic  #完整删除字典对象
```

## 内置函数，方法一览表

dict包含如下内置方法：

```python
clear() #删除所有键值对
copy() #浅复制
get(key,default = None) #返回指定key的值，如不存在则返回default
keys() #以列表的形式返回字典中所有的key
values() #以列表的形式返回字典中左右的value
items() #以列表的形式返回元组数组
pop(key) #删除指定的key所对应的值，同时返回key所对应的值
popitem() #删除最后一个键值对，并返回那个key-value
```

支持的内置函数如下

```python
len(dic) #求dic的键值对个数
str(dic) #把dic变成字符串
type(dic) #返回dic类型
```

## 实战技巧

```python
dic = {k1:v1, k2:v2, ..., kn:vn} 

使用keys方法
v = dic.keys()
for key in v:
    print(key) #此处索引出整个dic的key
    
使用values方法
v = dic.values()
for value in v:
    print(value) #此处索引出整个dic的value值

使用items方法
dict_item = dic.items()
for key, value in dict_item:
	print(key, value) #此处顺利索引出key，value
    
方法2：
for key in dic:
    value = dic[key]
    print(key, value) #此处索引出key，value
```

## 参考链接

[python字典详解](http://www.runoob.com/python/python-dictionary.html)


# regular expression正则表达式示例

作者：尹超

日期：2019-7-1

## 环视

`value = 78 ms`

经常会碰到形如上述字符串中寻找数字的问题，此时需要用到环视

```
(?=...)   肯定顺序环视，子表达式能匹配右侧的文本
(?!...)   否定顺序环视，子表达式不能匹配右侧的文本
(?<=...)  肯定逆序环视，子表达式能匹配左侧的文本
(?<!...)  否定逆序环视，子表达式不能匹配左侧的文本
```

pattern = "(?<=value = )\d+(?= ms)"

最终能找到78



## re使用的一般步骤

1. 先写pattern，正则表达式（核心步骤）
2. 再编译， reobj = re.compile(pattern)
3. 然后进行字符串匹配， result = reobj.findall(input_str)
4. 最后看看匹配结果， 如果找到，则result是一个数组

## 查找

一般来说，有两种查找方式

1. findall以list形式列出所有匹配项
2. search以group的方式可选列出匹配项

举例如下：

```python
import re


inputstr = '6050345'

pattern_id = '(\d\d)(\d{4})'
reobj = re.compile(pattern_id)
id = reobj.findall(inputstr)  #第一种方法
print(id)   #此处输出：'60','5034'

matchobj = re.search(pattern_id,inputstr)  #第二种方法
print(matchobj.group(0)) #此处输出：605034     group(0),完整匹配内容
print(matchobj.group(1)) #此处输出：60         group(1),第一个捕获
print(matchobj.group(2)) #此处输出：5034       group(2),第二个捕获
```

## 替换

基本思路

1. import re

2. 明确待处理的src_string = 'hello world'，待替换的内容： sub_content = 'python'

3. 想好正则表达式： pattern = 'world'

4. 编译正则表达式： reobj = re.compile(pattern)

5. 执行替换命令:  result = reobj.sub(sub_content, src_string)

示例程序

```python
import re
a = 'hello world'
strinfo = re.compile('world')
b = strinfo.sub('python',a)
print(b)
```

## 一个替换实例

需求： 替换文本中的版本号

假设有如下文本filename.txt需要替换版本号为1.2.0：

```
 #基本格式如下：
 xxx
 version = '1.1.0' 
 asfsaf
```

使用的替换语法：
` out = re.sub(pattern, replace, src_string)`

 其中

-  pattern为正则表达式，找到1.1.0这个字符串
-  replace为1.2.0，待替换的字符串
-  src_string为原始待替换的文本
-  out为替换后的文本

 源码为：

```python
with open(filename, 'r') as fh:
	content = fh.read() #读取文本
pattern = '(?<=version = \').+(?=\')'
out = re.sub(pattern, '1.2.0', content) #执行替换
with open(filename, 'w') as fh: #替换后的内容写入文本
	fh.write(out)
```



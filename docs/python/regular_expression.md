# regular expression正则表达式示例

作者：尹超

日期：2019-7-1

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


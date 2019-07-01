# 用于python的PEP8编码规范

## 代码布局

使用4个空格来缩进

使用反斜杠换行

最大行长79个字符

top level函数和类的定义间空两行

类中间的方法空一行

函数体中谨慎使用空行来分割不同逻辑，尽量保证同一个过程不空行

无关函数之间空一行

源文件中一直使用utf-8编码

## import导入

import必须单独成行，且一次import一个

import总是在最上行，位于脚本注释之后，全局变量之前

先import标准库，再import第三方库，最后import本地库

推荐用绝对路径导入，避免相对路径

```python
import a
import a.b
import a.b as d
from a import b #不推荐
```

## 空格

避免在任何行尾留下空格

避免紧跟在括号后面的空格

```
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )
```

避免紧跟在逗号，分号，冒号之前的空格

```
Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x
```

切片时禁止空格： a[1:9:3]

在如下操作符之间留空格（=、+=、==、<、is、and）

算术式下空格以突出优先级

函数内赋值时不用空格

```
# 好的方式
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# 不好的方式
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```



## 注释

修改代码时一定要注意同步修改注释（错误的注释比不注释更惨）

只使用英文注释

只允许使用#进行注释（'''  '''是docstrings独有）

块注释标准：

```python
# description：
# 
# input:
#
# output:
```

行注释最少和代码空两格，尽量不写，要写就要短小精悍，切忌冗余注释

## documentation Strings(docstrings) 注释标准

请遵循[PEP 257](http://legacy.python.org/dev/peps/pep-0257/) 规范

一定要为所有的公共模块、函数、类、方法编写docstrings，非公有则不必(但必须的def那一行写注释，以描述基本信息)

## 命名规范（业界一直未统一，本节为自定义的习惯）

类命请用驼峰法

模块、包全部小写，用下划线增加可读性

方法、函数名全部小写，下划线可选

全局变量尽量只在本模块内有效，只能用`__all__`的机制防止对外暴露或者在全局变量前加一个下划线以格外提醒。

常量总是大写，可用下划线分割

## 参考链接

[PEP8规范官方定义](https://legacy.python.org/dev/peps/pep-0008/)

[PEP8规范中文版](https://blog.csdn.net/ratsniper/article/details/78954852)
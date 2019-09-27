# pyinstaller将脚本编译成exe

## 背景

在python工程完成开发以后需要编译成可执行文件，如此一来生产环境和开发环境隔离开来便于用户使用（可独立使用，无需配置python开发环境）

## pyinstaller的安装

`pip install pyinstaller`

## pyinstaller执行原理和流程

- 先生成一个spec文件（手动或自动均可），该文件决定了实际编译规则
- 再自动生成一个build文件夹，所有自动编译的中间产物都放在其中
- 最后生成dist文件夹，存放编译输出

## pyinstaller使用

最简单（单个文件）：

 `pyinstaller xxx.py`

一般搞法（多文件）

- 先自动生成spec文件： `pyi-makespec xxx.py`
- 再根据自己的实际需求手动修改spec文件
- 最后统一installer： `pyinstaller xxx.spec`

## pyinstaller重要命令参数

h 打印帮助信息

v 打印版本信息

F 生成一个单一可执行文件

d 生成带各种依赖的文件夹，包含exe，dll,以及其他文件

i 修改exe生成的图标

p 指定搜索路径

w 禁止弹出控制台

## spec文件解析

```
Analysis: 
    ['Console.py','xxx.py'...] <- 此处列出的脚本生成exe后会按顺序依次执行！
    pathex <- 此处为搜索路径
    binaries <- 非python的库文件
    datas <- ini文件，字体，图片，icon什么的
    pure <- python模块
PYZ: <- 不用管
EXE: <- 输出配置
COLLECT: <- 不用管
```

## 路径冻结

如果编译后的exe在打包的机器上运行良好，放到别人机器上不能用了。很可能用了固定的绝对路径
解决方案是用相对路径

```python
#frozen_dir.py
import os,sys

def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)
```

添加frozen_dir.py后，app_path会生成一个绝对准确的基地址，所有的路径以此为基准即可

## 参考链接

[pyinstaller使用详细教程](https://www.crifan.com/use_pyinstaller_to_package_python_to_single_executable_exe/)

[pyinstaller官网手册](https://pyinstaller.readthedocs.io/en/v3.3.1/index.html)

[spec修改示例](https://blog.csdn.net/weixin_42052836/article/details/82315118)

[py,pyc,pyo,pyd的讲解，不同需求不同打包策略](https://blog.csdn.net/u010159842/article/details/53212443)
# python的路径问题

作者：尹超

日期：2019-7-1

## 背景描述

​	一般而言，python脚本在执行时候的工作路径都默认是该脚本的路径，但奇怪的是使用不同IDE（比如spyder）这一点不一定能保证。从而导致使用相对路径导入模块或读写数据失败。

​	解决方案是搞清楚工作路径在哪里，有必要的话可以主动切换。

## 获取当前执行脚本的路径

```
CUR_PATH = os.path.split(os.path.realpath(__ file __))[0]
```

## 获取给定路径的父路径

```
父路径 = os.path.abspath(os.path.join(子路径, os.pardir))
```

## 获取当前的工作路径（脚本执行路径不一定是工作路径）

```
os.getcwd() 
```

## 切换工作路径

```
os.chdir(PATH)
```

## 将当前路径增加到系统搜索

```
sys.path.append(WORK_PATH)
```

## 解析路径和文件名

```python
import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path) #此处解析路径和文件名
    print(head, tail)

path = r'E:/GitHubCenter/SuperGuard/data.xlsx'
file_name = path_leaf(path)
```


# python开发环境搭建

作者：尹超

日期：2019.1.9

## 1. python常见开发方法

anaconda：数据分析、机器学习常用

pycharm：据称是最好的商业python IDE	

vscode：轻量级VisualStudio，智能提示升级依赖包

最便利：安装Anaconda3，大部分的依赖包统统安装好，cmd/spyder/jupyter三种不同层次的调试环境都有了。

## 2. anaconda安装与配置

先去官网[下载anaconda安装包](http://docs.anaconda.com/anaconda/install/)

### 2.1 下载

非常简单，直接下载官方正版即可，[传送门](https://www.anaconda.com/distribution/)。

### 2.2 安装

一路默认安装即可

### 2.3 环境配置

一定要在系统变量的path里增加如下三条路径，缺一不可

```
your_installer_path\Anaconda3\
your_installer_path\Anaconda3\Scripts
your_installer_path\Anaconda3\Library\bin
```

之后记得重启生效

## 3. PyCharm配置

## 4. VSCode平台下python配置



## 坑

Anaconda方案中，如果没有正确配置系统参数，至少会导致如下两个问题

- cmd命令行下无法打开python的命令解释器

该问题出现的原因是windows系统默认路径下没有找到python.exe，根源在于python.exe的路径没有添加到系统路径下。

- cmd可以打开python解释器，但是无法pip安装软件，提示如下：

`pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available`

此问题是由于your_path\Anaconda3\Library\bin路径没有增加导致的

## 参考链接

[Anaconda官网安装教程](http://docs.anaconda.com/anaconda/install/windows/)

[python常用插件推荐](https://www.cnblogs.com/pleiades/p/8284562.html)

[VSCode正确编码姿势](http://www.cnblogs.com/bloglkl/p/5797805.html)
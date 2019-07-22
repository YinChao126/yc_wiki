# python版本问题

## 1. 版本共存（windows环境）

同一台PC中(windows操作系统下)，如果同时安装Python2和Python3环境，会在执行python命令时出现错误，操作系统会找到默认的配置进行执行。怎么样才能让python2和python3一起工作又互相不影响呢？

## 解决方案

找到python2的安装目录，把python.exe重命名为"python2.exe"

在系统变量中增加path路径

把如下三个路径增加到path里去（标准做法，一定要记得做）

```
python27
python27\scripts
python27\Library\bin
```

cmd中输入python2即可进入python2.7的环境了，特别地，现有状态下没办法通过pip来安装模块了，取而代之的是：

python2 -m pip install module_name

## 2. python3.5升级到python3.6+（linux环境）

```
#安装python3.6
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.6 /usr/bin/python3

#重新安装pip
wget https://bootstrap.pypa.io/get-pip.py  --no-check-certificate
sudo python get-pip.py
```

### 参考链接

[Ubuntu16.04怎样安装Python3.6](https://www.cnblogs.com/yjlch1016/p/8641910.html)

[ubuntu升级python版本(3.5->3.6)](https://blog.csdn.net/u013749068/article/details/84102749)
# 更换源提高pip下载速度

使用pip可以方便地安装软件包，形如：

- pip install packge_name
- pip install package_name=1.2.0

然而默认的pip源是国外的，导致有些包下载非常费时。

解决方法很简单，将pip的源改成国内的即可

## 步骤

linux下，修改 ~/.pip/pip.conf (没有就创建)， 修改 index-url至tuna，内容如下：

```
 [global]
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

```
 [global]
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

enjoy！


## 参考链接

[更改pip源至国内镜像，显著提升下载速度](https://blog.csdn.net/lambert310/article/details/52412059)
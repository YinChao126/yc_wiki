# NFS挂载

作者：尹超

日期：2020-1-15

## 1. NFS是什么

NFS，network file system，一种文件系统，是由[SUN](https://baike.baidu.com/item/SUN/69463)公司研制的[UNIX](https://baike.baidu.com/item/UNIX/219943)[表示层](https://baike.baidu.com/item/%E8%A1%A8%E7%A4%BA%E5%B1%82/4329716)协议，能使使用者访问网络上别处的文件就像在使用自己的计算机一样。其实就是[RPC](https://baike.baidu.com/item/%E8%BF%9C%E7%A8%8B%E8%BF%87%E7%A8%8B%E8%B0%83%E7%94%A8/7854346?fromtitle=RPC&fromid=609861)远程过程调用，是一个C/S架构。

NFS本质上与jffs2，yaffs，ext4等是一类东西，就是文件系统。但是区别在于可以通过网络来挂载，而不用写到设备上。

## 2. NFS怎么用

由于NFS是C/S结构，所以需要先搭建服务器，然后通过客户端来使用即可。

## 3. NFS服务器搭建

### Linux版

1. 下载NFS服务器： `sudo apt-get install nfs-kernel-server`

2. 配置NFS服务器：`sudo vim /etc/exports`

默认是没有任何配置的，可以添加：

```
/work/nfs *(rw,sync,no_root_squash) 
/var/lib/tftpboot *(rw,sync,no_root_squash)
```

配置解释：

- /work/nfs :允许客户端挂载的目录，可添加任意多个，如不设置服务器将不允许客户端挂载。
- *:允许所有IP的主机挂载该目录，详细配置[请参考](https://blog.csdn.net/redhat7890/article/details/6191735)。

3. 重启NFS服务器即可： `sudo /etc/init.d/nfs-kernel-server restart`

## Windows版

1. 下载NFS服务器：下载HaneWin：[NFS Server](http://r.hanewin.net/nfs1244.exe)，默认安装即可

2. 开放防火墙入站端口号2049（默认）
3. 以管理员的方式启动NFS Server，在Edit-Preferences-Exports选项卡中新增要挂载的目录：点击Edit exports file，新增 `E:\your_file -name:f1`，则将your_file目录重命名为f1，如此一来client只需要mount f1这个文件夹即可访问资源了
4. File-service-start，以启动NFS server即可

## 4. NFS客户端使用

### Linux版

先确保开启了NFS客户端功能，尝试：`showmount -e  NFS_server_ip`

如果没有信息，则需要重新安装NFS客户端： `sudo apt install nfs-common`

然后挂载NFS服务器资源：

syntax: `mount [NFS serverip]:[NFS share path] [Linux_mount_dir]`

举例： `mount 192.168.3.119:/car /home/yinchao/nfs_dir` 

此处尤其注意：192.168.3.119服务器上的真实挂载路径是E:/my_car, 通过配置文件重命名成/car了

### Windows版

先确保开启了NFS客户端功能：控制面板-启用或关闭Windows功能-NFS服务全部勾上

挂载NFS服务器资源： 

syntax： `mount [NFS server ip]:[NFS share path] 盘符`

举例： `mount 192.168.3.137:/home/yinchao/nfs_share Y:`

挂载完成后，在我的电脑上可以看到多出了一个盘符。

## 5. 卸载

```
umount 盘符     #指定卸载
umount -f -a   #全部卸载
```



## 6. FAQ

### 6.1 只读不能写？

A. NFS server中的配置信息决定了client端的权限，需要修改server的配置信息

B. client最终能否写并不仅仅只取决于配置信息，还取决于是否是root权限，具体解决参考[如下链接](https://jingyan.baidu.com/article/c910274bfd6800cd361d2df3.html)

C. 如果还不行，则右击文件，选择属性-NFS属性，将RWX属性全部勾选，所有者UID和组UID全部设置为0，基本上可写了。[参考出处](https://blog.csdn.net/qq_34158598/article/details/81976063)

### 6.2 中文传输乱码？

windows环境下：控制面板-区域-管理=更改系统区域设置-勾选Beta 版:使用UTF-8提供全球语言支持

## 参考链接

[NFS百度百科{基础知识参考}](https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/9719420?fromtitle=NFS&fromid=812203&fr=aladdin)

[通过NFS实现Linux和windows共享文件夹{文件共享参考}](https://blog.csdn.net/weixin_44024220/article/details/95624847)

[NFS挂载那些事{嵌入式开发参考}](https://zhuanlan.zhihu.com/p/28556875)

[Win10安装NFS服务器并实现Linux访问](https://blog.csdn.net/shouzang/article/details/80993749)
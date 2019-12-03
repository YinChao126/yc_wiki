# Linux和Windows局域网内实现文件共享

作者：尹超

日期：2019-10-10

## keywords

linux, windows, file share

## 前提：

处于同一个局域网内，相互之间能ping通

相应的端口要开放

## 1. Linux访问windows共享文件夹

### 1. 1 通过mount挂载windows的共享文件夹

```
挂载：mount -t cifs -o username=administrator,password=123456 //192.168.0.1/tmp /mnt/tmp

取消挂载：umount /mnt/tmp
```

### 1.2. 用smbclient

Linux下安装smbclient。 `sudo apt get install smbclient`

通过命令行访问

`smbclient //Windows_IP/share_file -U username%passwd`

### 1.3. 用SSH方式

ssh username@ip即可



## 2. windows访问linux的共享文件夹

请直接参考CSDN博客：[五分钟搞定windows和Linux系统的共享访问](https://blog.csdn.net/yinchao163/article/details/83620250)

## 3. FAQ

### smbclient连接出错

`protococl negotation failed:NT_STATUS_CONNECTION_RESET`

问题原因：默认安装下的smbclient采用SMB1协议，Win10以上系统采用SMB2协议

解决方案：修改smbclient配置文件并重启服务

```
sudo gedit /etc/samba/smb.conf
增加如下两行到[global]字段即可
client min protocol = SMB2
client max protocol = SMB3

sudo service smbd restart #这条命令不起作用
```

## 参考连接

[How to share files between a Linux and Windows computer](https://www.computerhope.com/issues/ch001636.htm)

[Windows 10 Share not accessible from Ubuntu 16.04 LTS](https://superuser.com/questions/1273456/windows-10-share-not-accessible-from-ubuntu-16-04-lts)
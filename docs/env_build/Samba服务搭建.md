# Linux搭建samba服务实现windows共享

日期：2018年11月01日 15:15:01

作者：尹超

## 需求

局域网内部的A/B两台机器需要相互之间传输文件

## 假设

A为Ubuntu 16.04LTS系统， B为Win10系统， A，B位于局域网内部，具有共同的网段。

## 实现方法

在A上兴建一个共享文件夹，只要B可以通过内网来访问该文件夹，即可实现AB的数据传输了

## 实现步骤

### 1. A上架设Samba服务器并启动服务

1.1 samba的安装

```
sudo apt-get install samba samba-common #下载samba软件
```

1.2 建立共享文件夹（假设为/home/share)

```bash
cd /home/user/
mkdir share
```

1.3 为共享文件夹开启读写权限

```bash
sudo chmod 777 share #把share文件夹的权限更改为所有人可操作
```

1.4 修改samba配置文件：打开smb.conf,在文件末尾添加5行配置信息

```
sudo gedit /etc/samba/smb.conf #打开samba配置文件
[share]
    path = /home/share
    avaliable = yes
    browseable = yes
    writable = yes
```

1.5 创建samba账号

```
sudo touch /etc/samba/smbpasswd #创建文件
sudo smbpasswd -a 你的用户名（终端上@符号前面的名字）#设置samba账户
```

1.6 重启samba服务，至此完成linux环境下的所有操作

```
sudo /etc/init.d/smbd restart #重启软件
```

### 2. 实现Windows环境下对Linux共享文件夹的访问

2.1 获取linux的ip地址(由别人告知，或者自己去linux主机上敲命令： ifconfig)

2.2 win+R打开“运行“对话框输入ip地址可以直接看到linux主机的共享文件夹

![img](https://img-blog.csdnimg.cn/20181101150246828.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbmNoYW8xNjM=,size_16,color_FFFFFF,t_70) ->  ![img](https://img-blog.csdnimg.cn/20181101150320865.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbmNoYW8xNjM=,size_16,color_FFFFFF,t_70)

2.3 别高兴太早，此时是不具备访问权限的

### 3. Windows环境下添加Linux访问权限

3.1 Win+R打开“运行”对话框，输入”control userpasswords2“

![img](https://img-blog.csdnimg.cn/20181101150628821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbmNoYW8xNjM=,size_16,color_FFFFFF,t_70)

3.2 在弹出的用户账户选项卡中依次点击： 高级->管理密码->windows凭据->添加windows凭据

 ![img](https://img-blog.csdnimg.cn/20181101150954114.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbmNoYW8xNjM=,size_16,color_FFFFFF,t_70)  ![img](https://img-blog.csdnimg.cn/20181101150908546.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbmNoYW8xNjM=,size_16,color_FFFFFF,t_70)

3.3 在windows凭证里添加之前的samba服务器的ip地址，用户名，密码

![img](https://img-blog.csdnimg.cn/20181101151027403.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbmNoYW8xNjM=,size_16,color_FFFFFF,t_70)

3.4 大功告成，再访问一下共享文件夹，应该具备所有权限了

## 后记

1. 公网上的相互访问还没有测试过，估计差别不大

2. 如果访问不到，可以考虑把linux的防火墙关了 systemctl  stop  firewalld

3. 如果发现linux主机可以ping通windows，但是windows不能ping通linux，参考如下解决方案

https://jingyan.baidu.com/article/a65957f4f557cb24e67f9ba6.html

## 参考链接

https://blog.csdn.net/m0_37673307/article/details/80112161

https://jingyan.baidu.com/article/c146541382b6950bfcfc4ca5.html
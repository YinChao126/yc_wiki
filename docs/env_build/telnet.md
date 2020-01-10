# telnet服务搭建与使用

作者：尹超

日期：2020-1-10

## keywords

telnet, RPC

## 基础介绍

telnet是Internet远程登陆服务的标准协议和主要方式，实际工作中可以在windows工作机上通过telnet远程连接到linux服务器

## Linux主机搭建telnet服务

安装telnet server

```
sudo apt-get install openbsd-inetd
sudo apt-get install telnetd
```

修改配置文件 /etc/inetd.conf

```
sudo vim /etc/inetd.conf
 
#添加内容
 telnet     stream  tcp     nowait  telnetd /usr/sbin/tcpd  /usr/sbin/in.telnetd
```

重启telnet服务

```
sudo /etc/init.d/openbsd-inetd restart
```

查看telnet服务是否开启

```
netstat -a | grep telnet
```

## windows配置telnet服务

开启telnet客户端

控制面板-程序-启用或关闭windows功能，勾选`telnet client`

测试是否成功

cmd下输入： `telnet`

出现： 欢迎使用 Microsoft Telnet Client即可

特别注意：有可能要开放windows的防火墙端口号【23】，如果实在是不通的话

## Windows使用telnet连接Linux服务器

### 方法一

语法： `telnet Linux_ip port_id`

特别注意：port_id为23【默认端口】

可先ping一下linux服务器的ip【假设为192.168.3.137】，如果通了的话再用telnet远程登陆

`telnet 192.168.3.137 23`

输入用户名和密码即可

### 方法二

1. 直接先cmd下输入telnet，进入telnet客户端，此时还未连接
2. 再 `o 192.168.3.137`即可，默认23端口号

## 参考链接

[telnet安装](https://blog.csdn.net/windsnow1/article/details/94429974)

[23端口问题](https://blog.csdn.net/chailihua0826/article/details/88798202)

[微软官方修补telnet服务未找到的问题](
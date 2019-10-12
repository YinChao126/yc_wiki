# Supervisor安装与使用

作者：尹超

日期：2019-10-12

## 1. 简介

supervisor是用**Python**开发的一个client/server服务，是Linux/Unix系统下的一个**进程管理工具**。可以很方便的监听、启动、停止、重启一个或多个进程。用supervisor管理的进程，当一个进程意外被杀死，supervisor监听到进程死后，会自动将它重启，很方便的做到进程自动恢复的功能，不再需要自己写shell脚本来控制。

supervisor4.0版本以上可以在python3上顺利运行（3.6上测试成功）

环境搭建非常简单，难的是配置文件

## 2. 安装

Ubuntu系统下直接： sudo pip install supervisor即可

特别注意：此处实际使用时有一个麻烦，普通用户下安装的supervisor，在root账户下是没有安装的，还要重新回到root账户下再安装一遍 pip install supervisor

## 3. 配置

首先要生成一个标准的配置文件

`echo_supervisord_conf > supervisord.conf`

然后根据官网说明对参数进行详细配置，参考**配置详解章节**，此处暂略

## 4. 启动与运行

supervisor有两个命令：supervisord和supervisorctl

supervisor的使用逻辑是，首先通过supervisord开启supervisor服务。然后用户通过supervisorctl在运行中实时调整和管理已运行的服务。

### 4.1 启动supervisor服务

`supervisord -c path_of_supervisord.conf`

特别备注：如果你需要启动的子程序享有root权限的话，请通过 sudo来启动supervisord

-c代表连接到指定配置文件，其他参数解释请参考[官网链接](http://supervisord.org/running.html)。

### 4.2 运行时的控制

基本上通过supervisorctl来实现运行时控制

方法一：

cmd line直接输入supervisorctl，不需要参数。进入supervisor客户端

然后直接 start/stop/restart task_name就可以实现应用程序的控制了

status查看运行状态

方法二：

通过bash终端命令行实现控制

```
supervisorctl status #查看状态
supervisorctl stop task_name
supervisorctl start task_name
supervisorctl restart task_name
supervisorctl reload #载入最新配置文件并重启服务
supervisorctl update #常用，修改conf文件后刷新配置
```

方法三：

如果你在配置文件中配置了[inet_http_server]字段，那么supervisord服务启动后你可以在本地浏览器中实现控制，地址是 local_ip:9001

特别注意：supervisorctl的配置文件必须和supervisord保持一致，权限也要相同

## 5. 配置详解

详细配置请参考[官网说明](http://supervisord.org/configuration.html) ，此处仅列举最小系统下的配置说明。

### 5.1 配置文件获取策略

推荐使用 -c 手动指定配置文件，省去默认顺序的烦恼

如果没有手动指定配置文件地址，默认根据[先后顺序](http://supervisord.org/configuration.html)依次查找。

### 5.2 格式

ini类型，每个段由[header]开头，段内以 key = value 形式保存配置信息

### 5.3 环境变量

统一格式为  `%(ENV_variable)s`， 代表使用variable系统变量   

例如：command=/usr/bin/example --loglevel=%(ENV_LOGLEVEL)s
代表loglevel使用linux系统自带的LOGLEVEL参数

使用环境变量的好处在于，让supervisor的配置和Linux系统挂钩，具备自适应性。

### 5.4 重要字段解释

把重要字段改了就能先用起来，其他字段参考官方文档慢慢摸索

**[inet_http_server]**

如果使能该字段，则可以在浏览器中实现supervisor的管理和控制

```
[inet_http_server]         
port=0.0.0.0:9001        
username=user              
password=123               
```

**[supervisor]**

supervisor的核心配置，可以直接按照默认值使用不用改

```
[supervisord]
logfile=/tmp/supervisord.log 
logfile_maxbytes=50MB        
logfile_backups=10           
loglevel=info                
pidfile=/tmp/supervisord.pid 
nodaemon=false               
minfds=1024                  
minprocs=200                 
```

**[supervisorctl]**

如果使能了inet_http_server字段，则该段配置必须和上述保证一致

```
[supervisorctl]
serverurl=http://127.0.0.1:9001
username=user              
password=123                
prompt=mysupervisor         
```

**[program:x]; 非常重要**

推荐单独兴建一个 module.ini文件，把program配置写进去，然后通过supervisord.conf文件的include字段统一包含。示例如下

```
; ui.ini文件
[program:ui]  ;定义了一个ui任务
command=./SkyUI debug  #实际执行的动作
autorestart=true #异常崩溃后自动重启
```

**[include] ;非常重要**

基本作用是链接其他配置文件。如果program字段太长，则可以将每个program单独写成一个文件，然后通过include统一包含，便于管理

```
[include]
files = /home/sky/supervisor_test/*.ini
```

然后可以包含各种ini配置文件了



重新配置好以后试试 supervisorctl update刷新一下配置文件，看看任务是否已经启动，且无法手动kill掉

## FAQ

报错： Unlinking stale socket /tmp/supervisor.sock

解决：sudo unlink /tmp/supervisor.sock

解决无法root启动子进程的几种方式：

1. sudo supervisord
2. 把密码当作参数启动： echo passwd | sudo -S command
3. 改变应用程序的权限：sudo chmod +s app
4. 发现居然是由于没有在root账户下安装supervisor导致root权限下根本就没有supervisord这个命令，于是切换到root账户，重新安装一遍supervisor，成功解决



## 参考链接

[supervisor官网](http://supervisord.org/index.html)

[使用 supervisor 管理进程](https://zju.date/supervisor-notes/)

[Python 进程管理工具 Supervisor 使用教程](https://www.cnblogs.com/restran/p/4854623.html)

[Supervisor简介、安装、配置](http://wangshengzhuang.com/2017/05/26/%E8%BF%90%E7%BB%B4%E7%9B%B8%E5%85%B3/Supervisor/Supervisor%E7%AE%80%E4%BB%8B/)


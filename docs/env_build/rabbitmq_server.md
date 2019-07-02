# Ubuntu16.04搭建RabbitMQ服务

作者：尹超

日期：2018-10-20

## 1. 大致思路

- 先安装erlang
- 再安装rabbitmq
- 再配置
- 最后开启服务，测试连通性

## 2. 详细步骤

### 2.1 安装erlang和rabbitmq

```
sudo apt-get update
sudo apt-get install erlang-nox     sudo apt-get update
sudo apt-get install rabbitmq-server
```

检查安装情况： `ps -ef|grep rabbit `

### 2.2 进入安装文件夹检查安装状态

```
cd /usr/lib/rabbitmq/bin
sudo ./rabbitmqctl status
```

此时如果发现有错误：TCP connection succeeded but Erlang dizstribution failed，请解决cookie不一致的问题，此时需要先关闭服务，然后修改配置文件，再开启服务（此时无法连接控制台）

具体解决步骤如下：

`/usr/lib/rabbitmq/bin$ invoke-rc.d rabbitmq-server stop`

2.2 进入安装文件夹/usr/lib/rabbitmq/bin,修改rabbitmqctl文件，查找位置并添加一行语句

```
RABBITMQ_USE_LONGNAME=${RABBITMQ_USE_LONGNAME} \
HOME=/var/lib/rabbitmq  \   <-----添加这一行语句
exec ${ERL_DIR}erl \
```

### 2.3 启动rabbitmq的服务

`sudo rabbitmq-server start `（成功启动6个插件后需要自己ctrl+c退出）

此处如果无法启动插件也没关系，尝试以下方法去开启服务（如果失败则继续往下做）

`rabbitmq-plugins enable rabbitmq_management `

### 2.4 启动web管理台

此时可以打开浏览器，通过localhost:15672查看本地控制台（如果不行再输入下面的命令）

`sudo ./rabbitmq-plugins enable rabbitmq_management `

### 2.5 开启远程web控制台

创建一个新的管理员账号（默认的guest只能监听localhost）

```
sudo rabbitmqctl  add_user yinchao 123456
sudo rabbitmqctl  set_user_tags yinchao administrator
sudo rabbitmqctl set_permissions -p "/" yinchao ".*" ".*" ".*"
```

查看与删除用户（把系统默认的那个guest删了去）

```
sudo rabbitmqctl  list_users
sudo rabbitmqctl delete_user username
（修改密码语法：rabbitmqctl  oldPassword  Username  newPassword）
```

打开网址并登录控制台： 127.0.0.1:15672    账号：yinchao       密码：123456 

此时如果无法登录，则重启一下

### 2.6 config文件配置

把rabbitmq.config拷贝到/etc/rabbitmq/目录下, 重启电脑即可

配置好后测试端口是否已经监听，查看是否可以通过ip:15672的方式在浏览器中远程打开控制台

再看看控制台的overview界面上，config file是否已经被使用了

## 3. 命令备忘

检查配置状态并开启server服务

```
sudo systemctl start rabbitmq-server.service
sudo systemctl enable rabbitmq-server.service
cd /usr/lib/rabbitmq/bin/
sudo ./rabbitmqctl status
```

//常用服务命令
查看rabbitmq-server有没有安装好，能查到说明已经安装成功了

`rpm -qa|grep rabbitmq`

开启server命令

```
sudo service rabbitmq-server start
sudo service rabbitmq-server restart
```

关闭服务

`sudo service rabbitmq-server stop`

开启服务器维护插件（6个）

`rabbitmq-plugins enable rabbitmq_management `

服务启动和停止命令

```
启动：sudo rabbitmq-server start
关闭： sudo rabbitmq-server stop
重启： sudo rabbitmq-server restart
查看状态：sudo rabbitmqctl status
```



## 4. 安装勘误

出现了[Sub-process /usr/bin/dpkg returned an error code错误](https://www.cnblogs.com/blfbuaa/p/7304921.html)

```
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info.bak
sudo mkdir /var/lib/dpkg/info
sudo apt-get update
sudo apt-get -f install rabbitmq-server
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info.bak
sudo rm -rf /var/lib/dpkg/info
sudo mv /var/lib/dpkg/info.bak /var/lib/dpkg/info
```

## 5. 参考链接

[RMQ官网](https://www.vultr.com/docs/how-to-install-rabbitmq-on-ubuntu-16-04-47)

[CSDN教程](https://blog.csdn.net/hui1788/article/details/79946619)


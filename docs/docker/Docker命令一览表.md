# Docker命令一览表

作者：尹超

日期：2020-1-7

完整命令解析请参见[命令大全链接地址](https://www.runoob.com/docker/docker-command-manual.html)，下文仅为常用命令的简化操作

## 容器操作

### run/create

run创建一个新的容器并运行一个命令，create创建新容器但不启动它

#### 语法

 `docker run [OPTIONS] IMAGE [COMMAND][ARG...]`

#### OPTIONS说明

- -d 后台运行，返回容器ID
- -i -t 交互模式运行
- --name="your_name"  为容器指定一个名称
- -p 指定端口映射，格式为： `主机端口:容器端口`

#### 举例

```
docker run --name test -d nginx:latest #运行一个nginx最新镜像并命名为test
docker run -p localhost:80:8080/tcp ubuntu bash #绑定容器的8080端口并将其映射到主机的80端口上
docker run -it nginx:latest /bin/bash #以交互模式启动容器并在容器内执行/bin/bash命令
```

### start/stop/restart/kill/rm

启动/停止/重启/中止/删除一个容器

#### 语法

`docker start/stop/restart [OPTIONS] CONTAINER [CONTAINER...]`

#### 举例

```
docker start my_container #开启my_container容器
docker stop $(docker ps -a -q) #停止所有容器
```

### ps

列出容器状态

#### 语法

`docker ps [OPTIONS]`

#### OPTIONS说明

-a 列出所有的，包括未运行的

-f 

-s 显示总文件大小

-n 列出最近创建的n个容器





## 镜像操作

### 查询镜像

docker search images， 查询网络镜像源

docker images ，查询本地镜像列表 

### 拉取镜像

docker pull ubuntu

docker pull ubuntu:16.04

终止方式是 ctrl+c

### 删除本地镜像

```
则先看看是否有关联容器存在，先删除了docker容器，才能删除镜像
docker ps -a
docker rm 容器id

docker images #查看本地镜像，找到image_id = 117843ade696
docker rmi 117843ade696 #删除镜像
```

## 容器操作

### 查看容器状态

docker ps -a

### 启动/停止容器

docker start/stop 容器id

### 停止/删除所有容器

docker stop/rm $(docker ps -a -q)
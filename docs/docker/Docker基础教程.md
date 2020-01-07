# docker简明教程

作者：尹超

日期：2020-1-7

## 1. 基本简介

Docker 是一个开源的应用容器引擎，基于 [Go 语言](https://www.runoob.com/go/go-tutorial.html) 并遵从 Apache2.0 协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

### 1.1 主要应用

- Web 应用的自动化打包和发布。
- 自动化测试和持续集成、发布。
- 在服务型环境中部署和调整数据库或其他的后台应用。

### 1.2 Docker的优点

一致性交付，保证相关依赖的完整性和独立性

响应式部署和扩展

同一硬件上可运行更多的工作负载（高性能虚拟机）

### 1.3 Docker架构

镜像，类似于root文件系统

容器，存放和运行镜像的载体，可以被创建，启动，停止，删除，暂停

仓库，代码控制中心，用来保存多个镜像

![img](https://www.runoob.com/wp-content/uploads/2016/04/576507-docker1.png)

## 2. Docker安装

### 2.1 win10安装

非常简单，有DockerDesktop，直接安装即可，[传送门](https://www.docker.com/get-started)

注意两点：

其一，开启Hyper-V功能【控制面板-启动或关闭windows功能-Hyper-V全部开启】

其二，开启镜像加速功能【安装完成后点击settings-Daemon-点动basic变成advanced选项，在registry-mirrors一栏中填入：https://registry.docker-cn.com就可以了，保证json的完整性】

### ubuntu安装

先卸载旧的版本： ` sudo apt-get remove docker docker-engine docker.io containerd runc`

使用shell脚本安装即可

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## 3. Docker使用

### 3.1 hello world

```
docker pull ubuntu:16.04
docker run ubuntu:16.04 /bin/echo "Hello world
```

### 3.2 运行交互式容器

run的时候带上两个参数即可

- -t 在容器内指定一个终端
- -i 允许你对容器进行STDIN交互

例如：`docker run -i -t ubuntu16.04 /bin/bash`

退出方法：

exit命令，或者CTRL+D

### 3.3 启动容器

`docker run -d ubuntu:16.04 /bin/sh -c "while true; do echo hello; sleep 1; done"`

以进行方式在后台启动一个容器

`docker ps`可以查看到容器ID和运行状态

`docker logs [容器ID]`可查看后台运行的标准输出

### 3.4 停止容器

`docker stop [容器ID或容器名]`

## 参考链接

[docker系列教程](https://www.runoob.com/docker/docker-tutorial.html)

[Docker 官网](https://www.docker.com)

[Github Docker 源码](https://github.com/docker/docker-ce)
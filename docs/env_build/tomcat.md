# Ubuntu搭建Tomcat服务

作者：尹超
日期：2019-6-22
描述：本文描述如何在阿里云主机（Ubuntu16.04）搭建Tomcat服务

## 大致思路：

1. 配置java环境
2. 配置tomcat环境
3. tomcat的使用测试

## 详细步骤：

### 1. 先配置java服务

[参考链接](https://blog.csdn.net/mucaoyx/article/details/82949450)

1. 先下载jdk压缩包

2. 解压到/usr/lib/目录下 (/usr/lib/java/jdk1.8.0_212/jre/bin)

3. 配置环境变量，使得java和特定的bin挂钩 

   `sudo vim /etc/profile`

   添加如下内容

   ```
   export JAVA_HOME=/usr/lib/java/jdk1.8.0_212
   export PATH=${JAVA_HOME}/bin:${PATH}
   ```

   配置完了以后source一下即可  `source /etc/profile`

### 2. 再[配置Tomcat服务](https://blog.csdn.net/oyy_90/article/details/80335932)：

2.1 [源码包下载](https://tomcat.apache.org/download-90.cgi): 选择：core, tar.gz

2.2 解压与配置

```
cd /opt/
mdkir tomcat
```

2.3 最终解压出来的根目录
`/opt/tomcat/apache-tomcat-9.0.21`

### 3. 修改配置文件

#### 3.1 修改profile    

`sudo vim /etc/profile`

添加如下信息

```
export CATALINA_HOME=/opt/tomcat/apache-tomcat-9.0.21
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:${CATALINA_HOME}/lib
export PATH=${CATALINA_HOME}/bin:$PATH
```

#### 3.2 修改tomcat的配置  

`sudo vim TOMCAT_PATH/bin/startup.sh`

添加如下信息

```
JAVA_HOME=你的JAVA路径
JRE_HOME=${JAVA_HOME}/jre
PATH=${JAVA_HOME}/bin:${JRE_HOME}:$PATH
CLASSPATH=.:${JRE_HOME}/lib/rt.jar:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar
TOMCAT_HOME=/opt/tomcat/apache-tomcat-9.0.21
```



#### 3.3 修改tomcat配置 

`sudo vim TOMCAT_PATH/bin/catalina.sh`

添加如下两行

```
export JAVA_HOME=/usr/lib/java/jdk1.8.0_212/
export JRE_HOME=${JAVA_HOME}/jre
```

## 测试可用性

最终测试：cd /opt/tomcat/apache-tomcat-9.0.21/bin

开启服务： sudo ./startup.sh

关闭服务： sudo ./shutdown.sh
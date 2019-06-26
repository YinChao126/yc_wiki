# 搭建属于自己的维基百科

作者：尹超

日期：2019-6-25

## 1. 背景

​	随着工作经验的逐步积累，涉及的知识面越来越多，有许多零散的知识散落在各地。这时候将知识分门别类，会惊奇地发现他们正慢慢形成一个知识体系。

​	另一方面，做过的工程总会留下许多宝贵的经验，然而如不加以整理，最终又会丢失，我们经常会碰到似曾相识的困难，又苦于找不到当时的解决步骤。

​	显然，我亟需整理出一套属于自己的知识体系。这个知识体系既可以让我**在任何地方以同样的方式来访问**，又可以让我有自主权**选择性地将部分内容分享**出来。同时，知识的搭建**放在本地**，不在别人的手中（比如CSDN）。终极解决方案就是搭建一个属于自己的wiki，然后让它挂在自己的服务器上以供访问。

## 2. 核心思想

​	首先选择一个开源的wiki系统（本人选择的是mkdocs），通过mkdocs可以将markdown文档生成带图片的网页，由于网页是静态的，这意味着它几乎可以部署在任何地方（本人选择部署在阿里云上，通过tomcat就可以将网页显示出来）。如果想更高级一点，可以自己申请一个域名，然后进行域名解析，再架设一个Nginx服务器对域名和端口号进行反向代理，最终你就可以在世界各地愉快地打开浏览器输入 https://your_web_site来进行访问了。

## 3. 具体步骤

首先需要搭建本地mkdocs服务，生成静态html，从而在本地开启wiki服务

然后将wiki文件夹进行GitHub托管，便于日后修改，部署与统一管理

最后把网页托管到阿里云上用tomcat部署，如此就可以通过网络远程访问wiki了

### 3.1 搭建本地wiki服务

安装： pip install mkdocs

检查是否安装成功：mkdocs --version

新建自己的wiki站点：mkdocs new yc_wiki

启动wiki服务：mkdocs serve

检查本地wiki站点是否成功启动，浏览器中输入：<http://127.0.0.1:8000/> 

至此，本地wiki服务已经搭建成功了！

### 3.2 将wiki托管到Github

​	你可以直接将wiki托管到GitHub上，也可以基于安全考虑，自己搭建一个私有的git仓库，然后进行托管（本人就是托管在自己的私有云的git仓库里），详细实现方法参见链接：

### 3.3 将wiki站点生成的html用tomcat部署到网上



## mkdocs.yml配置详解

mkdocs.yml决定了wiki的主题，名称，页面组织结构，是重要的配置文件

最重要的文件组织结构如下：

```python
#假设你的文件存储结构如下：
docs/
	index.md
	introduce.md
	dir1/
			f1.md
			f2.md
			dir2/
				sf3.md
				sf4.md
-------------------------------------------------------
nav:
	- title_1: index.md  #方法1
	- title_2:[index.md,introduce.md,dir1/f1.md] #方法2
	- title_1:
		- sub_title1:[index.md, dir1/f1.md] #方法3 
		- sub_title1:
			- sub_title2:[dir1/dir2/sf3.md, index.md] #方法4
```



## 参考链接
[MkDocs中文文档](https://markdown-docs-zh.readthedocs.io/zh_CN/latest/#_12)

[GitHub搭建自己的wiki知识管理系统](https://blog.csdn.net/jiasike/article/details/88930624)

[dokuwiki搭建自己的wiki](https://blog.csdn.net/caowei880123/article/details/60465518)

[mkdocs配置详解](<https://www.mkdocs.org/user-guide/configuration/#docs_dir>)


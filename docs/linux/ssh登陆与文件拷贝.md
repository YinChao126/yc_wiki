# SSH登陆远程主机并实现文件拷贝

作者：尹超

日期：2019-10-10

## linux实现SSH远程登陆

`ssh user@ip`

为了避免每次登陆都输入密码，可以将本地的公钥加到远程主机的**authorized_keys**文件中，详情参考[《阿里云搭建git私有仓库》](../env_build/阿里云搭建git私有仓库.md)免密认证章节。

## 文件拷贝

本地拷贝到远程

`scp local_file user@ip:path`

远程拷贝到本地

`scp user@ip:path/file local_path`

备注：

如果复制目录，则scp带参数 -r

必须将SSH加入信任列表里才可以完成拷贝动作

## 参考资料

[Linux下远程登录阿里云服务器](https://blog.csdn.net/shanghairuoxiao/article/details/78553513)

[SSH连接下复制远程linux服务器文件到本地的命令](https://www.cnblogs.com/zhuangliu/p/7610530.html)


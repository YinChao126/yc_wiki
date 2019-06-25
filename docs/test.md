![mkdocs](imags/test.jpg)

# 需求

要将项目托管便于管理，但是又不想用GitHub这种开源软件。所以打算将git服务托管到阿里云上（显然也可以部署到自己的服务器上）。

# 术语定义
服务器端 - 阿里云
客户端 - 本地用户环境（windows/Linux）

# 大致思路
  1. 确保服务端和客户端都有git服务
  2. 配置认证权限，避免之后频繁输入密码（可选）
  3. 服务器端兴建裸仓库用于项目托管
  4. 本地clone该仓库，进行远程pull/push操作，验证可用性

# 具体步骤
## 1. 服务器端git服务确认
先 git --version，看git服务是否已经安装，如果有版本信息，则跳过此步骤，如果没有：

    sudo apt update
    sudo apt upgrade
    sudo apt install git

为了统一管理，请创建一个git用户专门管理git服务
sudo adduser git
成功之后系统会自动建立一个/home/git文件夹

如果没有设置git的用户信息，请记得设置
查询：
git config user.name
git config user.email
新建/修改：
git config user.name
git config user.email

## 2. 免密认证配置
2.1. 服务器端先在git下建立.ssh文件夹和authorized_keys文件

    git@Linux:~$ mkdir .ssh
    git@Linux:~$ touch .ssh/authorized_keys
    git@Linux:~$ chmod 600 .ssh/authorized_keys 

2.2 然后在客户端上生成RSA公私钥对（公钥交给服务端保存，密钥自己保存）
Windows环境：win+r打开命令行：cd去~/.ssh目录(即：C:\Users\用户名\.ssh)
Linux环境直接敲命令即可（成功后内容保存在~/.ssh）：

    ssh-keygen -t rsa -C “youremail@example.com”

生成两个文件，其中.pub是公钥，需要将其交给服务器保存。另一个是私钥，自己保管。

2.3 服务器端公钥并打开RSA认证
将客户端生成的id_rsa.pub的内容添加到服务器端：.ssh/authorized_keys文件的末尾

// 在服务器端找到sshd_config文件下面3行并去掉注释
vim /etc/ssh/sshd_config
​    
​    RSAAuthentication yes     
​    PubkeyAuthentication yes     
​    AuthorizedKeysFile  /home/git/.ssh/authorized_keys <-注意修改路径

2.4 服务器端新建裸仓库用于托管

    cd /home/git
    mkdir test.git
    cd test.git
    git init --bare
    cd /home/git
    chown -R git test.git #修改仓库所属用户为git

2.5 用户在客户端正常使用
2.5.1 Windows环境
克隆：
git clone git@xx.xx.xx.xx:/home/git/test.git 
上传：
git push origin master
下载：
git pull origin master

2.5.2 Linux环境
和Windows类似，先 ls -al ~/.ssh查看一下是否已经有SSH key，如果有则将公钥添加到服务器端的authorized_keys列表的末尾（另起一行即可）。如果没有，则按上文所述去生成

然后克隆工程：
git clone git@xx.xx.xx.xx:/home/git/test.git 
此时可能会报错，
Host key verification failed.
此问题是SSH访问权限配置的问题，解决方案如下：
sudo vim /etc/ssh/ssh_config
把文档里的StrictHostKeyChecking ack改为StrictHostKeyChecking no，保存退出即可。
重复上述克隆操作，大功告成！（为了安全起见，又可以把no参数改回ack，此时该项目已经添加到信任列表里了）

# 后记
其实更简单的方法是搭建Gitlab服务，不过我自己的云服务器配置太低，一开启Gitlab服务就卡得要死，不得已才用此方法，效果也还蛮不错。

# 参考链接
https://blog.csdn.net/u011050582/article/details/78768408
https://www.cnblogs.com/yominhi/p/9759246.html
关于SSH key的生成
https://blog.csdn.net/jiayoudangdang/article/details/79477860
关于Linux环境下SSH连接失败的解决方法
https://blog.csdn.net/u010070526/article/details/80920643

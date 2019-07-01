# GitHub常用命令

## 仓库初始化

```
git init  //初始化当前文件夹为一个新的git仓库
git status  //查看状态

ssh-keygen.ext -t rsa -C "yc86247931@126.com" //生成SSH key（保存在C:\Users\用户名\.ssh）
git remote add origin git@github.com:YinChao126/Test.git  //本地仓库关联到远程仓库，并为远程仓库取别名为：origin
```

## 用户配置

1. 用户名和邮箱地址相当于你的身份标识，是本地Git客户端的一个变量，不会随着Git库而改变。
2. 每次commit都会用用户名和邮箱纪录。
3. github的contributions跟你的邮箱是有关联的。

查看用户信息

```
$ git config user.name
$ git config user.email
```

新建/修改用户

```
$ git config --global user.name "xxx"
$ git config --global user.email "xxx"
```

## 提交

```
git add .
git commit -m "comment"
git push origin master #提交到远程分支
```

## 别名设置

```
git config --global alias.st status //用st代替命令status
```

## 别名取消

```
vim .gitconfig
把对应的那一行删除即可
```

## 参考链接

[git命令大全](https://www.yiibai.com/git/git_clone.html)
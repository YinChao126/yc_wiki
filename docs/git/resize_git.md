# .git瘦身

作者：尹超

日期：2019-12-18

## 背景

用git托管久了，提交次数增多，.git文件会越来越大。尤其是一不小心托管了大文件，后来又删除，但由于托管记录存在，.git会尤其大。直接后果是你在其他地方clone会非常痛苦。

## 1. 最简单的方法

直接去.git/objects文件夹中找出对应的大文件并手动删除即可！

副作用是，你永远失去该资源的记录。无法通过退回到当前版本来复原【会显示该资源丢失】，所以如果你确信该资源是一定要删除的，可以放心大胆删掉。

使用前提：只能是历史记录中的某一条，如果是当前提交的资源，可能找不到head

## 2. 实测有效的办法

[原文参考链接](https://my.oschina.net/janl/blog/3089963)

前提：.git/objects/pack中有记录【如果没有，请执行如下两句】

```
git reflog expire --all --expire=now
git gc --prune=now --aggressive
```

按照如下顺序依次敲命令即可

```
1. 根据pack名称，查找大文件的文件名
git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 
#根据前10个记录进一步查看到底是什么文件名
git rev-list --objects --all | grep e28b267b24de7d5b32ed2391669   #假设得到的文件名是 your_file

2. 从仓库中删除与test.zip有关的所有记录
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch 【your_file】' --prune-empty --tag-name-filter cat -- --all

3. 回收仓库空间
git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now
git count-objects -v

4. 推送到远端
git push origin --force --all
```

## 3. 其他解决方案（未验证）

[参考StackOverflow](https://stackoverflow.com/questions/2116778/reduce-git-repository-size)

```
git reflog expire --all --expire=now
git gc --prune=now --aggressive
```

给出的[激进解决方案](https://stackoverflow.com/questions/3797907/how-to-remove-unused-objects-from-a-git-repository/14729486#14729486)，**危险慎用！！！**

[另一个解决方案](https://stackoverflow.com/questions/1904860/how-to-remove-unreferenced-blobs-from-my-git-repo)


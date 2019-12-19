# 删除提交记录

作者：尹超

日期：2019-12-19

## 当前提交需要复位

### 如果改动还未保存

 `git checkout [your_file]`

### 改动已保存，但未提交 

```
git reset HEAD  #取消add状态
git checkout [your_file] #撤销改动
```

### 已经add，已经提交，想删除最近的一个提交

```
git reset --hard head^  //回退到head的前一个版本
```

## 删除历史中的某一个提交

假设有1，2，3，4个提交，如何删除提交2又不影响其他内容？

### 方法1：

先查看log历史，找到commit记录，尤其是待删除的前一次commit hash值

然后修改日志，把日志中涉及此次提交的pick改为drop（第一行）

```
git log  #假设要删除commit2， 则记下commit1的id(假设为hash_1)
git rebase -i hash_1 #手动将pick改为drop
git log #查看，commit2应该已经被删除
git push origin HEAD -force #推送到远程仓库【可选】
```

### 方法2

直接一条命令搞定

```
git revert 0e2afdf78cea6953cb554713160e8b9d2f5e3f85
```

备注：上述两种方法有缺陷，提交历史在.git文件夹中留下了痕迹，未能得到清理（尤其是曾经有大文件提交的时候你会发现即便git删除了之后.git文件夹还是很大)



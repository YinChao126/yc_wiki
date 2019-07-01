# 分支与合并(branch)

## 1. 创建新分支

```
git branch new_br #创建新分支
git checkout -b new_br #创建新分支并切换过去
```

## 2. 切换分支

```
git checkout new_br
```

## 3. 查看分支

```
git branch  #查看本地分支
git branch -r #查看远程分支
git branch -a #列出所有分支
```

## 4. 删除分支

```
git branch -D br  #删除本地分支
git push origin :br #删除远程分支（origin后有空格）
```

## 5.合并

分支合并有两种方式:

merge：保留历史提交记录，完整合并

rebase：把老旧的分支直接删除，看起来就像没有被合并过一样

### 5.1 无冲突直接合并

假设新开发的版本是feature，已经验证成功，需要让develop合并新分支

```
develop ->
        |->feature -> step1 -> step2 -> ... -> feature
```


1. 确保feature是clean状态
  git status //看清楚了

2. 切换到develop分支
  git checkout develop

3. 执行合并 // 建议merge时总是使用 --no-ff选项
  git merge --no--ff feature

```
develop ->----------------------------------------------> develop
	 |->feature -> step1 -> step2 -> ... -> feature-----^
```

### 5.2 有冲突合并

有冲突的合并一般出现在并行开发的过程中
情景描述：
开发者1和开发者2同时从服务器拉取了origin版本进行协同开发，开发过程中1首先修改了代码并同步
到了origin，同时开发者2也修改了本地代码，但是肯定会与origin有冲突，此时的合并会出现问题

```
origin-|---------------------->origin

		|->user1->step1->step2-^

		|->user2->step3->step4-....->stepn
```

问题化简到user2分支与origin分支的合并，但是两个分支有冲突

1.切换到user2的分支，确保操作前一定是clean的
git checkout user2
git status

2.利用rebase进行精简式的合并（无用的老旧分支都会被删除），也可以利用merge合并
git rebase origin //此处会出现冲突

3.利用kdiff3软件进行手动冲突解除操作，并保存文件

4.得到了无冲突的文件后继续操作，直至合并成功
git -add //更新内容
git rebase --continue

最终的结果是user2获取了origin的最新内容，同时分支仍然处于user2上面

任何情况下，如果觉得不想继续合并，直接
git rebase --abort 即可
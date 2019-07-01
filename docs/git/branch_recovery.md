# 恢复误删的分支

如果不小心把分支删除了，后面又反悔了，如何恢复？

## 恢复步骤

### 1. 看log，找出被删除前的最新提交id号

git log -g

### 2. 建立一个用于恢复的新分支

git branch recover_br commit_id

### 3. 切换到新分支下，误删的分支在新分支下得以恢复

git checkout recover_br
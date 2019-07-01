# 清除状态

## 清除未保存到缓存区的文件

git checkout . #清除所有未提交状态

git checkout file #清除指定未提交文件

## 清除已保存但未提交的文件

git stash

git stash drop

## 清除被.gitignore忽视的所有文件（慎用！）

git clean -fdx

## 一键清除当前所有未被托管的内容（慎用！）

git checkout . && git clean -xdf


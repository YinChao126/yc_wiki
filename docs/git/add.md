# add与commit

## 常用add命令

```
git add .     //将所有文件添加
git add --all //将所有文件/文件夹/文件夹里面的文件一并添加
```

## 提交

```
git commit -m "comment"
```

## add出问题

情形1：**总是无法add成功**

原因：add了一个本身自带了.git的文件夹（比如拷贝了别人的经过git托管的工程）

[解决方案](https://blog.csdn.net/m0_37315653/article/details/83064810)：

输入以下两条命令即可

```
git rm --cached 未跟踪的文件夹
git add 未跟踪的文件夹
```

但是执行`git rm --cached directory`时，提示
fatal: Unable to create 'xx/.git/index.lock': File exists.

如果出现此问题：执行`rm -f xx/.git/index.lock`后解决

情形2：明明有未提交的文件，但是git status不显示

描述：试图在仓库中增加另外一个托管工程，发现git status根本就不会发现新增文件的情况，想起来没有删除.git文件。但是奇怪的是删除以后仍然不发现。但是改变文件名就可以发现了。

原因：**莫名其妙被ignore了**

[解决方案](https://blog.csdn.net/xiaotuni/article/details/77885140)：
git status --ignored

可以发现SkyTx和SkyConsole莫名其妙被当做忽略文件夹了
修改.gitignore就可以解决问题
ps:这是个低级错误，原因在于SkyConsole工程和生成的exe（SkyConsole）同名了
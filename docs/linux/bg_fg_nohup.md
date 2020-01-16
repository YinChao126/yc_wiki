# Linux任务后台执行命令详解

作者：尹超

日期：2019-12-13

## keywords

nohup, fg, bg, task

## 需求描述

很多时候我们需要Linux系统下的任务在后台执行，或者来回切换，或者在自己登出之后仍然能够执行

## 解决方案

### &

linux下我们如果想一个任务或者程序还后台执行可以使用&

### nohup

不挂断地运行命令（云端常用）

语法为： `nohup command [arg] [&]`

一个实际的例子： `nohup command > mylog.txt 2>&1`

让command命令不挂断运行，输出存入mylog.txt中

### jobs

查看当前有多少在后台运行的程序

### ctrl+z

将一个正在前台执行的命令放到后台，并暂停执行

### bg

将一个在后台暂停的命令变成后台继续执行

### fg

将后台中的命令调至前台继续执行

# Notepad++配置编译与运行环境

作者：尹超

日期：2018-10-18

## 背景

有时候需要快速开发小的程序，不想使用vs2013或者spyder这种重型IDE，类似于纯文档开发的时候不需要word一样，考虑使用notpad++来做这个工作。

## 环境配置

### 1. 下载notpad++](https://notepad-plus-plus.org/download/v7.5.9.html)

### 2. [下载MinGW](https://osdn.net/projects/mingw/releases/)

### 3. 默认安装MinGW，然后为其配置系统变量

path中添加： `;C:\MinGW\bin;C:\MinGW\include;C:\MinGW\lib`

### 4. notpad++中编辑测试代码并运行

4.1 兴建hello.cpp

```
#include <stdio.h>
int main()
{
printf("hello,world\n");
return 0;
}
```

4.2 按F5，弹出编译选项

编译命令：

`cmd /k gcc -Wall -o "$(CURRENT_DIRECTORY)\$(NAME_PART).exe" "$(FULL_CURRENT_PATH)" & PAUSE & EXIT`

运行命令：

`cmd /k "$(CURRENT_DIRECTORY)\$(NAME_PART).exe" & PAUSE & EXIT`

自行设置响应的快捷键即可

[参考链接](https://blog.csdn.net/u012685794/article/details/41519037)
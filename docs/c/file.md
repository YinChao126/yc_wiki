# 关于文件读写的问题

## keywords

c, file, filename

## 文件读写操作

[文件读写实现参考链接](http://www.360doc.com/content/13/0401/09/11764545_275223195.shtml#)

## 生成大量文件名

```C
#include<stdio.h>
int main()
{
    int m = 0;
    char filename[30];
    for (m=1; m<101; m++)
	{
        sprintf(filename,"%d.txt",m);
        //printf("%s\n",filename);
        if (fopen(filename, "at+") == NULL)
		{
            printf("can't open the disk");
            return 1;
        }
    }
    return 0;
}

```

## r和rb的区别

时间：2017-2-21

背景：以前在BF607工程的simulator模式下仿真，能够正确读取文件。现在需要开发基于21489的程序，发现原来的读取方式不行。读不到任何数据。

经检查：fscanf(…”rb”)和fscanf(…”r”)有区别。

查找资料：得到一条经验

文件文件(以文本方式写的)，最好以文本方式读。二进制文件(以二进制方式写的)，最好以二进制方式读。不然可能会不正确。

以后还是不要随便加b这个参数了

## 获得一行数据里感兴趣的内容并存为文档

时间：2017-5-5

背景：获得的原始数据格式不对，需要截取后面的数组，以便于MATLAB绘图处理

格式是： point:123 cycles: 21343

我只需要21343

 思路：

1. 使用 fgets获取一行字符串
2. 使用sscanf把获取的字符串按照自己的格式保存到两个数组中
3. 使用指针把cycle:21343的：之前的数据屏蔽

 

代码：

```c
FILE *DataIn, *DataOut;
char *pStr;
char Buff[128];
char Part1[64];
char Part2[64];
int Bios = 6; // “cycle:”刚好是6个字符，屏蔽之

…打开文件省略

while(!feof(DataIn))

{
	fgets(Buff, sizof(Buff), DataIn);
	sscanf(Buff, “%s %s”, Part1, Part2);
	int len = strlen(Part2);
	pStr = Part2 + Bios;
	fprintf(DataOut, “%s\n”,pStr);
}

…关闭文件省略
```


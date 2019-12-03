# C语言下查找文件名

作者：尹超

日期：2018-5-29

## keywords

c, search, filename, file

## 描述

本模块用来实现特定文件夹下的文件名搜索

高级用法：和pcre模块配合可以实现模糊查找功能。

## test_app.c

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "FileHandle.h"

int main()
{
	int file_num = 0; //检测该文件夹下有多少个文件
	char *pattern = ".\\out\\*.txt"; //查找./out文件夹下所有txt格式的文件，此处可以用通配符
	char file_result[5][MAX_FILE_NAME_LEN];  //查找结果：以列表显示，第一个字节代表该文件名的长度
	char (*p)[MAX_FILE_NAME_LEN] = file_result;


	SearchDir(pattern, p, &file_num);
	int i;
	for (i = 0; i < file_num; i++)
	{
		char name[50] = ".\\out\\";
		strcat(name, file_result[i]); //获取完整文件名
		remove(name); //删除./out/目录下所有txt文件
	}

	return 0; 
}
```

## FileHandle.h

```
/************************************************************************/
/* 模块名：FileHandle
** 作者：尹超
** 描述：该模块用以实现C环境下的文件应用级操作（搜索、查找文件名等）
** 更新时间：2018-5-29
** 已实现功能一览表：
** SearchDir->搜索特定文件夹，返回该文件夹下符合规则的文件名			*/
/************************************************************************/
#ifndef FILE_HANDLE_H
#define FILE_HANDLE_H

#define MAX_FILE_NAME_LEN 20 //容忍的最长文件名

/************************************************************************/
/* 原型：void SearchDir(const char* path, char(*file_name)[MAX_FILE_NAME_LEN], int *len)
** 版本：V1.0
** 描述：给定输入条件，返回该条件下的搜索情况，并统计搜索到的文件数量
** 输入：search_cond->查找条件（可以用通配符）
**		示例： search_cond = ".//*.txt"  查找本文件夹下所有txt格式的文档
** 输出：file_name->以列表形式输出的文件名
**		备注：file_name的第一个元素代表该文件名的长度，后面紧跟着文件名的内容
**		 len -> 搜索到的合法文件数量
** 缺陷：对搜索到的文件夹没有处理逻辑，暂时只处理文件*/
/************************************************************************/
void SearchDir(const char* search_cond, char(*file_name)[MAX_FILE_NAME_LEN], int *len);
#endif

```

## FileHandle.c

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <io.h>
#include "FileHandle.h"

//#include<time.h>
//#include<dos.h>
//#include<conio.h>
//#include <windows.h>
//#include <direct.h>


static int calc_file_len(char *instr) //辅助函数，用以计算文件名的长度
{
	int len = 0;
	char *index = instr;
	while (*index != '\0')
	{
		index++;
		len++;
	}
	return len+1;
}
void SearchDir(const char* search_cond, char(*file_name)[MAX_FILE_NAME_LEN], int *len)
{
	struct _finddata_t data;
	long hnd = _findfirst(search_cond, &data);    // 查找文件名与正则表达式chRE的匹配第一个文件
	if (hnd < 0)
	{
		perror(search_cond);
	}
	int  nRet = (hnd < 0) ? -1 : 1;
	while (nRet >= 0)
	{
		if (data.attrib == _A_SUBDIR)  // 如果是目录
		{
			printf("   [%s]*\n", data.name);
		}
		else
		{
			*len += 1;
			memcpy(file_name, &data.name, MAX_FILE_NAME_LEN); //文件名拷贝
			file_name++;
		}
		nRet = _findnext(hnd, &data);
	}
	_findclose(hnd);     // 关闭当前句柄
}

```


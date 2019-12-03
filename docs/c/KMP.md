# 字符串查找_KMP算法

作者：尹超

日期：2017-4-1

## keywords

c, KMP, string searching

## KMP.c

```
#include "KMP.h"

#ifdef Cplusplus
int KmpFind(const string& target, const string& pattern)
{
	const int target_length = target.size();
	const int pattern_length = pattern.size();
	int * overlay_value = new int[pattern_length];
	overlay_value[0] = -1;
	int index = 0;
	for (int i = 1; i<pattern_length; ++i)
	{
		index = overlay_value[i - 1];
		while (index >= 0 && pattern[index + 1] != pattern[i])
		{
			index = overlay_value[index];
		}
		if (pattern[index + 1] == pattern[i])
		{
			overlay_value[i] = index + 1;
		}
		else
		{
			overlay_value[i] = -1;
		}
	}
	//match algorithm start
	int pattern_index = 0;
	int target_index = 0;
	while (pattern_index<pattern_length&&target_index<target_length)
	{
		if (target[target_index] == pattern[pattern_index])
		{
			++target_index;
			++pattern_index;
		}
		else if (pattern_index == 0)
		{
			++target_index;
		}
		else
		{
			pattern_index = overlay_value[pattern_index - 1] + 1;
		}
	}
	if (pattern_index == pattern_length)
	{
		return target_index - pattern_index;
	}
	else
	{
		return -1;
	}
	delete[] overlay_value;
}

#else
int KmpFind(const char *target, const char *pattern)
{
	const int target_length = strlen(target);
	const int pattern_length = strlen(pattern);
	int * overlay_value = (int *)malloc(pattern_length * sizeof(int));
	if (overlay_value == NULL)
	{
		return -1;
	}
	overlay_value[0] = -1;
	int index = 0;
	for (int i = 1; i<pattern_length; ++i)
	{
		index = overlay_value[i - 1];
		while (index >= 0 && pattern[index + 1] != pattern[i])
		{
			index = overlay_value[index];
		}
		if (pattern[index + 1] == pattern[i])
		{
			overlay_value[i] = index + 1;
		}
		else
		{
			overlay_value[i] = -1;
		}
	}
	//match algorithm start
	int pattern_index = 0;
	int target_index = 0;
	while (pattern_index<pattern_length&&target_index<target_length)
	{
		if (target[target_index] == pattern[pattern_index])
		{
			++target_index;
			++pattern_index;
		}
		else if (pattern_index == 0)
		{
			++target_index;
		}
		else
		{
			pattern_index = overlay_value[pattern_index - 1] + 1;
		}
	}
	if (pattern_index == pattern_length)
	{
		return target_index - pattern_index;
	}
	else
	{
		return -1;
	}
	free(overlay_value);
}
#endif

```

## KMP.h

```
#ifndef _KMP_H_
#define _KMP_H_

//#define Cplusplus		//开启此处，启用C++代码，否则使用C


#ifdef Cplusplus
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int KmpFind(const string& target, const string& pattern);
#else
#include <string.h>
#include <stdlib.h>
/*
** 原型:int KmpFind(const char *target, const char *pattern)
** 作者：尹超
** 日期：2017-4-2
** 描述：KMP算法——字符串快速匹配
** 输入：target -> 收到的指令字符串
**       pattern ->
** 输出：无
** 返回值：	-1 -> 字符串不匹配
**			>=0 -> 匹配上的首地址
** 备注：该函数是标准库函数，请勿修改
*/
int KmpFind(const char *target, const char *pattern);
#endif
#endif
```


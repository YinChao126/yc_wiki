# string字符串操作

## keywords

c, string

## 头文件

#include<string.h>

## 可用函数

`strcpy(*dst, *src)`字符串拷贝

`strlen(*pstr)` 求字符串长度

`atoi(str)` 字符串转int数字

`atol(str) `字符串转long数字

`atof(str) ` 字符串转float数字

`sprintf(str, "%d", 1234)` 数字转字符串

`strcat` 字符串拼接

`toascii` 将字符串转成合法ASCII码字符

`toupper` 小写转大写

`tolower`  大写转小写

## 初始化与动态输入

```
#方法1
char *p;
p = "hello,world";
printf("%s",p)

#方法2
Char *p;
While(*p != ‘\n’)
{
	Scanf(“%c”,p);
P++;
}
```
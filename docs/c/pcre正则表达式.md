# pcre在C环境下实现正则表达式

作者：尹超

日期：2018-5-1

## 1. pcre简介

pcre能够在C的环境下实现正则表达式的功能（原生的C是不支持该特性的）

## 2. 大致思路

先下载pcre源码并编译成dll

然后以库函数的形式直接使用即可

## 3. pcre编译步骤

### 3.1 去[官网](https://sourceforge.net/projects/pcre/files/)下载pcre的源码

### 3.2 按照说明对源码进行相应处理（重要）

- 将源码根目录下的文件重命名


```
config.h.generic -> config.h
pcre.h.generic -> pcre.h
pcre_chartables.c.dist -> pcre_chartables.c
pcre_stringpiece.h.in -> pcre_stringpiece.h
pcrecpparg.h.in -> pcrecpparg.h
```

- config.h里定义#define SUPPORT_UTF 1。否则，则不支持Utf-8编码的文本（定义此处会出问题，提示没有_utf_table3，没有解决，所以暂时没有定义）

- 打开config.h，看有没有HAVE_MEMMOVE和HAVE_BCOPY的宏定义，如果有就将其注释掉

### 3.2 创建vs工程，并对工程进行配置

- VisualStudio新建一个dll工程（空工程），工程进行如下配置

- C/C++ -> 预处理器 -> 预处理器定义 -> 编辑（增加）： HAVE_CONFIG_H
- C/C++ -> 代码生成 -> 运行库 -> 选择：多线程/MT
- C/C++ -> 预编译头 -> 不适用预编译头

### 3.3 将源码编译成dll

将所有的pcre_xxx.c 和*.h的文件添加到工程中，直接编译即可生成dll（大功告成）

注意：嫌麻烦的话，直接把./便宜源文件的拷贝进工程即可，其余都可以忽略

## 4. pcre使用步骤

- 把pcre.dll集成到工程中，并进行相应配置【dll/lib/h三者缺一不可】

```
假设目标工程为example
1. Example工程的debug目录下添加pcre.dll
2. Example工程源码目录下添加pcre.lib和pcre.h
3. Example工程配置：配置属性 -> 连接器 -> 输入 -> 附加依赖项 -> 增加：pcre.lib
4. App源码中 #include "pcre.h"
```

- 编写正确的pattern
- 利用pcre_compile对pattern进行编译形成obj
- 利用pcre_exec对待搜索内容进行obj匹配，观测返回值
- 如果pcre_exec返回>0，代表找到了内容

## 5. 示例代码

```
#include "pcre.h"

#define OVECCOUNT 30    /* should be a multiple of 3 */

int main()
{
  ...... //
  	// regular expression filter...
  char *search_str = "M4_D2_12.0dB.bin"; //测试输入字符串
	char *re_pattern = "M4_D2_[0-9]+.0dB.bin"; //正则表达式
	printf("pattern = %s\n", re_pattern);
	printf("filter result\n");
	pcre *cstr;
	int erroroffset;
	int num;
	const char * error;
	char result[30];
	int ovector[OVECCOUNT];
	cstr = pcre_compile(re_pattern, 0, &error, &erroroffset, NULL);
  num = pcre_exec(cstr, NULL, search_str, strlen(search_str), 0, 0, ovector, (10) * 3);
  if (num > 0)
  {
    printf("%s\n", search_str);
  }
}
```



## 参考资料

[pcre官方源码下载地址](https://sourceforge.net/projects/pcre/files/)


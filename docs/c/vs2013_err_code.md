# VS2013错误代码汇总

## keywords

vs2013, visual studio, error code

## error LNK1120: 1个无法解析的外部命令

错误的根源：

使用的函数没有定义，可能是文件包含的问题，也可能是类没有实例化

## error LINK2019:无法检测的外部错误

描述：原工程中添加一个FIFO模块（FIFO.c/FIFO.h），确定包含完好，并且经过了严格测试。实际编译发现报错。error LNK2019:无法解析的外部信号。

 分析：FIFO模块本身绝无问题，路径也完全正确，包含格式也完全正确

 原因：**C/C++混合编译造成的错误**。源文件中有c++,c两种风格的。混编的时候出错。而且这种错误在编译的时候是不报错的，发现不了错误。只有运行时候才出错。

 解决方案：统一为C或者C++即可

## error 4996 : 不能使用fopen

背景描述：

想要进行文件读写操作，写了一句 in = fopen("***.txt","wb");

提示报错，不能使用fopen函数，建议使用更安全的fopen_s函数

解决方法：

1. 右击工程属性 - 配置属性 - C/C++ - 预处理器
2. 预处理器定义中添加一行：_CRT_SECURE_NO_WARNINGS
3. 问题解决

## error C2079: 使用未定义的内容

背景：

main中定义的全局变量不报错，想把全局变量挪个位置，放入VariableDefinition.c中统一管理，结果就报错了。

原组织结构

- Complex.c中定义了结构体 struct Complex …
- main.c中全局变量定义一个struct Complex test[1000];通过编译

 改动后的结构：

- Complex.c中定义了结构体 struct Complex …
- main.c中的test变量用global.c和global.h统一管理
- global.c中定义 struct Complex test[1000]; global.h中声明extern Complex test[1000]

编译后报错！！！

原因分析：

**超前引用**！在编译器编译过程中，global可能先于Complex编译，所以global中的Complex结构体还没有定义的，因此test的类型不明朗，所以报错。

## 未找到chkstk.asm

描述：VS2013下，程序编译正常，运行到某一个函数时报错：未找到chkstk.asm

 原因：**堆内存溢出**，需要把平台的默认设置堆内存调大一些。

 方法：项目-》属性-》配置属性-》链接器-》系统，将堆栈保留大小弄大点，如50M（52428800）

## error C4996 itoa错误

使用itoa整数转字符串的时候出现此错误

error C4996:’itoa’: The POSIX name for this item is deperecated/ Instead, use the ISO C++ conformant name:_itoa.

 原因很简单:

itoa函数可能有缺陷，在后续的标准中被删除了，取而代之的是_itoa或者_itoa_s

 解决方法：

使用 _itoa 取代itoa即可




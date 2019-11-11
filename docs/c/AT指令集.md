# AT指令集的实现

作者：尹超

日期：2017-4-6

## 用户调用

```
#include "AT_Codec.h"
#include <stdio.h>
#include <Windows.h>

int main()
{
	char *RecStr = "AT+SVER=98.176\r\n";
	int id;
	double value;
	AtDecoder(RecStr, &id, &value);
	system("pause");

	return 0;
}
```

## AT.c

```
#include "AT_Codec.h"
#include <string.h>
#include <stdlib.h>

//用户请修改此处的命令列表，后面枚举的跟随一起修改
char const *AtCommand[] = {
	"HBNT",
	"RECVOP",
	"SVER",
	"ID",
	"SNR",
	"STAT",
	"SFO",
	"CFO",
	"TUNER",
	"QSRV",
	"TIME",
	"CKFO",
	"BDRT",
	"FREQ",
	"RMODE",
	"PPS1",
	"SERV",
	"STUD",
	"UDDA",
	"NULL"
};

enum CmdDefine
{
	HBNT, //休眠
	RECVOP,	//接收机开关
	SVER,	//查询软件版本
	ID,	//查询产品ID
	SNR, //查询信噪比
	STAT, //查询状态
	SFO,	//查询时偏
	CFO,	//查询频偏
	TUNER,	//查询tuner状态
	QSRV,	//接收到有哪些业务
	TIME,	//日期时间
	CKFO,	//设置校验失败是否输出
	BDRT,	//设置波特率
	FREQ,	//设置频点
	RMODE,	//设置接收模式
	PPS1,	//设置1PPS开关
	SERV,	//输出所有业务或特定业务
	STUD,	//启动升级
	UDDA,	//传输升级数据
	TEST	//测试
};

#define N_AtCommand (sizeof(AtCommand) / sizeof(AtCommand[0]))

int AtDecoder(char *Command, int *CmdId, double *RcvPara)
{
	int BiosAddr = -1;
	int index;
	for (index = 0; index < N_AtCommand; index++)
	{
		BiosAddr = KmpFind(Command, AtCommand[index]);
		if (BiosAddr >= 0)
		{
			break;
		}
	}
	if (BiosAddr < 0)
	{
		return -1; // no command matched.
	}

	*CmdId = index;

	if (BiosAddr != 3)
	{
		return -3; //指令没对齐.
	}

	int len;
	char *p;
	char value[10];
	int ValueLen;
	switch (index)
	{
	case HBNT:
		break;
	case RECVOP:
		break;
	case SVER: //get the cmd's parameter.
		len = strlen(Command); // total len
		BiosAddr += 5; // 此处的10是数出来的 "SVER+"
		p = Command + BiosAddr;
		ValueLen = len - BiosAddr - 2;
		for (size_t i = 0; i < ValueLen; i++)
		{
			value[i] = *p++;
		}
		*RcvPara = atof(value);
		break;
	case ID:
		break;
	case SNR:
		break;
	case STAT:
		break;
	case SFO:
		break;
	case CFO:
		break;
	case TUNER:
		break;
	case QSRV:
		break;
	case TIME:
		break;
	case CKFO:
		break;
	case BDRT:
		break;
	case FREQ:
		break;
	case RMODE:
		break;
	case PPS1:
		break;
	case SERV:
		break;
	case STUD:
		break;
	case UDDA:
		break;
	case TEST: //通过串口回一条"+OK\r\n"信息
		break;
	default:
		return -2; // decode the command, but cannot handled it.
	}
	return 0;
}
```



## AT.h

```
#ifndef _AT_CODEC_H_
#define _AT_CODEC_H_
#include "KMP.h"

/*
** 原型:int AtDecoder(char *Command, int *CmdId, double *RcvPara)
** 作者：尹超
** 日期：2017-4-2
** 描述：一个AT指令集的示例程序
** 输入：Command -> 收到的指令字符串
** 输出：CmdId -> 解析出该字符串属于命令列表的第几行（第几号命令）
**		RcvPara -> 解析出的命令参数（如果有的话）
** 返回值：	0  -> 工作正常，输入命令得到解析并正确处理
**			-1 -> 命令不匹配
**			-2 -> 解析出正确的命令，但没有找到对应的处理过程（一般不会出现）
**			-3 -> 解析出正确命令，但是不对齐，检测到的头不是“AT+”
** 备注：	1. 该函数只是测试程序，仅供演示如何解析命令并得到参数
**			2. 输出参数如果有多个，则必须改成数组输出。如果类型各不一样，则需要
**			改成结构体输出
*/
int AtDecoder(char *Command, int *CmdId, double *RcvPara);

#endif
```


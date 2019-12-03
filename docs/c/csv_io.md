# CSV文件操作

作者：尹超

日期：2018-5-30

## keywords

c, csv, io, demo

## test_app.c

```
#include <stdio.h>
#include "csv_io.h"

int main(void)
{
	int ret;
	//1. 写入示例
	char *file_name = "test.csv";
	CsvCreateFile(file_name);

	char *info = "something you should record...";
	int para1 = 123;
	float para2 = 2.34;
	for (int i = 0; i < 10; i++)
	{
		CsvWriteRecord(file_name, para1, para2);
	}
	CsvCloseFile();

	//2. 读出示例
	ret = CsvReadExample(file_name);
	return 0;
}
```


## csv_io.h

```
/************************************************************************/
/* 模块名：csv_io
** 作者：尹超
** 描述：该模块用以实现C环境下的csv文件读写操作，并带有示例程序
** 更新时间：2018-5-30													*/
/************************************************************************/
#ifndef CSV_IO_H
#define CSV_IO_H
#include <stdio.h>

extern FILE *csv_out_file; //统一的csv写入句柄

void CsvCreateFile(char *file_name);
void CsvCloseFile(void);
void CsvWriteRecord(char *sub_file_name, int para1, float para2); //写入范例，实际应用需修改
int CsvReadExample(char *file_name); // 读出范例，实际应用需修改

#endif

```


## csv_io.c

```
#include "csv_io.h"

FILE *csv_out_file;

void CsvCreateFile(char *file_name)
{
	csv_out_file = fopen(file_name, "wt");
	char *head_info = "想要添加的头部信息";		//此处的头部信息可以自定义
	fprintf(csv_out_file, "%s,%s\n", head_info, "2018-5-30");
}

void CsvCloseFile(void)
{
	if (csv_out_file != NULL)
	{
		fclose(csv_out_file);
	}
}


void CsvWriteRecord(char *sub_file_name, int para1, float para2)
{
	fprintf(csv_out_file, "%s, %d, %f\n", sub_file_name, para1, para2);
}


int CsvReadExample(char *file_name)
{
	FILE *fin;
	fin = fopen(file_name, "rt");
	if (fin == NULL)
	{
		printf("cannot open thi file\n");
		return -1;
	}
	char *line, *record;
	char buffer[1024];
	char delims[] = ","; //默认的分隔符，如果需要请修改此处

	while ((line = fgets(buffer,sizeof(buffer),fin))!=NULL)
	{
		record = strtok(line, delims);
		while (record != NULL)
		{
			printf("%s", record);
			//printf("%s", delims);
			record = strtok(NULL, delims);
		}
	}
	fclose(fin);
	return 0;
}

```


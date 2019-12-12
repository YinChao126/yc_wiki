# Stack示例

作者：尹超

日期：2016-12-16

## 描述

下文给出了一个栈的实现模块，可直接使用

## stack.c

```
#include "Stack.h"
#include <assert.h>
StackType Stack[Stack_SIZE];
static int top_element = -1;

void ClearStack()
{
	top_element = -1;
}

void push(StackType *DataIn)
{
	assert(!is_full()); /* 压入堆栈之前先判断是否堆栈已满*/
	top_element += 1;
	Stack[top_element] = *DataIn;
}
void pop(StackType *DataOut)
{
	assert(!is_empty()); /* 弹出堆栈之前先判断是否堆栈已空 */
	*DataOut = Stack[top_element];
	top_element -= 1;
}

StackType top(void)
{
	assert(!is_empty());
	return Stack[top_element];
}

char is_empty()
{
	return top_element == -1;
}

char is_full()
{
	return top_element == Stack_SIZE - 1;
}

```

## stack.h

```
#ifndef __Stack_H
#define __Stack_H
#define Stack_SIZE 256
typedef int StackType;/* 堆栈所存储的值的数据类型 */

//void create_Stack(int size);
//void destroy_Stack(void);
void push(StackType *DataIn);
void pop(StackType *DataOut);
StackType top(void);
char is_empty(void);
char is_full(void);
void ClearStack();
#endif

```

## main.c

```
#include <stdio.h>
#include <stdlib.h>
#include "Stack.h"

int main(void)
{
	int val;
	push(10); push(9); push(7); push(6); push(5);
	push(4);  push(3); push(2); push(1); push(0);
	printf("push压入数值后：\n");

	printf("\n");
	pop(&val);
	pop(&val);
	printf("经过pop弹出几个元素后的堆栈元素:\n");

	printf("\n");
	printf("top()调用出来的值: %d\n", top());
	return 1;
}

```


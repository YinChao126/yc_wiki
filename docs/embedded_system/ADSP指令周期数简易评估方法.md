# ADSP指令周期数测算方法

作者：尹超

日期：2017-3-13



```
1. 添加头文件：
#define DO_CYCLE_COUNTS //很奇怪，必须要在cycle_count之前定义才能启动该功能
#include <cycle_count.h>
#include <stdio.h>

2.定义两个变量
	cycle_t start_count;
	cycle_t final_count;
	
3.在需要测试的两端加上代码
	START_CYCLE_COUNT(start_count);
<
    code section
>
	STOP_CYCLE_COUNT(final_count,start_count);
	
4. 显示结果
  PRINT_CYCLES("Number of cycles:",final_count);
  
更详细的请看说明书《Cycle Counting and Profiling》
```

Bug:如果定义了time.h，则该功能不可用，原因未知！
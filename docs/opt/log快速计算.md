# log近似运算

作者：尹超

日期：2019-7-1

## keywords

opt,  log, fast

## 背景描述

​	数字信号处理中经常要用到对数运算。虽然可以通过调用math.h的通用库函数来实现，但是效率是非常低下的。如果你对精度要求不高，对运算效率要求很高。就用下面的子函数来代替吧。

​	下面的算法是我自己翻出了一篇1960年的论文，然后再结合看了一些其他文章搞出来的，该函数求得的是近似值，我在MATLAB环境下评估了一下，1~10000范围精度保持在5%以内。符合精度要求不高的环境。尤其是通信上面的应用。

## 源码

```C
/*
** log快速运算
** 创建时间：2019-7-1
** 作者：尹超
** 版本号：V2.0
** 描述：用来快速计算以2为底的对数
** 输入：x->次数
** 输出：无
** 返回值：log2x的计算值
** 备注： x必须大于1
*/
double FastLog(double x)
{
    double m;
    int k = 1, op = 2;
    double tmp = x / op;
    if (x <= 1)     return 0;
    while (tmp >= 2)
    {
        op <<= 1;
        k++;
    }
    m = tmp - 1;
    if (m <= 0.25)      return 1.3125 * m + k;
    else if (m <= 0.5)  return 1.078125 * m + 0.00015625 + k;
    else if (m <= 0.75) return 1.015625 * m + 0.0625 + k;
    else if (m <= 1)    return 0.75 * m + 0.25 + k;
    else                return 0; 
}
int main()
{
    double y;
    y = FastLog(Val);
    return 0;
}  
```


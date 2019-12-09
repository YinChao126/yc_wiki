# 快速计算平方根

作者：尹超

日期：2018-10-9

## 背景介绍

下文给出了一个平方根的速算法，只需要50cycle即可完成计算

摘自《arm system developer's guid：Designing and Optimizing system software》

## usqrt_simple

```
// 输入：d->输入值    N->结果的最小表示位数
unsigned usqr_simple(unsigned d, unsigned N)
{
  unsigned t, q=0, r=d;
  do
  { /* calculate next quotient bit */
    N--; /* move down to next bit */
    t = 2*q+(1 << N); /* new r = old r - (t<<N) */
    if ( (r >> N) >= t ) /* if (r >= (t << N)) */
    {
      r -= (t << N); /* update remainder */
      q += (1 << N); /* update root */
    }
  } while (N);
  return q;
}

/***************************************************************
example：
int r = usqr_simple(256, 5);    r = 16
//此处结果是16，最少要用5bit表示。所以N取值大于5均可

int r = usqr_simple(5263418, 16);    r = 2294
//此处结果是2294，最少要用12位表示
***************************************************************/
```


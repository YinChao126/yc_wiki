# exp指数快速运算

作者：尹超

日期：2017-4-1

```c
double FastExp(double y)
{
    double result;
    *((int *)(&result) + 0) = 0;
    *((int *)(&result) + 1) = 1512775 * y + 1072632447;
    return result;
}
```

[参考出处](https://blog.csdn.net/yinchao163/article/details/68946239)
# 再论sleep延时

作者：尹超

日期：2019-7-25

## keywords

linux,  sleep

## 背景

在做通信项目的时候需要处理不同线程的数据流匹配问题，在加入sleep(second)延时函数后发现表现有点奇怪，仔细查阅api说明才了解到Linux下sleep函数和windows下的不一样！！！

## Linux下延时函数汇总

### sleep(int second)

秒级延时函数，输入浮点数的话会直接向下取整。所以sleep(0.9)实际上等于没有任何延时！（这正是我出bug 的缘由）

### usleep(int usecond)

微秒级延时函数

## 跨平台可用的毫秒延时函数

不要再纠结什么平台用什么函数了，下面这个一劳永逸解决跨平台延时问题

```
#ifdef WIN32
#include <windows.h>
#elif _POSIX_C_SOURCE >= 199309L
#include <time.h>   // for nanosleep
#else
#include <unistd.h> // for usleep
#endif

void sleep_ms(int milliseconds) // cross-platform sleep function
{
#ifdef WIN32
    Sleep(milliseconds);
#elif _POSIX_C_SOURCE >= 199309L
    struct timespec ts;
    ts.tv_sec = milliseconds / 1000;
    ts.tv_nsec = (milliseconds % 1000) * 1000000;
    nanosleep(&ts, NULL);
#else
    usleep(milliseconds * 1000);
#endif
}
```

## 参考链接

[Is there an alternative sleep function in C to milliseconds?](https://stackoverflow.com/questions/1157209/is-there-an-alternative-sleep-function-in-c-to-milliseconds)
# python的常用进程间通信汇总

作者：尹超

日期：2019-12-11

## Python常用多进程通信方法

pipe

queue

共享内存

socket

中间件

http

## Queue通信





## 共享内存

Python中的mmap模块是通过映射同一个普通文件实现共享内存的。文件被映射到进程地址空间后，进程可以像访问内存一样对文件进行访问。

最简单的实例【仅适用于Windows！！！】

### server

每隔一秒往共享内存中写入数据

```
import mmap
import contextlib
import time
with contextlib.closing(mmap.mmap(-1, 1024, tagname='daemon_area', access=mmap.ACCESS_WRITE)) as m:
    for i in range(1, 100):
        m.seek(0)
        msg = "msg " + str(i)
        msg = msg.encode('utf-8')
        m.write(msg)
        m.flush()
        time.sleep(1)
```

### client

每隔一秒读取共享内存的数据

```
import mmap
import contextlib
import time
 
while True:
    with contextlib.closing(mmap.mmap(-1, 1024, tagname='daemon_area', access=mmap.ACCESS_READ)) as m:
        s = m.read(10).decode('utf-8')
        print(s)
    time.sleep(1)
```



## 参考链接

[mmap官网解释](<https://docs.python.org/3/library/mmap.html>)

[python进程间通信之共享内存详解](https://www.jb51.net/article/127123.htm)
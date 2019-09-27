# 时间和日期操作

作者：尹超

日期：2019-9-24

## 类型转换

### str转datetime

`dtime = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")`

### datetime转str

`str_time = dtime.strftime("%Y-%m-%d %H:%M:%S")`

### datetime转unix

```
def dtime2unix(dtime):
	a = dtime.timetuple()           
	b = time.mktime(a)
	return int(b)
```

### unix转datetime

`dtime = datetime.datetime.fromtimestamp(unix_time)`

## 日期运算



## 工作日判断


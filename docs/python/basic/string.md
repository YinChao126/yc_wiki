# python中string的常用操作

作者：尹超

日期：2019-12-12

## 字符填充 zfill

描述：一个数字前需要补0

```

data = "1"
print(data.zfill(4))
#输出为 "0001"
```

## 字符删除 strip

描述：排除不需要的字符

```
data = b'test/x00/x00/x00/x00'
data = data.strip(b'/x00')
输出为：b'test'
```

## 分隔 split

描述：根据分隔符将数据分成多段

```
data = "1,2,3,4,5"
data = data.split(",")
输出为： data = ['1', '2', '3', '4', '5']
```


# Series操作大全（持续增加）

作者：尹超

日期：2019-9-27

## 1. 创建

```
from pandas import Series
ex_ser = Series([10, 20, 30, 40], index=list('abcd'))
```

## 2. 增

单个元素可以set_value,多数据增加用append。想在前面增加就concat拼接

### 2.1 头部增加

```
import pandas as pd
a = pd.Series([2,3,4])
pd.concat([pd.Series([1]), a])
```

### 2.2 尾部增加

```
ser_ex = ser_ex.set_value('sss', 1111)  #有标签1
ser_ex['s'] = 80  #有标签2
ser_ex[len(ser_ex)] = 111   #无标签
ser_ex = ser_ex.append(ser_2)  #尾部增加一个Series序列
```

## 3. 删

基本删除有drop/pop函数，还可以用内置的del

删除头

删除尾

指定删除

```
ser_ex = ser_ex.drop('lv') #删除所有index为lv的项
ser_ex.pop('lv')
```

清空

## 4. 改

**下标，索引标签，切片**三种方式可以进行修改

### 改特定位置的值

```
ser_ex[0] = 100  #下标改
ser_ex['a'] = 100  #索引标签改
ser_ex[1:4] = 100 #切片修改
```

### 重新设置索引值

```
ser_ex.index = [1,2,3,4,5] #最简单
ser_ex.reindex(list('fasd')) #方法2
```



## 5. 查

### 索引查询

`series1[2]`

### 标签查询

`series1['b']`

### 布尔索引

`series1[series1 > 20]`

### 切片

```
series1[1:3]
series1['b':'d']
```

### 多元素查询

```
series1[[0, 2, 3]]
series1[['a', 'c', 'd']]
```

### 查询数据，标签

```
ser_data.values  #获取数组数据（numpy.ndarray类型）
ser_data.
```



## 参考连接

[pandas—Series操作](https://blog.csdn.net/qq_39161737/article/details/78866191)
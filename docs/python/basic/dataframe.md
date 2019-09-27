# DataFrame操作大全（持续更新）

作者：尹超

更新日期：2019年07月09日

备注：下文无说明时，默认df为DataFrame格式的变量

## 1. 新建

### 1.1 字典创建

```python
from pandas import DataFrame 
head = ['sex', 'age', 'name']
data = {        
    'name':['zs','ls','ww'],        
    'age':[10,20,30],        
    'sex':['m','w','m']}
df1 = DataFrame(data) #（如果不指定columns，则表头会自动排序）
df2 = DataFrame(data,columns=head) #固定表头
```

df1: 

age name sex
0   10   zs   m
1   20   ls   w
2   30   ww   m

df2:

  sex  age name
0   m   10   zs
1   w   20   ls
2   m   30   ww

### 1.2 数组创建

```python
import numpy as np
import pandas as pd
ar = np.random.rand(9).reshape(3,3)
df1 = pd.DataFrame(ar)
print(df1)
df2 = pd.DataFrame(ar, index = ["a","b","c"], columns = ["one", "two", "three"])
print(df2)
```

          0         1         2
0  0.646752  0.405649  0.717825
1  0.202191  0.907458  0.590119
2  0.347748  0.999144  0.329197
​        one       two     three
a  0.646752  0.405649  0.717825
b  0.202191  0.907458  0.590119
c  0.347748  0.999144  0.329197

更详细的：https://blog.csdn.net/u010199356/article/details/85697860

## 2. CSV文件读写

### 2.1 写CSV文件

```python
df.to_csv(file_name) #默认增加一列0~n的index标号
df.to_csv(file_name,index = False) #不带默认的index标号
df.to_csv(file_name, mode='a', header=False) #以append方式写入，并且不带表头
```

### 2.2 读CSV文件

```python
df = pd.read_csv(file_name) #如果内容是数字，可能默认读成numpy类型
df = pd.read_csv(file_name, dtype=str) #如果内容是数字，可能默认读成numpy类型
```

## 3 排序

### 3.1 按行翻转

df = df[::-1]

### 3.2 按特定列排序

```python
df.sort_index()
df.sort_values(by='day')
df.sort_values(by=['day','month'])
```

### 3.3 按给定的列名重排序

```python
import pandas as pd
head = ['b','a','c']
data = {'c':[7,8,9],
        'b':[4,5,6],
        'a':[1,2,3]}
df1 = pd.DataFrame(data) #表头自动排序    
print(df1)    
df2 = df1.reindex(columns=head) #按规定的head重排序    
print(df2) 
df1:   a  b  c
    0  1  4  7
    1  2  5  8
    2  3  6  9
df2:   b  a  c
    0  4  1  7
    1  5  2  8
    2  6  3  9
```

参考链接：https://www.cnblogs.com/feigebaqi/p/9800496.html

## 4.元素索引

### 4.1 索引单个元素

方法1： df.iloc[1】[3]  #类似于二维数组索引

方法2： df.iloc[1,2]

方法3：df.loc['行名','列名']  #根据名字获取索引值

### 4.2 索引行

df.head() #索引前5行数据

df.head(3) #索引前三行

获取表头名称： df.columns  / df.columns.tolist()

获取行列数：df.shape

df.loc[n] #索引低n行

### 4.3 索引列

方法1： df['name'] #第name列

方法2： df.loc[:,'name'] #第name列

方法3： df.iloc[:,1] #第2列

### 4.4 索引满足特定条件的记录

```python
    data = {'name':['zs','ls','ww','lmz'],
            'age':[16,23,11,40], 
            'sex':[0,1,1,1]}    
    df = pd.DataFrame(data)    
    record1 = df[df.age < 20] #单个条件筛选    
    record2 = df[(df.age < 20) & (df.sex == 1)] #多条件筛选    

```

## 5. 修改

### 修改第1行第‘name’列的特定元素

`df.at[1, 'name'] = 'zs'` #目前只找了这种方法

### 5.1 改写column

方法1：

\>>>a.columns = ['a','b','c']
\>>>a
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9

方法二：

\>>>a.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace = True)
\>>>a
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9

### 5.2 改写index

对dataframe进行重排序或者增减操作后，index会乱序，如何将index重新编成0，1，2，3，...n这样的有序序列呢？如下两种方法可以做到这一点

```
df.index = pd.Index(range(len(df))) #method 1

df =  df.reset_index(drop=True) #method 2
```

### 5.3 增加

#### 5.3.1 增加行

 如果将增加的记录是dict类型或者series类型

```python
df = df.append(dict_record,ignore_index=True) #方法1， append
df.loc[2] = series_record #方法2， 显式合并
```

如果记录是list类型，则先转换为series，再append

`ser_data = pd.Series(list_para)`

#### 5.3.2 增加列

假如有一个名为ser_data的series序列需要增加到已有的df中，取名叫'para'，很简单

`df['para'] = ser_data`即可

### 5.4 删除

```python
df = df.drop[index] #删除一行
df = df.drop(index=[1,3,7]) #删除多行
```

### 5.5 去重

```python
interest_column = ['c1','c2']
df= df.drop_duplicates(subset=interest_column ,keep='last') #如果interest_column的值相同，则保留后面一条记录，keep='first'则保留前面一条记录
```

### 5.6 清空

`df.drop(df.index,inplace=True)`

## 6.多个DataFrame的合并、拼接

```python
df = pd.DateFrame(list(zip(s1,s2,s3)) #多个series合并成一个df
df = pd.concat([d1,d2]) #多个DataFrame合并成一个df
```

## 7. DataFrame的计算

### 7.1 按列求和，求平均

```python
df['column_name'].sum() #按列求和
df['column_name'].mean() #按列求平均
```

### 7.2 求得DataFrame的索引值

pd_data.index.tolist()

### 7.3 整列计算

```
df['col2'] = df['col1'].map(lambda x: x**2) #单列
df['new_col'] = df.apply(lambda x: x['col1'] + 2 * x['col2'], axis=1)  #多列计算(new_col可以是新增列)
```



## 参考链接

https://www.jianshu.com/p/a6139a1352d6

[python中dataframe常见操作：取行、列、切片、统计特征值](https://blog.csdn.net/tanlangqie/article/details/78656588)


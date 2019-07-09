# 利用pandas实现excel表格的数据处理

作者：尹超

日期：2019-7-9

背景：



## 主要知识点

- excel的存取操作
- pandas的基本操作

## 读取excel文件

```
import pandas as pd
excelFile = r'data.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
```

## 存储excel文件

```
import pandas as pd
df = xxx   #前提是df已经有数据了
df.to_excel('test.xlsx',index=False) 
```


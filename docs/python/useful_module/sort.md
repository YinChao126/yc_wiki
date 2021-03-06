# sort大全


## keywords

sort, num, re

## 1. sort by num_字符串中数字排序

## 应用场景描述

对于一个给定的字符串列表，根据字符串中的数字进行排序。特别适用于数据集排序

例如读取了一系列的文件名['10.txt','11,txt','2.txt','89.txt']，对其进行排序

## 源码

```python
import re

re_digits = re.compile(r'(\d+)')
def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces
    
def sort_str_by_emb_num(str_list):
    '''
    实现一个根据字符串中的数字来排序的函数，用于给大量数据集排序
    输入：文件名list
    输出：对该list进行重新排序（以文件名中的数字为参考）
    '''
    aux = [(emb_numbers(s),s) for s in str_list]
    aux.sort()
    return [s for __, s in aux]

###############################################################################
if __name__ == '__main__':
    ex_list = ['10.txt','11,txt','2.txt','89.txt']
    print(ex_list)    
    after_sort = sort_str_by_emb_num(ex_list)
    print(after_sort)
```

## 根据字符串中的数字排序（2）

需求：

有一个书单，后面有评分，需要根据评分为书单重新排序

```
基业长青    8.1 
22条商规   8.2
定价圣经    8.2
引爆流行    8.0
FACEBOOK效应    7.9 
创业的国度：以色列经济奇迹的启示    7.9
沸腾的岁月   7.6
丰田生产方式    8.2
华尔街之子：摩根    8.2
蓝海战略    7.7
撬动地球的GOOGLE   7.5
```

解决：

```

```

输出：

```

```




# 文件及文件夹操作

作者：尹超

日期：2019-6-28

## 读文件

```python
mode = 'r'  #str形式读出
mode = 'rb' #二进制读出
with open(file_name, mode) as fh: #读文件 
	content = fh.read() #读取完整文件，存为str
    conente_list = fh.readlines() #按行读取，存为list
```

## 写文件

```python
mode = 'w'  #或者二进制写入 wb 
mode = 'a' #append方式写入
with open(file_name, mode) as fh: #读文件 
	fh.read(content) #把所有内容完全写入
```

## 快速获取文件行数

```python
count = len(open(filename,'r').readlines())
```

## 文件查找

```python
#查找file_path下的所有文件，并将结果存入f
from os import walk
f = []
for (dirpath, dirnames, filenames) in walk(file_path):
    f.extend(filenames)
    break
```

## 判断文件是否存在

```
import os
os.path.exists(test_dir)
```

## 文件删除

`os.remove(file) #删除一个文件`

## 文件夹创建

```python
if not os.path.exists(directory):
    os.makedirs(directory)
```

## 清空文件夹

```
def clear_dir(path): #清空文件夹里所有文件，但保留该文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
```



## 文件夹删除

```
#删除空文件夹
os.rmdir(dirname) 

# 强力删除，递归删除包括本文件夹在内的所有资源
import shutil
shutil.rmtree("1")
```



## 文件拷贝

拷贝单个文件

```python
from shutil import copyfile
src_file = '1.txt'
dst_file = '2.txt'
copyfile(src_file, dst_file)
```

拷贝整个文件夹

```python
from distutils.dir_util import copy_tree
src_tree = '/a/b/c'
dst_tree = '/x/y/z'
copy_tree(src_tree, dst_tree)
```

[参考链接](https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth)
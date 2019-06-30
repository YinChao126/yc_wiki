# 文件及目录操作

作者：尹超

日期：2019-6-28

## 文件读写

## 文件查找

## 文件夹创建

```python
if not os.path.exists(directory):
    os.makedirs(directory)
```

## 文件夹删除



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
# python包管理器

## 安装的包在哪里（以Ubuntu为例）

- sudo apt-get install 安装的package存放在 /usr/lib/python2.7/dist-packages目录中
- pip 或者 easy_install安装的package存放在/usr/local/lib/python2.7/dist-packages目录中
- 手动从源代码安装的package存放在site-packages目录中

## 有哪些包管理器

```
pip(很实用的一种)
distutils(标准库)
setuptools/distribute
easy_install
conda
poetry
```

## 1. distutils

Python自带的包管理工具，是标准库的一部分。distutils包含一个setupt.py 文件，通过执行setupt.py 进行安装包及打包的操作：

```python
python setup.py install #安装包
python setup.py sdist #发布包
```

## 2. pip（完全取代了easy_install）

### pip常用命令

```
pip --version  #检查pip的版本
pip list #查看已经安装的包
pip install xxx #安装xxx包最新版本
pip install xxx==1.0.4 #安装xxx包1.0.4指定版本
pip install xxx>=1.0.4 #安装xxx包1.0.4以上的版本
pip uninstall xxx #卸载xxx包
pip install --upgrade xxx #更新xxx包
pip search xxx #搜索是否有xxx包资源
```

### pip不能安装、卸载、升级怎么办？

例如想要升级nibabel时

使用命令：`sudo pip install --upgrade nibabel`

报错： 

Cannot uninstall ‘nibabel’. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

问题解析：

旧版本依赖多，不能清晰的删除，此时应该**忽略旧版本强制升级**，即如下

```
sudo pip install nibabel --ignore-installed nibabel
```

## 3. Poetry

项目依赖管理工具

## 参考链接

[Python的依赖项管理工具](https://python.freelycode.com/contribution/detail/1275)
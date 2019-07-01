# python包管理器

python有许多包管理器

```
pip(很实用的一种)
distutils(标准库)
setuptools/distribute
easy_install
conda
poetry
```

## distutils

Python自带的包管理工具，是标准库的一部分。distutils包含一个setupt.py 文件，通过执行setupt.py 进行安装包及打包的操作：

```python
python setup.py install #安装包
python setup.py sdist #发布包
```

## pip（完全取代了easy_install）

pip --version  #检查pip的版本
pip list #查看已经安装的包

pip install xxx #安装xxx包最新版本
pip install xxx==1.0.4 #安装xxx包1.0.4指定版本
pip install xxx>=1.0.4 #安装xxx包1.0.4以上的版本
pip uninstall xxx #卸载xxx包

pip install --upgrade xxx #更新xxx包

pip search xxx #搜索是否有xxx包资源



Poetry项目依赖管理工具



## 参考链接

[Python的依赖项管理工具](https://python.freelycode.com/contribution/detail/1275)
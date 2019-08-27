# 包、模块、导入详解

作者：尹超

日期：2019-8-27

## 1. 基本概念

### 1.1 路径

工作目录：当前程序运行的类似于linux中使用pwd查询当前的工作目录一样，可以通过工程配置来决定。务必搞清楚这一点，这个是使用相对路径的基石（不同IDE，不同工程设置下这里都会不一样，最终导致各种问题）

#### 1.1.1 绝对路径：文件存储的磁盘路径

例如：D:\Workspace\python\module_test\main.py。（只要文件的存储地址不变，则该路径总是固定的）。

#### 1.1.2 相对路径：文件存储相对于工作目录的层级关系

只要工作目录发生改变，相对路径的关系就被破坏了

. 当前文件夹

.. 上一级文件夹

#### 1.1.3 系统路径（sys.path）

计算机的环境变量，主要用来处理系统默认路径，正是因为有了系统路径，你导入系统模块(eg: time, os, 或者安装的标准第三方模块)时，系统自动去找path指定路径下找资源，你也可以把自定义的模块添加到系统路径下

#### 1.1.4 各种路径的查询和修改方法：

```
import sys
import os

print(sys.argv[0]) #获得当前待执行的那个模块(py文件)
print(os.getcwd()) #获得当前工作目录
os.chdir("目标目录")   #修改当前工作目录为目标目录
print(os.path.abspath('.')) #获得当前工作目录
print(os.path.abspath('..')) #获得当前工作目录的父目录
print(os.path.abspath(os.curdir)) #获得当前工作目录
print(sys.path) #获得系统路径
```

### 1.2 模块(module)，包(package)

所谓模块，可以简单理解为“就是一个py文件”。

所谓包，可以简单理解为“多个想要组织在一起的py文件，放在了一个文件夹里”，而那个文件夹就是一个包。与普通的文件夹的不同之处在于，该文件夹里必须带一个"__init__.py"的文件（可以是空文件）。

一个简单的比方，试想如下的工程组织结构

```
package/
        __init__.py
        module1.py
        module2.py
        sub_package/
                    __init__.py
                    module11.py
                    module12.py
```

package文件夹就是一个包，module1和module2就是package的两个模块。其中package还有一个子包叫sub_package，它里面也有两个子模块分别叫module11和module12

### 1.3 对象，模块导入

——python的世界里，一切皆对象。不论是类，函数，变量，模块还是包，其名字只是这个对象的一个引用而已。

按照我的理解就是：我就是一个实体（对象），张三就是我的名字（引用）。你叫张三的时候其实本意是想叫我这个人过去，而不是对张三这个名字感兴趣，只不过你通过张三这个名字具体地叫到了我这个人。（也许你会发现我有多个小名）

我们通过import module 语句导入一个模块会发生什么？—— 你通过module这个名字实例化了一个对象（这个对象在成功import之后就存在于内存里了），一旦你成功实例化了这个module对象，你就可以用上module里面定义的内容了（变量，函数，类等）。

   导入一个sys模块时，首先是找到这个模块，然后会从头到尾执行这个模块，遇到def就创建一个函数对象，然后赋上函数名，遇到模块中被赋值的全局变量，那就创建这个赋值号右侧的对象，然后赋给变量。那我怎么知道这个module里到底导入了哪些资源呢？你可以这样查询

    print(dir(module))
    有可能得到如下的结果
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b']　
###  1.4 命名空间

​        接着上面的“我是张三”这个继续讲，如何建立起“实体->引用”的对应关系呢？用字典结构，不过取了一个叫做“命名空间”的术语而已。通过命名空间，就建立了引用和实体之间的映射关系了，所以你不用去操作内存，只要管这个对象叫啥名字就可以了。

 一个命名空间中不能有重名，但是不同的命名空间可以重名而没有任何影响。python中有3类命名空间

- local:函数调用时创建（调用返回后即消失），记录了函数入参，内部变量等
- global:模块加载时创建（除非人为手动卸载该模块，否则一直存在），记录了该模块所包含的资源
- built-in：系统自带（一直存在），任何模块均可访问（通常放置内置函数和异常）

### 1.5 导入机制

#### a. 导入原则

摘抄Python标准库参考手册3.6.4中对import语句的一段说明：

The basic import statement (no from clause) is executed in two steps:

find a module, loading and initializing it if necessary
define a name or names in the local namespace for the scope where the import statement occurs.
When the statement contains multiple clauses (separated by commas) the two steps are carried out separately for each clause, just as though the clauses had been separated out into individual import statements.

以import pandas as pd为例，模块导入过程首先是去寻找pandas模块，找到后将其与本地命名空间的资源进行比对（防止重复导入）。如果没有，则实例化pandas对象，在内存里创建相应的资源并为其初始化，如果有则跳过。最后将pandas这个资源和pd这个变量名绑定到一起，用户就可以通过pd.xxx来引用pandas的资源了

#### b. 模块搜索顺序（如果模块同名的话，此处可能会冲突）

When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. sys.path is initialized from these locations:

The directory containing the input script (or the current directory when no file is specified).
PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
The installation-dependent default.
After initialization, Python programs can modify sys.path. The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended. 

可见，系统在搜索模块(module.py)时，优先去找built-in的内置模块，找不到再通过sys.path变量去搜索module.py这个文件。

可以做个实验，自定义一个os.py的模块并随便定义一个函数，你会发现无论如何你自定义的os模块都不起作用

### 1.6 小结：

- 模块导入前首先确定自己的路径，再考虑用什么方法去导入。搞不清楚路径就不要谈导入了，一团乱麻
- 模块就是一个py文件，包就是一个带__init__.py的文件夹
- 成功导入一个对象意味着（有可能）实例化了一个对象并在内存中创建了与该模块相关的资源
- 命名空间就是一个字典，它实现了上述从模块名到实际对象的映射关系，正是因为这层映射关系你才可以通过模块名来引用该资源，而不用关注内存细节
- 模块导入的机制是：首先搜索到模块并对初始化（如果之前没导入过的话），然后将该模块的资源与一个名称绑定到命名空间中。例如import pandas as pd. 你可以利用pd来指代pandas，而pandas这个名字指代了实例化的pandas类所包含的一切资源
- 模块搜索的顺序是：先在built-in中搜索，如果没有再找sys.path求助
- sys.path本质上就是一个系统变量，它存储了一堆路径（工作路径，环境变量，site-package安装路径，其他默认路径等），特别地： sys.path[0] 指代了当前待执行脚本的路径

## 2. 导入

基本的导入语法有如下几种

- import module
- import package.module
- import package.module as pm
- from module import function（不推荐）
- from module import *(不推荐)

假如有如下组织结构的资源，需要进行相应调用

```
-- src
    |-- mod1.py
    |-- lib
    |    |-- mod2.py
    |-- test1.py
```

### 同级模块导入(test1调用mod1)

直接在test1.py中`import mod1`即可

### 导入下一级模块（test1调用mod2）

直接在test1.py中`import lib.mod2`即可

### 导入上一级模块（mod2调用mod1）

先将上一级目录增加到系统搜索路径，再按同级导入操作

```
sys.path.append("..")
import 
```

## 参考链接

[工作路径](https://blog.csdn.net/qq_15188017/article/details/53991216)

[详解命名空间](https://www.cnblogs.com/zhangxinhe/p/6963462.html)

[包/模块理解](https://www.cnblogs.com/kex1n/p/5977051.html)

[Python中import导入上一级目录模块及循环import问题的解决](https://www.cnblogs.com/sjy18039225956/p/9265461.html)


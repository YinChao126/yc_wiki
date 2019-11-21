# AppFrozen

## 描述

StackOverflow上找的一段代码。用于判断运行代码是源码调试阶段还是可执行程序运行阶段（冻结），在调试开发和部署阶段尤其有用

```
import os
import sys


def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


def is_frozen():
    if hasattr(sys, 'frozen'):
        return True
    return False


class App:
    def __init__(self):
        self.base_path = app_path()  # get app's path
        self.is_frozen = is_frozen()  # if app is source code, no frozen. if app compiled as a executable,  is frozen

```




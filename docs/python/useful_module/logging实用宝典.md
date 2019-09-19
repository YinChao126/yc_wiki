# logging实用宝典

作者：尹超

日期：2019-9-19

## 背景

logging日志系统是python的一大特色，功能强大，使用简单方便

- logging模块与print类似，都是输出消息，但是比print强大的多
- logging可以控制输出位置（console，file，http，ftp等）
- logging可以控制输出粒度，LEVEL自主可调
- logging可以附加进程和线程ID号（对故障分析尤其有用）
- logging可以捕获Traceback的原文信息（方便异常处理）
- logging提供配置共享机制，确保不同模块间采用统一的配置进行log输出
- logging的配置可以在文件中实现，而不必在程序中写死

## 1. 基础知识扫盲

### 1.1 基础概念

#### 日志级别

系统默认六种日志级别，也可以自定义

NOTSET（0）、DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）
logging执行时输出设定值及以上级别的日志信息

#### Logger：

Logger Main Class，进行日志记录时创建的对象，调用它的方法就可以生成日志记录
LogRecord：日志记录，由用户调用Logger的方法产生

#### Handler：

用来处理日志记录的实体，它负责将LogRecord输出到指定地址（控制台？文件？网络？），还决定了输出的格式

#### ParentHandler（没啥用）：

Handler之间可以存在分层关系，以便不同Handler之间可以共享相同的功能

#### Formatter：

日志记录的格式处理（由Handler调用）

#### Filter：

决定哪些日志记录可以输出（由Handler调用）


### 1.2 logging流程（完整执行机制，分log和handler两个独立流程）

Logger 流程：
Logger -> 用户调用log函数（触发LogRecord产生日志记录）
LogRecord -> 生成一条log信息并传递到Handler

Handler 流程：
Handler -> 消息的具体执行器，调用Filter和Formater以控制日志记录过滤，格式化输出，输出地点
Filter -> 过滤器提供粒度控制，决定哪些日志记录能够输出
Formatter -> 格式化器，规定了最终输出的日志采用何种格式

### 1.3 日志输出格式

默认： 日志级别：Logger实例名称：日志内容
格式支持自定义

### 1.4 基本使用方法

#### 1.4.1 傻瓜式： 使用basicConfig即可，其余全部默认配置

示例代码：

```
import logging
logging.basicConfig()
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

输出如下结果：（默认时只输出warning以上的）

```
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

#### 1.4.2 basicConfig函数自定义配置

- filename, 设置输出到文件
- filemode, 
- format,自定义格式
- datefmt,自定义日期和时间显示格式
- level， 自定义log的显示等级

示例代码：

```
logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
```

### 1.5 自定义Logger（实战中根据自己的需要来自定义log）

一个系统只有一个实例化Logger根对象，该对象不能被重复实例化，系统实际的输出都来源于此

获取Logger根对象的方式：getLogger

## 2. 工程实践方法

推荐用法：
1. 按时间的滚动日志记录方式（TimeRotationHandler）
2. 使用配置文件

这种好处是日志不会无限大，只保留最近N天的记录。需要修改日志规则直接改配置文件就好

具体的玩法如下：

```
--config.py
--main.py
--logger.conf
```

logger.conf保存YAML格式的logging配置供logging模块装载

config.py读取logger.conf配置并实例化一个（或多个）log对象，给出一个实际的操作方法（一个字都可以不用改）

```
# coding:utf-8
import yaml
import logging.config
import os

# config.py
def setup_logging(default_path="logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            logging.config.dictConfig(yaml.load(f, Loader=yaml.FullLoader))
    else:
        logging.basicConfig(level=default_level)


setup_logging(default_path="logging.yaml")

logger = logging.getLogger("fileLogger") #实例化的log生成器1
root_logger = logging.getLogger("root") #实例化的log生成器2

```

如此一来，其他模块中要调用logging功能就很简单了

先引用对象`from config import logger`，然后直接`logger.error, root_logger.debug`即可

给出一个demo.py的使用示例

```
from my_logging import logger
from my_logging import root_logger

logger.critical('f1')
logger.error('f2')
logger.warning('f2')
logger.info('f2')
logger.debug('f3')

root_logger.info('r1')
```

详细的YAML配置请参考[《logging模块YAML配置说明》](logging模块YAML配置说明.md)，有和config.py示例配套的配置，可直接拿来用。

## 链接

[日志官网基础教程](https://docs.python.org/zh-cn/3/howto/logging.html)

[日志记录配置详细说明(英文)](https://docs.python.org/zh-cn/3/library/logging.config.html#logging-config-api)

[Python logging模块使用配置文件记录日志](https://blog.csdn.net/langkew/article/details/51553549)


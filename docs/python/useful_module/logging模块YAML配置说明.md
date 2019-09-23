

# logging模块的YAML配置

作者：尹超

日期：2019-9-19

python的logging模块有多种配置方式，可以通过api进行直接配置，也可以通过配置文件的形式进行配置，各有利弊。

通过api进行配置好处是比较简单随意，缺点是配置不方便修改和共用

通过配置文件的形式进行配置的好处在于多模块可以复用相同配置，工程中常使用这种模式

而配置文件常见有两种形式

[`fileConfig()`](https://docs.python.org/zh-cn/3/library/logging.config.html#logging.config.fileConfig)

这种形式已经被淘汰不用了

```
[loggers]
keys=root,log02,log03,log04,log05,log06,log07

[handlers]
keys=hand01,hand02,hand03,hand04,hand05,hand06,hand07,hand08,hand09

[formatters]
keys=form01,form02,form03,form04,form05,form06,form07,form08,form09
```

 [`dictConfig()`](https://docs.python.org/zh-cn/3/library/logging.config.html#logging.config.dictConfig)

```
其一是以json格式的配置
其二是以yaml格式的配置（更简洁）
```

综上，本文统一采用yaml的配置模式

## 1.  YAML配置概览

| key名称                  | 描述                                                         |
| ------------------------ | ------------------------------------------------------------ |
| **version**              | 必选项，其值是一个整数值，表示配置格式的版本，当前唯一可用的值就是1 |
| **formatters**           | 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的格式器名称，value为格式器的配置信息组成的dict，如format和datefmt |
| filters                  | 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的过滤器名称，value为过滤器的配置信息组成的dict，如name |
| **handlers**             | 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的处理器名称，value为处理器的配置信息组成的dcit，如class、level、formatter和filters，其中class为必选项，其它为可选项；其他配置信息将会传递给class所指定的处理器类的构造函数，如下面的handlers定义示例中的stream、filename、maxBytes和backupCount等 |
| loggers                  | 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的日志器名称，value为日志器的配置信息组成的dcit，如level、handlers、filters 和 propagate（yes |
| root                     | 可选项，这是root logger的配置信息，其值也是一个字典对象。除非在定义其它logger时明确指定propagate值为no，否则root logger定义的handlers都会被作用到其它logger上 |
| incremental              | 可选项，默认值为False。该选项的意义在于，如果这里定义的对象已经存在，那么这里对这些对象的定义是否应用到已存在的对象上。值为False表示，已存在的对象将会被重新定义。 |
| disable_existing_loggers | 可选项，默认值为True。该选项用于指定是否禁用已存在的日志器loggers，如果incremental的值为True则该选项 |

官方规定只有version字段是强制配置的，其余全部可以选配

实际使用中，为了便于改动和自定义调整，常常还需配置如下三个字段

- formatters:定义输出格式
- handlers:定义log的过滤和实际输出（是log生成的核心）
- loggers:定义log生成器的名字和属性（与用户需要的log直接相关）

下文重点讲述以上三个字段的配置方法

## 2. formatters配置详解

可以将格式统一成几类并实例化，方便不同格式的输出

format配置：

默认情况下： "%(message)s"，最简单的输出形式，常见定义如下：

```
%(message)s 打印实际log内容（必选）
%(asctime)s 打印时间
%(name)s  打印logger的实例名
%(filename)s: 打印log的文件名
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(funcName)s: 打印函数名
%(levelname)s 打印log等级
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
```

datefmt配置: 

```
%F 显示日期
%T 显示时间
```

实际可用的配置示例：

```
formatters:
  simple:
    format: "%(levelname)s | %(message)s"
  full:
    format: "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    datefmt: #精确控制日期(%F)，时间(%T)的显示
      "%F %T"
```

## 3. handler配置详解

logging自带3个hanlder

- StreamHandler
- FileHandler
- NullHandler（没作用）

还有logging.handlers下的handler类型：

- WatchedFileHandler
- RotatingFileHandler
- TimedRotatingFileHandler

SocketHandler、DatagramHandler、SysLogHandler、NtEventHandler、SMTPHandler、MemoryHandler、HTTPHandler不常用，需要请参考官方文档

主要的配置属性有如下4个：

### class

handler类型定义，上述 

### level

日志级别：CRITICAL、ERROR、WARNING、INFO、DEBUG

### formatter

选择上述自定义好的formatter格式

### filters

可以不用配置

其他配置属性：请参见不同handler定义具体查看，[传送门](https://docs.python.org/zh-cn/3/library/logging.handlers.html#logging.StreamHandler)

给出一个示例

```
handlers:
  console: #可实例化的handler1
    class: logging.StreamHandler
    level: DEBUG
    formatter: full
  info_file_handler: #可实例化的hander2
    class: logging.handlers.RotatingFileHandler
    level: INFO
    formatter: simple
    filename: test.log
    maxBytes: 1024
    backupCount: 1
    encoding: "utf8"
```

## 4. loggers配置

logger为日志器设置具体名称，用户在此指定读取的log来源

root

loggers

需要为日志器指定level, handlers, propagate三个参数

### level 

指定输出的等级，只会输出等于或高于该等级的log

默认有如下5个等级，由高到低。用户亦可以自定义（完全够用了嘛）

```
CRITICAL
ERROR
WARNING
INFO
DEBUG
```

### handlers

决定该log生成器采用前文中哪一个handler配置

### propagate

看不懂的话该参数默认配置为0就好了

`propagate` entry is set to 1 to indicate that messages must propagate to handlers higher up the logger hierarchy from this logger, or 0 to indicate that messages are **not** propagated to handlers up the hierarchy.

意思是propagate有继承的意思，如果使能该参数，则低级别的logger日志会复制到上层logger，有可能会有重复输出，一般意义上需要显示将该参数设置为0

给出一个可用的示例

```
loggers: #默认生成器【不可以自定义】
  my_log: #生成器1，可随意取名字
    level: ERROR
    handlers: [info_file_handler]
    propagate: no
root: #默认生成器【不可以自定义】
  level: DEBUG
  handlers: [console]
  propagate: no
```

## 5. 完整可用YAML配置示例

```
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: "%(levelname)s | %(message)s"
  full:
    format: "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    datefmt:
      "%F %T"

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: full
  info_file_handler:
    class: logging.handlers.RotatingFileHandler
    level: INFO
    formatter: simple
    filename: test.log
    maxBytes: 1024
    backupCount: 1
    encoding: "utf8"

loggers:
  fileLogger:
    level: ERROR
    handlers: [info_file_handler]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
  propagate: no
```

## FAQ

### loggers和handlers中都定义了level，到底以哪一个为准？

很简单，以级别高的为准

### 运行正常，但是报warning?

`YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated,`

经查是YAML5.1标准以后禁止直接load()，需要显示指定load的来源：

```
yaml.load(f) #旧的报错
yaml.load(f, Loader=yaml.FullLoader) #新的没问题
```

## 参考链接

[官网配置说明](https://docs.python.org/zh-cn/3/library/logging.config.html#logging-config-api)

[详解python之配置日志的几种方式](https://www.jb51.net/article/114316.htm)

[logging模块yaml配置](https://blog.csdn.net/qq_15111861/article/details/81739875)


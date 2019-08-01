# python调用shell命令

作者：尹超

日期：2019-7-1

## python执行shell命令

最简单的方式： os.system(cmd_line),例如：

```python
os.system('ls -al')
```

执行要输入密码的shell指令：

```python
import os
passwd = '1234567'
cmd = 'ls -al'
os.system('echo %s | sudo -S %s' % (passwd, cmd))
```

执行一个sh脚本

`os.system('sh close.sh')`

## 查看shell的输出结果

```
#方法1
import os
result = os.system('ls -al')

#方法2
import subprocess
output = subprocess.getoutput("ls -l")
```


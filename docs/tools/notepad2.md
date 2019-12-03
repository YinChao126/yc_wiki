# notepad2安装与默认配置

## keywords

tools, notepad

notepad2是一个比windows自带txt好用的文本编辑器，如何将notepad2设置为默认打开呢？

实现步骤：

1.下载notepad2.exe
2.文本方式编写`notepad2.reg`注册表（粘贴，修改notepad2的路径即可）

粘贴部分：（注意自己的Notepad2.exe路径要修改）

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe]
"Debugger"="\"C:\\Program Files\\Notepad2\\Notepad2.exe\" /z"
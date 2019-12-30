# SSH远程连接与命令控制

作者：尹超

日期：2019-12-30

## keywords

ssh， paramiko

## 描述

有时需要远程登陆其他服务器进行文件或者脚本操作，此时需要SSH连接特性，python有一个paramiko库可以实现SSH登陆和FTP文件操作，直接调用api即可

## paramiko安装

`pip install paramiko`

## ssh client示例

```
# coding=utf-8
import paramiko

class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    #下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print(data.strip())    #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err.strip())     #输出错误结果
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()


if __name__ == "__main__":
    ip = ''
    username = ''
    passwd = ''
    
    conn = SSHConnection(ip, 22, username, passwd)
    localpath = 'hello.txt'
    remotepath = '/home/yc/workspace/test/'
    
#     conn.download(remotepath, localpath)  #下载
#     conn.put(localpath, remotepath) #上传

    # shell命令
    conn.exec_command('pwd') #单条命令
#     conn.exec_command('cd /home/yc/workspace/test;pwd;python test.py;ls') #多条命令
    conn.close()
```

## 参考链接

[SSH与Python模块paramiko](https://www.jianshu.com/p/486dd9993125)


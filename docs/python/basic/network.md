# python获取ip和mac地址

```python
import uuid
import socket

def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

myname = socket.getfqdn(socket.gethostname())#获取本机电脑名
myip = socket.gethostbyname(myname) #获取本机ip
mymac = get_mac_address() #获取本机mac地址
```


# 树莓派无法上网

作者：尹超

日期：2019-11-14

## keywords

linux,  network, raspberry, driver

## 症状

可以ping通公网IP，但是无法解析网页（例如无法百度）

## 可能解决方法

```
sudo vim /etc/resolv.conf

将里面的内容改为
nameserver 8.8.8.8
```


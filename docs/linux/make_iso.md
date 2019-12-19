# Linux系统自定义镜像

作者：尹超

日期：2019-12-19

## keywords

iso, image

## 1. 背景

嵌入式系统开发完毕，可以交付。此时需要将Linux系统完全固化，做成一个装机镜像iso

## 2. 解决方案

利用systemback即可自定义系统镜像了

### 2.1 systemback安装

```
sudo add-apt-repository ppa:nemh/systemback
sudo apt-get update && sudo apt-get install systemback unionfs-fuse
```

### 2.2 systemback使用

- systemback安装成功后在系统左上角的dash中输入systemback即可进入软件
- 直接点击右边的“Live system create”，记得勾选“include the user data files”，然后点击“Create New”傻瓜式等待完成
- 完成后，再点击“Convert to ISO”即可制成装机镜像

## FAQ

A:为什么生成的sblive无法制成ISO镜像？

Q:如果用户数据过多，系统备份如果大于4G，则无法直接一步制成装机镜像，需要解决超过4G镜像请参考[这里](https://blog.csdn.net/bluewhalerobot/article/details/73649272)。

## 参考资料

[systemback制作Ubuntu自己的系统镜像](https://blog.csdn.net/weixin_39871788/article/details/82926696)


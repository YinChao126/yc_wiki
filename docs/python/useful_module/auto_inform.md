# python消息推送机制

作者：尹超

日期：2019-7-3

## 1. 背景

有时候需要一个消息主动推送机制，能够自动告知用户一些信息，比如邮件提醒，天气预警，股票涨停提醒等，在实际项目中这种需求非常普遍。

## 2. 可行方案

通过调研，我发现了至少有如下三种途径可以实现这种需求（以手机推送为目标）

- 发短信
- 发微信
- 第三方自动推送APP

## 3. 短信方案实现

通过python给手机发送短信是一个简单又实用的方式，据我所知，有如下两种方式可以实现短信自动推送的功能。

​	一种是国内各大云厂商（阿里云、华为云等）开启短信推送服务。这种方式的好处一方面是可以大量发送（同时发1000个），另一方面服务稳定。劣势在于审批严格，需要机构证书来申请，个人身份只能申请推送验证码（那有啥用？），服务开启也挺麻烦，云端配置要折腾一番。此外还有一笔费用，大约0.04一条。

​	另一种可以通过第三方机构开启短信推送服务。典型的有twilio，优势在于服务开启非常简单，另外这个是完全免费的！劣势在于你只能发送很有限的几个号码，而且由于一个号码只免费一个月，需要手动换号码，麻烦。如果你想付费，那还挺贵~~~



### 3.1 利用twilio实现短信推送功能

#### 大致思路

- 先python安装twilio： `pip install twilio`
- 再去[官网注册](https://www.twilio.com/login/password)，获取twilio的tocken和API密钥
- 最后根据[twilio tutorial](https://www.twilio.com/docs/sms/send-messages)说明coding即可

也别找tutorial了，此处给出个通信模板照抄即可

```python
from twilio.rest import Client

#getting from your twilio account
twilio_phone = '17222688888' 
account_sid = 'AC2a86478ad53d686b2a9d3bcac1825704'
auth_token = '2b60d878ae361d4db910dcacb2293523'

client = Client(account_sid, auth_token)

def SendMsg(phone_number, msg):
    msg = client.messages.create(
    to='+86'+phone_number,
    from_=twilio_phone,
    body=msg)
    return msg.sid

SendMsg('15811828888','hello,world')
```

是不是简单的要死？还不懂给个[更详细的教程](https://blog.csdn.net/mp624183768/article/details/79905911)

### 3.2 通过阿里云开启短信推送功能

阿里云有官网教程可参考

## 4. 微信方案实现

itchat是一个开源项目，通过itchat可以快速实现微信消息推送功能，简便快捷而且完全免费。缺点是你必须登陆网页端微信（意味着除了手机微信以外，你无法再登陆该账号了，影响使用），其次itchat很慢，而且很容易重复发送或者漏发，用户体验很差（也许是coding时参数没配置好）

#### 大致思路

- 先安装itchat模块， `pip install itchat`
- 直接根据itchat API文档进行coding
- 扫码登陆，运行代码即可

常用功能代码如下

### 4.1 给文件助手发送信息

```
#给文件助手发送一条hello，world
import itchat
itchat.auto_login()
itchat.send('Hello, world', toUserName='filehelper')
```

### 4.2 自动应答

```
#收到什么信息就原样发送回去
import itchat
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login(hotReload=True)
itchat.run()
```

### 4.3 给好友发信息

```
#给张大力发送“你好”
import itchat
itchat.auto_login(hotReload=True)
def Send2Friend(names, msg):
    users = itchat.search_friends(names)
    who = users[0]['UserName']
    itchat.send(msg,toUserName = who)
Send2Friend(u'张大力', '你好')
```

### 4.3 发送文件

```
#给好友发送文件（txt,jpg,mp4是一回事）
import itchat
itchat.auto_login(hotReload=True)
def SendFile(names, file_dir):
    users = itchat.search_friends(names)
    who = users[0]['UserName']
    itchat.send_file(file_dir,toUserName = who)
SendFile(u'张大力','test.jpg')
```

之后可以和图灵测试结合，做一个自动聊天机器人，参考~

相关参考链接如下：

[itchat发送短信的教程](https://segmentfault.com/a/1190000009420701)

[itchat项目官网地址](https://itchat.readthedocs.io/zh/latest/)

[itchat API文档](http://itchat.readthedocs.io/zh/latest/api/)

## 5. 第三方自动推送APP

国外有许多free instant notifications的APP，可以实现消息自动推送功能。我曾经用过一个叫instapush的app，成功实现了自动推送，不过现在好像已经没有了。

google了一下，目测还有[pushover](https://pushover.net/)， [pushed](https://pushed.co/)，[onesignal](https://onesignal.com/)。太多了，给个[链接大全](https://www.businessofapps.com/guide/push-notifications/#1)，有兴趣的话再去研究研究

## 参考链接


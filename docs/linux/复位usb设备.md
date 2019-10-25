# 复位usb设备

作者：尹超

日期：2019-10-24

## 1. 背景

嵌入式开发过程中，尤其是调试过程中可能经常遇到程序运行出错的状况，此时重新插拔一下usb设备，让其清除状态就可以。但是硬件插拔既容易损坏USB接口，又麻烦，能不能找到个纯软件的解决方案呢？

## 2. 解决思路

1. 先根据usb设备信息获取其vendor id（vid）和product id（pid）

2. 然后根据vid和pid查看dmesg消息，找到该usb设备的端口号

3. 最后利用通用的复位命令对其进行复位即可


## 3. 操作步骤

假设你已经知道了该usb设备的vid【直接lsusb就可以看到，实在不知道去问设备供应商】，假设vid=2500

```
1. 输入：dmesg | grep idVendor=2500
可得到如下消息：
[3.049481] usb 2-2.2: New USB device found, idVendor=2500, idProduct=0020

2. 通过正则表达式提取出 2-2.2这个关键usb参数

3. 利用通用usb复位语句实现usb设备的复位过程
sudo sh -c "echo 0 > /sys/bus/usb/devices/2-2.2/authorized"
sudo sh -c "echo 1 > /sys/bus/usb/devices/2-2.2/authorized"
```

## 4. 实操演练

### 4.1 复位指定usb设备（python版本）

```
#reset_usb.py
import re

def get_usb_para(vendor_id):
	# 辅助函数，根据vendor_id获取usb设备挂载在总线上的真实参数
	# 备注：输入必须是str类型的
	pattern = 'idVendor=' + vendor_id
	cmd = 'dmesg | grep %s' % pattern
	log = subprocess.getoutput(cmd).split('\n')
	log = log[-1] #只找最新的记录，防止反复插拔设备导致错误
	pattern = "(?<=usb )([-\d.]+)(?=:)"
	result = re.findall(pattern, log)
	if len(result) > 0:
		return result[0]
	else:
		return 0
		
def reset_usb(vid):
	# 描述：根据vid复位一个usb设备
	# 备注：vid必须是str类型，比如： "07ab"
	usb_para = get_usb_para(vid)
	if isinstance(usb_para, int):
		print("无法复位%s设备" % vid)
	
	cmd_0 = "sh -c \"echo 0 > /sys/bus/usb/devices/%s/authorized\"" % usb_para
	os.system(cmd_0)
	time.sleep(0.25)
	cmd_1 = "sh -c \"echo 1 > /sys/bus/usb/devices/%s/authorized\"" % usb_para
	os.system(cmd_1)
	print("成功复位%s设备" % vid)
	return 0
```

### 4.2 一次性复位所有usb设备（shell版本）

```
for i in /sys/bus/pci/drivers/[uoex]hci_hcd/*:*; do
  [ -e "$i" ] || continue
  echo "${i##*/}" > "${i%/*}/unbind"
  echo "${i##*/}" > "${i%/*}/bind"
done
```

ps：本来我在下面给出的连接中找到了各位大神给出的解决方案以为万事大吉了。结果机器运行到后面还是出了问题，仔细定位还是usb复位逻辑搞错了，没办法又研究了一番，上文已经是本人能给出的最简解决方案。

## 参考连接

[How do you reset a USB device from the command line?](https://askubuntu.com/questions/645/how-do-you-reset-a-usb-device-from-the-command-line)
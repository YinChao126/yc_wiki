# USB硬件设备操作

作者：尹超

日期：2019-7-25

## 背景

经常会碰到硬件检测相关的问题，设备是否正确连接？能否软复位该设备从而避免手动去插拔usb设备。下文的示例程序可以很轻松解决**usb设备状态查询与复位**的问题

## Linux操作usb设备基础命令介绍

linux系统提供了一系列usb设备检测的命令

### 1. lsusb

可以列出当前主机检测到的usb设备，并列出其usb参数，形如：

```
yc@yc:~/dev$ lsusb
Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 002: ID 04f2:b027 Chicony Electronics Co., Ltd Gateway USB 2.0 Webcam
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

其中Bus 007 Device 001就是该usb设备的usb参数(bus id, device id)/(usb总线, 挂载在该总线上的设备号)， ID 1d6b:0001就是usb的(vendor id: product id)/(供应商ID, 产品ID)

lsusb -v可以获取更详细的信息

### 2. dmesg

dmesg是一个重要的用于打印或者控制内核环形缓冲区的命令。环形缓冲区是一种数据结构，它存放着内核操作数据的信息。

运行如下的命令来查看内核操作信息，它同时也会打印出USB设备的信息：

```
[ 1055.720971]  sde: sde4
[ 1055.816921] sd 6:0:0:0: [sde] Attached SCSI removable disk
[ 1168.185175] usb 1-1: USB disconnect, device number 6
[ 1250.915177] usb 1-1: new full-speed USB device number 7 using ohci-pci
[ 1251.361378] usb 1-1: New USB device found, idVendor=8644, idProduct=800b
[ 1251.364410] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[ 1251.367812] usb 1-1: Product: USB Flash Disk               
[ 1251.370072] usb 1-1: Manufacturer: General                      
[ 1251.372505] usb 1-1: SerialNumber: 000000000000C4FC
[ 1251.378864] usb-storage 1-1:1.0: USB Mass Storage device detected
[ 1251.383180] scsi host7: usb-storage 1-1:1.0
[ 1252.415350] scsi 7:0:0:0: Direct-Access     General  USB Flash Disk   1.00 PQ: 0 ANSI: 2
[ 1252.424925] sd 7:0:0:0: Attached scsi generic sg5 type 0
[ 1252.451723] sd 7:0:0:0: [sde] 15669248 512-byte logical blocks: (8.02 GB/7.47 GiB)
[ 1252.481780] sd 7:0:0:0: [sde] Write Protect is off
[ 1252.484715] sd 7:0:0:0: [sde] Mode Sense: 03 00 00 00
[ 1252.507694] sd 7:0:0:0: [sde] No Caching mode page found
[ 1252.510073] sd 7:0:0:0: [sde] Assuming drive cache: write through
```

下文的资源是对上述命令的包装，使得用户可以直接通过usb设备的vendor id来实现相应的需求

## 资源及API描述

本资源应用场景是在linux主机下检查并操控usb硬件设备，提供了如下几个功能：

- is_in_lsusb 查看特定usb设备是否已连接
- find_usb_para 查看特定usb设备的usb参数
- find_com_port 查看一个usb转串口设备的串口号
- reset_usb_device 复位一个特定usb设备

## 源码

```
#coding:utf-8
'''
本模块用以获取usb设备状态并对其进行复位
作者：尹超
更新时间：2019-7-24
'''
import re
import os
import subprocess

def runbash(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out
    

def is_in_lsusb(vendor_id):
    '''
    描述:输入usb设备的vendor_id看lsusb是否有记录，从而判断主机是否已连接该设备
    输入:vendor_id(str) ex:'2500'
    输出:True/False(bool) ex: True
    '''
    lsusb_log = subprocess.getoutput('lsusb')
    result = re.findall(vendor_id, lsusb_log)
    if len(result) > 0:
        return True
    else:
        return False

def find_usb_para(vendor_id):
    '''
    描述:输入usb设备的vendor_id，以元组形式返回usb参数(usb root, device number)
    输入:vendor_id(str) ex:'42b2' 
    输出: 成功->(bus, device_id) ex:('001', '003') 其中001是str类型
          失败->(0, 0)
    '''
    lsusb_log = subprocess.getoutput('lsusb').split('\n')
    for i in range(len(lsusb_log)):
        result = re.findall(vendor_id,lsusb_log[i])
        if len(result) > 0:
            pattern = 'Bus (\d+) Device (\d+)'
            result = re.findall(pattern, lsusb_log[i])
            return result[0]
    return (0,0)

def find_com_port(vendor_id):
    '''
    描述：输入vendor_id，查找该usb转串口设备的串口号
    输入: vendor_id(str)
    输出: 成功 -> port_info(str) ex: 'ttyUSB5'
          失败 -> -1(str)
    '''
    error_output = '-1'
    
    #1. lsusb查到该usb设备的bus root 和device number
    usb_info = find_usb_para(vendor_id)
    if usb_info[0] == 0 and usb_info[1] == 0:
        return error_output 
    usb_root = int(usb_info[0])
    device_number = int(usb_info[1])
    pattern = 'usb ' + str(usb_root) + '-' + str(device_number)
    
    #2. dmesg查到具体usb转串口的信息
    out = subprocess.getoutput('dmesg | grep tty')
    data = out.split('\n')
    
    #3. 正则表达式找出匹配的信息，最终输出
    for i in range(len(data)):
        result = re.findall(pattern,data[i])
        if len(result) > 0:
            #print(data[i]) #得到实际的usb转串口的信息
            comport_info = re.findall('\w+$',data[i]) #筛选ttyUSB*
            return comport_info
    return error_output  
    
def reset_usb_device(vendor_id):
    '''
    描述：输入vendor_id，实现该usb设备的软复位
    输入:vendor_id(str)
    '''
    usb_para = find_usb_para(vendor_id)
    if usb_para[0] == 0 and usb_para[1] == 0:
        print('error! cannot reset %s' % vendor_id)
        return
    
    sub_dirs = []
    path='/sys/bus/usb/devices/'
    dev_num = int(usb_para[1])
    if (dev_num == 0):
        return 0
    for root, dirs, files in os.walk(path):
            for name in dirs:
                    sub_dirs.append(os.path.join(root, name))

    dev_found = 0
    for sub_dir in sub_dirs:
            if True == os.path.isfile(sub_dir+'/devnum'):
                    fd = open(sub_dir+'/devnum','r')
                    line = fd.readline()
                    if int(dev_num) == int(line):
                            #print ('Your device is at: '+sub_dir)
                            dev_found = 1
                            break
                    fd.close()

    if dev_found == 1:
            reset_file = sub_dir+'/authorized'
            runbash('echo 0 > '+reset_file) 
            runbash('echo 1 > '+reset_file) 
            print ('Device %s reset successful' % vendor_id)

    else:
            print ("No such device")

```

## 参考链接




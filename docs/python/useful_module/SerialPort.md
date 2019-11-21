# 串口通信示例程序

作者：尹超

日期：2018-5-22

说明：直接import serial模块即可

```
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:29:51 2018

@author: Administrator
"""
#串口接收并回传
import time
import serial  
try:
    ser=serial.Serial("COM2",9600,timeout=None) #此处的timeout默认值0.5
    print('com2 opened!')
    rec_num = 0
    fo = open("data.txt", "w")
        
except:
    print('error, com2 has already opened!')
    ser.close()

while 1:
    a = ser.in_waiting()
    if a > 0:
        content = ser.read_all()
        #content = self.ser.readline()#按行读取
        a = str(content, encoding = "utf-8") #bytes to string
        fo.write(a)
        rec_num = rec_num + len(content)
        print(rec_num)
    if rec_num > 100:
        fo.close()
        break
#        ser.write(content) #回写

if ser.is_open == True: #关闭逻辑
    ser.close() 
```

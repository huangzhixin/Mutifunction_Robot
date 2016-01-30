# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2014-10-19 
* Discribe : 机器人类
"""

import serial
import time

class Robot:
  def __init__(self):
      self.ser = serial.Serial('/dev/ttyACM0', 9600)
      self.Stand()
  
  def Stand(self):
      cmd1 = "#1P1500#2P1700#3P2300#4P1500#5P1500#6P1300#7P700#8P1500#9P1500#10P1500#11P1500#12P1500#13P1500#14P1500#15P1500#16P1500#17P1500#18P2300#19P1700#20P1500#21P1500#22P700#23P1300#24P1500T1000\r\n"
      self.ser.write(cmd1)
      time.sleep(0.5)
  
  def StartForward(self):
      cmd1 = "#1P1500#2P2100#3P1611#4P1211#5P1500#6P1500#7P700#8P1500#9P1500#10P1500#11P1500#12P1500#13P1500#14P1500#15P1500#16P1500#17P1500#18P2300#19P1500#20P1500#21P1789#22P1389#23P900#24P1500T1000\r\n" 
      cmd2 = "#1P1700#5P1300#20P1367#24P1633T1000\r\n"
      cmd3 = "#2P2300#3P1189#4P1011T1000\r\n" 
      self.ser.write(cmd1)
      time.sleep(0.5)
      self.ser.write(cmd2)
      time.sleep(0.5)
      self.ser.write(cmd3)
      time.sleep(0.5)

if __name__ == "__main__":
   huang = Robot()
   while(1):
     var = input("打开开关，按任意键继续: ")
     if var:	   
       break
   huang.StartForward()
   print "end"
  

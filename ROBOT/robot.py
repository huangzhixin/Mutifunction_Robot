# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2015-2-8 
* Discribe : 机器人类
"""

import serial
import time
import globalvariable
from devo import Devo 
from head import Head
from armleft import ArmLeft
from armright import ArmRight
from legleft import LegLeft
from legright import LegRight
from threading import Thread
import socketserver as Socket
from xmlmovement import XmlMovement

class Robot:
  def __init__(self):
      self.ip="192.168.10.1"
      self.port=9988
      self.socket = Thread(target=Socket.InitSocketServer,args=[self.ip,self.port])
      self.socket.setDaemon(1)
      self.socket.start()
      self.ser = serial.Serial('/dev/ttyAMA0', 9600)
      self.head = Head() 
      self.armleft = ArmLeft()
      self.armright = ArmRight()
      self.legleft = LegLeft()
      self.legright = LegRight()
      self.Action()
      print "creat a robot"
   
  def Renew(self):
      result=[]
      for i in self.head.Renew():
        result.append(i) 
      for i in self.armleft.Renew():
        result.append(i) 
      for i in self.armright.Renew():
        result.append(i)
      for i in self.legleft.Renew():
        result.append(i)
      for i in self.legright.Renew():
        result.append(i)
      return result

  def CreatCMD(self,time):
      cmdArray = self.Renew()
      if(self.Judge(cmdArray)):
        string=""
        for i in cmdArray:
          string+="#"+str(i[0])+"P"+str(i[1])
        string+="T"+str(time)+"\r\n" 
        #print string
        return string
      else:
        #print "Commder ist not illigo" 
        return ""   
  
  def Judge(self, cmdArray):
      if(len(cmdArray)):
        return 1
      else:
        return 0

  def Action(self,time):
      cmd=self.CreatCMD(time)
      if(cmd):
        print "action this commder: "+cmd
        self.ser.write(cmd)
  def Movement(self, move):
      xml=XmlMovement(move)
      for i in range(0,len(xml.moves)-1):
        move=xml.getmovement(i)
        self.legleft.SetValue(move[0][0],move[0][1],move[0][2],move[0][3],move[0][4])
        self.legright.SetValue(move[1][0],move[1][1],move[1][2],move[1][3],move[1][4])
        self.armleft.SetValue(move[2][0],move[2][1],move[2][2])
        self.armright.SetValue(move[3][0],move[3][1],move[3][2])
        T=move[4]
        self.Action(T)
        time.sleep(float(T)/1000)
        
      
if __name__ == "__main__":
   huang = Robot()
   while 1:
     time.sleep(0.1)
     if(globalvariable.socketflag=='true'):     #如果有新的消息接收
        print globalvariable.socketbuf
        if(globalvariable.socketbuf=="forward"):
          huang.Movement("forward")
        else:
          huang.head.SetRelativeValue(globalvariable.socketbuf)
          huang.Action(100)
        globalvariable.socketflag='false'       #接受消息后设置为已读
     #huang.head.HeadLockenTarget(1)
     #huang.Action()	
"""
   huang.head.SetValue(1200,700)   
   huang.armleft.SetValue(1500,600,1500) 
   huang.armright.SetValue(1500,2400,1500)
   huang.legleft.SetValue(1500,600,650,2450,1500)
   huang.legright.SetValue(1500,2400,2350,550,1500)
   huang.Action(1000)
   huang.head.SetRelativeValue("H1U30H2L50")
   huang.armleft.SetRelativeValue("AL1B500AL2L100AL3L500")
   huang.armright.SetRelativeValue("AR1F500AR2R100AR3R500")
   huang.legleft.SetRelativeValue("LL1R200LL3B50LL4F50LL5R1100")
   huang.legright.SetRelativeValue("LR1L200LR2B400LR4F50LR5L1000")
   huang.Action(1000)
"""

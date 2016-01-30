# -*- coding: utf-8 -*-
"""
* Author：黄志新
* Create Date：2015-2-8
* Discribe : 舵机类
"""



class Devo:
  def __init__(self,num,value=1500):
      self.value=value
      self.num=num
      self.flag="true"

  def SetValue(self,value):
      if(self.flag == "false"):
         self.value=value
         self.flag = "true"
      else:
         print "Devo"+str(self.num)+" can not change!"
  
  def GetValueAndFlag(self):
      return [self.value,self.flag]
  
  def SetFalse(self):
      self.flag="false"
  
  def GetNum(self):
      return self.num
  
  def GetValue(self):
      return self.value

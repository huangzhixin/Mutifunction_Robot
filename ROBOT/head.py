# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2015-2-8 
* Discribe : 头类
"""

from devo import Devo 
from eye import Eye

class Head:
  def __init__(self):
      self.head1 = Devo(10,1350)
      self.head2 = Devo(9,1500)
      self.eye =Eye("192.168.10.1")
      print "creat a head"

  def IsOutRange(self, value1,value2):
      pass

  def SetRelativeValue(self,string):
      H1R=string[string.find("H1")+2]
      H1V=""
      for i in range(string.find("H1")+3,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          H1V+=string[i]
        else:
          break
      if(H1R == "U" and 1100<=self.head1.GetValue()-int(H1V)):
         self.head1.SetValue(self.head1.GetValue()-int(H1V))

      if(H1R == "D" and self.head1.GetValue()+int(H1V)<=1600):
         self.head1.SetValue(self.head1.GetValue()+int(H1V))

      H2R=string[string.find("H2")+2]
      H2V=""
      for i in range(string.find("H2")+3,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          H2V+=string[i]
        else:
          break
      if(H2R == "L" and 500<=self.head2.GetValue()-int(H2V)):
         self.head2.SetValue(self.head2.GetValue()-int(H2V))

      if(H2R == "R" and self.head2.GetValue()-int(H2V)<=2500):
         self.head2.SetValue(self.head2.GetValue()+int(H2V))

  def SetValue(self,value1,value2):
      if(str(value1).isdigit()and 1100<=value1<=1600):
        self.head1.SetValue(value1)
      if(str(value2).isdigit()and 500<=value2<=2500):
        self.head2.SetValue(value2)

  def GetValueAndFlag(self):
      return [self.head1.GetValueAndFlag(),self.head2.GetValueAndFlag()]

  def Renew(self):
      result = self.GetValueAndFlag()
      result1 = []
      if(result[0][1] == "true"):
        result1.append([self.head1.GetNum(),result[0][0]])
        self.head1.SetFalse()
      if(result[1][1] == "true"):
        result1.append([self.head2.GetNum(),result[1][0]])
        self.head2.SetFalse()
      return result1

  def HeadLockenTarget(self, Parameters):
		cmd=self.eye.LockForHead(Parameters)
		if(cmd):
		  self.SetRelativeValue(cmd)

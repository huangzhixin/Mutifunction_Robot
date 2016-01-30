# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2015-2-9 
* Discribe : 右胳膊类
"""

from devo import Devo 

class ArmRight:
  def __init__(self):
      self.ArmRight1 = Devo(17,1500)
      self.ArmRight2 = Devo(18,2400)
      self.ArmRight3 = Devo(19,1500)
      print "creat a right arm"
  def IsOutRange(self, Value1,Value2,Value3):
      pass

  def SetRelativeValue(self,string):
      AR1R = string[string.find("AR1")+3]
      AR1V=""
      for i in range(string.find("AR1")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          AR1V+=string[i]
        else:
          break
      if(AR1R == "F" and 500<=self.ArmRight1.GetValue()-int(AR1V)):
         self.ArmRight1.SetValue(self.ArmRight1.GetValue()-int(AR1V))

      if(AR1R == "B" and self.ArmRight1.GetValue()+int(AR1V)<=2500):
         self.ArmRight1.SetValue(self.ArmRight1.GetValue()+int(AR1V))

      AR2R = string[string.find("AR2")+3]
      AR2V=""
      for i in range(string.find("AR2")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          AR2V+=string[i]
        else:
          break
      if(AR2R == "R" and 500<=self.ArmRight2.GetValue()-int(AR2V)):
         self.ArmRight2.SetValue(self.ArmRight2.GetValue()-int(AR2V))

      if(AR2R == "L" and self.ArmRight2.GetValue()+int(AR2V)<=2400):
         self.ArmRight2.SetValue(self.ArmRight2.GetValue()+int(AR2V))

      AR3R = string[string.find("AR3")+3]
      AR3V=""
      for i in range(string.find("AR3")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          AR3V+=string[i]
        else:
          break
      if(AR3R == "R" and 500<=self.ArmRight3.GetValue()-int(AR3V)):
         self.ArmRight3.SetValue(self.ArmRight3.GetValue()-int(AR3V))

      if(AR3R == "L" and self.ArmRight3.GetValue()+int(AR3V)<=2350):
         self.ArmRight3.SetValue(self.ArmRight3.GetValue()+int(AR3V))

  def SetValue(self,value1,value2,value3):
      if(str(value1).isdigit()and 500<=value1<=2500):
        self.ArmRight1.SetValue(value1)
      if(str(value2).isdigit()and 500<=value2<=2400):
        self.ArmRight2.SetValue(value2)
      if(str(value3).isdigit()and 500<=value3<=2350):
        self.ArmRight3.SetValue(value3)
  
  def GetValueAndFlag(self):
      return [self.ArmRight1.GetValueAndFlag(),self.ArmRight2.GetValueAndFlag(),self.ArmRight3.GetValueAndFlag()]

  def Renew(self):
      result = self.GetValueAndFlag()
      result1 = []
      if(result[0][1] == "true"):
        result1.append([self.ArmRight1.GetNum(),result[0][0]])
        self.ArmRight1.SetFalse()
      if(result[1][1] == "true"):
        result1.append([self.ArmRight2.GetNum(),result[1][0]])
        self.ArmRight2.SetFalse()
      if(result[2][1] == "true"):
        result1.append([self.ArmRight3.GetNum(),result[2][0]])
        self.ArmRight3.SetFalse()
      return result1

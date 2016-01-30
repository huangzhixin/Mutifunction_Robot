# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2015-2-9 
* Discribe : 左胳膊类
"""

from devo import Devo 

class ArmLeft:
  def __init__(self):
      self.ArmLeft1 = Devo(8,1500)
      self.ArmLeft2 = Devo(7,600)
      self.ArmLeft3 = Devo(6,1500)
      print "creat a left arm"

  def IsOutRange(self, value1,value2,value3):
      pass

  def SetRelativeValue(self,string):
      AL1R = string[string.find("AL1")+3]
      AL1V=""
      for i in range(string.find("AL1")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          AL1V+=string[i]
        else:
          break
      if(AL1R == "B" and 500<=self.ArmLeft1.GetValue()-int(AL1V)):
         self.ArmLeft1.SetValue(self.ArmLeft1.GetValue()-int(AL1V))

      if(AL1R == "F" and self.ArmLeft1.GetValue()+int(AL1V)<=2500):
         self.ArmLeft1.SetValue(self.ArmLeft1.GetValue()+int(AL1V))

      AL2R = string[string.find("AL2")+3]
      AL2V=""
      for i in range(string.find("AL2")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          AL2V+=string[i]
        else:
          break
      if(AL2R == "R" and 600<=self.ArmLeft2.GetValue()-int(AL2V)):
         self.ArmLeft2.SetValue(self.ArmLeft2.GetValue()-int(AL2V))

      if(AL2R == "L" and self.ArmLeft2.GetValue()+int(AL2V)<=2500):
         self.ArmLeft2.SetValue(self.ArmLeft2.GetValue()+int(AL2V))

      AL3R = string[string.find("AL3")+3]
      AL3V=""
      for i in range(string.find("AL3")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          AL3V+=string[i]
        else:
          break
      if(AL3R == "R" and 650<=self.ArmLeft3.GetValue()-int(AL3V)):
         self.ArmLeft3.SetValue(self.ArmLeft3.GetValue()-int(AL3V))

      if(AL3R == "L" and self.ArmLeft3.GetValue()+int(AL3V)<=2500):
         self.ArmLeft3.SetValue(self.ArmLeft3.GetValue()+int(AL3V))

  def SetValue(self,value1,value2,value3):
      if(str(value1).isdigit()and 500<=value1<=2500):
        self.ArmLeft1.SetValue(value1)
      if(str(value2).isdigit()and 600<=value2<=2500):
        self.ArmLeft2.SetValue(value2)
      if(str(value3).isdigit()and 650<=value3<=2500):
        self.ArmLeft3.SetValue(value3)
  
  def GetValueAndFlag(self):
      return [self.ArmLeft1.GetValueAndFlag(),self.ArmLeft2.GetValueAndFlag(),self.ArmLeft3.GetValueAndFlag()]

  def Renew(self):
      result = self.GetValueAndFlag()
      result1 = []
      if(result[0][1] == "true"):
        result1.append([self.ArmLeft1.GetNum(),result[0][0]])
        self.ArmLeft1.SetFalse()
      if(result[1][1] == "true"):
        result1.append([self.ArmLeft2.GetNum(),result[1][0]])
        self.ArmLeft2.SetFalse()
      if(result[2][1] == "true"):
        result1.append([self.ArmLeft3.GetNum(),result[2][0]])
        self.ArmLeft3.SetFalse()
      return result1

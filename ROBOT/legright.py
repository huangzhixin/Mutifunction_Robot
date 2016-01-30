# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2015-2-10 
* Discribe : 左腿类
"""

from devo import Devo 

class LegRight:
  def __init__(self):
      self.LegRight1 = Devo(20,1500)
      self.LegRight2 = Devo(21,2400)
      self.LegRight3 = Devo(22,2350)
      self.LegRight4 = Devo(23,550)
      self.LegRight5 = Devo(24,1500)
      print "creat a right leg"

  def IsOutRange(self, value1,value2,value3,value4,value5):
      pass
  
  def SetRelativeValue(self,string):
      LR1R = string[string.find("LR1")+3]
      LR1V=""
      for i in range(string.find("LR1")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LR1V+=string[i]
        else:
          break
      if(LR1R == "L" and 1300<=self.LegRight1.GetValue()-int(LR1V)):
         self.LegRight1.SetValue(self.LegRight1.GetValue()-int(LR1V))

      if(LR1R == "R" and self.LegRight1.GetValue()+int(LR1V)<=2500):
         self.LegRight1.SetValue(self.LegRight1.GetValue()+int(LR1V))

      LR2R = string[string.find("LR2")+3]
      LR2V=""
      for i in range(string.find("LR2")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LR2V+=string[i]
        else:
          break
      if(LR2R == "B" and 500<=self.LegRight2.GetValue()-int(LR2V)):
         self.LegRight2.SetValue(self.LegRight2.GetValue()-int(LR2V))

      if(LR2R == "F" and self.LegRight2.GetValue()+int(LR2V)<=2500):
         self.LegRight2.SetValue(self.LegRight2.GetValue()+int(LR2V))

      LR3R = string[string.find("LR3")+3]
      LR3V=""
      for i in range(string.find("LR3")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LR3V+=string[i]
        else:
          break
      if(LR3R == "F" and 500<=self.LegRight3.GetValue()-int(LR3V)):
         self.LegRight3.SetValue(self.LegRight3.GetValue()-int(LR3V))

      if(LR3R == "B" and self.LegRight3.GetValue()+int(LR3V)<=2500):
         self.LegRight3.SetValue(self.LegRight3.GetValue()+int(LR3V))

      LR4R = string[string.find("LR4")+3]
      LR4V=""
      for i in range(string.find("LR4")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LR4V+=string[i]
        else:
          break
      if(LR4R == "F" and 500<=self.LegRight4.GetValue()-int(LR4V)):
         self.LegRight4.SetValue(self.LegRight4.GetValue()-int(LR4V))

      if(LR4R == "B" and self.LegRight4.GetValue()+int(LR4V)<=2500):
         self.LegRight4.SetValue(self.LegRight4.GetValue()+int(LR4V))

      LR5R = string[string.find("LR5")+3]
      LR5V=""
      for i in range(string.find("LR5")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LR5V+=string[i]
        else:
          break
      if(LR5R == "L" and 500<=self.LegRight5.GetValue()-int(LR5V)):
         self.LegRight5.SetValue(self.LegRight5.GetValue()-int(LR5V))

      if(LR5R == "R" and self.LegRight5.GetValue()+int(LR5V)<=1900):
         self.LegRight5.SetValue(self.LegRight5.GetValue()+int(LR5V))

  def SetValue(self,value1,value2,value3,value4,value5):
      if(str(value1).isdigit()and 1300<=value1<=2500):
        self.LegRight1.SetValue(value1)
      if(str(value2).isdigit()and 500<=value2<=2500):
        self.LegRight2.SetValue(value2)
      if(str(value3).isdigit()and 500<=value3<=2500):
        self.LegRight3.SetValue(value3)
      if(str(value4).isdigit()and 500<=value4<=2500):
        self.LegRight4.SetValue(value4)
      if(str(value5).isdigit()and 500<=value5<=1900):
        self.LegRight5.SetValue(value5)

  def GetValueAndFlag(self):
      return [self.LegRight1.GetValueAndFlag(),self.LegRight2.GetValueAndFlag(),self.LegRight3.GetValueAndFlag(),self.LegRight4.GetValueAndFlag(),self.LegRight5.GetValueAndFlag()]

  def Renew(self):
      result = self.GetValueAndFlag()
      result1 = []
      if(result[0][1] == "true"):
        result1.append([self.LegRight1.GetNum(),result[0][0]])
        self.LegRight1.SetFalse()
      if(result[1][1] == "true"):
        result1.append([self.LegRight2.GetNum(),result[1][0]])
        self.LegRight2.SetFalse()
      if(result[2][1] == "true"):
        result1.append([self.LegRight3.GetNum(),result[2][0]])
        self.LegRight3.SetFalse()
      if(result[3][1] == "true"):
        result1.append([self.LegRight4.GetNum(),result[3][0]])
        self.LegRight4.SetFalse()
      if(result[4][1] == "true"):
        result1.append([self.LegRight5.GetNum(),result[4][0]])
        self.LegRight5.SetFalse()
      return result1

# -*- coding: utf-8 -*-
"""
* Author：黄志新 
* Create Date：2015-2-10 
* Discribe : 左腿类
"""

from devo import Devo 

class LegLeft:
  def __init__(self):
      self.LegLeft1 = Devo(5,1500)
      self.LegLeft2 = Devo(4,600)
      self.LegLeft3 = Devo(3,650)
      self.LegLeft4 = Devo(2,2450)
      self.LegLeft5 = Devo(1,1500)
      print "creat a left leg"

  def IsOutRange(self, value1,value2,value3,value4,value5):
      pass
  
  def SetRelativeValue(self,string):
      LL1R = string[string.find("LL1")+3]
      LL1V=""
      for i in range(string.find("LL1")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LL1V+=string[i]
        else:
          break
      if(LL1R == "L" and 500<=self.LegLeft1.GetValue()-int(LL1V)):
         self.LegLeft1.SetValue(self.LegLeft1.GetValue()-int(LL1V))

      if(LL1R == "R" and self.LegLeft1.GetValue()+int(LL1V)<=1700):
         self.LegLeft1.SetValue(self.LegLeft1.GetValue()+int(LL1V))

      LL2R = string[string.find("LL2")+3]
      LL2V=""
      for i in range(string.find("LL2")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LL2V+=string[i]
        else:
          break
      if(LL2R == "F" and 500<=self.LegLeft2.GetValue()-int(LL2V)):
         self.LegLeft2.SetValue(self.LegLeft2.GetValue()-int(LL2V))

      if(LL2R == "B" and self.LegLeft2.GetValue()+int(LL2V)<=2500):
         self.LegLeft2.SetValue(self.LegLeft2.GetValue()+int(LL2V))

      LL3R = string[string.find("LL3")+3]
      LL3V=""
      for i in range(string.find("LL3")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LL3V+=string[i]
        else:
          break
      if(LL3R == "B" and 500<=self.LegLeft3.GetValue()-int(LL3V)):
         self.LegLeft3.SetValue(self.LegLeft3.GetValue()-int(LL3V))

      if(LL3R == "F" and self.LegLeft3.GetValue()+int(LL3V)<=2500):
         self.LegLeft3.SetValue(self.LegLeft3.GetValue()+int(LL3V))

      LL4R = string[string.find("LL4")+3]
      LL4V=""
      for i in range(string.find("LL4")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LL4V+=string[i]
        else:
          break
      if(LL4R == "B" and 500<=self.LegLeft4.GetValue()-int(LL4V)):
         self.LegLeft4.SetValue(self.LegLeft4.GetValue()-int(LL4V))

      if(LL4R == "F" and self.LegLeft4.GetValue()+int(LL4V)<=2500):
         self.LegLeft4.SetValue(self.LegLeft4.GetValue()+int(LL4V))

      LL5R = string[string.find("LL5")+3]
      LL5V=""
      for i in range(string.find("LL5")+4,len(string)):
        if(string[i].isdigit()):
          #print string[i]  
          LL5V+=string[i]
        else:
          break
      if(LL5R == "L" and 1100<=self.LegLeft5.GetValue()-int(LL5V)):
         self.LegLeft5.SetValue(self.LegLeft5.GetValue()-int(LL5V))

      if(LL5R == "R" and self.LegLeft5.GetValue()+int(LL5V)<=2500):
         self.LegLeft5.SetValue(self.LegLeft5.GetValue()+int(LL5V))

  def SetValue(self,value1,value2,value3,value4,value5):
      if(str(value1).isdigit()and 500<=value1<=1700):
        self.LegLeft1.SetValue(value1)
      if(str(value2).isdigit()and 500<=value2<=2500):
        self.LegLeft2.SetValue(value2)
      if(str(value3).isdigit()and 500<=value3<=2500):
        self.LegLeft3.SetValue(value3)
      if(str(value4).isdigit()and 500<=value4<=2500):
        self.LegLeft4.SetValue(value4)
      if(str(value5).isdigit()and 1100<=value5<=2500):
        self.LegLeft5.SetValue(value5)

  def GetValueAndFlag(self):
      return [self.LegLeft1.GetValueAndFlag(),self.LegLeft2.GetValueAndFlag(),self.LegLeft3.GetValueAndFlag(),self.LegLeft4.GetValueAndFlag(),self.LegLeft5.GetValueAndFlag()]

  def Renew(self):
      result = self.GetValueAndFlag()
      result1 = []
      if(result[0][1] == "true"):
        result1.append([self.LegLeft1.GetNum(),result[0][0]])
        self.LegLeft1.SetFalse()
      if(result[1][1] == "true"):
        result1.append([self.LegLeft2.GetNum(),result[1][0]])
        self.LegLeft2.SetFalse()
      if(result[2][1] == "true"):
        result1.append([self.LegLeft3.GetNum(),result[2][0]])
        self.LegLeft3.SetFalse()
      if(result[3][1] == "true"):
        result1.append([self.LegLeft4.GetNum(),result[3][0]])
        self.LegLeft4.SetFalse()
      if(result[4][1] == "true"):
        result1.append([self.LegLeft5.GetNum(),result[4][0]])
        self.LegLeft5.SetFalse()
      return result1

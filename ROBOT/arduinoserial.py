# -*- coding: utf-8 -*-
import serial
import time
ser = serial.Serial('/dev/ttyUSB1', 9600)

def SringRead():
   string=ser.readline()
   return string

def StringWrite(string):
   ser.write(string)

def main():
  while(1):
     var = input("Enter string: ")
     if not var:	   
        continue
     StringWrite(var)
     time.sleep(0.5)
     result=SringRead()
     if result:
        print result
  
	
if __name__ == "__main__":
     main()



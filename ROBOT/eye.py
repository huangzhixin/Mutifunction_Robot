# -*- coding: utf-8 -*-
"""
* Author：黄志新
* Create Date：2015-2-10
* Discribe : 眼睛类
"""

import urllib
import time 
import cv2
import socket

class Eye:
  def __init__(self,address):
      self.address = address
      self.html = self.GetHtml("http://"+self.address+"/index.html")
      str1='haarcascade_frontalface_default.xml'
      str2='cascade.xml'
      str3='apple.xml'
      self.face_cascade = cv2.CascadeClassifier(str1)
      #self.cap = cv2.VideoCapture(0)
      self.GetImg()
      img = cv2.imread('1.jpg',3)
      self.x= img.shape[1]
      self.y= img.shape[0]
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
      self.sock.connect(('192.168.10.1',9988))

      self.num=0  
      self.test=[]
      
  def GetHtml(self,url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

  def GetImg(self):
    urllib.urlretrieve("http://"+self.address+":8001/?action=snapshot","1.jpg")

  def Snapshot(self,isGary="no"):
    self.GetImg()
    if(isGary == "no"):
      img = cv2.imread('1.jpg',3)
    else:
      img = cv2.imread('1.jpg',3)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return img

  def Display(self,isGary="no",isDetect="yes",isDispLay="yes"):
    while 1:
      img = self.Snapshot(isGary)
      if(isDetect == "yes"):
        img = self.Detect(img)
        cmd=self.LockForHead(1)
        if(cmd):
          print cmd
          self.sock.send(cmd)
          print self.sock.recv(12)
      if(isDispLay == "yes"):
        cv2.circle(img,(int(0.5*self.x),int(0.5*self.y)),4,(0,255,0),2)
        cv2.imshow("Image", img)
        if cv2.waitKey(10) == 27:
          cv2.destroyAllWindows()
          break

  def FaceRecognize(self,img):
    faces = self.face_cascade.detectMultiScale(img, 1.1, 3,1) #http://docs.opencv.org/2.4.10/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale#cv2.CascadeClassifier.detectMultiScale
    return faces

  def Detect(self,img):
    faces = self.FaceRecognize(img)
    #print self.faces
    self.Track(faces)
    for (x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
      cv2.circle(img,(x+int(0.5*w),int(y+0.5*h)),2,(255,0,0),5)
    return img

  def Track(self,faces):
    if(len(faces)):
      (x,y,w,h) = faces[0]
      target = (x+int(0.5*w),int(y+0.5*h))
      ziel = (int(0.5*self.x),int(0.5*self.y))
      x=target[0]-ziel[0]
      y=target[1]-ziel[1]
      #print [x,y]
      return [x,y]
      
  def LockForHead(self,Parameters):
    img = self.Snapshot("no")
    faces = self.FaceRecognize(img)
    if(len(faces)):
      camerexy = self.Track(faces)
      self.num+=1
      self.test.append(camerexy)
      if(self.num%10==0):
        self.Test()
      devoX = Parameters*camerexy[0]
      devoY = Parameters*camerexy[1]
      if(devoX<0 and devoY<0):
        return "H1U"+str(abs(devoY))+"H2R"+str(abs(devoX))
      if(devoX>0 and devoY<0):
        return "H1U"+str(abs(devoY))+"H2L"+str(abs(devoX))
      if(devoX<0 and devoY>0):
        return "H1D"+str(abs(devoY))+"H2R"+str(abs(devoX))
      if(devoX>0 and devoY>0):
        return "H1D"+str(abs(devoY))+"H2L"+str(abs(devoX))
  def Test(self):
      f=file("testdata.txt","a+")
      for i in self.test:
         f.writelines(str(i[0])+"	"+str(i[1])+"\n")
      self.test[:]=[]
if __name__ == "__main__":

  huang=Eye("192.168.10.1")
  huang.Display("no","yes","yes")
  #while(1):
    #print huang.LockForHead(10)


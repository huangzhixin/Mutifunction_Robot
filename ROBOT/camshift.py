# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
* Author：黄志新
* Create Date：2015-2-10
* Discribe : 眼睛类
"""

import urllib
import time 
import cv2
import socket
import numpy as np


class Eye:
    def __init__(self,address):
        self.address = address
        self.html = self.GetHtml("http://"+self.address+"/index.html")
        cv2.namedWindow('camshift')
        cv2.setMouseCallback('camshift', self.onmouse)

        self.selection = None
        self.drag_start = None
        self.tracking_state = 0
        self.show_backproj = False
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

    def onmouse(self, event, x, y, flags, param):
        x, y = np.int16([x, y]) # BUG
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
            self.tracking_state = 0
            flags=1
        if self.drag_start:
            if flags & cv2.EVENT_FLAG_LBUTTON:
                h, w = self.frame.shape[:2]
                xo, yo = self.drag_start
                x0, y0 = np.maximum(0, np.minimum([xo, yo], [x, y]))
                x1, y1 = np.minimum([w, h], np.maximum([xo, yo], [x, y]))
                self.selection = None
                if x1-x0 > 0 and y1-y0 > 0:
                    self.selection = (x0, y0, x1, y1)
            else:
                self.drag_start = None
                if self.selection is not None:
                    self.tracking_state = 1

    def show_hist(self):
        bin_count = self.hist.shape[0]
        bin_w = 24
        img = np.zeros((256, bin_count*bin_w, 3), np.uint8)
        for i in xrange(bin_count):
            h = int(self.hist[i])
            cv2.rectangle(img, (i*bin_w+2, 255), ((i+1)*bin_w-2, 255-h), (int(180.0*i/bin_count), 255, 255), -1)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        cv2.imshow('hist', img)
    def Track(self,target):
        
        if(target):
          print target
          ziel = (int(0.5*self.x),int(0.5*self.y))   #摄像头中心点坐标
          x=target[0]-ziel[0]
          y=target[1]-ziel[1]
          #print [x,y]
        return [x,y]      #返回离中心点的相对距离
    def LockForHead(self,Parameters,target):
        camerexy=self.Track(target)
        if(camerexy):
          
          devoX = int(Parameters*camerexy[0])
          devoY = int(Parameters*camerexy[1])
          if(devoX<0 and devoY<0):
            return "H1U"+str(abs(devoY))+"H2R"+str(abs(devoX))
          if(devoX>0 and devoY<0):
            return "H1U"+str(abs(devoY))+"H2L"+str(abs(devoX))
          if(devoX<0 and devoY>0):
            return "H1D"+str(abs(devoY))+"H2R"+str(abs(devoX))
          if(devoX>0 and devoY>0):
            return "H1D"+str(abs(devoY))+"H2L"+str(abs(devoX))
    
    def run(self):
        while True:
            self.frame = self.Snapshot()
            vis = self.frame.copy()
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

            if self.selection:
                x0, y0, x1, y1 = self.selection
                self.track_window = (x0, y0, x1-x0, y1-y0)
                hsv_roi = hsv[y0:y1, x0:x1]
                mask_roi = mask[y0:y1, x0:x1]
                hist = cv2.calcHist( [hsv_roi], [0], mask_roi, [16], [0, 180] )
                cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX);
                self.hist = hist.reshape(-1)
                self.show_hist()

                vis_roi = vis[y0:y1, x0:x1]
                cv2.bitwise_not(vis_roi, vis_roi)
                vis[mask == 0] = 0

            if self.tracking_state == 1:
                self.selection = None
                prob = cv2.calcBackProject([hsv], [0], self.hist, [0, 180], 1)
                prob &= mask
                term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
                track_box, self.track_window = cv2.CamShift(prob, self.track_window, term_crit)
                #print track_box
                if self.show_backproj:
                    vis[:] = prob[...,np.newaxis]

                #cmd=self.targetTrack(1,track_box[0])
                cmd=self.LockForHead(1.2,track_box[0])
                if(cmd):
                   print cmd
                   self.sock.send(cmd)
                   print self.sock.recv(12)
                cv2.circle(vis,(int(track_box[0][0]),int(track_box[0][1])),15,(0,255,0),2)
                cv2.circle(vis,(int(0.5*self.x),int(0.5*self.y)),4,(0,255,0),2)
                #try: cv2.ellipse(vis, track_box, (0, 0, 255), 2)    
                #except: print "asd"
            
            cv2.imshow('camshift', vis)

            ch = 0xFF & cv2.waitKey(5)
            if ch == 27:
                break
            if ch == ord('b'):
                self.show_backproj = not self.show_backproj
        cv2.destroyAllWindows()


if __name__ == '__main__':
    
    Eye("192.168.10.1").run()


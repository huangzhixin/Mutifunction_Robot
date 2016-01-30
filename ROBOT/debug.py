#!/usr/bin/env python    
# -*- coding: utf-8 -*-  
from numpy import *
def loadDataSet():
    dataMat = []
    fr = open("testdata.txt")
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])    #还有为啥还要设置第一列！！！！！
    return dataMat

def plotBestFit():
    import matplotlib.pyplot as plt
   
    dataMat= loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]     #这里是数据的行数,也就是样本数
    xcord1 = []; ycord1 = []
    for i in range(n):
       xcord1.append(dataArr[i,0]);   ycord1.append(dataArr[i,1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red', marker='s')
    plt.xlabel('x'); plt.ylabel('y')
    plt.show()

if __name__ == "__main__":
    plotBestFit()

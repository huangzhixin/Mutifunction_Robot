#coding:utf-8
import socket
from threading import Thread
import time
import string
#import websocketserver as websocket
import globalvariable 
#host = ""
#port = 23211
#sendbrain="qwe"
 
def handlechild(clientsock):
    clientInfo = str(clientsock.getpeername())
    print "Got connection from %s" % clientInfo
    while True:
      time.sleep(1)
      buf = clientsock.recv(1024)
      if buf:
        if buf == 'q' :
         clientsock.send('please go out!')
         clientsock.close()
         break
        else :  
           if(globalvariable.socketflag=="true"):   #这里判断brain.py是否读了之前的消息，如果没读给客户端说系统繁忙
             clientsock.send('系统繁忙请再次输入\n')
           else:
             globalvariable.socketbuf=buf     #如果之前传送的消息已经被brain.py读过，那就接受客户端的新消息，并设置标记说有新消息了
             clientsock.send('收到\n')
             globalvariable.socketflag="true"
         #global sendbrain 
         #sendbrain = buf
         #str1=buf.split(',')
         #num1 = string.atoi(str1[0])
         #num2 = string.atoi(str1[1])
         #print num1
         #print num2
         #clientsock.sendall(clientInfo)
    print 'close %s connection.' % clientInfo
    clientsock.close()

def InitSocketServer(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    while 1:
       try:
          clientsock, clientaddr = sock.accept()
       except (KeyboardInterrupt, SystemExit):
          raise
       except:
          continue
       t = Thread(target=handlechild, args=[clientsock])
       t.setDaemon(1)
       t.start()

def main():
    InitSocketServer("192.168.1.107","23211")
	
if __name__ == "__main__":
	main()



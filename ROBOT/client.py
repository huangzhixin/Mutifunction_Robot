import socket
from eye import Eye
import time
if __name__ == "__main__":  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.connect(('192.168.10.1',9988))  
    sock.send("stand\n")    #rightward

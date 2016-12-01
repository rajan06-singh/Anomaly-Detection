import socket
from struct import * 

def ConnectedPort(host, port, i):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    msg = "TCP port " + str(i) + " open \n"
    packed_msg = bytes(msg, 'utf-8')
    addr = (host, port)
    c.connect(addr)
    c.sendall(packed_msg)
    c.close()

range = [3389, 80, 22, 445]
Not_Connected = [ ]

for i in range:
    host = '127.0.0.1'
    addr = (host, i)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
      s.connect(addr) 
      if True:
          print ("connected")
          ConnectedPort('10.0.0.51', 5555, i)
          s.close()
    except Exception:
        Not_Connected.append(i)
        print ("not connected")

print (Not_Connected)


for i in Not_Connected:
    host = '127.0.0.1'
    addr = (host, i)
    if i <= len(Not_Connected):       
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     
    try:
         s.connect(addr)
         while True:
             print ("Connected")
             ConnectedPort('10.0.0.51', 5555, i)
             Not_Connected.remove(i)
             s.close()
    except Exception:
         print ("Not connected")
         print (Not_Connected)
            
    else:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         i == 0
         try:
            s.connect(addr)
            while True:
                print ("Connected")
                ConnectedPort('10.0.0.51', 5555, i)
                Not_Connected.remove(i)
                s.close()
         except Exception:
            print (Not_Connected)
               
    
     



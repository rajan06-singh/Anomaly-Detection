import socket
from time import gmtime, strftime, localtime

server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
buffer = 512
addr =('10.0.0.51', 5555)
server1.bind(addr)
server1.listen(5)
x = strftime("%a, %d %b %Y %H:%M:%S ", localtime())

try:
    while True:
              c, addr = server1.accept()
              print ("Connection from client : ", addr[0])
              data = c.recv(buffer)
              if data:
                    f = open("storage.dat", 'a+')
                    f.write(x)
                    f.write(" : ")
                    f.write("Notification from client - ")
                    f.write(addr[0])
                    f.write(" [:] ")
                    f.write(data.decode("utf-8"))
                    f.close()
finally:
       server1.close()

#!/usr/bin/env  python2
import  socket

#  calling  udp method
#                       ipv4 ,        UDP type 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  here s  is udp  type with  ipv4  socket 
#  defining  ip and port  for comm
ip_addr="0.0.0.0"
port=8888

conn=(ip_addr,port)
# binding  ip  and port 
s.bind(conn)
#          data buffer size rec from  per client/sender  
while True:
	print  s.recvfrom(100)
















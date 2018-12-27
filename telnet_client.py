#!/usr/bin/env  python2
import  socket
import  time
#  calling  udp method
#                       ipv4 ,        UDP type 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  here s  is udp  type with  ipv4  socket 
#  defining  ip and port  for comm
ip_addr="192.168.10.101"
port=8888

while 4 >  2 :

	data=raw_input("enter your command  :  ")
	s.sendto(data,(ip_addr,port))
	print  s.recvfrom(100)
	time.sleep(1)
	print  "to disconnect type exit "




















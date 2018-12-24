#!/usr/bin/env  python2
import  socket

#  calling  udp method
#                       ipv4 ,        UDP type 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  here s  is udp  type with  ipv4  socket 
#  defining  ip and port  for comm
ip_addr="192.168.10.253"
port=8888

while 4 >  2 :

	data=raw_input("enter your data :  ")
	s.sendto(data,(ip_addr,port))



















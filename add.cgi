#!/usr/bin/python2

import  cgi
import  commands
import  os
import  cgitb  # traceback errors in  web apps
cgitb.enable()

print  "Content-Type: text/html"
print  ""
# gettting  html data 
mypage_data=cgi.FieldStorage()

f_num=mypage_data.getvalue('x')
s_num=mypage_data.getvalue('y')
mycmd=mypage_data.getvalue('c')
#  adding numbers 
print  int(f_num)    +       int(s_num)
print   "<br/>"
print   "<pre>"
print   commands.getoutput('sudo  '+mycmd)
print   "</pre>"

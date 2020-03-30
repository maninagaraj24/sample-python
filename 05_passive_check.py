#!/usr/bin/python3
import socket
import subprocess
import os
ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
socket.gethostbyname(socket.gethostname())
cmd = 'echo'
ip = 'localhost'
code= '0'
status = 'okk'
service_data = ["postman", "CRN status", "VerifyMPIN", "CCList", "AccList"]

for i in service_data:
        ser = ('localhost'+ ';' + i + ';' + '0' + ';' + 'OK')
        #print (ser)

nsca = os.system(['/opt/nagios/bin/send_nsca -H 192.168.2.191 -d', ';' ,'-c /etc/nagios/send_nsca.cfg'])
service = os.system( 'echo', ser,'|', nsca)


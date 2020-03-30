#!/usr/bin/python3
import socket
import subprocess
import os
ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
socket.gethostbyname(socket.gethostname())
cmd = 'echo'
ip = 'localhost'
code= '1'
status = 'okk'
service_data = ["postman", "Login", "CClist", "ACClist"]

for i in service_data:
        ser = (ip+ ';' + i + ';' + code + ';' + status)
        try:
            sp=subprocess.run(f'echo \"{ser}\" | /opt/nagios/bin/send_nsca -H 192.168.2.191 -d \";\" -c /etc/nagios/send_nsca.cfg',capture_output=True,text=True,shell=True) 
            print(sp.stdout)
         # subprocess.run([' echo', "{0};{1};{2};{3}".format(ip, i, code, status),],check=True)
           # subprocess.run([ '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)

        except subprocess.CalledProcessError as e:
            e.returncode    

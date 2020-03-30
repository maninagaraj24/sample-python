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
        #ser = ('localhost'+ ';' + i + ';' + '0' + ';' + 'OK')
        try:
            subprocess.run([ cmd,ip,';', i, ';',code,';', status, '|', '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)
            subprocess.run(['echo', "{0};{1};{2};{3}".format(ip, i, code, status),],check=True)
            subprocess.run([ '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)
        except subprocess.CalledProcessError as e:
             e.returncode


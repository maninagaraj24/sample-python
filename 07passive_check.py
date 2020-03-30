#!/usr/bin/python3
import socket
import subprocess
import os
ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
socket.gethostbyname(socket.gethostname())
cmd = 'echo'
send_ncsa_bin='/opt/nagios/bin/send_nsca -H 192.168.2.191 -d'
deli='\";\"'
send_nsca_cfg= '-c /etc/nagios/send_nsca.cfg'
ip = 'localhost'
code= '0'
status = 'okk'
pipe= '|'
service_data = ["postman", "CRN status", "VerifyMPIN", "CCList", "AccList"]
#s= subprocess.Popen(('echo', '\"localhsot;postman;0;ok\"'), stdout=subprocess.PIPE)
#output = subprocess.Popen(( '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d', ';' '-c /etc/nagios/send_nsca.cfg'),stdin=s.stdout)
#s.wait()
for i in service_data:
        ser = ( ip+ ';' + i + ';' + code + ';' + status)
        
        try:
            #sp=subprocess.run([cmd,ser],check=True)
            sp=subprocess.Popen(['echo', ser,' |', send_ncsa_bin, deli, send_nsca_cfg], shell=False)
            #subprocess.Popen(['echo', sp,'|', nsca],shell=True)
            
           # subprocess.run([' echo', "{0};{1};{2};{3}".format(ip, i, code, status),],check=True)
           # subprocess.run([ '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)

        except subprocess.CalledProcessError as e:
            e.returncode


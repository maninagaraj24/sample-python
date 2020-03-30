#!/usr/bin/python3
import socket
import subprocess
import os
cmd='/opt/nagios/bin/send_nsca -H 192.168.2.191 -d, ';', -c /etc/nagios/send_nsca.cfg'
e='echo'
send='localhost;postmant;1;okKKK'
#nsca=subprocess.run(['echo', send],check=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
socket.gethostbyname(socket.gethostname())
cmd = 'echo'
print(ip)
#ip = 'localhost'
code= '0'
status = 'okk'
service_data = ["postman", "CRN status", "VerifyMPIN", "CCList", "AccList"]

for i in service_data:
        ser = (ip+ ';' + i + ';' + code + ';' + status)
        try:
            #sp=subprocess.run([cmd, ser, '|', '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d', ';',' -c /etc/nagios/send_nsca.cfg'],check=True) 
           # subprocess.run([' echo', "{0};{1};{2};{3}".format(ip, i, code, status),],check=True)
           # subprocess.run([ '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)
            nsca=subprocess.run(['echo', send, '|', '/opt/nagios/bin/send_nsca', '-H', '192.168.2.191', '-d', ';', '-c', '/etc/nagios/send_nsca.cfg'],shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
       #     sp=subprocess.Popen([cmd],stdin=nsca.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
       #     nsca.stdout.close()
           # output = nsca.communicate()[0]
            print(nsca)

        except subprocess.CalledProcessError as e:
            e.returncode    

import socket
import subprocess
import os
ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
socket.gethostbyname(socket.gethostname())

service_data = ["postmanBDD", "CRN status", "VerifyMPIN", "CCList", "AccList"]

for i in service_data:
        ser = ('localhost'+ ';' + i + ';' + '0' + ';' +'OK')
        try:
            subprocess.run(['echo', ser, '|', '/opt/nagios/bin/send_nsca 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)
            # print (ser)
        except subprocess.CalledProcessError as e:
            print(e.returncode)    
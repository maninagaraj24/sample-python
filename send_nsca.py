#!/usr/bin/python
import socket
print('{0}'.format(socket.gethostbyname(socket.gethostname())))
# socket.gethostbyname(socket.gethostname())

service_data = ["postmanBDD", "CRN status", "VerifyMPIN", "CCList", "AccList"]

for i in service_data:
        print ('localhost'+ ';' + i + ';' + '0' + ';' +'OK')

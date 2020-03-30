#!/usr/bin/python

#service_description = {'Login', 'Logout'}
#
#for n in service_description:
#     name = n
#send_nsca = ('localhost' + ';'  + name + ';' + '1' + ';' + 'This service is Failed')
#
#
#print ('---' * 64)
#print (send_nsca)
#print ('---' * 64)

import socket
import os
ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
# socket.gethostbyname(socket.gethostname())

service_data = ["postmanBDD", "CRN status", "VerifyMPIN", "CCList", "AccList"]

for i in service_data:
        ser = (ip + ';' + i + ';' + '0' + ';' +'OK')
        print (type(ser))

#os.system ("/opt/nagios/bin/nsca -c /etc/nagios/nsca.cfg

os.system ( "/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg")





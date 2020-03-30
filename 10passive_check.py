#!/usr/bin/python3

import subprocess

p1 = subprocess.run('echo \"localhost;postman;1;warn\" | /opt/nagios/bin/send_nsca -H 192.168.2.191 -d \";\" -c /etc/nagios/send_nsca.cfg', capture_output=True,text=True, shell=True)

print(p1.stdout)
#

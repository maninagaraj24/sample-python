#!/usr/bin/python3
import subprocess
cmd='/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'
cmdlist=['/opt/nagios/bin/send_nsca',  '-c', '/etc/nagios/nsca.cfg']
cmdsendlist=['/opt/nagios/bin/send_nsca', '-H', '192.168.2.191', '-d', ';', '-c', '/etc/nagios/send_nsca.cfg']
#print(cmd.split())
service=['echo', '\"localhost;postman;0;mani\"']
#print (service)
#se=subprocess.Popen(service,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
#rc=se.wait()
#out=se.communicate()[0]
#print(f'out is: {out}')
#print(err)


sp=subprocess.Popen(cmdlist,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
#se.stdout.close()
out,err=sp.communicate()
#sp.stdout.close()
print(f'out is: {out}')
print(err)
#print(output)

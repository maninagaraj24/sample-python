#!/usr/bin/python3
import subprocess

cmd='/opt/nagios/bin/send_nsca -H 192.168.2.191 -d, ';', -c /etc/nagios/send_nsca.cfg'
e='echo'
send='localhost;postmant;0;ok'
nsca=subprocess.run(['echo', send],check=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
#print(nsca)
#rc=nsca.wait()
#out,err=nsca.communicate()
#
#print(f'OUTPUT IS: {out}')
#print(f'Error is: {err}')
sp=subprocess.run([cmd],stdin=nsca.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
nsca.stdout.close()
output = sp.communicate()[0].strip()
sp.stdout.close()
#print(sp)
#sp.check_returncode()
#nsca.stdout.close()
#output=sp.communicate()[0]
#sp.stdout.close()
#rc=sp.wait()
#out,err=sp.communicate()
#print(f'OUTPUT IS: {out}')
#print(f'Error is: {err}')
#ouput= subprocess.check_output((cmd),stdin=nsca.stdout)



#rc=ser.wait()
#out,err=ser.communicate()
#print(f'OUTPUT IS: {out}')
#print(f'Error is: {err}')


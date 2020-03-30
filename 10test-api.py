#!/usr/bin/python3
import json 
import subprocess
from datetime import date
import glob
import os

#list_of_files = glob.glob('/home/infra/newman/newman/*.json')
#latest_file = max(list_of_files, key=os.path.getctime)
#print (latest_file)
#da = date.today()

subprocess.run("newman run https://www.getpostman.com/collections/88c4dde55656d4e451ab -r cli,json", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
with open ( os.path.join(newman/*.json)) as summary_json:
  read_content = json.load(summary_json)
   
def success_source_summary():
    save_items_data = []
    run_summary = read_content['run']
    failure_data = run_summary['executions']
    for error_data in failure_data:
        error_summary = error_data['item']
        items = error_summary['name']
        save_items_data.append(items)
    return save_items_data   
save_items_data = success_source_summary()

#for success_service in save_items_data:
#  
#       ss= ('localhost'+ ';' + success_service + ';' + '0' + ';' +'Success')
#       savefile = open ('success_service','w')
#       savefile.write (ss)
#       savefile.close()
#      # print(ss)
##       try:
#       sp=subprocess.run(f'echo \"{ss}\" | /opt/nagios/bin/send_nsca -H 192.168.2.248 -d \";\" -c /etc/nagios/send_nsca.cfg' ,capture_output=True,text=True, shell=True)
#       print(sp.stdout)
# #      except subprocess.CalledProcessError as e:
#  #          e.returncode

for success_service in save_items_data:
    ss = ('localhost'+ ';' + success_service + ';' + '0' + ';' +'Success')
    savefile = open ('success_service','a+',)
    savefile.seek(0)
    data = savefile.read(100)
    if len(data) > 0:
      savefile.write("\n")
    savefile.write (ss)
    savefile.close()

print ('---' * 64)

def error_source_summary():
    save_error_data = []
    run_summary = read_content['run']
    failure_data = run_summary['failures']
    for error_data in failure_data:
        error_summary = error_data['source']
        error = error_summary['name']
        save_error_data.append(error)
    return save_error_data    
save_error_data = error_source_summary()

#for failed_service in save_error_data:
# 
#  es = ('localhost'+ ';' + failed_service + ';' + '2' + ';' +'This service has Failed')
#  savefile = open ('success_service','w')
#  savefile.write (es)
#  savefile.close()
#
#  print (es)
#  err=subprocess.run(f'echo \"{es}\" | /opt/nagios/bin/send_nsca -H 192.168.2.248 -d \";\" -c /etc/nagios/send_nsca.cfg' ,capture_output=True,text=True, shell=True)
#  print(err.stdout)

for failed_service in save_items_data:
    es = ('localhost'+ ';' + failed_service + ';' + '2' + ';' +'This service has Failed')
    savefile = open ('success_service','a+',)
    savefile.seek(0)
    data = savefile.read(100)
    if len(data) > 0:
      savefile.write("\n")
    savefile.write (es)
    savefile.close()










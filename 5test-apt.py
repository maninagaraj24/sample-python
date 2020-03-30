#!/usr/bin/python
import json

with open('newman.json') as summary_json:
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

for success_service in save_items_data:
  
  print ('localhost'+ ';' + success_service + ';' + '0' + ';' +'This service has Success')

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

for failed_service in save_error_data:
 
  print ('localhost'+ ';' + failed_service + ';' + '2' + ';' +'This service has Failed')
  










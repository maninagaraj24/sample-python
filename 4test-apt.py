#!/usr/bin/python


import json
with open('newman.json') as summary_json:
  read_content = json.load(summary_json)

def api_test_summary():
    run_summary = read_content['run']
    failure_data = run_summary['failures']
    for error_data in failure_data:
        test_summary = error_data['error']
        api = test_summary['test']
           
api_test_summary() 
def source_test_summary():
    run_summary = read_content['run']
    failure_data = run_summary['failures']
    for error_data in failure_data:
        source_summary = error_data['source']
        source = source_summary['name']
        print(source)  
source_test_summary()      

#print (source_test_summary(),api_test_summary())

#!/usr/bin/python
import json
with open('kmb.json') as summary_json:
  read_content = json.load(summary_json)
def error_source_summary():
    summary = []
    run_summary = read_content['run']
    failure_data = run_summary['failures']
    for error_data in failure_data:
        error_summary = error_data['source']
        error = error_summary['name']
        service = (error)
        summary.append(service)
    return summary
summary = error_source_summary()

for i in summary:
    print ('localhost'+ ';' + i + ';' + '0' + ';' +'OK')

#error_source_summary()
# error_source_summary()      

# my_dict['service'] = 'init'


# print (my_dict)

#save_data = []

#error_source_summary()

#print(str(save_data))

##name = (str(save_data))
#print (name)
#service = '' .join ({ i : 5 for i in (name)})
#print (str(service))
#print (name)
#dictOfWords = { i : 5 for i in listOfStr }


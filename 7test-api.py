import json

with open('kmb.json') as summary_json:
  read_content = json.load(summary_json)


   
def success_source_summary():
    run_summary = read_content['run']
    failure_data = run_summary['executions']
    for error_data in failure_data:
        error_summary = error_data['item']
        items = error_summary['name']
        save_items_data.append(items)
save_items_data = []
success_source_summary()
with open ('source.json', 'w') as file:
    json.dump(save_items_data, file)

with open('source.json') as service:
    for i in service:
      print (i)  

# print ('---' * 64)
# print (type((success_source_summary())))
# print ('---' * 64)
# # for i in save_items_data:
# #     print (i)

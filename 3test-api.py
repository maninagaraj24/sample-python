#!/usr/bin/python
import json

req_file="newman.json"

fo=open(req_file, 'r')
print(json.load(fo).get('failures'))


fo.close()

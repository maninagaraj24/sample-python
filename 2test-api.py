#!/usr/bin/python

import json 

with open('newman.json') as json_data:
    data = json.load(json_data)
    for r in data['run']:
        fo = open(r[failures'2']+".json","wb")
        fo.write(r['error'])
        fo.close()

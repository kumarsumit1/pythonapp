# -*- coding: utf-8 -*-
"""
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html
@author: sumit.kumar
"""
import json

"""
The format of JSON encoding is almost identical to Python syntax except 
for a few minor changes. For instance, True is mapped to true,
 False is mapped to false, and None is mapped to null. 
"""

d = {'a': True,'b': 'Hello','c': None}


json.dumps(d)

print(json.dumps(d, indent=4))


print(json.dumps(d, sort_keys=True))

#deserialize the json string to a dynamic object
p = lambda:None
p.__dict__ = json.loads('{"action": "print", "method": "onData", "data": "Madan Mohan","parent":{"child":{"name":"henry"}}}')

print(type(p.__dict__))
p.action

p.method

#Parent child relation doesnt work
#p.parent
 

json_response='''{
	"createdBy": "Sumit Kumar",
	"createdDate": 1511173428000,
	"modifiedBy": "Sumit Kumar",
	"modifiedDate": 1511173428000	
} '''



data = json.loads(json_response)


#To iterate over all the key value pairs of dict
for key, value in data.items():
    print( key, value)


print(data['createdBy'])

print(data['test']['test2'])


print(data['test'][0]['test'])

#However below syntax is not allowed    
#print(type(data.createdBy))

#But we can conver the Json dictionary  to Python Object

class JSONObject:
    def __init__(self, d):
         self.__dict__ = d

obj = json.loads(json_response, object_hook=JSONObject)

print(type(obj)) 


obj.createdBy 


print(obj.groupAccess.isActive)  

for x in obj.testList:
    print (x.createdBy)
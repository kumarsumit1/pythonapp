import jsonschema

from jsonschema import Draft3Validator, ValidationError, FormatChecker,validate

#import simplejson as json
import json

#with open('schema-example.json', 'r') as f:
#    schema_data = f.read()

schema_data='''{
  "type": "object",
  "properties": {
    "name": {
      "type": ["string","null"] ,
        "maxLength": 12      
    },
    "price": {
      "type": ["number","null"],
              "minimum":0,
              "maximum":99999
    },
    "sku": {
      "description": "Stock Keeping Unit",
      "type": "integer"
    }
  },
  "required": ["name", "price"]
}'''





schema = json.loads(schema_data)

json_obj1 = {"name": "eggs", "price": 21.47}
validate(json_obj1, schema)

json_obj2 = {"name": "eggs", "price": "blue"}
#jsonschema.validate(json_obj, schema)

ret1=Draft3Validator(schema).is_valid(json_obj1)
print("The return value is ::",ret1)
ret2=Draft3Validator(schema).is_valid(json_obj2)
print("The return value is ::",ret2)



import json
import jsonschema
dat='{"TID":"122","CUR":"USD","DAT1":"t","DAT2":11}'

print type(dat)
def validJson(rowData):
    jsonRec=json.loads(rowData)
    jsonSc=json.loads('''{  "title": "usecase", "type": "object",  "properties": { "TID" : { "type": [ "string" ]  },"CUR" : { "type": [ "string" ]  , "maxLength" : 3 },"DAT1" : { "type": [ "number","null"]  , "maximum" : 99999999999 },"DAT2" : { "type": [ "number" ,"null"]  , "maximum" : 112 } },  "required": [  "TID",  "CUR",  "DAT1",  "DAT2" ] }''')
    val = jsonschema.Draft3Validator(jsonSc).is_valid(jsonRec)
    print "is records valid ::"+str( val)
    va=jsonschema.validate(jsonRec, jsonSc)
    print "records validated "+str(va)
    return json.dumps(jsonRec)

print validJson(dat)


# jsonschema.exceptions.ValidationError: 'blue' is not of type 'number'
#
# Failed validating 'type' in schema['properties']['price']:
#     {'type': 'number'}
#
# On instance['price']:
#     'blue'
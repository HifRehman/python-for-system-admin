'''
JSON = (JavaScript Object Notation) is a popular data format used for representing structured data.
XML = The purpose xml is to transfer the data from server to application and app to server.

It's common to transmit and receive data between a server and web application in JSON format.

Python  == JSON Equivalent
dict  <---> object
list,tuple <---> array
str <---> str
int,float <---> number
True <---> true
False <---> false
None <---> null

'''

import json 

req_file = "/home/ansadmin/py-for-sys/JSON/my_json.json"

fo = open(req_file, 'r')
#print(fo.read())
#print(type(fo.read()))
#print(json.load(fo))
#print(type(json.load(fo)))
my_dict = {'name':'kells', 'skills':['Python','shell', 'yaml', 'AWS']}
req_file1 = "myinfo.json"
fo=open(req_file1,'w')
json.dump(my_dict, fo, indent=4)

fo.close()
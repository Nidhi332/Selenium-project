import jsonpath
import requests
import json

url="https://reqres.in/api/users/2"

file=open ("C:\\Users\\sagar\\Desktop\\Test_demo.json","r")
str_request=file.read()
print(str_request)

json_requst =json.loads(str_request)
print(json_requst)

response=requests.put(url,json_requst)
print(response.status_code)


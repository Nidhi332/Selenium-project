import jsonpath
import requests
import json

url="https://reqres.in/api/users"

file=open ("C:\\Users\\sagar\\Desktop\\Test_demo.json","r")
str_request=file.read()
print(str_request)

json_requst =json.loads(str_request)
print(json_requst)

#requesting json to create data

response=requests.post(url,json_requst)
print(response.status_code)

#parse response to Json format
response_json=json.loads(response.text)
print(response_json)

#id using json path
id=jsonpath.jsonpath(response_json,"id")
print(id)
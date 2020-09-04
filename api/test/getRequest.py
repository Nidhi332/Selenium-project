import json
import jsonpath
import requests

url= "https://reqres.in/api/users?page=2"

response=requests.get(url)
print(response)

print(response.content)

#fetch response header
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))

print(response.status_code)

#fetch cookies
print(response.cookies)
print(type(response))

print(response.encoding)
#elapsed timr
print(response.elapsed)

#Parse response to Json format

json_fomrat = json.loads(response.text)
print(json_fomrat)

pages=jsonpath.jsonpath(json_fomrat,"total_pages")
print(pages)

for i in range(0,4):
    first_name=jsonpath.jsonpath(json_fomrat,"data["+str(i)+"].first_name")
    print(first_name)
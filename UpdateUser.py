import requests
import jsonpath
import json


url="https://dummyjson.com/users/1"

data = {
    "firstName": "Tony",
    "lastName": "Stark",
    "username":"Jarvis",
    "password":"H3ll0J@rVis"    
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.put(url,data=json.dumps(data), headers=headers)
json_response = json.loads(response.text)
print("Status code is :"+str(response))
print(json_response)
firstName = json_response["firstName"]
lastName = json_response["lastName"]
username =json_response["username"]
password =json_response["password"]

assert firstName == "Tony"
assert lastName == "Stark"
assert username == "Jarvis"
assert password == "H3ll0J@rVis"

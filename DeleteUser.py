import requests
import jsonpath
import json

url="https://dummyjson.com/users/1"

response = requests.delete(url)
print("Status Code is :"+str(response.status_code))
json_response=json.loads(response.text)
isDeleted = json_response["isDeleted"]
print(isDeleted)
assert isDeleted == True
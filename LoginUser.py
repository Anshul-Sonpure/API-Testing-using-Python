import requests
import jsonpath
import json
from hamcrest import assert_that, equal_to

url="https://dummyjson.com/auth/login"
data = {
    "username": "kminchelle",
    "password": "0lelplR"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

response = requests.post(url,data=json.dumps(data), headers=headers)
json_response = json.loads(response.text)
print("Status Code:"+" "+str(response.status_code))
token=json_response["token"]
firstName=json_response["firstName"]
lastName =json_response["lastName"]
print("Received token is:"+token)
assert firstName == "Jeanne"
assert lastName == "Halvorson"


import requests
import jsonpath
import json
url ="https://fakestoreapi.com/users/1"
response = requests.get(url)
print("Status Code is : "+" "+str(response.status_code))
json_response = json.loads(response.text)
print(json_response)
email =""
email = email.join(jsonpath.jsonpath(json_response,'email'))
print(email)

#In below code we will fetch complete json array from https://reqres.in/api/users?page=2
#for user id = 9 
url='https://reqres.in/api/users?page=2'
response= requests.get(url)
response=json.loads(response.text)
data=jsonpath.jsonpath(response,'data[2]')
print("Data for id=9->",data)
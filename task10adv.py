# name = input("Enter your name: ");
# print("Hello " + name + "!");
import requests
user     = {
  "loginName": "19001001",
  "password": "Abc@1234"
}
headers={'Content-type':'application/json', 'Accept':'application/json'}

# Get

getFunc  = requests.get('https://w3schools.com')
print("GET REQUEST")
print(getFunc.status_code)
print(getFunc.encoding)
print(getFunc.cookies)
print(getFunc.text)
print(getFunc.json())
print("=====================")

# Post
postFunc = requests.post("https://api.tingconnect.com/api/Account/login", json = user, headers = headers) 

print("POST REQUEST")
print(postFunc.status_code)
print(postFunc.elapsed)
print(postFunc.headers)
print(postFunc.history)
print(postFunc.is_permanent_redirect)
print(postFunc.iter_content())
print(postFunc.links)
print(postFunc.raise_for_status())
print(postFunc.text)
print(postFunc.json())
print("=====================")
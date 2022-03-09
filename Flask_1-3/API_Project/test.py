import requests


BASE = "http://127.0.0.1:5000/"

response_1 = requests.get(BASE + "helloworld/Stephen")
response_2 = requests.put(BASE + "video/1", {"name": "something", "views": 100, "likes": 10})
response_3 = requests.get(BASE + "video/1")
response_4 = requests.get(BASE + "video/4")
response_5 = requests.put(BASE + "video/4", {"name": "something two", "views": 200, "likes": 20})
response_6 = requests.get(BASE + "video/4")
response_7 = requests.delete(BASE + "video/6")
response_8 = requests.delete(BASE + "video/4")


print(response_1.json())
print(response_2.json())
print(response_3.json())
print(response_4.json())
print(response_5.json())
print(response_6.json())
print(response_7)
print(response_8)

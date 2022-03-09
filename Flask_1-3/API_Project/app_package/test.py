import requests


BASE = "http://127.0.0.1:5000/"



# response_1 = requests.get(BASE + "api/blogpostlist")
# response_1 = requests.get(BASE + "helloworld/Stephen")
# response_2 = requests.post(BASE + "api/post/1", {"author": "A1", "title": "T1", "likes": 100})
# response_3 = requests.post(BASE + "api/post/2", {"author": "A2", "title": "T2", "likes": 200})
# response_4 = requests.post(BASE + "api/post/3", {"author": "A3", "title": "T3", "likes": 300})
# response_5 = requests.put(BASE + "api/post/3", {"likes": 333})
response_6 = requests.delete(BASE + "/api/post/3")
# response_7 = requests.get(BASE + "api/post/3")


# print(response_1.json())
# print(response_2.json())
# print(response_3.json())
# print(response_4.json())
# print(response_5.json())
print(response_6.json())
# print(response_7.json())

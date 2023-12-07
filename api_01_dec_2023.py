import requests
#
# url = 'https://jsonplaceholder.typicode.com/photos'
#
# # get
# responce = requests.get(url)
# print(responce.json())
#
# # post
# jsonPayload = {'albumId':1, 'title':'test', 'url':'nothing.com',
# 'thumbnailUrl':'nothing.com'}
# responce = requests.post(url, json=jsonPayload)
# print(responce.json())
#
# # put. change particulat photo
# url = 'https://jsonplaceholder.typicode.com/photos/100'
# responce = requests.put(url, json=jsonPayload)
# print(responce.json())
#
# # delete
# responce = requests.delete(url)
# print(responce.json())

# next
url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())



# import requests
#
# url='https://jsonplaceholder.typicode.com/todos/'
# response = requests.get(url=url)
# print(response.text)

# import requests
#
# response = requests.get(url='http://httpbin.org/')
# print(response.text)

import requests

response = requests.get(url='http://httpbin.org/image/jpeg')
with open('image.jpeg', 'wb') as file:
    file.write(response.content)
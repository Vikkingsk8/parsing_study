import requests

count = 1
for i in range(1,161):
    response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png')
    with open(fr"C:\Users\vikto\PycharmProjects\parser_study\images\image{count}.png", 'wb') as file:
        file.write(response.content)
        count += 1

# import requests
#
# for i in range(1, 161):
#     with open(f'image_req/{i}.png', 'wb') as file:
#         responce = requests.get(url=f'http://parsinger.ru/img_download/img/ready/{i}.png').content
#         file.write(responce)
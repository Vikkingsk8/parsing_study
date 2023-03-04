import requests

url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'  # url was here
response = requests.get(url=url, stream=True)
with open('file.mp4', 'wb') as file:
    file.write(response.content)


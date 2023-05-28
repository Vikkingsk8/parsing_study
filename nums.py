import requests
import webbrowser


print('go')
site = input('url input')
era = input('year, month, day')
url = 'https://web.archive.org/' % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data['archive_snapshots']['closest']['url']
    print('find copy: ', old_site)
    print('i will open it')
    webbrowser.open(old_site)

except:
    print('no copy')
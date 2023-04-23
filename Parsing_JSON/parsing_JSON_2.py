import requests

responce = requests.get("https://parsinger.ru/downloads/get_json/res.json").json()
caty = set(i["categories"] for i in responce)
dct = dict(zip(caty, [0] * len(caty)))
for price in responce:
    if price["categories"] in dct:
        dct[price["categories"]] += int(price["price"].split()[0]) * int(price["count"])
print(dct)


from bs4 import BeautifulSoup
import requests
import json

for x in range(1,33):
    url = f'https://parsinger.ru/html/mouse/3/3_{x}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = [x.text for x in soup.find_all('p', id='p_header')]
    article = [x.text.replace('Артикул: ','') for x in soup.find_all('p', class_='article')]
    description = soup.find('ul', id='description').find_all('li')
    li_id = [x['id'] for x in description]
    li_text = [x.text.strip() for x in description]
    count = [x.text.replace('В наличии: ','') for x in soup.find_all('span', id = 'in_stock')]
    price = [x.text.replace(' руб','') for x in soup.find_all('span', id='price')]
    old_price = [x.text.replace(' руб', '') for x in soup.find_all('span', id='old_price')]
    link = url
    result_json = []

    for name, article, descr, price, old_price, link in zip(name, article, description, price, old_price, link):
        result_json.append({
            'category': 'mouse',
            'name': name,
            'article': article,
            'description': {
                li_id[0]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][0]).strip(),
                li_id[1]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][1]).strip(),
                li_id[2]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][2]).strip(),
                li_id[3]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][3]).strip(),
                li_id[4]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][4]).strip(),
                li_id[5]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][5]).strip(),
                li_id[6]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][6]).strip(),
                li_id[7]: ([x.text.split(':')[1] for x in soup.find('ul', id = 'description').find_all('li')][7]).strip()
            },
            'price': price,
            'old_price': old_price,
            'link': url

        })

    with open('res1.json', 'a', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
import requests
from bs4 import BeautifulSoup
import json


def find_deep_link(url_prefix, url_start, category):
    link_list = []
    response = requests.get(url=url_start)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    url_seach = [x["href"] for x in soup.find("div", class_="nav_menu").find_all("a") if
                 x.find("div")["id"] == category]
    url_need = url_prefix + url_seach[0]
    res = requests.get(url_need)
    res.encoding = 'utf-8'
    soup1 = BeautifulSoup(res.text, 'lxml')
    url_need_pages = [url_prefix + x['href'] for x in soup1.find("div", class_="pagen").find_all("a")]
    for link in url_need_pages:
        res_link = requests.get(link)
        res_link.encoding = 'utf-8'
        soup_link = BeautifulSoup(res_link.text, 'lxml')
        link_list.extend(url_prefix + x.find("a")["href"] for x in
                         soup_link.find("div", class_="item_card").find_all("div",
                                                                            class_="sale_button"))
    return link_list


def parse_all(link_list, category, result_json):
    for link in link_list:
        main_dict = dict()
        response = requests.get(url=link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = soup.find("p", id="p_header").text.strip()
        article = soup.find("p", class_="article").text.split(':')[1].strip()
        description_tags = [x.text.split(':')[0].strip() for x in soup.find('ul', id='description').find_all('li')]
        description_values = [x.text.split(':')[1].strip() for x in soup.find('ul', id='description').find_all('li')]
        count = soup.find("span", id="in_stock").text.split(':')[1].strip()
        price = soup.find("span", id="price").text.strip()
        old_price = soup.find("span", id="old_price").text.strip()
        main_dict["categories"] = category
        main_dict["name"] = name
        main_dict["article"] = article
        main_dict["description"] = dict(zip(description_tags, description_values))
        main_dict["count"] = count
        main_dict["price"] = price
        main_dict["old_price"] = old_price
        main_dict["link"] = link
        result_json.append(main_dict)
    return result_json


def write2json(result_json):
    with open('task3.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)


url_prefix = "https://parsinger.ru/html/"
url_start = 'https://parsinger.ru/html/index1_page_1.html'
key_list = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
result_json = []

write2json(parse_all(find_deep_link(url_prefix, url_start, key_list[0]), key_list[0], result_json))

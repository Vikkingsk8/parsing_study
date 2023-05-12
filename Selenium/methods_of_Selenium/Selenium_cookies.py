# from pprint import pprint
# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     pprint(cookies)

# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     for cookie in cookies:
#         print(cookie['name']) # или cookie['value'] чтобы получить их значение

# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     print(webdriver.get_cookie('_ym_uid')['expiry'])
#
# >>>1685520499

# import time
# from pprint import pprint
# from selenium import webdriver
#
# cookie_dict = {
#     'name': 'any_name_cookie',    # Любое имя для cookie
#     'value': 'any_value_cookie',  # Любое значение для cookie
#     'expiry': 2_000_000_000,      # Время жизни cookie в секундах
#     'path': '/',                  # Директория на сервере для которой будут доступны cookie
#     'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
#     'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
#     'httpOnly': True,  # or False # Ограничивает доступ к cookie по средствам API
#     'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
# }
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/4/index.html')
#     webdriver.add_cookie(cookie_dict)
#     pprint(webdriver.get_cookies())
#     time.sleep(10)
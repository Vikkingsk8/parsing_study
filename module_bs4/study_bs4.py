from bs4 import BeautifulSoup

# find module
# primer 1
###
#
# html_doc = """
# <html>
#     <head>
#         <title>Example Page</title>
#     </head>
#     <body>
#         <h1>Hello World</h1>
#         <p class="info">This is a paragraph.</p>
#         <p class="info">This is another paragraph.</p>
#     </body>
# </html>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# # Найдёт первый тег h1
# first_h1 = soup.find('h1')
# print(first_h1)
#
# print('----разделитель----')
#
# # Найдёт первый тег p с классом "info"
# first_p = soup.find('p', {'class': 'info'})
# print(first_p)


# primer 2
#####
# html_doc = """
# <html>
#     <head>
#         <title>Example Page</title>
#     </head>
#     <body>
#         <div id="main">
#             <h1>Hello World</h1>
#             <p class="info">This is a paragraph.</p>
#             <p class="info">This is another paragraph.</p>
#             <ul>
#                 <li>Item 1</li>
#                 <li>Item 2</li>
#                 <li>Item 3</li>
#             </ul>
#         </div>
#         <div id="secondary">
#             <p>Some additional information.</p>
#         </div>
#     </body>
# </html>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# s = soup.findAll()

# Находим первый div с id "main"
# main_div = soup.find('div', {'id': 'main'})
# print(main_div)
#
# print('----разделитель----')
#
# # Найдите первый тег h1 внутри «основного» div
# main_h1 = main_div.find('h1')
# print(main_h1)
#
# print('----разделитель----')
#
# # Найдите первый тег p с классом «информация» внутри «основного» div
# main_p = main_div.find('p', {'class': 'info'})
# print(main_p)
#
# print('----разделитель----')
#
# # Найдите первый тег ul внутри «основного» div
# main_ul = main_div.find('ul')
# print(main_ul)

# primer 3
####
# html_doc = """
# <html>
#     <head>
#         <title>Example Page</title>
#     </head>
#     <body>
#         <div id="main">
#             <h1>Hello World</h1>
#             <p class="info">This is a paragraph.</p>
#             <p class="info">This is another paragraph.</p>
#             <ul>
#                 <li>Item 1</li>
#                 <li>Item 2</li>
#                 <li>Item 3</li>
#             </ul>
#         </div>
#         <div id="secondary">
#             <p>Some additional information.</p>
#         </div>
#     </body>
# </html>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# # Найдите первый div с идентификатором «main»
# main_div = soup.find('div', attrs={'id': 'main'})
# print(main_div)
#
# print('----разделитель----')
#
# # Найдите первый тег p с классом "info"
# info_p = soup.find('p', attrs={'class': 'info'})
# print(info_p)


# ----------------------------------------------------------
# html_doc = """
# <html>
#     <head>
#         <title>Example Page</title>
#     </head>
#     <body>
#         <div id="main">
#             <h1>Hello World</h1>
#             <p class="info">This is a paragraph.</p>
#             <p class="info">This is another paragraph.</p>
#             <ul>
#                 <li>Item 1</li>
#                 <li>Item 2</li>
#                 <li>Item 3</li>
#             </ul>
#         </div>
#         <div id="secondary">
#             <p>Some additional information.</p>
#         </div>
#     </body>
# </html>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# s = soup.findAll('p', attrs={'class': 'info'})
# print(s)


# ------------------------------------------------------
# .text .get_text()

# primer 1
'''html_doc = """
<html>
    <body>
        <div id="main">
            <p>This is a paragraph</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим первый элемент с тегом p
p = soup.find('p')

# Используем .text, чтобы получить текст внутри тега p
print(p.text)  # This is a paragraph
'''

# example 2

'''html_doc = """
<html>
    <body>
        <div id="main">
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим все теги li
lis = soup.find_all('li')

# Выводим текст внутри каждого тега li с помощью .text
for li in lis:
    print(li.text)'''

# example 3 .get_text()

'''html = """
<html>
    <body>
        <h1>Example Page</h1>
        <p>This is some text.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
        <p>This is some more text.</p>
        <p>This is even more text.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

header = soup.h1
header_text = header.get_text()
print(header_text)
print(header)'''

# example 4

'''html = """
<html>
    <body>
        <h1>Example Page</h1>
        <p>This is some text.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
        <p>This is some more text.</p>
        <p>This is even more text.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

all_text = soup.get_text()
print(all_text)

Вывод:

Example Page
This is some text.

Item 1
Item 2
Item 3

This is some more text.
This is even more text.'''

# ---------------------------------------------------------------------------------------------
# select()

# '''Тег: select("p")
# Класс: select(".class")
# Идентификатор: select("#id")
# Атрибут: select("[attribute=value]")
# Несколько селекторов: select("p.class")'''

# example 1
'''html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p` с классом `text-class`
result = soup.select('p.text-class')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `id`
result = soup.select('p#text-id')
for tag in result:
    print(tag.text)
    
print('----разделитель----')

# Найти все теги `p` внутри тега `body`
result = soup.select('body p')
for tag in result:
    print(tag.text)'''

# example 2
'''html = """
<html>
  <body>
    <p class="highlight">This is a highlighted paragraph.</p>
    <p>This is a normal paragraph.</p>
    <div id="div1">
      <p>This is a paragraph in a div.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight"
highlighted_paras = soup.select(".highlight")
for para in highlighted_paras:
    print(para.text)

print('----разделитель----')

# Выберем все параграфы, находящиеся внутри элемента с идентификатором "div1"
div_paras = soup.select("#div1 p")
for para in div_paras:
    print(para.text)'''

# example 3
'''html = """
<html>
  <body>
    <div id="div1">
      <p class="highlight">This is a highlighted paragraph in div1.</p>
      <p>This is a normal paragraph in div1.</p>
    </div>
    <div id="div2">
      <p class="highlight">This is a highlighted paragraph in div2.</p>
      <p>This is a normal paragraph in div2.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight"
highlighted_paras = soup.select("p[class='highlight']")
print("Highlighted paragraphs:")
for para in highlighted_paras:
    print(para.text)'''
# ----------------------------------------------------------------------------------------
# select_one()
'''html = """
<html>
  <body>
    <div id="div1">
      <p class="highlight">This is a highlighted paragraph in div1.</p>
      <p>This is a normal paragraph in div1.</p>
    </div>
    <div id="div2">
      <p class="highlight">This is a highlighted paragraph in div2.</p>
      <p>This is a normal paragraph in div2.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем первый параграф с классом "highlight"
highlighted_para = soup.select_one("p[class='highlight']")
print("Highlighted paragraph:")
print(highlighted_para.text)'''

# example 2
'''html_doc = """
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <div class="container">
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </div>
        <div class="container">
            <p>This is a third paragraph.</p>
            <p>This is a fourth paragraph.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Выберем первый div с классом "container"
first_container = soup.select_one('.container')
print(first_container)
Вывод:

<div class="container">
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
</div>'''

# example 3

'''html_doc = """
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <div class="container">
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </div>
        <div class="container">
            <p class="highlight">This is a highlighted paragraph.</p>
            <p>This is a fourth paragraph.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Выберем первый div с классом «container», у которого есть дочерний элемент p с классом «highlight».
highlighted_paragraph = soup.select_one('.container p.highlight')
print(highlighted_paragraph)
Вывод:
<p class="highlight">This is a highlighted paragraph.</p>'''

# ---------------------------------------------------------------------------

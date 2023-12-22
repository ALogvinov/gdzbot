import requests
from bs4 import BeautifulSoup


# Запрос страницы
url = "https://www.euroki.org/gdz/ru/informatika/6_klass/otvety-po-informatike-6-klass-semenov-408/zadanie-1"
page = requests.get(url).text
# Подключили объект bs
soup = BeautifulSoup(page, 'html.parser')

# Заголовок страницы
page_title = soup.title.string
print(page_title)

# Все ссылки страницы
# for link in soup.find_all('a'):
#     print(link.get('href'))
authors = soup.find(itemprop="author")

classes = soup.find(class_='block')
list_classes = classes.find_all('li')
for cl in list_classes:
    print(cl.text)

data = [
    {
        "task": 1,
        "src": "https://imgs.euroki.org/books/gdzs/5660/2074359.png?v=1607018536",
        "title": "ГДЗ Информатика 6 класс Семенов 2023 № 3 | Фото решебник"
    },
    {
        "task": 2,
        "src": "https://imgs.euroki.org/books/gdzs/5660/2074359.png?v=1607018536",
        "title": "sdfsdfsdfsdsfsdfник"
    }
]

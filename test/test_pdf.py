# Импорт библиотек
import requests
from bs4 import BeautifulSoup

# Запрос содержимого страницы
url = "https://www.euroki.org/gdz/ru/russkiy/6_klass/ladyzhenskaya-fgos-2023-465/zadanie-64"
html = requests.get(url).text

# Преобразование к soup для парсинга
soup = BeautifulSoup(html, 'html.parser')

# Удаление лишних блоков (тэгов) из soup
soup.find('nav', class_='navbar').decompose()
soup.find('div', class_='dsk_nav').decompose()
soup.find('div', class_='ads').decompose()

print(soup)
# Сохранение html
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

# Сохранение в pdf

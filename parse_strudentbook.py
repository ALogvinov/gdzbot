# Скрипт будет получать на вход адрес учебника.
# В результате его работы в заданной папке должны сохраниться все странцы в файлах с номер страницы

# 6_klass
#   russkiy
#      ladyzhenskaya-fgos-2023-465
#           1.html
#           2.html
#           406.html
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import time

# Параметры
target = 'russkiy'
class_name = '6_klass'
studentbook = 'ladyzhenskaya-fgos-2023-465'
site = 'https://www.euroki.org'
url = f"{site}/gdz/ru/{target}/{class_name}/{studentbook}"

# Проверяем, существует ли нужные папки. Если папки нет, то создаем ее
save_path = f"data/{class_name}/{target}/{studentbook}"
Path(save_path).mkdir(parents=True, exist_ok=True)

# Получаем содержимое страницы
html = requests.get(url).text

# Преобразуем страницу в soup
soup = BeautifulSoup(html, 'html.parser')

# Парсим ссылки на разделы, сохраняем в массив
links = soup.find_all('a', class_='gdz_link')

# В цикле проходим по количеству страниц
for link in links:
    # Скачиваем содержимое страницы
    href = site + '/' + link['href']
    print(f'Скачиваем страницу {href}...')
    page = requests.get(href).text
    page_soup = BeautifulSoup(page, 'html.parser')

    # Удаляем лишнее
    page_soup.find('nav', class_='navbar').decompose()
    page_soup.find('div', itemprop='mainEntity').decompose()
    page_soup.find('ul', class_='primary').decompose()
    page_soup.find('ul', class_='secondary').decompose()
    page_soup.find('div', class_='send_error').decompose()
    page_soup.find('div', class_='sharethis-inline-reaction-buttons').decompose()
    page_soup.find('div', style='margin-top: 10px;').decompose()
    page_soup.find('div', class_='ads').decompose()
    page_soup.find('div', class_='breadcrumbs').decompose()

    # Получаем название задания
    page_number = link.text

    # Сохраняем каждую страницу в нужную папку в html
    with open(f'{save_path}/{page_number}.html', 'w', encoding='utf-8') as f:
        f.write(str(page_soup))

    # Ожидаем 4 сек
    time.sleep(4)


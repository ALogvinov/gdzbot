import pdfkit
import requests
from bs4 import BeautifulSoup

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Запрос страницы
url = 'https://www.euroki.org/gdz/ru/matematika/6_klass/vilenkin-fgos-192/3-zadanie-14'
page = requests.get(url).text
# Подключили объект bs
soup = BeautifulSoup(page, 'html.parser')

# Удаляем лишнее
soup.find('nav', class_='navbar').decompose()
soup.find('div', class_='ads').decompose()
soup.find('div', class_='navs').decompose()
soup.find('div', class_='breadcrumbs').decompose()
soup.find('div', class_='send_error').decompose()

html = str(soup)

# Сохраняем HTML в файл
with open('edited_page.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Преобразуем HTML в PDF
pdfkit.from_file('edited_page.html', 'page.pdf')

# pdfkit.from_string(str(soup), 'out.pdf', options={'--disable-local-file-access': None})
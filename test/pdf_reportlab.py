from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from bs4 import BeautifulSoup
import requests
from io import BytesIO
import html2text

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

# Преобразуем объект soup в HTML
html = str(soup)
html = html2text.html2text(page)

# Создаем PDF
doc = SimpleDocTemplate("page.pdf", pagesize=letter)
styles = getSampleStyleSheet()
content = [Paragraph(html, styles["Normal"])]
doc.build(content)
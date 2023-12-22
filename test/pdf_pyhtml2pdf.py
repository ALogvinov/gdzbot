from pyhtml2pdf import converter
import requests

url = 'https://www.euroki.org/gdz/ru/matematika/6_klass/vilenkin-fgos-192/3-zadanie-14'
page = requests.get(url).text
with open('test.html', 'w', encoding="utf-8") as f:
    f.write(page)
converter.convert('test.html', 'sample2.pdf')
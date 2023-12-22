import requests

url = 'https://www.euroki.org/gdz/ru/matematika/6_klass/vilenkin-fgos-192/3-zadanie-14'
response = requests.get(url)

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
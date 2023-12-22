from weasyprint import HTML

url = 'https://www.euroki.org/gdz/ru/matematika/6_klass/vilenkin-fgos-192/3-zadanie-14'
HTML(url).write_pdf('weasyprint-website.pdf')
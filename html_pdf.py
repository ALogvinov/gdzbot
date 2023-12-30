# Импорт библиотек
from os import listdir
from os.path import isfile, join
import os
from ironpdf import *


def html2pdf(filepath):
    """
    Преобразует файл html в формат pdf и сохраняет его
    :return:
    """
    # Считать данные этого файла
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Считать имя файла до .html
    name, extension = os.path.splitext(filepath)
    # Сконвертировать в PDF
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderHtmlAsPdf(html)
    pdf.SaveAs(f"{name}.pdf")

# Считать все файлы из заданной директории (учебника)
mypath = 'data/6_klass/russkiy/ladyzhenskaya-fgos-2023-465'
html_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# В цикле пробежаться по названиям файла
for html_file in html_files:
    # Считать расширение файла (после точки)
    # Считать имя файла до .html
    name, extension = os.path.splitext(html_file)

    # Сохраняем каждый html в pdf с аналогичным именем
    filepath = mypath + '/' + html_file
    if extension == '.html':
        print(filepath)
        html2pdf(filepath)



#html2pdf('data/6_klass/russkiy/ladyzhenskaya-fgos-2023-465/1.html')

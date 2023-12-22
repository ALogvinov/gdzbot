# Импорт библиотек
from os import listdir
from os.path import isfile, join
import os

# Считать все файлы из заданной директории (учебника)
mypath = 'data/6_klass/russkiy/ladyzhenskaya-fgos-2023-465'
html_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# В цикле пробежаться по названиям файла
for html_file in html_files:
    # Считать расширение файла (после точки)
    # Считать имя файла до .html
    name, extension = os.path.splitext(html_file)
    print(name, extension)

    # Сохраняем каждый html в pdf с аналогичным именем
    html2pdf(p1, p2..)

def html2pdf(параметры):
    """
    Преобразует файл html в формат pdf и сохраняет его
    :return:
    """
    # Вывод содержимого файла print


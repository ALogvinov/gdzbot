# Импорт библиотек
from os import listdir
from os.path import isfile, join
import os
from ironpdf import *

# Считать все файлы из заданной директории (учебника)
mypath = 'data/6_klass/russkiy/ladyzhenskaya-fgos-2023-465'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def pdf2png(pdf_filepath, jpg_filepath):
    pdf = PdfDocument.FromFile(pdf_filepath)

    # Extract all pages to a folder as image files
    pdf.RasterizeToImageFiles(f"{jpg_filepath}/*.png", DPI=96)

# В цикле пробежаться по названиям файла
for file in files:
    # Считать расширение файла (после точки)
    # Считать имя файла до .html
    name, extension = os.path.splitext(file)
    if extension == '.pdf':
        # Сохраняем каждый html в pdf с аналогичным именем
        filepath = mypath + '/' + file
        imgpath = mypath + '/' + name
        pdf2png(filepath, imgpath)




#pdf2png('data/6_klass/russkiy/ladyzhenskaya-fgos-2023-465/1.pdf',
 #       'data/6_klass/russkiy/ladyzhenskaya-fgos-2023-465/1')
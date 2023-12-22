from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('txt_cont.pdf')

for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save('page' + str(i) + '.jpg', 'JPEG')

#https://stackoverflow.com/questions/53481088/poppler-in-path-for-pdf2image
#https://sourceforge.net/projects/poppler-win32/files/latest/download

from ironpdf import *

pdf = PdfDocument.FromFile("page.pdf")

# Extract all pages to a folder as image files
pdf.RasterizeToImageFiles("assets/page/*.png",DPI=96)

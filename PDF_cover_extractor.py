from pdf2image import convert_from_bytes
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import sys

if len(sys.argv)>1:
    input_file = sys.argv[1]
else:
    input_file = input("\x1b[0;33mType the PDF file name to create cover photo:\x1b[0m ")

inp = PdfFileReader(input_file, "rb")
page = inp.getPage(0)

wrt = PdfFileWriter()
wrt.addPage(page)

r = io.BytesIO()
wrt.write(r)

images = convert_from_bytes(r.getvalue())
images[0].save(input_file[:-4]+".png")
print("\x1b[0;33mDone, your cover photo has been saved as {}.\x1b[0m".format(input_file[:-4]+".png"))
r.close()

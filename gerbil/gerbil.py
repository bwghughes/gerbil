import os
from optparse import OptionParser
import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import gray
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFError

from clint.textui import progress

pdfmetrics.registerFont(TTFont('Bliss-Regular', 'Bliss-Regular.ttf'))


def get_page_size(options, default=A4):
    if options.page_width and options.page_height:
        width, height = float(options.page_width), float(options.page_height)
    else:
        width, height = default
    return width, height


def create_footer(options):
    pdf = StringIO.StringIO()
    width, height = get_page_size(options)
    if options.landscape:
        width, height = height, width
    can = canvas.Canvas(pdf, pagesize=(width, height))
    can.setFillColor(gray)
    can.setFont('Bliss-Regular', 8)
    can.setAuthor(options.author)
    can.setSubject(options.subject)
    can.drawCentredString(width / 2.0, height / 2.0, options.text)
    can.save()
    return pdf


def merge_files(options, footer):
    footer.seek(0)
    new_pdf = PdfFileReader(footer)
    try:
        book = PdfFileReader(open(options.input, "rb"))
    except Exception, e:
        print "Unable to load input PDF - {}".format(e)
        exit()

    output = PdfFileWriter()
    for index, page in progress.dots(enumerate(book.pages)):
        page = book.getPage(index)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    outputStream = open(options.output, "wb")
    output.write(outputStream)
    outputStream.close()
    print "Written {}".format(options.output)


def test_if_file_exists(filename):
    if os.path.isfile(filename):
        return True

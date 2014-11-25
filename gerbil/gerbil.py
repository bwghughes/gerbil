import os
from os.path import splitext, isfile, basename
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


def get_page_size(options, default=A4):
    if options.page_width and options.page_height:
        width, height = float(options.page_width), float(options.page_height)
    else:
        width, height = default
    return width, height


def test_if_file_exists(filename):
    if filename is None:
        return False
    return isfile(filename)


def create_font_args(options):
    if test_if_file_exists(options.font):
        font_name, font_path = (basename(splitext(options.font)[0]),
                                options.font)
        options.font_name = font_name
        options.font_path = font_path
        return False
    else:
        return True


def create_footer(options):
    if not options.text:
        return None, "No text to write, exiting"

    pdf = StringIO.StringIO()
    width, height = get_page_size(options)
    if options.landscape:
        width, height = height, width
    can = canvas.Canvas(pdf, pagesize=(width, height))
    can.setFillColor(gray)
    size = 8
    if options.size:
        size = options.size
    can.setFont(options.font_name, size)
    can.drawCentredString(width / 2.0, height / 2.0, options.text)
    can.save()
    return pdf, None


def merge_files(options, footer):
    footer.seek(0)
    new_pdf = PdfFileReader(footer)

    if not test_if_file_exists(options.input):
        print "Could not read the input file - did you specify one?"
        exit(1)

    if not options.output:
        print "No output path specified"
        exit(1)

    try:
        book = PdfFileReader(open(options.input, "rb"))
    except Exception, e:
        print "Unable to load input PDF - {}".format(e)
        exit(1)

    output = PdfFileWriter()

    if options.author:
        output.addMetadata({"/Author": options.author})

    if options.subject:
        output.addMetadata({"/Subject": options.subject})

    for index, page in progress.dots(enumerate(book.pages)):
        page = book.getPage(index)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    outputStream = open(options.output, "wb")
    output.write(outputStream)
    outputStream.close()
    print "Written {}".format(options.output)

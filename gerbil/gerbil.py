import io
import os
from optparse import OptionParser
from os.path import basename, isfile, splitext

from clint.textui import progress
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib import colors, pagesizes
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFError, TTFont
from reportlab.pdfgen import canvas


def get_paper_size(size):
    return {
        'A0': pagesizes.A0,
        'A1': pagesizes.A1,
        'A2': pagesizes.A2,
        'A3': pagesizes.A3,
        'A4': pagesizes.A4,
        'A5': pagesizes.A5,
        'A6': pagesizes.A6,
        'LETTER': pagesizes.LETTER,
        'LEGAL': pagesizes.LEGAL,
        'B0': pagesizes.B0,
        'B1': pagesizes.B1,
        'B2': pagesizes.B2,
        'B3': pagesizes.B3,
        'B4': pagesizes.B4,
        'B5': pagesizes.B5,
        'B6': pagesizes.B6,
    }.get(size, pagesizes.A4)


def get_page_size(options):
    if options.page_width and options.page_height:
        width, height = options.page_width * cm, options.page_height * cm
    else:
        width, height = get_paper_size(options.paper_size)
        if options.landscape:
            width, height = height, width
    return width, height


def test_if_file_exists(filename):
    if filename is None:
        return False
    return isfile(filename)


def get_color(color):
    return HexColor(color)


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

    pdf = io.BytesIO()
    width, height = get_page_size(options)

    can = canvas.Canvas(pdf, pagesize=(width, height))
    color = options.font_color
    can.setFillColor(color)

    size = 8
    if options.font_size:
        size = options.font_size
    can.setFont(options.font_name, size)
    if options.top and options.side:
        can.drawString(
            options.side * cm, height - options.top * cm, options.text)
    else:
        can.drawCentredString(width / 2.0, height / 2.0, options.text)
    can.save()
    return pdf, None


def merge_files(options, footer):
    footer.seek(0)
    new_pdf = PdfFileReader(footer)

    if not test_if_file_exists(options.input):
        print("Could not read the input file - did you specify one?")
        exit(1)

    if not options.output:
        print("No output path specified")
        exit(1)

    try:
        book = PdfFileReader(open(options.input, "rb"))
    except (Exception, e):
        print("Unable to load input PDF - {}".format(e))
        exit(1)

    output = PdfFileWriter()

    if options.author:
        output.addMetadata({"/Author": options.author})

    if options.subject:
        output.addMetadata({"/Subject": options.subject})

    for index, page in progress.dots(enumerate(book.pages)):
        page = book.getPage(index)
        if index >= options.skip_pages:
            page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    outputStream = open(options.output, "wb")
    output.write(outputStream)
    outputStream.close()
    print("Written {}".format(options.output))

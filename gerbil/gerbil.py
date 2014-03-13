import os
from optparse import OptionParser
import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import gray
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFError

from clint.textui import progress

pdfmetrics.registerFont(TTFont('Bliss-Regular', 'Bliss-Regular.ttf'))


def create_footer(options):
    pdf = StringIO.StringIO()
    can = canvas.Canvas(pdf, pagesize=A4)
    width, height = A4
    can.setFillColor(gray)
    can.setFont('Bliss-Regular', 8)
    can.setAuthor(options.author)
    can.setSubject(options.subject)
    can.drawCentredString(width / 2.0, 20, options.text)
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


def main():
    parser = OptionParser()
    parser.add_option('-t', '--text',
                      help="The text to appear on footer the page.")
    parser.add_option('-f', '--font',
                      help="The TrueType font file to be used (*.ttf)")
    parser.add_option('-a', '--author',
                      help="The author to appear in metadata.")
    parser.add_option('-s', '--subject',
                      help="The subject to appear in metadata.")
    parser.add_option('-i', '--input',
                      help="The input file for the text to be added to.")
    parser.add_option('-o', '--output',
                      help="The ouput file to be saved.")
    parser.add_option('-p', '--padding',
                      help="The padding from the bottom of the page")
    (options, args) = parser.parse_args()

    f = create_footer(options)
    merge_files(options, f)

    # for filename in [options.input, options.font]:
    #     if os.path.isfile(filename):
    #
    #     else:
    #         print "Input & Font files need to be valid files."
    #         print "Run gerbil --help for more info."

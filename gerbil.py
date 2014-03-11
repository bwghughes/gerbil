from optparse import OptionParser
import StringIO
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import gray

from clint.textui import progress

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))


def create_footer(options):
    # create a new PDF with Reportlab
    packet = StringIO.StringIO()
    can = canvas.Canvas(packet, pagesize=A4)
    width, height = A4
    can.setFillColor(gray)
    can.setFont('Arial', 8)
    can.setAuthor("VFQ Education from Emergn")
    can.setSubject("This publication forms part of Value, Flow, Quality\
                    Education. Details of this and other Emergn courses can be\
                    obtained from Emergn, Fitzwilliam Hall, Fitzwilliam Place,\
                    Dublin 2, Ireland or Emergn, One International Place,\
                    Suite 1400, Boston, MA 02110, USA.Alternatively, you may\
                    visit the Value, Flow, Quality website at \
                    http://www.valueflowquality.com where you can learn more\
                    about the range of courses offered by Value, Flow, Quality")
    can.drawCentredString(width/2.0, 20, options.text)
    can.save()
    return packet


def merge_files(options, footer):
    footer.seek(0)
    new_pdf = PdfFileReader(footer)
    book = PdfFileReader(open(options.input, "rb"))
    output = PdfFileWriter()
    for index, page in progress.dots(enumerate(book.pages)):
        page = book.getPage(index)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    outputStream = open(options.output, "wb")
    output.write(outputStream)
    outputStream.close()
    print "Written {}".format(options.output)

def main():
    parser = OptionParser()
    parser.add_option('-t', '--text',
                      help="The text to appear on footer the page.")
    parser.add_option('-i', '--input',
                      help="The input file for the text to be added to.")
    parser.add_option('-o', '--output',
                      help="The ouput file to be saved.")

    (options, args) = parser.parse_args()
    footer = create_footer(options)
    merge_files(options, footer)

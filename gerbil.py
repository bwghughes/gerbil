import StringIO
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import gray

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

def create_footer(footer_string):
    # create a new PDF with Reportlab
    packet = StringIO.StringIO()
    can = canvas.Canvas(packet, pagesize=A4)
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
    can.drawString(220,30, footer_string)
    can.save()
    return packet


def merge_files(footer):
    footer.seek(0)
    new_pdf = PdfFileReader(footer)
    book = PdfFileReader(open("prioritisation-book.pdf", "rb"))
    output = PdfFileWriter()
    for index, page in enumerate(book.pages):
        print "Adding to page {}".format(index)
        page = book.getPage(index)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    outputStream = open("david-bochenski-prioritisation-book.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

footer = create_footer("Created for David Bochenski by Gerbils.")
merge_files(footer)

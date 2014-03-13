import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.lib.colors import gray

from clint.textui import progress


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

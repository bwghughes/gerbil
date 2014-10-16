from os.path import splitext, isfile, basename
from optparse import OptionParser
from .gerbil import create_footer, merge_files

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_font_args(options):
    if isfile(options.font):
        font_name, font_file = (basename(splitext(options.font)[0]),
                                options.font)
        return font_name, options.font
    else:
        print "Can't find {}".format(options.text)


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
                      help="NOT IMPLEMENTED YET !! - The padding from the \
                            bottom of the page ")
    parser.add_option('--page-width',
                      help="The width of the page")
    parser.add_option('--page-height',
                      help="The height of the page")
    parser.add_option('--landscape',
                      action="store_true", dest="landscape", default=False,
                      help="Specify landscape orientation, otherwise portrait")
    
    (options, args) = parser.parse_args()

    pdfmetrics.registerFont(TTFont(*create_font_args(options)))
    f = create_footer(options)
    merge_files(options, f)

from optparse import OptionParser
from .gerbil import create_footer, merge_files, create_font_args

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def main():
    parser = OptionParser()
    parser.add_option('-t', '--text',
                      help="The text to appear on footer the page.")
    parser.add_option('-i', '--input',
                      help="The input file for the text to be added to.")
    parser.add_option('-o', '--output',
                      help="The ouput file to be saved.")
    parser.add_option('-f', '--font',
                      default="Bliss-Regular.ttf",
                      help="Path to the TrueType font file to be used (*.ttf)")
    parser.add_option('-s', '--size',
                      type="float",
                      default=8,
                      help="The font size px to be used (default = 8)")
    parser.add_option('-a', '--author',
                      help="The author to appear in metadata.")
    parser.add_option('-u', '--subject',
                      help="The subject to appear in metadata.")
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

    err = create_font_args(options)
    if not err:
        pdfmetrics.registerFont(TTFont(options.font_name, options.font_path))
        f, err = create_footer(options)
        if err is None:
            merge_files(options, f)
        else:
            print err
    else:
        print "Can't find {} Exiting".format(options.font)
        exit(1)

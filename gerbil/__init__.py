from optparse import OptionParser
from .gerbil import create_footer, merge_files, create_font_args

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import pkg_resources  # part of setuptools
try:
    version = pkg_resources.require("gerbil")[0].version
except:
    pass


def main():
    parser = OptionParser(version=version)
    parser.add_option('-t', '--text',
                      help="The text to appear on footer the page.")
    parser.add_option('-i', '--input',
                      help="The input file for the text to be addedso.")
    parser.add_option('-o', '--output',
                      help="The ouput file to be saved.")
    parser.add_option('-f', '--font',
                      default="Bliss-Regular.ttf",
                      help="Path to the TrueType font file to be used (*.ttf)")
    parser.add_option('-c', '--font-color',
                      default="#545454",
                      help="Hex color, defaults to Grey: #545454")
    parser.add_option('-s', '--font-size',
                      type="float",
                      default=8,
                      help="The font size px to be used (default = 8)")
    parser.add_option('-a', '--author',
                      help="The author to appear in metadata.")
    parser.add_option('-u', '--subject',
                      help="The subject to appear in metadata.")
    parser.add_option('--top',
                      type="float",
                      help="The padding from the left hand side of the page (cm)")
    parser.add_option('--side',
                      type="float",
                      help="The padding from the top of the page (cm)")
    parser.add_option('-x', '--page-width',
                      type="float",
                      help="The width of the page (cm)")
    parser.add_option('-y', '--page-height',
                      type="float",
                      help="The height of the page (cm)")
    parser.add_option('--paper-size',
                      default="A4",
                      help="Default = A4. The named size of the paper Supported: A0 - A6, B0 - B6, LETTER, LEGAL.  Paramter ignored if -x and -y are supplied ")
    parser.add_option('--landscape',
                      action="store_true", dest="landscape", default=False,
                      help="Default = portrait unless this flag is supplied. Defines the page orientation,  (ignored if -x and -y are given)")
    parser.add_option('--skip-pages',
                      type="int",
                      default=0,
                      help="number of pages to skip before stamping starts. Default = 0"
                      )
    (options, args) = parser.parse_args()

    err = create_font_args(options)

    if not err:
        pdfmetrics.registerFont(TTFont(options.font_name, options.font_path))
        f, err = create_footer(options)
        if err is None:
            merge_files(options, f)
        else:
            print(err)
    else:
        print("Can't find {} Exiting".format(options.font))
        exit(1)

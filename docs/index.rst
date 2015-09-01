.. Gerbil documentation master file, created by
   sphinx-quickstart on Thu Mar 13 10:09:17 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Gerbil's documentation!
===================================

Gerbil is a tool to simply watermark the bottom of existing PDF pages
with a personalised text message - name and function inspired by those awesome folks at `Pragmatic Programmers <http://pragprog.com/>`_.

Installation
------------

Gerbil is hosted on PyPi, but comes with a CLI, called, you guessed it gerbil.

To install simply run:

.. code-block:: bash

    pip install gerbil

You make need to run

.. code-block:: bash

    sudo pip install gerbil

if you run into permission errors.


Usage
-------

Show me do works for me - should be self explanatory.

.. code-block:: bash

    gerbil -i prioritisation-book.pdf \
           -o prioritisation-book-new.pdf \
           -t "Made lovingly by Gerbils" \
           -f Bliss-Regular.ttf

An explanation of the options can be shown by running:

.. code-block:: bash

    gerbil --help

Which displays:

.. code-block:: bash

    $ gerbil --help
    Usage: gerbil [options]

    --version             show program's version number and exit
  -h, --help            show this help message and exit
  -t TEXT, --text=TEXT  The text to appear on footer the page.
  -i INPUT, --input=INPUT
                        The input file for the text to be addedso.
  -o OUTPUT, --output=OUTPUT
                        The ouput file to be saved.
  -f FONT, --font=FONT  Path to the TrueType font file to be used (*.ttf)
  -c FONT_COLOR, --font-color=FONT_COLOR
                        Hex color, defaults to Grey: #545454
  -s FONT_SIZE, --font-size=FONT_SIZE
                        The font size px to be used (default = 8)
  -a AUTHOR, --author=AUTHOR
                        The author to appear in metadata.
  -u SUBJECT, --subject=SUBJECT
                        The subject to appear in metadata.
  --top=TOP             The padding from the left hand side of the page (cm)
  --side=SIDE           The padding from the top of the page (cm)
  -x PAGE_WIDTH, --page-width=PAGE_WIDTH
                        The width of the page (cm)
  -y PAGE_HEIGHT, --page-height=PAGE_HEIGHT
                        The height of the page (cm)
  --paper-size=PAPER_SIZE
                        Default = A4. The named size of the paper Supported:
                        A0 - A6, B0 - B6, LETTER, LEGAL.  Paramter ignored if
                        -x and -y are supplied
  --landscape           Default = portrait unless this flag is supplied.
                        Defines the page orientation,  (ignored if -x and -y
                        are given)
  --skip-pages=SKIP_PAGES
                        number of pages to skip before stamping starts.
                        Default = 0



To Do
------

0. Tests !!!!

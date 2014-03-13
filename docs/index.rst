.. Gerbil documentation master file, created by
   sphinx-quickstart on Thu Mar 13 10:09:17 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Gerbil's documentation!
===================================

Gerbil is a tool to simply watermark the bottom of existing PDF pages
with a personalised text message - name and function inspired by our awesome publishing friends at `Pragmatic Programmers <http://pragprog.com/>`_.

Installation
------------

Gerbil is hosted on PyPi, but somes with a CLI, called, you guessed it gerbil.

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

    Options:
      -h, --help            show this help message and exit
      -t TEXT, --text=TEXT  The text to appear on footer the page.
      -f FONT, --font=FONT  The TrueType font file to be used (*.ttf)
      -a AUTHOR, --author=AUTHOR
                            The author to appear in metadata.
      -s SUBJECT, --subject=SUBJECT
                            The subject to appear in metadata.
      -i INPUT, --input=INPUT
                            The input file for the text to be added to.
      -o OUTPUT, --output=OUTPUT
                            The ouput file to be saved.
      -p PADDING, --padding=PADDING
                            The padding from the bottom of the page


Shortcomings
------------

This is a scratch an itch for a project we're doing at `Action Agile <http://actionagile.co.uk/>`_ at the moment. See below for things that need adding.

Currently Gerbil only supports adding text to the bottom of portrait oriented, unencrypted, unlocked, PDF's in grey. Awesome isn't it? :)


To Do
------

0. Tests !!!!
1. Options for paper sizes & orientation
2. Different distances from bottomof page.
3. Different colors.
4. PDF Password support.
5. PDF Meta data - currently hard wired.
6. Better exception handling.

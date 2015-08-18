#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import gerbil

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.md').read().replace('.. :changelog:', '')

setup(
    name='gerbil',
    version=gerbil.__version__,
    description='Tool for adding text to the bottom of PDF pages.',
    long_description=readme + '\n\n' + history,
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='https://github.com/bwghughes/gerbil',
    include_package_data=True,
    install_requires=[
        'Pillow==2.9.0',
        'args==0.1.0',
        'clint==0.4.1',
        'reportlab==3.2.0',
    ],
    dependency_links = ['https://github.com/jerickbixly/PyPDF2#egg=PyPDF2'],
    packages=[
        'gerbil',
    ],
    package_dir={'gerbil': 'gerbil'},
    license="BSD",
    zip_safe=False,
    keywords='gerbil',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts':
            ['gerbil=gerbil:main']
    }

)

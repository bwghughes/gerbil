#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import roomyjob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements_lines = [line.strip() for line in open('requirements.txt').readlines()]
install_requires = list(filter(None, requirements_lines))

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='gerbil',
    version=roomyjob.__version__,
    description='Tool for adding text to the bottom of PDF pages.',
    long_description=readme + '\n\n' + history,
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='https://github.com/bwghughes/roomyjob',
    packages=[
        'roomyjob',
    ],
    package_dir={'roomyjob': 'roomyjob'},
    include_package_data=True,
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='roomyjob',
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
            ['roomyjob=roomyjob:main']
    }

)

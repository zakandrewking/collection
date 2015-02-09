#!/usr/bin/env python
# 
# -*- coding: utf-8 -*-
# 

import sys
from os.path import join, dirname, realpath, exists

try:
    from setuptools import setup
except:
    from distutils.core import setup

directory = dirname(realpath(__file__))
sys.path.insert(0, join(directory, 'collection'))
version = __import__('version').__version__

setup(name='collection',
      version=version,
      author='Zachary King',
      packages=['collection'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
      ],
      install_requires=[
          'Jinja2>=2.7.3',
          'tornado>=4.0.2',
          'pytest>=2.6.2',
          'SQLAlchemy>=0.9.8',
          'psycopg2>=2.5.4'
      ],
      extras_require={
          'dev': [
              'ipython>=2.4.0',
              'ipdb>=0.8.0'
          ]
      })

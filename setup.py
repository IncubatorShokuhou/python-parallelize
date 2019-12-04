#!/usr/bin/env python

import os
from distutils.core import setup


setup(name='python-parallelize',
      version='1.0.0.0_qb',
      description='Make the for loop run in parallel',
      author='IncubatorShokuhou',
      author_email='lh@lasg.iap.ac.cn',
      url='https://github.com/IncubatorShokuhou/python-parallelize',
      
      license="Apache 2.0",
      
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Topic :: Software Development',
      ],

      provides=['parallelize'],
      py_modules=['parallelize']
)

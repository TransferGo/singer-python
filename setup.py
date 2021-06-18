#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess
import shutil
import os

if os.path.isdir('build'):
    shutil.rmtree('build')

setup(name="singer-python",
      version='5.12.1',
      description="Singer.io utility library",
      author="Stitch",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      url="http://singer.io",
      install_requires=[
          'pytz==2018.4',
          'jsonschema==2.6.0',
          'simplejson==3.11.1',
          'python-dateutil>=2.6.0',
          'backoff==1.8.0'
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipython',
              'ipdb',
              'nose',
              'singer-tools'
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)

# clean-up
if os.path.isdir('build'):
    shutil.rmtree('build')
shutil.rmtree('singer_python.egg-info')
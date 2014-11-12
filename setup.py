# -*- coding: utf-8 -*-
#
#  setup.py
#  referredby
#

"""
Packaging for the referredby project.
"""

from setuptools import setup

VERSION = '0.1.3'

setup(
    name='referredby',
    description="Parsing referrer URLS for common search engines.",
    url="http://github.com/larsyencken/referredby/",
    version=VERSION,
    author="Lars Yencken",
    author_email="lars@yencken.org",
    license="ISC",
    long_description=open('README.rst').read(),
    packages=[
        'referredby',
    ],
    test_suite='test_referredby',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)

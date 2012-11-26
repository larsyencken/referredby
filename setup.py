# -*- coding: utf-8 -*-
#
#  setup.py
#  referredby
#

"""
Packaging for the referredby project.
"""

from setuptools import setup

VERSION = '0.1.0'

setup(
        name='referredby',
        description="Parsing referrer URLS for common search engines.",
        url="http://bitbucket.org/larsyencken/referredby/",
        version=VERSION,
        author="Lars Yencken",
        author_email="lars@yencken.org",
        license="ISC",
        long_description=open('README.rst').read(),
        packages=[
            'referredby',
        ],
    )
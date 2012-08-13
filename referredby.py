# -*- coding: utf-8 -*-
#
#  referredby.py
#  referredby
#

"""
Methods for determining who referred you.
"""

from collections import namedtuple
import urlparse

SearchEngine = namedtuple('SearchEngine', 'name domain keywords')
UnknownSource = namedtuple('UnknownSource', 'url')

def who(url):
    parts = urlparse.urlparse(url)
    domain = parts.netloc
    query = urlparse.parse_qs(parts.query)

    if 'google' in domain:
        if 'q' in query:
            return SearchEngine('Google', domain, query['q'][0].split(' '))
        return SearchEngine('Google', domain, [])

    return UnknownSource(url)

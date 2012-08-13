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

import engines

def who(url):
    "Try to parse the referrer url into a search engine and query terms."
    parts = urlparse.urlparse(url)
    domain = parts.netloc
    query = urlparse.parse_qs(parts.query)

    enginedef = engines.search.get(domain)
    if not enginedef:
        return UnknownSource(url)

    if enginedef.param in query:
        return SearchEngine(enginedef.name, domain,
                query[enginedef.param][0].split(' '))

    return SearchEngine(enginedef.name, domain, [])

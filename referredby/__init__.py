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
MailProvider = namedtuple('MailProvider', 'name')

import engines


def who(url):
    "Try to parse the referrer url into a search engine and query terms."
    parts = urlparse.urlparse(url)
    domain = parts.netloc
    query = urlparse.parse_qs(parts.query)

    result = engines.detect_any(domain)
    if isinstance(result, engines.EngineDef):
        keywords = query.get(result.param, [''])[0].split(' ') or None
        return SearchEngine(result.name, domain, keywords)

    elif isinstance(result, engines.MailDef):
        return MailProvider(result.name)

    return result

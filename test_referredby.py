# -*- coding: utf-8 -*-
#
#  test_referredby.py
#  referredby
#

import unittest

import referredby


class SearchEngineTestCase(unittest.TestCase):
    def test_google(self):
        url = 'http://www.google.com/aclk?sa=l&ai=c0564f78eeb0f4287b645d1be6d7fd5a&sig=81014def7eff1c830904851cbe03b917&ved=d53c790199a166e45ef51223996c1fe4&adurl=http://my.domain.com/%3Fad%26utm_medium%3Dcpc%26utm_source%3Dadwords%2Bsearch%26utm_campaign%3Dmycompany%2BBranded%2B-%2BUS%26utm_content%3Dterm1%2Bterm2%2B-%2BExact%26utm_creative%3D13752172593%26utm_target%3D%26utm_term%3Dterm1%2520term2%26utm_placement%3D&rct=j&q=term1+term2'  # nopep8

        self.assertEqual(
                referredby.who(url),
                referredby.SearchEngine('Google', 'www.google.com',
                    ['term1', 'term2']),
            )

    def test_google_2(self):
        url = 'http://www.googleadservices.com/pagead/aclk?q=99+designs'
        self.assertEqual(
                referredby.who(url),
                referredby.SearchEngine('Google Adwords', 'www.googleadservices.com',
                    ['99', 'designs']),
            )

    def test_yahoo(self):
        url = 'http://id.search.yahoo.com/search?fr=mkg030&p=term1%20term2'

        self.assertEqual(
                referredby.who(url),
                referredby.SearchEngine(
                    'Yahoo! Indonesia',
                    'id.search.yahoo.com',
                    ['term1', 'term2'],
                ),
            )

    def test_yahoo_unknown(self):
        url = 'http://frank.search.yahoo.com/search?fr=mkg030&p=term1%20term2'

        self.assertEqual(
                referredby.who(url),
                referredby.SearchEngine(
                    'Yahoo!',
                    'frank.search.yahoo.com',
                    ['term1', 'term2'],
                ),
            )

    def test_yahoo_mail(self):
        url = 'http://some.subdomain.mail.yahoo.net/some/path'

        self.assertEqual(
                referredby.who(url),
                referredby.MailProvider('Yahoo! Mail'),
            )


def suite():
    return unittest.makeSuite(SearchEngineTestCase)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run(suite())

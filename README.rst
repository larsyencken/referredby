referredby
==========

.. image:: https://travis-ci.org/larsyencken/referredby.png

A Python module for parsing referrer URLs, in particular for common search engines.

It's main entry point is the ``referredby.who`` method::

    >>> import referredby
    >>> referredby.who('http://id.search.yahoo.com/search?fr=mkg030&p=friendly%20cat')
    SearchEngine(name='Yahoo! Indonesia', domain='id.search.yahoo.com', keywords=['friendly', 'cat'])

The list of search engines that it matches is borrowed from Spiros Denaxas's `URI::ParseSearchString <https://github.com/spiros/URI-ParseSearchString>`_ project.

Release notes
=============

0.1.4
-----

- Add a bunch of new Google country domains
- Support Python 3

0.1.3
-----

- Add ``googleadservices.com`` domain

0.1.2
-----

- Improve matching of Yahoo mail
- Add mail engine matching to the ``who()`` method

0.1.1
-----

- Add more flexible matching of Yahoo search domains


.. image:: https://d2weczhvl823v0.cloudfront.net/larsyencken/referredby/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free


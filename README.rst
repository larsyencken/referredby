referredby
==========

A Python module for parsing referrer URLs, in particular for common search engines.

It's main entry point is the ``referredby.who`` method::

    >>> import referredby
    >>> referredby.who('http://id.search.yahoo.com/search?fr=mkg030&p=friendly%20cat')
    SearchEngine(name='Yahoo! Indonesia', domain='id.search.yahoo.com', keywords=['friendly', 'cat'])

The list of search engines that it matches is borrowed from Spiros Denaxas's `URI::ParseSearchString <https://github.com/spiros/URI-ParseSearchString>`_ project.

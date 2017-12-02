Granblue Fantasy - Back Me Up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crawl and save ``I need backup!`` related data from Twitter stream API.

Usage
-----
You have to apply a `Twitter app <https://apps.twitter.com>`_ first,
then put the authenticate data in ``auth.ini`` under ``gbf_backmeup`` directory:

.. code-block:: ini

    [AUTH]
    consumer key = xxxxxxxxxxxxxxx
    consumer secret = xxxxxxxxxxxxxxxx
    token = xxxxxxxxxxxxxxxxx
    token secret = xxxxxxxxxxxxxxxx

``$ make model`` - start to create table schema.

``$ make crawl`` - start to crawl data from twitter stream API,
and save them in database.

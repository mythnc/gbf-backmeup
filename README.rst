Granblue Fantasy - Back Me Up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crawl and save ``I need backup!`` related data from Twitter stream API.

Prerequisite
------------

You have to apply a `Twitter app <https://apps.twitter.com>`_ first,
then put the authenticate data in ``auth.ini`` under ``gbf_backmeup`` directory:

.. code-block:: ini

    [AUTH]
    consumer key = xxxxxxxxxxxxxxx
    consumer secret = xxxxxxxxxxxxxxxx
    token = xxxxxxxxxxxxxxxxx
    token secret = xxxxxxxxxxxxxxxx

Usage
-----

Create table schema and predefined dataset:

``$ make model``

or

.. code-block: python

    from gbf_backmeup import api
    api.model()

Crawl ``I need backup!`` related data from twitter stream API, and save them in database:

``$ make crawl``

or

.. code-block: python

    from gbf_backmeup import api
    api.crawl()

It will continuously crawl data from twitter unless interrupted manually.

Find battles you want to help:

.. code-block: python

    from gbf_backmeup import api
    boss_name = 'Luminiera Omega'
    boss_level = 75
    api.find(boss_name, boss_level)

Currently, because there is no thread design, it is suggested execute ``make crawl`` and find battles simultaneously and in diffenet processes.

Wipe out your granblue fantansy related tweets and battle data in database:

``$ make wipeout``

or

.. code-block: python

    from gbf_backmeup import api
    api.wipeout()

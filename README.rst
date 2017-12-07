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

.. code-block:: python

    from gbf_backmeup import model
    model()

Crawl ``I need backup!`` related data from twitter stream API, and save them in database:

``$ make crawl``

or

.. code-block:: python

    from gbf_backmeup import crawl
    crawl()

It will continuously crawl data from twitter unless interrupted manually.

Search battles you want to help:

.. code-block:: python

    from gbf_backmeup import search_battles
    boss_name = 'Luminiera Omega'
    boss_level = 75
    search_battles(boss_name, boss_level)

Currently, because there is no thread design,
it is suggested execute ``make crawl`` and find battles simultaneously and in diffenet processes.

You could also use ``search_battles_example.py`` as an example.

Wipe out your granblue fantansy related tweets and battle data in database:

``$ make wipeout``

or

.. code-block:: python

    from gbf_backmeup import wipeout
    wipeout()

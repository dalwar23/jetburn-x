JETBURN
=======
Airline tickets explorer program

.. warning::

   This is not a flight ticket booking system

Installation
------------
.. code-block:: python

    pip install jetburn

or

.. code-block:: python

   python setup.py install

Usage
-----
After installation, type in a terminal

.. code-block:: shell

   jetburn

To get help please type

.. code-block:: shell

   jetburn --help

To see the valid currency list, type

.. code-block:: shell

   jetburn --info currency

To find airports by city name, use

.. code-block:: shell

   jetburn --find-airport london

This will show all the airports and their ``IATA`` codes within ``LONDON`` area.

To see preferred number of results use `-r` flag followed by
an integer. Default is set to 5.

.. code-block:: shell

   jetburn -r 12

This will show 12 results for that particular flight search.

Change Log
----------
version v1.0
^^^^^^^^^^^^
1. One way flight ticket fare explorer
2. Find airport by city name
3. Find valid currencies list
4. User defined currency and conversion between EURO
5. User defined display list (number of search results shown on screen)
6. Single mode execution

Bug Report
----------
`dalwar.hossain@protonmail.com <mailto:dalwar.hossain@protonmail.com>`_


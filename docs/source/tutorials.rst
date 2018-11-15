Tutorials
=========

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

   jetburn --currency-info all

To find airports by city name, use

.. code-block:: shell

   jetburn --find-airport london

This will show all the airports and their ``IATA`` codes within ``LONDON`` area.

To see preferred number of results use `-r` flag followed by
an integer. Default is set to ``5`` and maximum is ``200``.

.. code-block:: shell

   jetburn -r 10

This will show 10 results for that particular flight search.

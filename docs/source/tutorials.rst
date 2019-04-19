Tutorials
=========

Usage
-----
After installation, check the installation

.. code-block:: shell

   jetburn --version

Get full information about ``jetburn``

.. code-block:: shell

    jetburn-info

To get help please type

.. code-block:: shell

   jetburn --help

To start the app, type

.. code-block:: shell

    jetburn

To find airports by city name, use

.. code-block:: shell

   jetburn --find-airport london

This will show all the airports and their ``IATA`` codes within ``LONDON`` area.

To see preferred number of results use `-r` flag followed by
an integer. Default is set to ``5`` and maximum is ``200``.

.. code-block:: shell

   jetburn -r 10

This will show 10 results for that particular flight search.

To see the price in desired currency please type

.. code-block:: shell

    jetburn -c <desired_currency_code>

How to get desired currency code? To see the valid currency list, type

.. code-block:: shell

   jetburn --currency-info all

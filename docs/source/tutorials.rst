Tutorials
=========

Usage
-----
After installation, check the installation

.. code-block:: shell

   jetburn --version

.. code-block:: python

    2.1.0

Get full information about ``jetburn``

.. code-block:: shell

    jetburn-info

.. code-block:: python

    » jetburn-info
    ✔ Package: jetburn
    ✔ Version: 2.1.0
    ✔ License: LGPL-3.0
    ℹ Author: Dalwar Hossain (dalwar.hossain@protonmail.com)

To get help, type

.. code-block:: shell

   jetburn --help

.. code-block:: python

    » jetburn --help
    usage: jetburn [-h] [-m MODE] [-c CURRENCY_CODE] [-r RESULTS]
                   [--valid-currency VALID_CURRENCY] [--find-airport CITY_NAME]
                   [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -m MODE, --mode MODE  Execution mode of the program.
                            Compact[c/compact](default), Advanced[a/advanced] and
                            Expert [e/expert]. Usage: jetburn -m e OR jetburn -m
                            expert
      -c CURRENCY_CODE, --currency CURRENCY_CODE
                            Three letter currency code.[EUR], USD, AUD, CAD, RON,
                            PLN etc. Usage: jetburn -c USD
      -r RESULTS, --result RESULTS
                            Number of results to show per search. Default is [5]
                            Usage: jetburn -r 10
      --valid-currency VALID_CURRENCY
                            Displays if the currency is valid or not for this
                            program. (To be used with -c flag) Usage: jetburn
                            --valid-currency <ISO_4217_currency_code>
      --find-airport CITY_NAME
                            Finds airport names and IATA code by city name. Usage:
                            jetburn --find-airport <city_name>
      -v, --version         Shows current version of jetburn, Usage: jetburn
                            -v/--version

To start the app, type

.. code-block:: shell

    jetburn

.. code-block:: python

    » jetburn
         ________     ___________
         ______(_)______  /___  /_____  _______________
         _____  /_  _ \  __/_  __ \  / / /_  ___/_  __ \
         ____  / /  __/ /_ _  /_/ / /_/ /_  /   _  / / /
         ___  /  \___/\__/ /_.___/\__,_/ /_/    /_/ /_/
         /___/

    +----------------------------------------------------------+
    | Airline ticket explorer program [19-April-2019 19:19:39] |
    | Author: Dalwar Hossain (dalwar.hossain@protonmail.com)   |
    | Version: 2.1.0 / License: LGPL-3.0                       |
    | Need help? jetburn -h/--help                             |
    +----------------------------------------------------------+
    |                   ..:: DISCLAIMER ::..                   |
    | This program is not an airline ticket booking system and |
    | has no affiliation with any airlines or ticketing agents |
    +----------------------------------------------------------+
    ℹ Initializing program.....
    ℹ Preparing airbase.....
    ? Round Trip?  (Y/n)

To find airports by city name, use

.. code-block:: shell

   jetburn --find-airport london

This will show all the airports and their ``IATA`` codes within ``LONDON`` area.

.. code-block:: python

    » jetburn --find-airport london
         ________     ___________
         ______(_)______  /___  /_____  _______________
         _____  /_  _ \  __/_  __ \  / / /_  ___/_  __ \
         ____  / /  __/ /_ _  /_/ / /_/ /_  /   _  / / /
         ___  /  \___/\__/ /_.___/\__,_/ /_/    /_/ /_/
         /___/

    +----------------------------------------------------------+
    | Airline ticket explorer program [19-April-2019 19:21:36] |
    | Author: Dalwar Hossain (dalwar.hossain@protonmail.com)   |
    | Version: 2.1.0 / License: LGPL-3.0                       |
    | Need help? jetburn -h/--help                             |
    +----------------------------------------------------------+
    |                   ..:: DISCLAIMER ::..                   |
    | This program is not an airline ticket booking system and |
    | has no affiliation with any airlines or ticketing agents |
    +----------------------------------------------------------+
    ℹ Collecting airport information.....
    ℹ Requesting IATA airport codes.....
    ✔ IATA airport codes received
    +-----------------------------------+---------------------+-------------+
    | Airport Name                      | City                | IATA Code   |
    +===================================+=====================+=============+
    | London Airport                    | London              | YXU         |
    +-----------------------------------+---------------------+-------------+
    | London Luton Airport              | London              | LTN         |
    +-----------------------------------+---------------------+-------------+
    | London Biggin Hill Airport        | London              | BQH         |
    +-----------------------------------+---------------------+-------------+
    | London Gatwick Airport            | London              | LGW         |
    +-----------------------------------+---------------------+-------------+
    | London City Airport               | London              | LCY         |
    +-----------------------------------+---------------------+-------------+
    | London Heathrow Airport           | London              | LHR         |
    +-----------------------------------+---------------------+-------------+
    | London Stansted Airport           | London              | STN         |
    +-----------------------------------+---------------------+-------------+
    | RAF Northolt                      | London              | NHT         |
    +-----------------------------------+---------------------+-------------+
    | Ben Schoeman Airport              | East London         | ELS         |
    +-----------------------------------+---------------------+-------------+
    | Groton New London Airport         | Groton (New London) | GON         |
    +-----------------------------------+---------------------+-------------+
    | London-Corbin Airport/Magee Field | London              | LOZ         |
    +-----------------------------------+---------------------+-------------+

To see preferred number of results use `-r` flag followed by
an integer. Default is set to ``5`` and maximum is ``200``.

.. code-block:: shell

   jetburn -r 10

This will show 10 results for that particular flight search.

To see the price in desired currency please type

.. code-block:: shell

    jetburn -c <desired_currency_code>

The output of previous two commands will look something like this -

.. code-block:: python

    » jetburn -r 10 -c USD
         ________     ___________
         ______(_)______  /___  /_____  _______________
         _____  /_  _ \  __/_  __ \  / / /_  ___/_  __ \
         ____  / /  __/ /_ _  /_/ / /_/ /_  /   _  / / /
         ___  /  \___/\__/ /_.___/\__,_/ /_/    /_/ /_/
         /___/

    +----------------------------------------------------------+
    | Airline ticket explorer program [19-April-2019 19:23:51] |
    | Author: Dalwar Hossain (dalwar.hossain@protonmail.com)   |
    | Version: 2.1.0 / License: LGPL-3.0                       |
    | Need help? jetburn -h/--help                             |
    +----------------------------------------------------------+
    |                   ..:: DISCLAIMER ::..                   |
    | This program is not an airline ticket booking system and |
    | has no affiliation with any airlines or ticketing agents |
    +----------------------------------------------------------+
    ℹ Initializing program.....
    ℹ Preparing airbase.....
    ? Round Trip?  No
    ? Origin airport:  FRA
    ? Destination airport:  BCN
    ? Fly out date (dd/mm/yyyy):  12/12/2019
    ? Adults (>16 Years)?  1
    ? Teens (12-15 Years)?  0
    ? Children (2-11 Years)?  0
    ? Infants (<2 Years)?  0
    ℹ Getting ready for take off.....
    ℹ Requesting to takeoff.....
    ✔ Cleared for takeoff.....
    +------------------+-----------------+--------+------------------+-----------------+-------+
    | Thu 12 Dec 07:00 | FRA---PMI---BCN | 7h 20m | Thu 12 Dec 14:20 | 69 USD / 61 EUR | FR-FR |
    +------------------+-----------------+--------+------------------+-----------------+-------+
    +------------------+-----------------+--------+------------------+-----------------+-------+
    | Thu 12 Dec 07:00 | FRA---PMI---BCN | 7h 10m | Thu 12 Dec 14:10 | 70 USD / 62 EUR | FR-VY |
    +------------------+-----------------+--------+------------------+-----------------+-------+
    +------------------+-----------+--------+------------------+-----------------+----+
    | Thu 12 Dec 16:10 | FRA---BCN | 2h 20m | Thu 12 Dec 18:30 | 73 USD / 65 EUR | FR |
    +------------------+-----------+--------+------------------+-----------------+----+
    +------------------+-----------------+---------+------------------+-----------------+-------+
    | Thu 12 Dec 20:30 | FRA---DUB---BCN | 13h 15m | Fri 13 Dec 09:45 | 88 USD / 78 EUR | FR-FR |
    +------------------+-----------------+---------+------------------+-----------------+-------+
    +------------------+-----------------+-------+------------------+-----------------+-------+
    | Thu 12 Dec 16:55 | HHN---NAP---BCN | 7h 4m | Thu 12 Dec 23:59 | 92 USD / 82 EUR | FR-VY |
    +------------------+-----------------+-------+------------------+-----------------+-------+
    +------------------+-----------------+---------+------------------+-----------------+-------+
    | Thu 12 Dec 16:55 | HHN---NAP---BCN | 19h 30m | Fri 13 Dec 12:25 | 93 USD / 83 EUR | FR-FR |
    +------------------+-----------------+---------+------------------+-----------------+-------+
    +------------------+-----------------+---------+------------------+------------------+-------+
    | Thu 12 Dec 07:00 | HHN---RAK---BCN | 16h 40m | Thu 12 Dec 23:40 | 104 USD / 93 EUR | FR-VY |
    +------------------+-----------------+---------+------------------+------------------+-------+
    +------------------+-----------------+--------+------------------+------------------+-------+
    | Thu 12 Dec 09:20 | FRA---LIS---BCN | 7h 30m | Thu 12 Dec 16:50 | 109 USD / 96 EUR | LH-VY |
    +------------------+-----------------+--------+------------------+------------------+-------+
    +------------------+-----------------+---------+------------------+------------------+-------+
    | Thu 12 Dec 17:30 | HHN---PMO---BCN | 23h 35m | Fri 13 Dec 17:05 | 108 USD / 96 EUR | FR-VY |
    +------------------+-----------------+---------+------------------+------------------+-------+

How to get desired currency code? To see the valid currency list, type

.. code-block:: shell

   jetburn --valid-currency AUD

This will check if the currency is valid not not (for ``jetburn`` program currency conversion)

.. code-block:: python

   » jetburn --valid-currency NZD
         ________     ___________
         ______(_)______  /___  /_____  _______________
         _____  /_  _ \  __/_  __ \  / / /_  ___/_  __ \
         ____  / /  __/ /_ _  /_/ / /_/ /_  /   _  / / /
         ___  /  \___/\__/ /_.___/\__,_/ /_/    /_/ /_/
         /___/

    +----------------------------------------------------------+
    | Airline ticket explorer program [23-April-2019 21:56:49] |
    | Author: Dalwar Hossain (dalwar.hossain@protonmail.com)   |
    | Version: 2.1.0 / License: LGPL-3.0                       |
    | Need help? jetburn -h/--help                             |
    +----------------------------------------------------------+
    |                   ..:: DISCLAIMER ::..                   |
    | This program is not an airline ticket booking system and |
    | has no affiliation with any airlines or ticketing agents |
    +----------------------------------------------------------+
    ℹ Evaluating currency input.....
    ✔ [NZD] is a valid currency


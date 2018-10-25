JETBURN
=======
Airline ticket explorer program

.. image:: https://img.shields.io/badge/license-LGPL3.0-blue.svg
    :alt: License
    :target: https://opensource.org/licenses/LGPL-3.0

.. image:: https://badge.fury.io/py/jetburn.svg
    :alt: Pypi Version
    :target: https://pypi.org/project/jetburn/

.. image:: https://travis-ci.org/dharif23/jetburn.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/dharif23/jetburn

Description
-----------
Jetburn is an airline ticket explorer program designed to find the
lowest priced tickets from origin airport to destination airport. This program is not
an airline ticket booking system and has **no partnership** with any airlines whatsoever.

.. warning::

   This is not a flight ticket booking system

Installation
------------
Linux/Mac
^^^^^^^^^
Considering that ``pip`` is configured:

.. code-block:: python

    pip install jetburn

or

.. code-block:: python

   python setup.py install

Windows
^^^^^^^
Windows terminal (cmd/power shell) doesn't support all the unicode codecs and To get the best results -
please use a terminal emulator like, cmder [`Download Cmder <http://cmder.net/>`_] or
ConEmu [`Download ConEmu <https://conemu.github.io/>`_]. Please use *<xterm>* color scheme from `settings`
menu, for the best visual representation of the program.

Considering ``python`` is installed and ``pip`` is configured.
(*If pip is not configured, please configure ``pip`` first. For installing
``python`` and configuring ``pip`` see the instructions at the bottom of
this page.*)

Open Cmder/ConEmu and Type:

.. code-block:: python

   pip install jetburn

Or

.. code-block:: python

   python setup.py install

This command should install ``jetburn`` with all the required dependencies.

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
an integer. Default is set to 5.

.. code-block:: shell

   jetburn -r 12

This will show 12 results for that particular flight search.

Change Log
----------
Please refer to ``changelog.rst``

Bug Report
----------
`dalwar.hossain@protonmail.com <mailto:dalwar.hossain@protonmail.com>`_


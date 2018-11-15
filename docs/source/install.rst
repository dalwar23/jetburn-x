Install
=======
JetBurn (``jetburn``) requires Python 2.7, 3.5, 3.6 or 3.7. If you do not already have a Python environment configured
on your computer, please see the `Python <https://www.python.org>`_ page for instructions on installing Python
environment.

.. note::
   if you are on Windows and want to install optional packages (e.g., scipy) then you will need to install a python
   distribution such as `Anaconda <https://www.anaconda.com>`_, `Enthought Canopy <https://www.enthought.com/product/canopy>`_
   or `Pyzo <https://www.pyzo.org>`_. If you use one of these Python distributions, please refer to their online
   documentation.

Assuming that the default python environment is already configured on your computer and you intend to install
``jetburn`` inside of it. To create and work with Python virtual environments, please follow instructions on
`venv <https://docs.python.org/3/library/venv.html>`_ and
`virtual environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

To start the installation process, please make sure the latest version of ``pip`` (Python package manager) is installed.
If ``pip`` is not installed, please refer to the `Pip documentation <https://pip.pypa.io/en/stable/installing/>`_ and
install ``pip`` first.

Linux/macOS
-----------
Install the latest release of ``jetburn`` with ``pip``:

.. code-block:: python

   pip install jetburn

To upgrade to a newer version use the ``--upgrade`` flag:

.. code-block:: python

   pip install --upgrade jetburn

If system wide installation is not possible for permission reasons, use ``--user`` flag to install ``jetburn`` for
current user

.. code-block:: python

   pip install --user jetburn

.. note::
   If you get an error message while installing in macintosh computer (macOS). Please try to use the following command.
   ``pip install jetburn --ignore-installed six``
   Please remember at the time of writing this documentation, v1.4 doesn't fully support macOS. Send any bug reports to
   `dalwar.hossain@protonmail.com<>dalwar.hossain@protonmail.com`_

Windows
-------
Windows terminal (cmd/power shell) doesn't support all the unicode codecs and To get the best results -
please use a terminal emulator like, cmder [`Download Cmder <http://cmder.net/>`_] or
ConEmu [`Download ConEmu <https://conemu.github.io/>`_]. Please use *<xterm>* color scheme from `settings`
menu, for the best visual representation of the program.

Considering ``python`` is installed and ``pip`` is configured.

Open Cmder/ConEmu and Type:

.. code-block:: python

   pip install jetburn

Or

.. code-block:: python

   python setup.py install

This command should install ``jetburn`` with all the required dependencies.

Install from Github
-------------------
Alternatively, ``jetburn`` can be installed manually by downloading the current version from
`GitHub <https://github.com/dharif23/jetburn>`_ or `PyPI <https://pypi.org/project/jetburn/>`_.
To install a downloaded versions, please unpack it in a preferred directory and run the following commands at the top
level of the directory:

.. code-block:: python

   pip install .

or run the following:

.. code-block:: python

   python setup install

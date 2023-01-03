Welcome to User Identification System's documentation!
======================================================
User Identifier System is a tool you can use to create a powerful login and signup system.
This package contains many helpful tools in order to create a robust login and signup system.
It encrypts the user's important crendentials and stores them in a database.

.. toctree::
   :maxdepth: 3
   :caption: Table of contents:

   ./pages/basic/homepage.rst
   ../pages/extraPass/homepage.rst

Installation
------------
.. note:: This package requires a python version of >= 3.6.

Follow this link to view the pypi repository: https://pypi.org/project/user-Identification-System/

The package also required a module that handles and encrypts passwords ==> `pypasstools` [#F1]_. See its
pypi repository: https://pypi.org/project/pypasstools/

Use the following command to install the package along with its dependencies:

.. code-block:: console

    pip install user-Identification-System
    pip install pypasstools

To import ``user-Identification-System`` in your python code, use the following code-snippet:

.. code-block:: python

   import UserIdentificationSystem as uis

Version details
---------------
**Current version:** 0.0.91

#. `autotask` feature was removed.
#. System can now log user's actions and save them in a `log.txt` file.
#. Contains important bugs and error fixes.

.. _Github: https://github.com/Ayaan-Imran/User-Indentifier-System
.. _`Pypi repository`: https://pypi.org/project/user-Identification-System/
.. _`Pypasstools Pypi repo`: https://pypi.org/project/pypasstools/

Links and references
--------------------
- Github_
- `Pypi repository`_
- `Pypasstools Pypi repo`_
- miskiacuberayaan2509@gmail.com

.. rubric:: Footnotes

.. [#F1] If the module ``pypasstools`` is not installed, the program will be end, displaying an error message that instructs the user to install pypasstools.

Basic login and signup system
=============================
The ``UserIdentificationSystem`` package has a class that allows users
to register, login, and signup using a username and 1 password.

This class is called ``Basic()``

Parameters ``Basic()``
----------------------
+------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
| Parameter  | Default value       | Description                                                                                                                                                | Data Type  |
+============+=====================+============================================================================================================================================================+============+
| filename   | REQUIRED PARAMETER  | The name of the database the user's credentials will be stored. The Basic() class will automatically create and initialise a new database with this name.  | string     |
+------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
| log        | False               | If set to True, the system will automatically log user's actions to a "log.txt" file.                                                                      | boolean    |
+------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+

Methods ``Basic()``
-------------------
Simplified version
******************

+-----------------------------+----------------------------------------------------------------------------------------------------------+
| Method                      | Short description                                                                                        |
+=============================+==========================================================================================================+
| :ref:`get_log()`            | This function gets all the logs recorded by the system.                                                  |
+-----------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`get_usernames()`      | This function gets all the usernames that have been registered in the system.                            |
+-----------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`username_is_valid()`  | This function is to check if a username is valid or not.                                                 |
+-----------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`signup()`             | This function will register a new user in the database.                                                  |
+-----------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`login()`              | This function will compare the username and password with the system.                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`deluser()`            | This function will delete a user from the system.                                                        |
+-----------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`secure()`             | This function is vital to be present at the end of your code to securely close the database connection.  |
+-----------------------------+----------------------------------------------------------------------------------------------------------+

.. _get-log-ref:

get_log()
*********
If the ``self.log`` class variable is set to true during the setup, a ``log.txt`` file will
automatically be generated along with the database file. *This can also be done optionally
using the create_log() method*.

**Returns:**
   This method returns a list that contains each log (represented as a single dictionary).

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.db", log=True) # Log must be True
   logs = controller.get_log() # Returns the logs from the log file.

.. _get-useranmes-ref:

get_usernames()
***************
The ``get_usernames()`` method is a useful feature that provides you with all the registered
and valid users in the system.

**Returns:**
   This method returns a list containing all the usernames registered in the system.

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.db")
   log = controller.get_usernames() # Returns a list with all the registered usernames.

.. _username-is-valid-ref:

username_is_valid()
*******************
The ``username_is_valid()`` method checks whether or not a username is valid. The username is
valid if it is not already taken by another user.

+------------+------------+
| Parameter  | Data type  |
+============+============+
| username   | String     |
+------------+------------+

**Returns:**
   Returns a boolean depending on if the username provided is valid or not.

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.db")

   # Returns a boolean depending on if the username is valid or not.
   log = controller.username_is_valid("uis learner")

.. _signup-ref:

signup()
********
The ``signup()`` method allows you to register users into the system.

+------------+-------------------------------------------------+------------+
| Parameter  | Description                                     | Data type  |
+============+=================================================+============+
| username   | A unique name the user will be represented by.  | String     |
+------------+-------------------------------------------------+------------+
| password   | The authentication key the user has selected.   | String     |
+------------+-------------------------------------------------+------------+

**Returns:**
   This method returns a boolean depending on if the process was executed successfully or not.

   If this method returns a ``False``, it could occur because:

   #. The username was invalid (It was already in use by another user).
   #. An error occurred with the database (Rare case).

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.db", log=True) # Log is optional

   # If log is set to True...
   # ...it will automatically log a signup statement (both if it failed or if it was successful.
   success = controller.signup("uis learner", "password123") # Will return True if process was successful

.. _login-ref:

login()
*******
The ``login()`` method compares the user's credentials with the credentials stored in the database.

+------------+---------------------------------------------------+------------+
| Parameter  | Description                                       | Data type  |
+============+===================================================+============+
| username   | The unique name the user chose while signing up.  | String     |
+------------+---------------------------------------------------+------------+
| password   | The password assigned to that specific username.  | String     |
+------------+---------------------------------------------------+------------+

**Returns:**
   This method returns a boolean depending on the validity of the user's credentials.

   If this method returns ``False``, it could occur because of the following reasons:

   1. The username passed in does not exist.
   2. The user's credentials are invalid.
   3. There is an error with the database (Rare case).

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.db", log=True) # Log is optional

   # If log is set to True...
   # ...it will automatically log a login statement (both if it failed or if it was successful).
   success = controller.login("uis_learner", "password123")

.. _deluser-ref:

deluser()
*********
The ``deluser()`` method deletes a user from the database, after confirming the validity of the user.

+------------+---------------------------------------------------+------------+
| Parameter  | Description                                       | Data type  |
+============+===================================================+============+
| username   | The unique name the user chose while signing up.  | String     |
+------------+---------------------------------------------------+------------+
| password   | The password assigned to that specific username.  | String     |
+------------+---------------------------------------------------+------------+

**Returns:**
   This method returns a boolean depending on the validity of the user's credentials.

   If this method returns ``False``, it could occur because of the following reasons:

   1. The username passed in does not exist.
   2. The user's credentials are invalid.
   3. There is an error with the database (Rare case).

.. note:: If ``log=True`` during the setup of the system, then a delete statement along with a login statement will be logged into the ``log.txt`` file.

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.md", log=True) # Log is optional
   success = controller.deluser("uis learner", "password123")

.. _secure-ref:

secure()
********
The ``secure()`` method is essential to be present at the end of your code. It is responsible to close the
connection of the databse. If the databse is not closed, it stays open until it goes out of scope.

**Returns:**
   This method returns ``True`` if the database was successfully closed.

.. code-block:: python
   :linenos:

   controller = Basic("mydatabase.db") # This method does not log
   # login(), signup(), deluser(), get_usernames(), username_is_valid()...
   # ...can be called here.
   controller.secure()

Class variables ``Basic()``
---------------------------
Simple overview
***************

+------------------------+----------------------------------------------------+------------+
| Class variable         | Description                                        | Data type  |
+========================+====================================================+============+
| self.log               | Configuration for ``log`` at setup of the system.  | Boolean    |
+------------------------+----------------------------------------------------+------------+
| self.filename          | The filename of the database.                      | String     |
+------------------------+----------------------------------------------------+------------+
| :ref:`self.username`   | The latest username used in the system.            | String     |
+------------------------+----------------------------------------------------+------------+

.. _self.username-ref:

self.username
*************
The ``username`` class variable contains the latest username used in the system.
The ``username`` is updated in the following cases:

1. If the ``signup()`` method returns ``True``.
2. If the username passed in the ``login()`` method is valid.
3. If the username passed in the ``deluser()`` method is valid.

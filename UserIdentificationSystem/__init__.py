import sqlite3
import datetime
import os

try:
    import passtools

except ModuleNotFoundError:
    print("\u001b[31m" + "[MODULE NOT FOUND ERROR]" + "\u001b[0m")
    print()
    negative = "\u001b[36m" + "[" + "\u001b[0m" + "\u001b[31m" + "!" + "\u001b[0m" + "\u001b[36m" + "]" + "\u001b[0m" + " "
    neutral = "\u001b[36m" + "[" + "\u001b[0m" + "\u001b[33m" + "-" + "\u001b[0m" + "\u001b[36m" + "]" + "\u001b[0m" + " "
    print(negative + "Module " + "\u001b[30m" + "pypasstools" + "\u001b[0m" + " is not installed.")
    print(neutral + "Use the following command to install the missing package:")
    print("    " + "\u001b[40m" + "\u001b[37m" + "pip install pypasstools" + "\u001b[0m")
    quit()

__version__ = "0.0.9"
__doc__ = "User Identification System is a package that will allow you to create complex login and registration system in a simple way"
__author__ = "Ayaan Imran"
__gitgub__ = "https://github.com/Ayaan-Imran/User-Indentifier-System"

class Basic():
    __connection = None
    __c = None

    def __init__(self, filename: str, log: bool = False):
        self.username = None
        self.log = log

        if self.log == True:
            self.create_log()

        global __connection
        global __c

        # Clean the filename
        if filename[-3:] != ".db":
            filename = filename + ".db"
        self.filename = filename  # Make the filename variable global within the instance

        __connection = sqlite3.connect(filename)
        __c = __connection.cursor()
        __c.execute("""CREATE TABLE IF NOT EXISTS account (
            username text,
            password text
        )
        """)
        __connection.commit()

    def create_log(self):
        """
        This functions creates a log file that notes down any login or registered users with its respected time.
        :return: Returns a boolean depending on if the log file has been created.
        """

        if os.path.exists("log.txt") == False:
            with open("log.txt", "w") as _:
                return True

        else:
            return False

    def get_log(self):
        """
        This function gets all the logs recorded by the system
        :return: A list with each log appended as one dictionary. Dictionary keys: {num, datetime, action, username, databasenum}
        """

        if self.log == False:
            return False

        # Open log file and note down the contents
        with open("log.txt", "r") as logfile:
            lines = logfile.readlines() # Get all the log file lines

            # Loop through all the lines
            logdictslist = []
            for line in lines:
                dictionary = {} # Reset dict variable

                line = line.strip("\n") # Strip the line from new line characters
                items = line.split(",") # Get each item in the line

                dictionary["num"] = int(items[0])
                dictionary["datetime"] = items[1]
                dictionary["action"] = items[2]
                dictionary["username"] = items[3]
                dictionary["databasenum"] = int(items[4])

                logdictslist.append(dictionary) # Append the dictionary to the list

        # Return the list
        return logdictslist

    def signup(self, username: str, password: str):
        """
        This function will register a new user in the database.
        :param username: A unique name the user will be represented by.
        :param password: The authentication key the user has selected.
        :return: True if signup process is successful, False if not (Occurs when the username is already taken by another user).
        """
        global __c
        global __connection

        if self.username_is_valid(username):
            password = passtools.passhash(password, hash_strength=3)
            __c.execute("INSERT INTO account VALUES(?,?)", (username, password))
            __connection.commit()

            self.username = username

            # Add log
            if self.log == True:
                # Get number
                with open("log.txt", "r") as logfile:
                    number = len(logfile.readlines())

                # Get database number
                usernames = self.get_usernames()
                databasenum = usernames.index(username) + 1

                # Append the log in the logfile
                with open("log.txt", "a") as logfile:
                    character = ""
                    if number != 0:
                        character = "\n"

                    logline = f"{character}{number},{datetime.datetime.now()},signed up,{username},{databasenum}"
                    logfile.write(logline)

            return True
        else:
            return False

    def login(self, username: str, password: str):
        global __c
        global __connection

        # Check if username does not exist
        if username not in self.get_usernames():
            return False

        __c.execute("SELECT * FROM account")
        users = __c.fetchall()
        __connection.commit()

        password = passtools.passhash(password, hash_strength=3)
        permission = False
        for i in users:
            if (i[0] == username) and (i[1] == password):
                permission = True
                break

        self.username = username

        # Add log
        if self.log == True:
            # Get number
            with open("log.txt", "r") as logfile:
                number = len(logfile.readlines())

            # Get database number
            usernames = self.get_usernames()
            databasenum = usernames.index(username) + 1


            # Append the log in the logfile
            with open("log.txt", "a") as logfile:
                character = ""
                if number != 0:
                    character = "\n"

                if permission == True:
                    logline = f"{character}{number},{datetime.datetime.now()},logged in,{username},{databasenum}"
                else:
                    logline = f"{character}{number},{datetime.datetime.now()},logged in failed,{username},{databasenum}"

                logfile.write(logline)

        return permission

    def deluser(self, username: str, password: str):
        global __c
        global __connection

        try:
            # Get database number
            databasenum = self.get_usernames().index(username) + 1

        except ValueError:
            return False

        test = Basic(self.filename)
        if test.login(username, password): # No need to hash the password, because the login function already hashed it
            __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
            __connection.commit()

            self.username = username

            # Add log
            if self.log == True:
                # Get number
                with open("log.txt", "r") as logfile:
                    number = len(logfile.readlines())

                # Append the log in the logfile
                with open("log.txt", "a") as logfile:
                    character = ""
                    if number != 0:
                        character = "\n"

                    logline = f"{character}{number},{datetime.datetime.now()},deleted,{username},{databasenum}"
                    logfile.write(logline)

            return True

        else:
            self.username = username

            # Add log
            if self.log == True:
                # Get number
                with open("log.txt", "r") as logfile:
                    number = len(logfile.readlines())

                # Append the log in the logfile
                with open("log.txt", "a") as logfile:
                    character = ""
                    if number != 0:
                        character = "\n"

                    logline = f"{character}{number},{datetime.datetime.now()},delete process failed,{username},{databasenum}"
                    logfile.write(logline)

            return False

    def get_usernames(self):
        global __c
        global __connection

        __c.execute("SELECT username FROM account")
        lst = __c.fetchall()
        lst = [i[0] for i in lst]
        __connection.commit()

        return lst

    def username_is_valid(self, username: str):
        """
        This function is to check if a username exists or not
        :param username: To check if it is valid
        :return: A boolean depending on if it is valid or not
        """
        global __c
        global __connection

        if username in self.get_usernames():  # If username exists, then that means it is not valid
            return False
        else:
            return True  # If username does not exist, then that means username can be used and is valid

    def secure(self):
        """
        This function is vital to be present at the end of your code to securely close the database connection
        :return: Returns True if database closed successfully
        """
        global __connection
        __connection.close()
        return True

class ExtraPass():
    __connection = None
    __c = None

    def __init__(self, filename: str, log :bool = False):
        self.username = None
        self.log = log

        if self.log == True:
            self.create_log()

        global __connection
        global __c

        # Clean the filename
        if filename[-3:] != ".db":
            filename = filename + ".db"
        self.filename = filename  # Set the filename to be global within the instance

        __connection = sqlite3.connect(self.filename)
        __c = __connection.cursor()
        __c.execute("""CREATE TABLE IF NOT EXISTS account (
            username text,
            password text,
            extra text
        )""")

    def create_log(self):
        """
        This functions creates a log file that notes down any login or registered users with its respected time.
        :return: Returns a boolean depending on if the log file has been created.
        """

        if os.path.exists("log.txt") == False:
            with open("log.txt", "w") as _:
                return True

        else:
            return False

    def get_log(self):
        """
        This function gets all the logs recorded by the system
        :return: A list with each log appended as one dictionary. Dictionary keys: {num, datetime, action, username, databasenum}
        """

        if self.log == False:
            return False

        # Open log file and note down the contents
        with open("log.txt", "r") as logfile:
            lines = logfile.readlines() # Get all the log file lines

            # Loop through all the lines
            logdictslist = []
            for line in lines:
                dictionary = {} # Reset dict variable

                line = line.strip("\n")  # Strip the line from new line characters
                items = line.split(",")  # Get each item in the line

                items = line.split(",") # Get each item in the line
                dictionary["num"] = int(items[0])
                dictionary["datetime"] = items[1]
                dictionary["action"] = items[2]
                dictionary["username"] = items[3]
                dictionary["databasenum"] = int(items[4])

                logdictslist.append(dictionary) # Append the dictionary to the list

        # Return the list
        return logdictslist

    def login(self, username: str, password: str, extra: str):
        global __connection
        global __c

        # Check if username does not exist
        if username not in self.get_usernames():
            return False

        __c.execute("SELECT * FROM account")
        lst = __c.fetchall()
        __connection.commit()

        password = passtools.passhash(password, hash_strength=3)
        extra = passtools.passhash(extra, hash_strength=3)

        permission = False
        for i in lst:
            if (i[0] == username) and (i[1] == password) and (i[2] == extra):
                permission = True
                break

        self.username = username

        # Add log
        if self.log == True:
            # Get number
            with open("log.txt", "r") as logfile:
                number = len(logfile.readlines())

            # Get database number
            usernames = self.get_usernames()
            databasenum = usernames.index(username) + 1

            # Append the log in the logfile
            with open("log.txt", "a") as logfile:
                character = ""
                if number != 0:
                    character = "\n"

                if permission == True:
                    logline = f"{character}{number},{datetime.datetime.now()},logged in,{username},{databasenum}"
                else:
                    logline = f"{character}{number},{datetime.datetime.now()},logged in failed,{username},{databasenum}"

                logfile.write(logline)

        return permission

    def signup(self, username: str, password: str, extra: str):
        """
        This function will resister a new user in the database.
        :param username: A unique name the user will be represented by.
        :param password: The authentication key the user has selected.
        :param extra: The extra authentication key the user has selected
        :return: True if signup process is successful, False if not (Occurs when the username is already taken by another user).
        """
        global __connection
        global __c

        if self.username_is_valid(username) == False:  # If username is not valid, then it will return False
            return False

        else:
            password = passtools.passhash(password, hash_strength=3)
            extra = passtools.passhash(extra, hash_strength=3)

            __c.execute("INSERT INTO account VALUES (?,?,?)", (username, password, extra))
            __connection.commit()

            self.username = username

            # Add log
            if self.log == True:
                # Get number
                with open("log.txt", "r") as logfile:
                    number = len(logfile.readlines())

                # Get database number
                usernames = self.get_usernames()
                databasenum = usernames.index(username) + 1

                # Append the log in the logfile
                with open("log.txt", "a") as logfile:
                    character = ""
                    if number != 0:
                        character = "\n"

                    logline = f"{character}{number},{datetime.datetime.now()},signed up,{username},{databasenum}"
                    logfile.write(logline)

            return True

    def deluser(self, username: str = None, password: str = None, extra: str = None):
        global __c
        global __connection

        # Gets databasenum depending on if the username is valid
        try:
            # Get database number
            databasenum = self.get_usernames().index(username) + 1

        except ValueError:
            return False

        test = ExtraPass(self.filename)
        if test.login(username, password, extra):  # NOTE: No need for encryption before passing because login function already encrypts the important variables.
            __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
            __connection.commit()

            self.username = username

            # Add log
            if self.log == True:
                # Get number
                with open("log.txt", "r") as logfile:
                    number = len(logfile.readlines())

                # Append the log in the logfile
                with open("log.txt", "a") as logfile:
                    character = ""
                    if number != 0:
                        character = "\n"

                    logline = f"{character}{number},{datetime.datetime.now()},deleted,{username},{databasenum}"
                    logfile.write(logline)

            return True
        else:
            self.username = username
            # Add log
            if self.log == True:
                # Get number
                with open("log.txt", "r") as logfile:
                    number = len(logfile.readlines())

                # Append the log in the logfile
                with open("log.txt", "a") as logfile:
                    character = ""
                    if number != 0:
                        character = "\n"

                    logline = f"{character}{number},{datetime.datetime.now()},delete process failed,{username},{databasenum}"
                    logfile.write(logline)

            return False

    def get_usernames(self):
        """
        This function provides user with the registered usernames.
        :return: A list with all the registered valid usernames
        """
        global __c
        global __connection

        __c.execute("SELECT username FROM account")
        lst = __c.fetchall()
        lst = [i[0] for i in lst]
        __connection.commit()

        return lst

    def username_is_valid(self, username: str):
        """
        This function is to check if a username exists or not
        :param username: To check if it is valid
        :return: A boolean depending on if it is valid or not
        """
        global __connection
        global __c

        if username in self.get_usernames(): # If username exists, then that means it is not valid
            return False
        else:
            return True  # If username does not exist, then that means username can be used and is valid

    def secure(self):
        """
            This function is vital to be present at the end of your code to securely close the database connection
            :return: Returns True if database closed successfully
            """
        global __connection
        __connection.close()
        return True
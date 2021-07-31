import sqlite3
import secrets
import hashlib
import getpass

def encryt(prompt:str):
    return hashlib.sha256(bytes(prompt, "utf-8")).hexdigest()

class Basic():
    __connection = None
    __c = None

    def __init__(self, filename:str):
        self.username = None

        global __connection
        global __c

        # Clean the filename
        if filename[-3:] != ".db":
            filename = filename + ".db"
        self.filename = filename # Make the filename variable global within the instance

        __connection = sqlite3.connect("{}.db".format(filename))
        __c = __connection.cursor()
        __c.execute("""CREATE TABLE IF NOT EXISTS account (
            username text,
            password text
        )
        """)
        __connection.commit()

    def signup(self, username:str=None, password:str=None, autotask:bool=False):
        global __c
        global __connection

        if autotask == False:
            if self.username_exists(username):
                password = encryt(password)
                __c.execute("INSERT INTO account VALUES(?,?)", (username, password))
                __connection.commit()
                return True
            else:
                return False
        else:
            username1 = input("[+] * Please make a username: ")
            password1 = encryt(getpass.getpass("[+] * Please make a password for security: "))

            if self.username_is_valid(username1) == False: # If username is not valid, then ask again for another username
                while True:
                    username1 = input("[-] * The username you entered is already in use. Please make another one: ")
                    if self.username_is_valid(username1): # If this function returns true, that means this username is valid
                        break

            __c.execute("INSERT INTO account VALUES(?,?)", (username1, password1))
            __connection.commit()
            self.username = username1
            return True

    def login(self, username:str=None, password:str=None, autotask:bool=False):
        global __c
        global __connection

        if not autotask:
            __c.execute("SELECT * FROM account")
            users = __c.fetchall()
            __connection.commit()

            password = encryt(password)
            permission = False
            for i in users:
                if (i[0] == username) and (i[1] == password):
                    permission = True
                    break

            return permission
        else:
            username1 = input("[+] * Please enter your username: ")
            self.username = username1

            password1 = encryt(input("[+] * Please enter your password: "))

            __c.execute("SELECT * FROM account")
            users = __c.fetchall()
            __connection.commit()

            permission = False
            for i in users:
                if (i[0] == username1) and (i[1] == password1):
                    permission = True
                    break

            return permission

    def deluser(self, username:str=None, password:str=None, autotask:bool=False):
        global __c
        global __connection

        test = Basic(self.filename)
        if autotask == False:
            if test.login(username, password):
                __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
                __connection.commit()
                return True
            else:
                return False
        else:
            username = input("[+] * Please enter your username: ")
            self.username = username

            password = input("[+] * Please enter your password for confirmation: ")

            if test.login(username, password):
                password = input("[+] * Please renter your password again for confirmation: ")
                if test.login(username, password):
                    __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
                    __connection.commit()
                    return True
                else:
                    return False
            else:
                return False

    def get_usernames(self):
        global __c
        global __connection

        __c.execute("SELECT * FROM account")
        lst = __c.fetchall()
        __connection.commit()

        lst = [i[0] for i in lst]
        return lst

    def username_is_valid(self, username:str):
        global __c
        global __connection

        lst = self.get_usernames()

        if username in lst: # If username exists, then that means it is not valid
            return False
        else:
            return True # If username does not exist, then that means username can be used and is valid

    def secure(self):
        global __connection
        __connection.close()


class ExtraPass():
    __connection = None
    __c = None

    def __init__(self, filename:str):
        self.username = None

        global __connection
        global __c

        # Clean the filename
        if filename[-3:] != ".db":
            filename = filename + ".db"
        self.filename = filename # Set the filename to be global within the instance

        __c = __connection.cursor()
        __c.execute("""CREATE TABLE IF NOT EXISTS account (
            username text,
            password text,
            extra text
        )""")

    def login(self, username:str=None, password:str=None, extra:str=None, autotask:bool=False):
        global __connection
        global __c

        if autotask == False:
            __c.execute("SELECT * FROM account")
            lst = __c.fetchall()
            __connection.commit()

            password = encryt(password)
            extra = encryt(extra)

            permission = False
            for i in lst:
                if (i[0] == username) and (i[1] == password) and (i[2] == extra):
                    permission = True
                    break

            return permission
        else:
            username = input("[+] * Please enter your username: ")
            password = encryt(input("[+] * Please enter your password: "))
            extra = encryt(input("[+] * Please enter the extra layer of password you added: "))

            __c.execute("SELECT * FROM account")
            lst = __c.fetchall()
            __connection.commit()

            permission = False
            for i in lst:
                if (i[0] == username) and (i[1] == password) and (i[2] == extra):
                    permission = True
                    break

            if permission:
                self.username = username
            return permission

    def signup(self, username:str=None, password:str=None, extra:str=None, autotask:bool=False):
        global __connection
        global __c

        if autotask == False:
            if self.username_is_valid(username) == False: # If username is not valid, then it will return False
                return False
            else:
                password = encryt(password)
                extra = encryt(extra)

                __c.execute("INSERT INTO account VALUES (?,?,?)", (username, password, extra))
                __connection.commit()
                return True
        else:
            username = input("[+] * Please make a username: ")
            password = encryt(input("[+] * Please make a password: "))
            extra = encryt(input("[+] * Please enter another password that can be different for extra layer of security: "))

            if self.username_is_valid(username): # If username is not valid, then it will ask for a new one
                while True:
                    username = input("[-] * The username you entered is already in use. Please enter another one: ")
                    if self.username_is_valid(username): # If username is valid then it will stop asking for a new one
                        break
                    else:
                        continue

            __c.execute("INSERT INTO account VALUES (?,?,?)", (username, password, extra))
            __connection.commit()
            self.username = username
            return True

    def deluser(self, username:str=None, password:str=None, extra:str=None, autotask:bool=False):
        global __c
        global __connection

        test = ExtraPass(self.filename)
        if autotask == False:
            if test.login(username, password, extra): # NOTE: No need for encryption before passing because login function already encypts the important variables.
                __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
                __connection.commit()
                return True
            else:
                return False
        else:
            # NOTE: No need for encryption before passing because login function already encypts the important variables.
            username = input("[+] * Please enter your username: ")
            password = input("[+] * Please enter your password for confirmation: ")
            extra = input("[+] * Please enter the password you gave for extra layer: ")

            if test.login(username, password, extra):
                global username1
                username1 = username
                __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
                __connection.commit()

                self.username = username
                return True
            else:
                return False

    def get_usernames(self):
        global __c
        global __connection

        __c.execute("SELECT * FROM account")
        lst = __c.fetchall()
        __connection.commit()

        lst = [i[0] for i in lst]
        return lst

    def username_is_valid(self, username:str):
        global __connection
        global __c

        lst = self.get_usernames()

        if username in lst:
            return False
        else:
            return True

    def secure(self):
        global __connection
        __connection.close()


def passgen(length:int=10, caplock:str="mix"):
    # Define the letter, numbers and symbols
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ["@", "#", "%", "!", "*", ">", "<", "$"]

    # Check if length parameter is valid
    if length < 3:
        raise ValueError("Length is too short. It has to be greater than 2")

    # Create generator instance
    generartor = secrets.SystemRandom()

    # Create the random string
    result = ""
    turn = "letter"
    for _ in length:
        if turn == "letter":
            result += generartor.choice(letters)
        elif turn == "number":
            result += generartor.choice(numbers)
        else:
            result += generartor.choice(symbols)

    # Shuffle the randomized string
    for _ in 10:
        result = generartor.shuffle(result)

    # Return the result
    return result

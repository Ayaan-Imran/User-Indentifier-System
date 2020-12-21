import sqlite3

class Basic():
    __connection = None
    __c = None
    def __init__(self, filename):
        self.username = None
        self.filename = filename
        global __connection
        global __c

        __connection = sqlite3.connect("{}.db".format(filename))
        __c = __connection.cursor()
        __c.execute("""CREATE TABLE IF NOT EXISTS account (
            username text,
            password text
        )
        """)
        __connection.commit()

    def signup(self, username=None, password=None, autotask=False):
        global __c
        global __connection
        if autotask == False:
            __c.execute("SELECT * FROM account")
            users = __c.fetchall()
            __connection.commit()
            users = [i[0] for i in users]

            if username not in users:
                __c.execute("INSERT INTO account VALUES(?,?)", (username, password))
                __connection.commit()
                return True
            else:
                return False
        else:
            username1 = input("Please make a username: ")
            self.username = username1
            password1 = input("Please make a password for security: ")

            __c.execute("SELECT * FROM account")
            users = __c.fetchall()
            __connection.commit()

            users = [i[0] for i in users]

            if username1 in users:
                while True:
                    username1 = input("The username you entered is already in use. Please make another one: ")
                    if username1 not in users:
                        break

            print("This username is perfect")

            __c.execute("INSERT INTO account VALUES(?,?)", (username1, password1))
            __connection.commit()
            return True

    def login(self, username=None, password=None, autotask=False):
        global __c
        global __connection
        if not autotask:
            __c.execute("SELECT * FROM account")
            users = __c.fetchall()
            __connection.commit()

            permission = False
            for i in users:
                if (i[0] == username) and (i[1] == password):
                    permission = True
                    break
            return permission
        else:
            username1 = input("Please enter your username: ")
            self.username = username1
            password1 = input("Please enter your password: ")
            __c.execute("SELECT * FROM account")
            users = __c.fetchall()
            __connection.commit()

            permission = False
            for i in users:
                if (i[0] == username1) and (i[1] == password1):
                    permission = True
                    break
            return permission

    def deluser(self, username=None, password=None, autotask=False):
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
            username = input("Please enter your username: ")
            password = input("Please enter your password for confirmation: ")
            if test.login(username, password):
                password = input("Please enter your password again for confirmation: ")
                if test.login(username, password):
                    global username1
                    username1 = username
                    __c.execute("DELETE FROM account WHERE username = '{}'".format(username))
                    __connection.commit()
                    return True
                else:
                    return False
            else:
                return False

    def secure(self):
        global __connection
        __connection.close()
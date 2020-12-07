import sqlite3

connection = None
c = None

def setup(filename):
    global connection
    global c

    connection = sqlite3.connect("{}.db".format(filename))
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS account (
        username text,
        password text
    )
    """)
    connection.commit()

def signup(username=None, password=None, autotask=False):
    if autotask == False:
        c.execute("SELECT * FROM account")
        users = c.fetchall()
        connection.commit()

        if (username not in users):
            c.execute("INSERT INTO account VALUES(?,?)", (username, password))
            connection.commit()
            return True
        else:
            return False
    else:
        username1 = input("Please make a username: ")
        password1 = input("Please make a password for security: ")

        c.execute("SELECT * FROM account")
        users = c.fetchall()
        connection.commit()

        users = [i[0] for i in users]

        if username1  in users:
            while True:
                username1 = input("The username you entered is already in use. Please make another one: ")
                if username1 not in users:
                    break

        print("This username is perfect")

        c.execute("INSERT INTO account VALUES(?,?)", (username1, password1))
        connection.commit()
        return True



def login(username = None, password = None, autotask = False):
    if not autotask:
        c.execute("SELECT * FROM account")
        users = c.fetchall()
        connection.commit()

        permission = False
        for i in users:
            if (i[0] == username) and (i[1] == password):
                permission = True
                break
        return permission
    else:
        global username1
        global username2
        username1 = input("Please enter your username: ")
        password1 = input("Please enter your password: ")
        c.execute("SELECT * FROM account")
        users = c.fetchall()
        connection.commit()

        permission = False
        for i in users:
            if (i[0] == username1) and (i[1] == password1):
                permission = True
                break
        return permission

def getusername():
    return username1

def secure():
    connection.close()

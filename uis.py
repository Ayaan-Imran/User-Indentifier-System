import sqlite3
username1 = "None"

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
        global username1
        username1 = input("Please make a username: ")
        password1 = input("Please make a password for security: ")

        c.execute("SELECT * FROM account")
        users = c.fetchall()
        connection.commit()

        users = [i[0] for i in users]

        if username1 in users:
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
def deluser(username = None, password = None, autotask = False):
    if autotask == False:
        if login(username, password):
            c.execute("DELETE FROM account WHERE username = '{}'".format(username))
            connection.commit()
            return True
        else:
            return False
    else:
        username = input("Please enter your username: ")
        password = input("Please enter your password for confirmation: ")
        if login(username, password):
            password = input("Please enter your password again for confirmation: ")
            if login(username, password):
                global username1
                username1 = username
                c.execute("DELETE FROM account WHERE username = '{}'".format(username))
                connection.commit()
                return True
            else:
                return False
        else:
            return False

def chgcred(username=None, password=None, newusername=None, newpassword=None, credmode=None, autotask=False):
    if autotask == False:
        if credmode == "username":
            if login(username, password) == True:
                c.execute("SELECT * FROM account")
                lst = c.fetchall()
                connection.commit()
                newlist = [i[0] for i in lst]

                if newusername not in newlist:
                    c.execute("UPDATE account SET username='{}' WHERE username='{}'".format(username, newusername))
                    return True
                else:
                    return False
            else:
                return False
        else:
            if login(username, password) == True:
                c.execute("UPDATE account SET password='{}' WHERE username='{}'".format(newpassword, username))
                return True
            else:
                return False
    else:
        if credmode == "username":
            username = input("Please enter your current username: ")
            password = input("Please enter your password: ")
            if login(username, password) == True:
                nusername = input("Please enter your new username: ")
                c.execute("SELECT * FROM account")
                lst = c.fetchall()
                connection.commit()
                new_lst = [i[0] for i in lst]

                if nusername in new_lst:
                    while True:
                        nusername = input("The username you entered is already in in use. Enter another one: ")
                        if username not in new_lst:
                            break
                print("The username is valid")

                c.execute("UPDATE account SET username='{}' WHERE username='{}'".format(nusername, username))
                return True
            else:
                return False
        else:
            username = input("Please enter your current username: ")
            password = input("Please enter your password: ")
            if login(username, password) == True:
                password = input("Please enter your new password: ")
                c.execute("UPDATE account SET password='{}' WHERE username='{}'".format(password, username))
                return True
            else:
                return False


def getusername():
    return username1

def secure():
    connection.close()


setup("user")
mode = input("Do you want to login(1) or signup(2) or delete account(3): ")
if mode == "1":
    if login(autotask=True) == True:
        print("Welcome " + getusername())
    else:
        print("Access denied")
elif mode == "2":
    if signup(autotask=True) == True:
        print("Account created " + getusername())
    else:
        print("Account creation failed")
else:
    if deluser(autotask=True) == True:
        print("Account deleted. Bye {}. We were having a good time".format(getusername()))
    else:
        print("Error ocurred!")



mode = input("Do you want to change username(1) or password(2): ")
if mode == "1":
    username = input("username: ")
    password = input("Password: ")
    nusername = input("Enter your new username: ")
    if chgcred(username=username, password=password, credmode="username", newusername=nusername) == True:
        print("Username changed!")
    else:
        print("Some kinda error ocurred!")
else:
    username = input("username: ")
    password = input("Password: ")
    npassword = input("Enter your new password: ")
    if chgcred(username=username, password=password, credmode="password", newusername=npassword) == True:
        print("Password changed!")
    else:
        print("Some kinda error ocurred!")

secure()
# User Identifier System (uis) 
_____________________________
User Identifier System is a tool you can use to create a cool an easy login and signup system.

## Version details
**Current version:** 0.0.91
1. `autotask` feature was removed.
2. System can now log user's actions and save them in a `log.txt` file.
3. Contains important bugs and error fixes.

## Installation
**Note:** This is a python package. It will not work without python 🤣!  
Install the `UserIdentificationSystem` with the command:  
```commandline
pip install user-Identification-System
pip install pypasstools
```


## Example codes [Mini documentary]

### Import command
To import `UserIdentificationSystem` into your code, use the following command:
```python
import UserIdentificationSystem as uis
```
### A basic signup and login system
In the `UserIdentificationSystem` package, there is a class that allows users to register, login, and signup using a username and a password. The class is called `Basic()`.   

| Parameter |    Default value   |                                                                        Description                                                                        | Data Type |
|:---------:|:------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------:|
| filename  | REQUIRED PARAMETER | The name of the database the user's credentials will be stored. The Basic() class will automatically create and initialise a new database with this name. |   string  |
| log       |        False       | If set to True, the system will automatically log user's actions to a "log.txt" file.                                                                     |  boolean  |


```python
import UserIdentificationSystem as uis
import passtools # Package comes installed

controller = uis.Basic("user", log=False)
mode = input("Do you want to login(1) or signup(2) or delete account(3): ")

if mode == "1":
    username = input("Enter your username: ")
    password = passtools.passask("Enter your password: ", do_hash=False)
    
    if controller.login(username, password):
        print("Welcome " + controller.username)
    else:
        print("Access denied")
        
elif mode == "2":
    username = input("Create your username: ")
    password = input("Create your password: ")
    
    if controller.signup(username, password):
        print("Account created " + controller.username)
    else:
        if controller.username_is_valid(username) == False:
            print("Username " + username + "  already exists.")
        
        else:
            print("Account creation failed")
        
else:
    username = input("Enter your username: ")
    password = passtools.passask("Enter your password: ", do_hash=False)
    
    if controller.deluser(username, password):
        print("Account deleted. Bye {}. We were having a good time".format(controller.username))
    else:
        print("Error occurred! Invalid credentials.")

controller.secure()
```

#### Output
Case 1
```commandline
>> Do you want to login(1) or signup(2) or delete account(3): 2
>> Create a username: uis_learner
>> Create a password for security: 1111
Account created uis_learner
```

Case 2
```commandline
>> Do you want to login(1) or signup(2) or delete account(3): 1
>> Enter your username: uis_learner
>> Enter your password: [PASSWORD IS NOT ECHOED]
Welcome uis_learner
```

Case 3
```commandline
>> Do you want to login(1) or signup(2) or delete account(3): 3
>> Enter your username: uis_learner
>> Enter your password: [PASSWORD IS NOT ECHOED]
Account deleted. Bye uis_learner. we were having a good time 
```

### A more secure signup and login system
In the `UserIdentificationSystem` package, there is a class that allows users to register, login, and signup using a username and 2 passwords. The class is called `ExtraPass()`.

| Parameter |    Default value   |                                                                        Description                                                                        | Data Type |
|:---------:|:------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------:|
| filename  | REQUIRED PARAMETER | The name of the database the user's credentials will be stored. The Basic() class will automatically create and initialise a new database with this name. |   string  |
| log       |        False       | If set to True, the system will automatically log user's actions to a "log.txt" file.                                                                     |  boolean  |

#### controller.signup()
In the `signup()`, you have to pass the user's username, password and an extra password. Then it will store it in the database. The signup() returns true if the process went well. You will get false when the username is already taken by some other user
```python
username = input("Please make a username: ")
password = input("Please make a password: ")
extra = input("Please make an extra password for security: ")

if controller.signup(username, password, extra) == True:
    print("Account created")
else:
    print("Username is already in use")
```

#### controller.login()
In the `login()`, you have to pass the user's username, password and their extra password. It will return true is the user is identified, or else it will return false 
```python
username = input("Please enter your username: ")
password = input("Please enter your password: ")
extra_password = input("Please enter your extra password: ")

if controller.login(username, password, extra_password):
    print("Hello " + username)
else:
    print("Access denied")
```

#### controller.deluser()
The `deluser()` function allows you to delete a user's account. You need to pass in the username, password and extra password for confirmation. It will return True if it is deleted and False if it didn't go well.  
**Note:** Once it is deleted, there is no turning back
```python
username = input("Please enter your username: ")
password = input("Please enter your password: ")
extra = input("Please enter your extra password: ")

if controller.deluser(username, password, extra) == True:
    print("Hello " + username)
else:
    print("Error occured")
```
If the `deluser()` returns false: 
1. It maybe because the username or password don't match.
2. The account doesn't exist.
3. There was some error in the deletion process (This is rare case).


#### controller.get_usernames()
The `get_usernames()` function will return a list of usernames who already signup in your system.

```python
print(controller.get_usernames())
```

**output**
```commandline
["test", "test2", "uis_learner"]
```

#### controller.username_is_valid()
This is a helpful function when user wants to check if a username exists and is not in use by someone else.  
You have to pass in a username that you want to check. It will return `True` if the username valid (Not used by another user) and `False` if the username is invalid (Used by another user).

```python
print(controller.username_is_valid("uis_learner"))
```
**output**
```console
True
```

#### controller.secure()
You have to end your programme with this function so that everything is completely safe and secure!
```python
controller.secure()
```

### Important variables [BOTH Basic() AND ExtraPass()]
1. **controller.username**  
Contains the most recent username used in the system.
2. **controller.filename**
This will give you the filename you have given to the database which stores the user's credentials.
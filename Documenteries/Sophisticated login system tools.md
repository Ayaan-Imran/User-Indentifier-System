# Guide on using uis
User Identifier System is basically a tool to help you create a login and signup system!  

## Import

```python
import uis
```

## Functions 
### setup()
To start the setup, we need to create an instance of the ExtraPass() class. In the ExtraPass class, you need to pass in a filename witch will be storing your user's credentials.
```python
controller = uis.ExtraPass("users")
```
**Note:** When you will run your programme, it will create a database file that will be stored in you current working directory

### Some details
1. **controller.username**  
This will allow you to get the user's name when you will use autotask feature (Which will be discussed)
2. **controller.filename**
This will give you the filename you have given to the database which stores the user's credentials

### controller.signup()
In the signup(), you have to pass the user's username, password and an extra password. Then it will store it in the database. The signup() returns true if the process went well. You will get false when the username is already taken by some other user
```python
username = input("Please make a username: ")
password = input("Please make a password: ")
extra = input("Please make an extra password for security")

if controller.signup(username, password, extra):
    print("Account created")
else:
    print("Username is already in use")
```
if you don't want to make a signup system, you can enable autotask. This feature will take the username and password and extra password by itself and will also check that if the username is already in use; If it is then it will ask for the username again until the user gets a right one! It will return true at the end eventually:
```python
if uis.signup(autotask=True):
    print("Account created " + controller.username)
```

#### Output:
```commandline
>> Please make a username: Test
>> Please make a password: 1111
>> Please enter another password that can be different for extra layer of security: 2222
This username is perfect
Account created
```

#### Output (If the username is already taken):
```commandline
>> Please make a username: Test
>> Please make a password: 1111
>> Please enter another password that can be different for extra layer of security: 2222
>> The username you entered is already in use. Please make another one: Test2
This username is perfect
Account created
```

### controller.login()
In the login(), you have to pass the user's username, password and their extra password. It will return true is the user is identified, or else it will return false 
```python
username = input("Please enter your username: ")
password = input("Please enter your password: ")
extra_password = input("Please enter your extra password: ")

if controller.login(username, password, extra_password):
    print("Hello " + username)
else:
    print("Access denied")
```

If you don't want to manually make a username and password entry, you can enable auto task. Auto task will simply take the input and output byitself and will return true if the login details are matching
```python
if controller.login(autotask=True) == True:
    print("Hello " + controller.username)
else:
    print("Access denied")
```
#### Output:
```commandline
>> Please enter your username: Test 
>> Please enter your password: 1111
>> Please enter the extra layer of password you added: 2222
Hello Test
```

### controller.deluser()
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
1. It maybe because the username or password don't match
2. The account doesn't exist
3. There was some error in the deletion process (This is rare case)

Like in all the other functions, this has an **autotask**
```python
if controller.deluser(autotask=True):
    print("Bye " + controller.username)
else:
    print("Error ocurred")
```

#### Output
```commandline
>> Please enter your username: Test
>> Please enter your password for confirmation: 1111
>> Please enter your password again for confirmation: 1111
>> Please enter the password you gave for extra layer (Password "2"): 2222
Bye Test
```

### secure()
You have to end your programme with this function so that everything is completely safe and secure!
```python
controller.secure()
```


## Example of a login and signup system

```python
import uis

controller = uis.ExtraPass("user")
mode = input("Do you want to login(1) or signup(2) or delete account(3): ")
if mode == "1":
    if controller.login(autotask=True):
        print("Welcome " + controller.username)
    else:
        print("Access denied")
elif mode == "2":
    if controller.signup(autotask=True):
        print("Account created " + controller.username)
    else:
        print("Account creation failed")
else:
    if controller.deluser(autotask=True):
        print("Account deleted. Bye {}. We were having a good time".format(controller.username))
    else:
        print("Error occurred!")

controller.secure()
```
or

```python
import uis

controller = uis.ExtraPass("user")

mode = input("Do you want to login(1) or signup(2) or delete account(3): ")
if mode == "1":
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    extra_password = input("Please enter your extra password: ")

    if controller.login(username, password, extra_password):
        print("Hello " + username)
    else:
        print("Access denied")
elif mode == "2":
    username = input("Please make a username: ")
    password = input("Please make a password: ")
    extra_password = input("Please make an extra password: ")

    if controller.signup(username, password, extra_password):
        print("Welcome " + username)
    else:
        print("So error occurred")
else:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    extra_password = input("Please enter your extra password: ")

    if controller.deluser(username, password, extra_password):
        print("Bye " + username)
    else:
        print("So error occurred")

controller.secure()
```

#### Output
Case 1
```commandline
>> Please make a username: uis_learner
>> Please make a password: 1111
>> Please enter another password that can be different for extra layer of security: 2222
This username is perfect
Account created
```

Case 2
```commandline
>> Please enter your username: uis_learner 
>> Please enter your password: 1111
>> Please enter the extra layer of password you added: 2222
Hello uis_learner
```

Case 3
```commandline
>> Please enter your username: uis_learner
>> Please enter your password for confirmation: 1111
>> Please enter your password again for confirmation: 1111
>> Please enter the password you gave for extra layer (Password "2"): 2222
Bye uis_learner
```
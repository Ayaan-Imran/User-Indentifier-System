# Guide on using uis
User Identifier System is bassically a tool to help you create a login and signup system!

## Import
```python
import uis
```

## Functions 
### setup()
You need to start your project with the setup(). The setup() function takes 1 parameter (the name of a file)
```python
uis.setup("users")
```
**Note:** When you will run your programme in which you have your `setup()`, it will create a database file that will be stored in you current working directory

### getusername()
This function will be available when you will use autotask parameter in the below function. This will give the username that the user passed

### signup()
In the signup(), you have to pass the user's username and password. Then it will store it in the database. The signup() returns true if the prcess went well. You will get false when the username is alreasy taken by some other user
```python
username = input("Please make a username: ")
password = input("Please make a passward for security: ")
uis.signup(username, password)
```
if you don't want to make a signup system, you can enable autotask. This will take the username and password byitself and will also check that if the username is already in use; If it is then it will ask for the username again until the user gets a right one! It will return true at the end eventually:
```python
if uis.signup(autotask=True):
    print("Account created " + uis.getusername())
```

#### Output:
```commandline
>> Please make a username: Test
>> Please make a password: 1111
This username is perfect
Account created
```

#### Output (If the username is already taken):
```commandline
>> Please make a username: Test
>> Please make a password: 1111
>> The username you entered is already in use. Please make another one: Test2
This username is perfect
Account created
```

### login()
In the login(), you have to pass the user's username and password. It will return true is the user is identified, or else it will return false 
```python
username = input("Please make a username: ")
password = input("Please make a passward for security: ")
if uis.login(username, password) == True:
    print("Hello " + username)
else:
    print("Access denied")
```

If you don't want to manually make a username and password entry, you can enable auto task. Auto task will simply take the input and output byitself and will return true if the login details are matching
```python
if uis.login(autotask=True) == True:
    print("Hello " + uis.getusername())
else:
    print("Access denied")
```
#### Output:
```commandline
>> Please enter your username: Ayaan 
>> Please enter your password: 1111
Hello Ayaan
```

### detetuser()
The `deluser()` function allows you to delete a user's account. You need to pass in the username and password for confirmation. It will return True if it is deleted and False if it didn't go well.  
**Note:** Once it is deleted, there is no turning back
```python
username = input("Please enter your username: ")
password = input("Please enter your password: ")
if uis.deluser(username, password) == True:
    print("Hello " + username)
else:
    print("Error occured")
```
If the `deluser()` returns false: 
1. It maybe because the username or password don't match
2. The account doesn't exist
3. There was some error in the deletion process (This is rare case)

Like in all the other functions, this has an `autotask`
```python
if uis.deluser(autotask=True):
    print("Bye " + uis.getusername())
else:
    print("Error ocurred")
```

#### Output
```commandline
>> Please enter your username: Test
>> Please enter your password for confirmation: 1111
>> Please enter your password again for confirmation: 1111
Bye Test
```

### secure()
You have to end your programe with this function so that everything is completely safe and secure
```
secure()
```


## Example of a login and signup system
```python
import uis

uis.setup("user")
mode = input("Do you want to login(1) or signup(2) or delete account(3): ")
if mode == "1":
    if uis.login(autotask=True) == True:
        print("Welcome " + uis.getusername())
    else:
        print("Access denied")
elif mode == "2":
    if uis.signup(autotask=True) == True:
        print("Account created " + uis.getusername())
    else:
        print("Account creation failed")
else:
    if uis.deluser(autotask=True) == True:
        print("Account deleted. Bye {}. We were having a good time".format(uis.getusername()))
    else:
        print("Error ocurred!")
        
uis.secure()
```

#### Output
Case 1
```commandline
>> Do you want to login(1) or signup(2) or delete account(3): 2
>> Please make a username: uis_learner
>> Please make a password for security: 1111
This username is perfect
Account created uis_learner
```

Case 2
```commandline
>> Do you want to login(1) or signup(2) or delete account(3): 1
>> Please enter your username: uis_learner
>> Please enter your password: 1111
Welcome uis_learner
```

Case 3
```commandline
>> Do you want to login(1) or signup(2) or delete account(3): 3
>> Please enter your username: uis_learner
>> Please enter your password for confirmation: 1111
>> Please enter your password again for confirmation: 1111
Account deleted. Bye uis_learner we were having a good time 
```
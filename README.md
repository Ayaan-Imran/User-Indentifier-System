# User Identifier Sytem (uis)
User Identifier System is bassically a tool to help you create a login and signup system!

## Functions 
### setup()
You need to start your project with the setup(). The setup() function takes 1 parameter (the name of a file)
```python
setup("users")
```
**Note:** When you will run your programme in which you have your `setup()`, it will create a database file that will be stored in you current working directory

### signup()
In the signup(), you have to pass the user's username and password. Then it will store it in the database. The signup() returns true if the prcess went well. You will get false when the username is alreasy taken by some other user
```python
username = input("Please make a username: ")
password = input("Please make a passward for security: ")
signup(username, password)
```

### login()
In the login(), you have to pass the user's username and password. It will return true is the user is identified, or else it will return false 
```python
username = input("Please make a username: ")
password = input("Please make a passward for security: ")
if login(username, password) == True:
    print("Hello " + username)
else:
    print("Access denied")
```

### secure()
You have to end your programe with this function so that everything is completely safe and secure
```
secure()
```

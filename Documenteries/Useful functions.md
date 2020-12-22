# Guide on using uis
This is not only a tool to help you make a login and signup system. You can do other stuff too!


### Importing
We need to import the uis file
```python
import uis
```

### Generate random password
This feature will allow you to generate strong passwords with customizable feature  
To start, you have to use this function
```python
password = uis.passgen()
```
**output**
```commandline
OJrtetawrI!6547
```
**Note**: The default length of this function is set to 10, which will increase the length of the password. It is also set to mode of mix will be explained later

You can customize it my passing few parameters  
1. You can pass in the len parameter which will make your password lengthy
```python
password = uis.passgen(len=12)
```

**output**
```commandline
jTFTbHKrGrEd!5209
```
2. You can change the mode to be capitalised or lowercase. The default is set to mix, which means that it contains both capital and lower-case words
```python
password = uis.passgen(caplock=True) # You do this for making everything capital
```

```commandline
GIHEMOLBTL@5694
```
___
```python
password = uis.passgen(caplock=False) # You do this for making everything lowercase
```

```commandline
fjztungvje$9320
```
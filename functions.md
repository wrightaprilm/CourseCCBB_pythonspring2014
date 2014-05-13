#Functions

Functions group together code to carry out some sort of action. Let's read the below together:

```Python
import os
def get_list():
    file_list = []
    for file in os.listdir('.'):
        if file.endswith('.md'):
            file_list.append(file)
    print file_list
    return file_list

```

+ What is this code doing?
+ What is the output?


#Why Functions?

+ Functions make your code easier to read.
+ Functions make it easier to implement tests and checks.
+ Functions reduced replication. 

##How it works

```Python
import os
import re
def get_list():
#Define the function. This is how python knows not to execute the code now, but to save it until 'called'
    file_list = []
    for file in os.listdir('.'):
        if file.endswith('.md'):
            file_list.append(file)
    print file_list
#Visually show the results
    return file_list
#Return ... what's that?

```
Call this function as such:

```Python
get_list()
```

To illustrate return, let's try something else. Since data should generally be treated as read-only, let's make a directory so we can put processed data in it:

```Python
def use_files():
    files = get_list()
    for file in files:
	print file

```

Try taking out the return statement in get_list() and rerun it. What happens when you call use_files()?

Functions can also take input.

```Python
my_files = os.listdir('.')
def get_list(list):
#Define the function. This is how python knows not to execute the code now, but to save it until 'called'
    file_list = []
    for file in list:
        if file.endswith('.md'):
            file_list.append(file)
    print file_list
#Visually show the results
    return file_list
#Return ... what's that?
```

Try calling the file_list returned in the interpreter. What's wrong here? How can we get around this? 

#Exercise

Grab your file iteration code from this morning. 

+ Break this into three functions: A reading function, a math function and a writing-out function. Before you code out any of this, draw it out on a board. What input and output must be present at each step?
+ Before you code it up, write a test for each piece. 
	+ For the reading in function: Each line should have 4 columns. How can you test this [hint: think about how we measure length of object]?
        + For the math function: There are a few possibilities for testing either the in or output. Pick one.
        + For the writing out: Test either the in or output. Choose your own.


















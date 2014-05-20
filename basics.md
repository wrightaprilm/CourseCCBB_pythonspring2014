#Basics of Python

Python is a readable and versatile programming language. Python has a lot of nice qualities, including:

+ Active user base  
+ Helpful error messages  
+ Nice trade-off between developer and computer time  
+ Many libraries for specialized analyses  
	
## Running Python

Hopefully, all of you completed the installs per the e-mail.

During most of today, we will be working at the interpreter. This is accessed by typing 

```UNIX
$ python
```

at the prompt.

Python commands can also be saved to text files and executed in the terminal, like so:

```UNIX
$ python my_script.py
```

Note that the '.py' extension isn't necessary, but it can be useful to label for easy indexing. 

## Commenting

Through out the day, as you make notes, you might want to save your work as a script. 

And you might be worried you won't recall what it does when you get home on Sunday. In Python, '#' denotes a comment. Using comments in your scripts allows you to remember and explain what blocks of code are using. Use them! Love them!

##Quitting

When working at the interpreter,

```python
exit()
```
## Version Control and Sharing Code

So, how many of you tried to fix a borken bit of code and made it worse in the process today? Or erased something important and didn't notice until later?

Enter version control.

Version control is a system of tracking changes made to documents. So, for example, if you write some code in a document and enter it into a version control system, you can manage future edits of that code. Obviously, this is quite handy. If your code is working, and you later make a change to it that causes it to malfunction, you can roll back to a previous change. You can also write and track different versions of the code for experimental development.

There are many different types of version control. Today, we're going to talk about git. Git has become quite popular, due in no small amount to the website GitHub, which has very nice features for information sharing and collaborative coding.

First create a new folder, if you haven't already created one for this workshop.

```UNIX
$ mkdir ccbb_workshop
```

And change directories into your directory:

```UNIX
$ cd ccbb_workshop
```

Recall that you can always check where you are in the computer by typing

```UNIX
$ pwd
```

In git, we store our code (or other documents, this is great for manuscripts!) in what we call a 'repository'. A repository will hold all of our code snapshots and all of our other documents. But we want this to be linked to us and our name. So let's make sure git knows who we are:

```UNIX
$ git config --global user.name "Your Name"
$ git config --global user.email "your@e-mail.edu"
$ git config --list
$ git config user.name
```
Now that git knows who we are, we can fork the class repository in a webbrowser. And we can clone it to our machine.

```UNIX
git clone https://github.com/your_username/ccbb_pythonspring2014.git
```

This will start a new repository on your local machine. This should only be used once per project, and git repositories should not be nested within each other. Let's see the status of our repository. First change directories into your cloned repository:

```UNIX
$ git status
```

Let's add a note to the repository. In a text editor, write a couple sentences about who you are what what you do for your science.

```python
$ git add my_file
```

Once added, we can commit our code into git's memory like so:

```UNIX
$ git commit -m 'my awesome note'
```

The -m option allows us to add a 'commit message'. These are very useful for recalling later on, what exactly you added to your repositories and when. They're also helpful for your collaborators to snoop on what all you've been doing (or, to, you know, collaboratively write code).


##Sharing code online

This is the part of the hour that we're going to have trouble with without the internet.

GitHub.com allows users to broadcast code to the internet. This can be really useful for sharing information with collaborators and maintaining long-standing versions of your code for others to use.

```UNIX
$ git push
``` 

For example, pushes all the changes we make to our online repository. Look online to see what you've added to your repository.

## So my code is on the internet ... 

Yep. It's kind of scary to share code at first. But there are lots of good reasons to do it.

+ Your code is discoverable: People can find you, see the code, and cite the paper to which it is connected!
+ It's open: Science thrives on reproducibility. If your code lives online, people can do science with your work.
+ It's convenient: If I'm without my computer, but want to chat code with someone, I can pull up GitHub on their computer and show them stuff.
+ It's permanent (hopefully)

We'll use Github in class to submit exercises.




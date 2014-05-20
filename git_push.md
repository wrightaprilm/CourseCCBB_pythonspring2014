## A little more with Git

What we're going to do first thing this morning is sync your repositories to mine. That way, you'll have all of the exercises I've worked on over night.

The first step is to add my repository into git's memory.

```UNIX

git remote add upstream https://github.com/wrightaprilm/ccbb_pythonspring2014.git

```

The syntax of this means 'add April's repository as an alias called upstream'.

```UNIX
git pull upstream master
```

This command pulls any changes I've made into your repository. Let's add a note to the repository. In a text editor, write a couple sentences about who you are what what you do for your science.

```python
$ git add my_file
```

Once added, we can commit our code into git's memory like so:

```UNIX
$ git commit -m 'my awesome note'
```

The -m option allows us to add a 'commit message'. These are very useful for recalling later on, what exactly you added to your repositories and when. They're also helpful for your collaborators to snoop on what all you've been doing (or, to, you know, collaboratively write code).

GitHub.com allows users to broadcast code to the internet. This can be really useful for sharing information with collaborators and maintaining long-standing versions of your code for others to use.

```UNIX
$ git push
``` 
For example, pushes all the changes we make to our online repository. Look online to see what you've added to your repository.



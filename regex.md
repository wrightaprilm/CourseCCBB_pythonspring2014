#Regular Expressions

The module 're' in python provides tools for processing strings. 	Regular expressions use characters that have special meanings to match strings, find matches within strings or modify strings.

##Special characters 

```Python
. ^ $ * + ? { } [ ] \ | ( )

```

These characters are used to group regular expressions or to give positional information to the regular expression. Alphanumeric characters usually represent themselves.

##Regexpal.com

Let's take five and just play with RegexPal to try and get a little more comfortable. Grab an entry from sequences.txt and pin the regex cheatsheet at the top of the screen. Try various commands to try slice up the entry.

##Regex and scripting

RegexPal is great, and allows us to look at how our regular expressions work. But what we really want to be able to do is process data. Python's re module allows us to implement regular expressions in a scripting context.

```python
import re
str = '>gi|357123948|ref|XP_003563669.1| PREDICTED: protein brittle-1, chloroplastic/amyloplastic-like [Brachypodium distachyon]'

```

The first thing we have to do is import re and define some string.

Now we can do some processing.

```Python

re.findall(r'>gi', str)
['>gi']

```

We can see the output of this is a list. If we had multiple objects we might like returned, findall() is a method that can pull those out for us.

```Python
search_string = re.search(r'XP_\d{9}\.\d', str)

search_string.group()

'XP_003563669.1'

```

Search looks through a string and finds a match to the entered phrase, storing it in a Match Object called search_string. 

Regex searching can be automated, too:

```Python

motifs = ['IRKKAKKRGLK', 'AFDTANKF', 'VNVIRVAPSK']
seq_string = 'FASVGHKVGVGFPASSSSSGATSSGNPQDPYRKYVSPEAVETSLPVPGDGVGLRGKGKKKAVRIKIKVGNSHLKRLISGG'

for motif in motifs:
    if re.search(motif, aa):
        print 'Following motif found:%s' % motif
```

And we can use regex to make substitutions:

```python

new_string = re.sub("predicted", "Synthesized", str)


```

Uh-oh, what happened? 

```python

new_string = re.sub("(?i)predicted", "Synthesized", str)
```

Case of the letters can be ignored in .search() with re.IGNORECASE.

Exercise:

Create a script that does a regex of your choice on a string of your choice.
If you get this working: think about some of the challenges presented by performing this on a file. How can we import a file and still have the strings we need to do regex?

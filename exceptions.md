#Hey, how good do you feel about your data?

##You're really sure it's perfect and there are no weird or missing values?

###Get out.

Let's look at a familiar, but ugly data set:

```python 
for line in f:
    line_list.append((line).strip().split(','))
     

line_list

 ['Lake_Creek', '4', '12', '180'],
 ['Los_Alamos', '8', '340'],
 ['Big_Bend', 'a', '6', '280'],
 ['McDonald', '5', '20', '280'],
 ['Balmorrhea', '3', '3', '174']

```

What do you notice about these data?

If we wanted to do some processing, we'd probably be frustrated. These data have non-numeric characters in with the numerics, and one is missing a value.

```Python
val_list = []
for line in line_list:
    print line[1]
    try: 
        line[1].isdigit()
        val_list.append(int(line[1]))
        print "Data passes initial quality check"
    except ValueError:
        print "This is not a number:", line[1]

```

What have we done here?

Try-except clauses are useful for a variety of situations. The one that's probalby most common is for catching issues with data that might not be fatal. For example, we have an 'a' in our data. If that wasn't a huge deal, like if we had many data points, we might just want to ignore it. If it is a big deal, we might want finding an 'a' character to be fatal. Enter, the assert statement. 

```Python

for line in line_list:
    assert (line[1].isalpha()), "Value is not numeric!"

```

What's different about how this executes?

We're going to go over some more complicated data filtration and replacement tomorrow. For tonight, have a look at homework 2. 




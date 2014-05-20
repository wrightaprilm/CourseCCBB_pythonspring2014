##Solutions

```python
last_name = []
last_name = ['w','r','i','g','h','t','5','1','2']
type(last_name)


letters = []
numbers = []
for letter in last_name:
    if letter.isalpha():
        letters.append(letter)
    elif letter.isdigit():
        numbers.append(letter)

for item in numbers:
    print int(item)


```

Nice properties of this for solution:
    + It does what we want
    + It's compact and easy to read
    + We have a couple tests so we know our work isn't garbage

Not as nice:
    + Our test of our input is interactive. We need to manually execute it and look for feedback.

Here's a solution that automates that first test:


```Python
last_name = []
last_name = ['w','r','i','g','h','t','5','1','2']
letters = []
numbers = []
if type(last_name) == list:
    for letter in last_name:
        if letter.isalpha():
            letters.append(letter)
        elif letter.isdigit():
            numbers.append(letter)

for item in numbers:
    print int(item)'

```

Nice properties of this solution:
    + It does what we want
    + It's compact and easy-to-read
    + Our test is now integral. If we don't pass, we don't execute the code








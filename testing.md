#Testing

No one wants to end up having their paper retracted.

Over the course of the week, we're going to integrate testing into our exercises and homeworks. Testing, like programming itself, is a skill. Testing involves aking the self-critical questions about the pipeline you're building: What *must* be true of my input for my script to work and return acceptable results? What *must* be true about my output for further analysis, or for my science to make sense?

For example, I am collecting records of how many species I saw at a site per day for a week, and I'm going to use that to calculate a species richness value for each site. Species richness is just the number of species in some defined area.

What do I know about my input?

+ It must be numerical
+ It must be integers (you can't really see half a species)
+ I know my output should be a whole number
+ I will know how many sites I went to and how many days I went, so I can make sure I have the right number of observations.

The first three observations are fairly simple, and we should be able to test these on the exercise we just did.

##Some helpful methods for testing

| Name | Example | Plain English |
|-------|--------|---------------|
| .isdigit() | my_string.isdigit() | Looks at a user-provided string and determines if it is a number |
| .isalpha() | my_string.is_alpha() | Looks at a user-provided string and decides if it is a letter |
| int() and float() | int(my_number) or float(my_number) | Changes the type of a number string to an integer or float | 
| type() | type(my_object) | Tells you what kind of object you have |


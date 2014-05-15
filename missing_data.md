#Handling weird stuff in your data with Pandas

Go ahead and load in the 'sites_complicated.xlsx' file with the first column as an index and the first row as column names. What's different here about the way in which this data is displayed, compared to how we saw it yesterday?

That's right: NaN. NaN means 'not a number", although some things that are not numbers are not considered by Pandas to be NaN. Pandas generally considers sort of blank value a NaN. 

#What is a NaN, in the context of Pandas?

+ A NaN is treated as a zero in computation.
	+ This might be OK for what you want to do.
+ If your computation returns an array, it will contain the NaN.

Let's explore that behavior.

```python

df.ix[:,2].sum()
914

df.ix[:,2]
Site
Los_Alamos    NaN
Big_Bend      280
McDonald      280
Balmorrhea    174
Name: Expenditure, dtype: float64

```

The above should make pretty good sense: The NaN is factored in as a 0, but it still exsists.


```python

sum_val = df.ix[:,2].sum()
sum_val/len(df.ix[:2])

127
```

What happened there? Pandas automatically excluded this value from the averaging because it has no value. That's pretty smart. Other types of weirdo values are more insidious. 

```python
df.ix[:,0]
Lake_Creek    4
Los_Alamos    8
Big_Bend      a
McDonald      5
Balmorrhea    3
Name: Observations, dtype: object
```

This is a little harder: we have character data in here, but it's not a number like we expect. How could we catch data of this type?

```python
import numpy

df.applymap(numpy.isreal)

           Observations Species Expenditure
Site                                       
Lake_Creek         True    True        True
Los_Alamos         True    True        True
Big_Bend          False    True        True
McDonald           True    True        True
Balmorrhea         True    True        True

[5 rows x 3 columns]

```

That's a handy way to view this data. But it might not be great for huge data sets. Pandas, however, has some nice mappings that can help us locate these types of characters.

```python

df[~df.applymap(numpy.isreal).all(1)]

         Observations  Species  Expenditure
Site                                       
Big_Bend            a        6          280

[1 rows x 3 columns]
```

If these were data from a lab notebook, perhaps we could go double-check that data and enter the real value:

```python
df.ix['Big_Bend',0] = 9
```

This notation replaces the data point in question.

##Grouping

Sometimes, we might have data that are repeats, or we might want to classify together. This is common if you have repeated rows of subject data (for example, if you've done measurements on an organism multiple times and saved this as rows). Pandas groupby feature can help use with this.

```python

grouped = df.groupby('Expenditure')
grouped.groups
{174.0: [u'Balmorrhea'],
 180.0: [u'Lake_Creek'],
 280.0: [u'Big_Bend', u'McDonald']}

```

It's a litte odd that those two locations have the same expenditure - you have to pay to get into McDonald. This might lead us to believe that perhaps someone misrecorded the location. Maybe we'd like to get species richness considering these two parks as one.

```python
df.groupby(['Expenditure']).sum()

             Species
Expenditure         
174                3
180               12
280               26

```

Groupby allows us to do this.


##Exercise

I've attached a file called "MissingData.md' to the course site. Try these different missing data filters. Are they doing what you expect? When do you think the various methods would be helpful?






#Plotting

One are where R has had a huge advantage over Python is plotting and making attractive graphics. Python recently got its own version of the popular ggplots library, which we'll be working with today.

```python

from ggplot import * 

my_plot =  ggplot(df, aes(x='Expenditure',y='Species')) + geom_point() + xlim(0,350) + ylim(0,21)

my_plot
```

Easy, a scatter plot. The syntax here might look a little alien. Plots, in Python and R, are generally build by combining objects (or 
"layers") together for some effect. For example, in our plot, we've defined that we'll be making a plot uing data from the dataframe df with two specific coloumns as the X and Y axes. Additional objects provided are axis limits.

You'll notice that this plot has opened in a viewer window. We can change this behavior.

```Python

ggsave(my_plot, "my_plot", "png")

```

OK, that's all well and good. Let's try this with some Biggish Data. Let's say we've got a big matrix. Half the data was collected by me, half by my labmate. I'm suspcious that we've not done collection in the exact same way. What I want to do is load up my data, add a column that shows who collected what, and plot the two subsets against each other.

```Python
big_matrix = pd.read_csv('/home/april/Documents/ccbb_pythonspring2014/random_mat', index_col=None, header=None)

big_matrix['1001'] = '1001'
big_matrix['1001'][0:250] = 'Me'
big_matrix['1001'][251:500] = 'My labmate'
```

Print out that matrix. Does it look like you thought it might? What's with the row and column names? Let's check and make sure that the reassignment worked.

```python

ggplot(aes(x=big_matrix.ix[0:500,2], y = range(0,500), color='1001'), data=big_matrix) + geom_point() +geom_jitter()  + ylab("Y Axis") + xlab("X Axis") +ylim(0,500) + xlim(0,1) + theme_bw()
```

OK, that looks good.

Let's actually overlay my data and hers:

```python
ggplot(aes(x=big_matrix.ix[0:499,2], y = big_matrix.ix[:,1], color='1001'), data=big_matrix) + geom_point() +geom_jitter()  + ylab("Y Axis") + xlab("X Axis") +ylim(0,1) + xlim(0,1) + theme_bw()

```

Hmmm, some of her points are right on mine, some aren't. It looks like maybe we had some different practices in data collection. 

##Exercise:

Try removing some of the geoms. What happens. I've attached a cheatsheet, 'Plot_types.md'. Try a couple of the different options and see what they do. What types of plots would be good for your data?






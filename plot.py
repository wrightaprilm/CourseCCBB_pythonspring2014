#!/usr/bin/env python 

def get_files():
    file_list = []
    for file in os.listdir('.'):
        if file.endswith('.csv'):
#What if you have multiple extensions?
	    file_list.append(file)
    print file_list
    return(file_list)

def plot():
    file_list = get_files()
    for file in file_list:
        name = os.path.splitext(file)[0]
#Why is this necessary? Hint: Look at the 'ggsave' call.
	print name
        data = pandas.read_csv(file, header=False)
#How could you manage a directory in which some files had headers and some did not?
        scaled_sub = data.ix[:,2]/1.5
#One file should give you some trouble
        plot = ggplot(aes(x=data.ix[:,1],y=scaled_sub), data=data) + geom_point() + stat_smooth(color='blue', se=True) + ylab("Y label!") + xlab("X or Something") +ylim(0,100) + xlim(2,3) +theme_bw()
#What in here needs to change?
        ggsave(plot, name, 'tiff')


#What's going to happen if you run this without a function call?  

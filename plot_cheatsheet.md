#Plots Cheatsheet

ggplot for Python is very new. Documentation is [here](http://ggplot.yhathq.com/docs/).

##Popular options

|Name | Call | Other |
|-----|------|-------|
|ABline| geom_abline(intercept = x, slope = y) | Used to draw an intercept line through data |
|Stat_smooth | stat_smooth(se = False) | Used to make a trendline in data. Can show standard error or not. |
|Stat_bin | stat_bin2d() | Makes a heat map | 
| Color Brewer | scale_color_brewer(type='qual') | For more types of color palette, see [here](http://ggplot.yhathq.com/docs/scale_color_brewer.html) |

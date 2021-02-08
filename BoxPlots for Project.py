#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#BoxPlots for Project.py
#Ben Valois, Sharon Fitzsimmons, Renae Rohde, Mark McGrail
#April 24, 2019
#This program will create box plots for the data used

#We, surprisingly have a lot of outliers. In an interesting turn of events, 
#we only have outliers on the high end, so we can examine what is working
#for them. Anything over 0.75 percentile should be studied, but if that is too
#many, definitely anything over 0.9 percentile. I didn't see any, but if any
#are under the 0.25 percentile, obviously it would be good to see what was going 
#on there as well.


# In[28]:


import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

file = pd.ExcelFile("SOWC Cleaned.xlsx")
dataWom = pd.read_excel(file, 'Copy of Women')

dataWom.columns = dataWom.loc[1].fillna('')

dataWom = dataWom.drop(dataWom.index[202:])
dataWom = dataWom.set_index('Countries and areas')

value1 = dataWom['Life expectancy: females as a % of males']
value2 = dataWom['Survival rate to the last grade of primary: females as a % of males']

#creates the figuresize then sets up the boxplot
plt.figure(figsize=(45,5)) 
box_plot_data=[value1,value2]
box=plt.boxplot(box_plot_data,vert=0,patch_artist=True,labels=['LE F%M','SR F%M PS'], )
 
#set colors (yea if that was unclear)
colors = ['cyan', 'lightblue', 'lightgreen']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

print(dataWom['Life expectancy: females as a % of males'].quantile([0.25, 0.5, 0.75, 0.9, 1]))
print(dataWom['Survival rate to the last grade of primary: females as a % of males'].quantile([0.25, 0.5, 0.75, 0.9, 1]))


# In[ ]:






# coding: utf-8

# In[15]:


#HeatMap.py
#Ben Valois, Sharon Fitzsimmons, Renae Rohde, Mark McGrail
#April 24, 2019
#This program creates the heat map for the provided csv.
#Manipulation in Excel was simpler than coding in Python/Pandas, so CSV file was 
#created from original file (SOWC Cleaned) and exported from Excel. 
#It also scans the specified column for values higher than howCorrelated is set to

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#https://stackoverflow.com/questions/42422509/python-using-pandas-to-convert-xlsx-to-csv-file-how-to-delete-index-column/42422542
#data_xls = pd.read_excel('SOWC cleaned Edited High2.xlsx', 'Basic Indicators', index_col=None)
#data_xls.to_csv('csvfile.csv', encoding='utf-8')
df = pd.read_csv('csvfileHigh.csv')

plt.figure(figsize=(100,100))

sns.heatmap(df.corr(), annot=True)


# In[20]:


a = df.corr()
#the following is how you access the different parts of the data
#data.iloc[row, column]
#there should be 210 rows and columns
b = []

#howCorrelated represents the level of correlation used for checking the heatmap
howCorrelated = .69

#uncomment the following code to find all correlations above howCorrelated
#for i in range(209):
#    for j in range(210):
#        if i + 1 == j:
#            break
#        elif a.iloc[i + 1, j] >= howCorrelated or a.iloc[i + 1, j] <= -(howCorrelated):
#            b = b + [[a.iloc[i + 1, j], i+ 1, j]]

#these are the names of the columns and rows in the dataset being used so labeling at the end can be done properly
cols = a.columns.values
rows = a.index.values

#the following commented code will scan the entirety of the heatmap looking for correlations based on howCorrelated
#c = []
#for i in range(len(b)):
#    c = c + [[b[i][0], rows[b[i][1]], cols[b[i][2]]]]


d = []
print('The following is the representation of correlations above |', howCorrelated, '| for life expectancy of females as a % of males and all other categories tested')
print('(represented as [correlated value, variable 1, variable 2] where variable 2 is life expectancy)')
print('\n')

#this will scan the column of the given value, in this case 26 is life expectancy of females as a % of males, and will put all correlations above howCorrelated in a list
for i in range(210):
    if a.iloc[i, 26] >= howCorrelated or a.iloc[i, 26] <= -(howCorrelated):
        d = d + [[a.iloc[i,26], rows[i], cols[26]]]
#prints out the list of correlations above howCorrelated
for i in d:
    print(i)

    
#print("The following are correlations of ", howCorrelated)
#for i in c:
#    print(i)


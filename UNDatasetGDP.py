#!/usr/bin/env python
# coding: utf-8

# In[1]:

#UNDatasetGDP.py
#Ben Valois, Sharon Fitzsimmons, Renae Rohde, Mark McGrail
#April 24, 2019
#This code is used for data prep, returning a csv

import pandas as pd
#files = ['Women_In_Parliament.csv', 'Ratio_GB_Education.csv', 'Population_Area_Density.csv','GDP.csv','Employment.csv','Expenditure_on_Education.csv','Crimes.csv']
delet = ['Series', 'Region/Country/Area', 'Footnotes', 'Source', 'Year']
master = pd.read_csv('Internet_Usage.csv',encoding='latin1')
master.columns = master.iloc[0]
master = master[146:]
master = master[master['Year'] > '2016']
    


# In[2]:



delet = ['Series', 'Region/Country/Area', 'Footnotes', 'Source', 'Year']
for title in delet:
    del master[title]
master.columns = ['Country', '% Internet Use']

#filename: Women_In_Parliament
data = pd.read_csv('Women_In_Parliament.csv',encoding='latin1')
data.columns = data.iloc[0]
m = list(data.columns.values)
data = data[140:]
data = data[data['Year'] > '2017']

delet = ['Series', m[4], 'Last Election Date footnote','Footnotes','Source','Region/Country/Area','Year']
for title in delet:
    del data[title]
data.columns = ['Country', '% Women in Govt']

master = pd.merge(master, data, on = 'Country', how = 'outer')


# In[3]:


#filename: Ratio_GB_Education
data = pd.read_csv('Ratio_GB_Education.csv',encoding='latin1')
data.columns = data.iloc[0]
data = data[229:]
data = data[data['Year'] > '2015']

m = list(data.columns.values)
m[1] = 'Country'
m[4] = 'G to B in Primary Ed'
data.columns = m

delet = [m[0], m[2], m[5], m[6]]
for title in delet:
    del data[title]


#master = pd.merge(master, data, on = 'Country')


# In[4]:


grouped = data.groupby(['Series'])
Prim = grouped.get_group('Ratio of girls to boys in primary education')
master = pd.merge(master,Prim, on = 'Country', how = 'outer')
master = master[:210]


# In[5]:


m = list(data.columns.values)
m[2] = 'G to B Secondary Education'
data.columns = m


# In[6]:


grouped = data.groupby(['Series'])
Second = grouped.get_group('Ratio of girls to boys in secondary education')
master = pd.merge(master,Second, on = 'Country', how = 'outer')


# In[7]:


m = list(data.columns.values)
m[2] = 'G to B Tertiary Education'
data.columns = m


# In[8]:


grouped = data.groupby(['Series'])
Prim = grouped.get_group('Ratio of girls to boys in tertiary education')
master = pd.merge(master,Prim, on = 'Country', how = 'outer')


# In[9]:


del master['Series_x']
del master['Series_y']
del master['Series']


# In[10]:



data = pd.read_csv('Population_Area_Density.csv',encoding='latin1')
data.columns = data.iloc[0]
data = data[900:]
data = data[data['Year'] == '2015']
poss = data.Series.unique().tolist()

delet = ['Region/Country/Area', 'Year','Footnotes','Source']
for title in delet:
    del data[title]
m = list(data.columns.values)
m[0] = 'Country'
data.columns = m

grouped = data.groupby(['Series'])
for item in poss:
    Set = grouped.get_group(item)
    master = pd.merge(master,Set, on = 'Country', how = 'outer')



   
del master['Series_x']
del master['Series_y']


# In[11]:


master = master[:210]


# In[12]:


i = 0
m = list(master.columns.values)
m = m[:6]
for item in poss:
    #use index of poss list to relabel 
    m.append(poss[i])
    i +=1
m
master.columns = m

        #then delete the extra columns
        #then rename the columns using data.columns = m


# In[13]:


master


# In[14]:


data = pd.read_csv('GDP.csv',encoding='latin1')
data.columns = data.iloc[0]
data = data[835:]
data = data[data['Year'] == '2015']
poss = data.Series.unique().tolist()

delet = ['Region/Country/Area', 'Year','Footnotes','Source']
for title in delet:
    del data[title]
m = list(data.columns.values)
m[0] = 'Country'
data.columns = m

grouped = data.groupby(['Series'])
for item in poss:
    Set = grouped.get_group(item)
    master = pd.merge(master,Set, on = 'Country', how = 'outer')



   
del master['Series_x']
del master['Series_y']

i = 0
m = list(master.columns.values)
m = m[:14]
for item in poss:
    #use index of poss list to relabel 
    m.append(poss[i])
    i +=1
master.columns = m


# In[15]:


master = master[:210]


# In[16]:


master


# In[17]:


master.to_csv('UNData.csv')


# In[29]:


Surv = pd.read_excel('SOWC Cleaned Edited.xlsx')
p = list(Surv.columns.values)


# In[34]:


p[0]


# In[38]:


Survival = Surv[[p[0],p[31]]].copy()


# In[40]:


Survival.rename(columns={'Countries and Areas':'Country'}, inplace=True)


# In[41]:


master = pd.merge(master,Survival, on = 'Country')


# In[42]:


master.to_csv('UNData.csv')


# In[43]:


master


# In[ ]:





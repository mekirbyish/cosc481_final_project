#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#ModelingBigProj.py
#Ben Valois, Sharon Fitzsimmons, Renae Rohde, Mark McGrail
#April 24, 2019
#This code will take the provided data and plot it using linear regression

import numpy as np
from sklearn import linear_model
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[12]:


import pandas as pd
data = pd.read_csv('csvfileHigh.csv')

#replace missing values with mean per column
data = data.fillna(data.mean())


# In[ ]:


p = list(data.columns.values)
p


# In[13]:


data.rename(columns={'Life expectancy: females as a % of males':'LifeExp'}, inplace=True)
data.rename(columns={'Minimum acceptable diet 6-23 months (%) 2011-2016*':'Diet'}, inplace=True)
data.rename(columns={'Households with at least one ITN        (%)':'ITN'}, inplace=True)
data.rename(columns={'Population annual growth rate (%) 1990-2016':'PopGrow'}, inplace=True)
data.rename(columns={'Stunting prevalence in children under 5 (moderate & severe) Ratio of poorest to richest':'Stunting'}, inplace=True)


# In[15]:





train, test = train_test_split(data, test_size=0.3)

y_train = train.LifeExp
x1_train = train.Diet
x2_train = train.ITN
x3_train = train.PopGrow
x4_train = train.Stunting

y_test = test.LifeExp
x1_test = test.Diet
x2_test = test.ITN
x3_test = test.PopGrow
x4_test = test.Stunting

x1_train = np.array(x1_train).reshape(-1,1)
x2_train = np.array(x2_train).reshape(-1,1)
x3_train = np.array(x3_train).reshape(-1,1)
x4_train = np.array(x4_train).reshape(-1,1)
y_train = np.array(y_train).reshape(-1,1)

x1_test = np.array(x1_test).reshape(-1,1)
x2_test = np.array(x2_test).reshape(-1,1)
x3_test = np.array(x3_test).reshape(-1,1)
x4_test = np.array(x4_test).reshape(-1,1)
y_test = np.array(y_test).reshape(-1,1)


regr1 = linear_model.LinearRegression()
regr2 = linear_model.LinearRegression()
regr3 = linear_model.LinearRegression()
regr4 = linear_model.LinearRegression()
regr1.fit(x1_train,y_train)
regr2.fit(x2_train,y_train)
regr3.fit(x3_train,y_train)
regr4.fit(x4_train,y_train)
         


# In[22]:



print("Mean Squared Error of regr1:" + str(np.mean(regr1.predict(x1_test) - y_test) ** 2))
print("Mean Squared Error of regr2:" + str(np.mean(regr2.predict(x2_test) - y_test) ** 2))
print("Mean Squared Error of regr3:" + str(np.mean(regr3.predict(x3_test) - y_test) ** 2))
print("Mean Squared Error of regr4:" + str(np.mean(regr4.predict(x4_test) - y_test) ** 2)) 


plt.scatter(x1_train, y_train, color="red")
plt.scatter(x1_test, y_test, color="blue")
plt.plot(x1_test, regr1.predict(x1_test))
plt.title('How Diet Predicts Life Expectancy F % M')
plt.show()

plt.scatter(x2_train, y_train, color="red")
plt.scatter(x2_test, y_test, color="blue")
plt.plot(x2_test, regr2.predict(x2_test))
plt.title('How Mosquito Nets Predict Life Expectancy F % M')
plt.show()

plt.scatter(x3_train, y_train, color="red")
plt.scatter(x3_test, y_test, color="blue")
plt.plot(x3_test, regr3.predict(x3_test))
plt.title('How Population Growth Predicts Life Expectancy F % M')
plt.show()

plt.scatter(x4_train, y_train, color="red")
plt.scatter(x4_test, y_test, color="blue")
plt.plot(x4_test, regr4.predict(x4_test))
plt.title('How Poor Nutrition Predicts Life Expectancy F % M')
plt.show()


# In[ ]:





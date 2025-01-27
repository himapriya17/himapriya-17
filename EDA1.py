#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[34]:


data.info()


# In[35]:


#dataframe atrributes
print(type(data))
print(data.shape)
print(data.size)


# In[36]:


#drop duplicate column(temp c) and unamed column 
data1 = data.drop(['Unnamed: 0',"Temp C"], axis=1)
data1


# In[37]:


#convert the month column data type to  float data type
data['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[38]:


#print all duplicated rows
data1[data1.duplicated(keep = False)]


# In[39]:


#drop duplicated rows
data1.drop_duplicates(keep='first', inplace = True)
data1


# In[40]:


#rename the columns
#CHANGE COLUMN NAME(RENAME THE COLUMNS)
data1.rename({'Solar.R': 'Solar'}, axis=1, inplace = True)
data1


# In[41]:


#imput the missing values
#display the data1 info()
data1.info()


# In[42]:


#display data1 missing values count in each column using isnull().sum()
data1.isnull().sum()


# In[43]:


#viusalize dat1 missing values using heat map
cols = data1.columns
colors = ['black', 'blue']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[44]:


#find the mean and median values of each
median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[45]:


#replace the ozone missing values with median value
data1["Ozone"] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[49]:


#find the mode values of categorcial column(weather)
print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[51]:


#impute missing values(replace nan with mode etc.) of "weather" using mh=fillnan()
data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# 
# detection of outliers in the columns
# 

# In[56]:


#create a figure with two subplots, stacked vertically
fig, axes = plt.subplots(2, 1, figsize=(8,6),gridspec_kw={'height_ratios':[1,3]})
#plot the boxplot un the first (top) subplot
sns.boxplot(data=data1['Ozone'], ax=axes[0], color='skyblue',width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")

sns.histplot(data1["Ozone"], kde=True, ax=axes[1], color='Purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()


# In[ ]:





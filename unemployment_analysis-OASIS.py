#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


data = pd.read_csv("Unemployment in India.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data


# In[6]:


print(data.isnull().sum())


# In[7]:


data.dropna()


# In[8]:


print(data.isnull().sum())


# In[ ]:





# In[10]:


data = data.dropna()


# In[11]:


print(data.isnull().sum())


# In[12]:


data.columns= ["Region","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Area"]


# In[17]:


plt.style.use('dark_background')
plt.figure(figsize=(14, 14))
sns.heatmap(data.corr())
plt.show()


# In[19]:


data.columns= [ "Region","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Area" ]


# In[20]:


regions = data['Region'].unique()


# In[21]:


for region in regions:
    # extract the data for the current region
    region_data = data[data['Region'] == region]['Estimated Employed']
    # plot the histogram
    plt.hist(region_data, alpha=0.5, label=region)


# In[30]:


plt.legend()
plt.xlabel('Estimated Employed')
plt.ylabel('Frequency')
plt.title('Indian Unemployment')
plt.show()


# In[ ]:





# In[25]:


data.columns= ["Region","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Area" ]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# In[32]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment of Different Regions ")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()


# In[46]:


unemployment = data[["Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemployment, path=["Region"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="Viridis", 
                     title="Unemployment Rate in India")
figure.show()


# In[40]:


unemployment_rates = {}
for region in data['Region'].unique():
    unemployment_rates[region] = data[data['Region'] == region]['Estimated Unemployment Rate'].values


# In[41]:


for region, rates in unemployment_rates.items():
    sns.histplot(rates, kde=False, label=region)


# In[42]:


plt.title('Histogram of Estimated Unemployment Rate by Region')
plt.xlabel('Estimated Unemployment Rate')
plt.ylabel('Count')

# Show the legend and plot
plt.legend()
plt.show()






# In[ ]:





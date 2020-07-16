#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv('avocado.csv')


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.head(3)


# In[7]:


df.tail(6)


# In[8]:


df['AveragePrice'].head()


# In[9]:


df.AveragePrice.head()


# In[10]:


albany_df = df[df['region']=="Albany"]


# In[11]:


albany_df.head()


# In[12]:


albany_df.index


# In[13]:


albany_df.set_index("Date")


# In[15]:


albany_df.head()


# In[16]:


albany_df = albany_df.set_index("Date")


# In[17]:


albany_df.head()


# In[18]:


albany_df['AveragePrice'].plot()


# In[20]:


df['Date'] = pd.to_datetime(df['Date'])


# In[21]:


albany_df = df[df['region']=="Albany"]
albany_df.set_index("Date", inplace=True)

albany_df["AveragePrice"].plot()


# In[22]:


albany_df["AveragePrice"].rolling(25).mean().plot()


# In[23]:


albany_df.sort_index(inplace=True)


# In[24]:


albany_df["AveragePrice"].rolling(25).mean().plot()


# In[25]:


albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()


# In[26]:


albany_df.head()


# In[27]:


albany_df.tail()


# In[28]:


albany_df = df.copy()[df['region']=="Albany"]
albany_df.set_index('Date', inplace=True)
albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()


# In[29]:


df['region']


# In[30]:


df['region'].values


# In[32]:


df['region'].values.tolist()



print(set(df['region'].values.tolist()))


# In[33]:


df['region'].unique()


# In[34]:


graph_df = pd.DataFrame()

for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets!
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])


# In[35]:


graph_df.tail()


# In[37]:


import pandas as pd

df = pd.read_csv("avocado.csv")
df = df.copy()[df['type']=='organic']

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by="Date", ascending=True, inplace=True)
df.head()


# In[38]:


graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets! (so df rather than series)
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

graph_df.tail()


# In[39]:


graph_df.plot(figsize=(8,5), legend=False)


# In[ ]:





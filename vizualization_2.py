#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


plt.clf()
sns.set_palette("pastel")


# In[37]:


merged_euro = pd.read_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))
#merged_euro = merged_euro[merged_euro["rank"].isin([1,2,3])] // if we want top 3 finishes only


# In[49]:


df_plot = merged_euro.groupby(['rank', 'country']).size().reset_index().pivot(columns='rank', index='country', values=0)
print(df_plot)

# ordering by descending total (and then deleting the total column so that it won't be rendered in the graph)
df_plot['total'] = df_plot.fillna(0)[1] + df_plot.fillna(0)[2] + df_plot.fillna(0)[3] + df_plot.fillna(0)[4] + df_plot.fillna(0)[5]
df_plot = df_plot.sort_values(by=['total'],ascending=False)
del df_plot['total']


# In[50]:


chart = df_plot.plot(kind='bar', stacked=True)
plt.gcf().set_size_inches(10,8)
plt.setp(chart.get_legend().get_texts(), fontsize='22') # for legend text
plt.setp(chart.get_legend().get_title(), fontsize='22') # for legend title
chart.set_title('Number of Eurovision Top Finishes By Country')

plt.savefig('winspercountry.png')

# In[40]:


#todo: show countries that didn't place in top 5, clickable?, double check if we want top 3 or top 5


# In[ ]:





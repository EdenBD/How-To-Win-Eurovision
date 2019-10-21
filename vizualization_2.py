#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


# In[52]:


plt.clf()
sns.set_palette("pastel")


# In[53]:


merged_euro = pd.read_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))
#merged_euro = merged_euro[merged_euro["rank"].isin([1,2,3])] // if we want top 3 finishes only


# In[126]:


df_plot = merged_euro.groupby(['rank', 'country']).size().reset_index().pivot(columns='rank', index='country', values=0)

# adding zero values for the countries that've never placed in the top in Eurovision
listEurovisionCountries = ["Albania","Andorra","Armenia","Australia","Austria","Azerbaijan",                            "Belarus","Bosnia and Herzegovina","Bulgaria","Croatia","Cyprus","Czech Republic",                          "Denmark","Estonia","Finland","France","Georgia","Germany","Greece","Hungary",                           "Iceland","Ireland","Israel","Italy","Latvia","Lithuania","Luxembourg",                           "Macedonia, FYR","Malta","Moldova","Monaco","Montenegro","Morocco","Netherlands",                           "Norway","Poland","Portugal","Romania","Russia",                            "San Marino","Serbia","Slovak Republic","Slovenia","Spain","Sweden","Switzerland",                            "Turkey","Ukraine","United Kingdom"]
winning_countries = [x.lstrip()  for x in df_plot.index] # getting rid of extra spaces
other_countries =  [item for item in listEurovisionCountries if item not in winning_countries]
for o in other_countries:
    df_plot.loc[o] =  [0, 0, 0, 0, 0]


# ordering by descending total (and then deleting the total column so that it won't be rendered in the graph)
df_plot['total'] = df_plot.fillna(0)[1] + df_plot.fillna(0)[2] + df_plot.fillna(0)[3] + df_plot.fillna(0)[4] + df_plot.fillna(0)[5]
#df_plot = df_plot.sort_values(by=['total'],ascending=False)
del df_plot['total']


# In[127]:


chart = df_plot.plot(kind='bar', stacked=True)
plt.gcf().set_size_inches(20,14)
plt.setp(chart.get_legend().get_texts(), fontsize='22') # for legend text
plt.setp(chart.get_legend().get_title(), fontsize='22') # for legend title
chart.set_title('Number of Eurovision Top Finishes By Country')


# In[118]:


#todo: clickable?, double check if we want top 3 or top 5


# In[128]:


plt.savefig('winspercountry.png')


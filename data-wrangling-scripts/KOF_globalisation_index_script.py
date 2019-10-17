#!/usr/bin/env python
#!pip install xlrd
# coding: utf-8

# ### KOF Globalisation Index
# 
# #### Definition and Description:
# 
# The KOF Globalisation Index is a measure of the economic, social and political dimensions of globalisation. The higher the index score, the higher the level globalisation that country has. KOF_Globalisation_Index.xlsx contains the globalisation statistics for all countries from 1970-2016.
# 
# If a country doesn't have KOF measurements for a particular year, the cells in that row are blank (and represented as NaN in the Pandas dataframe we are making). I noticed that 13 countries (most from the former Soviet bloc countries) only had KOFGI starting at 1991 - we should discuss how to treat the missing data (more detail below).
# 
# For each year in a country, there are many different globalisation measures represented in different columns in this dataset.
# Here is the complete list:
# KOFGI	KOFGIdf	KOFGIdj	KOFEcGI	KOFEcGIdf	KOFEcGIdj	KOFTrGI	KOFTrGIdf	KOFTrGIdj	KOFFiGI	KOFFiGIdf	KOFFiGIdj	KOFSoGI	KOFSoGIdf	KOFSoGIdj	KOFIpGI	KOFIpGIdf	KOFIpGIdj	KOFInGI	KOFInGIdf	KOFInGIdj	KOFCuGI	KOFCuGIdf	KOFCuGIdj	KOFPoGI	KOFPoGIdf	KOFPoGIdj
# 
# According to the definitions in Table 1 in this paper (https://www.e-jei.org/upload/JEI_34_1_133_158_2013600183.pdf), we probably should be focusing on the 'KOFGI' (defined as "KOF overall globalization") column in KOF_Globalisation_index.xlsx as a start.
# 
# 
# 
# 
# #### Source:
# We downloaded KOF_Globalisation_Index.xlsx from https://kof.ethz.ch/en/forecasts-and-indicators/indicators/kof-globalisation-index.html (the link entitled "KOF Globalisation Index_2018_2 (XLSX, 2.9 MB)").
# 
# Citation: Gygli, Savina, Florian Haelg, Niklas Potrafke and Jan-Egbert Sturm (2019): The KOF Globalisation Index – Revisited, Review of International Organizations, https://doi.org/10.1007/s11558-019-09344-2
# 
# 
# 
# 

# In[1]:


import pandas as pd
import os
kof_index = pd.read_excel("../data/KOF_Globalisation_Index.xlsx")


# Next,we create a filter of the 49 countries who have ever participated in Eurovision.
# 
# *Please note that former contestants Serbia and Montenegro and Yugoslavia were both dissolved and came back as separate countries, so we don't need additional entries for them  - The country "Serbia and Montenegro" became Yugoslavia, which became the 2 separate modern day countries, Serbia and Montenegro.

# In[2]:


listEurovisionCountries = ["Albania","Andorra","Armenia","Australia","Austria","Azerbaijan",                            "Belarus","Bosnia and Herzegovina","Bulgaria","Croatia","Cyprus","Czech Republic",                          "Denmark","Estonia","Finland","France","Georgia","Germany","Greece","Hungary",                           "Iceland","Ireland","Israel","Italy","Latvia","Lithuania","Luxembourg",                           "Macedonia, FYR","Malta","Moldova","Monaco","Montenegro","Morocco","Netherlands",                           "Norway","Poland","Portugal","Romania","Russian Federation",                            "San Marino","Serbia","Slovak Republic","Slovenia","Spain","Sweden","Switzerland",                            "Turkey","Ukraine","United Kingdom"]
filterCountries = (kof_index["country"].isin(listEurovisionCountries))
justEurovisionCountries = kof_index[filterCountries]

print("==============================================================================================")
print("Here is all KOF_Index statistics for countries that have participated in Eurovision before:\n")
print(justEurovisionCountries)
print("==============================================================================================")


# #### Example of using justEurovisionCountries:
# 
# Getting the KOFGI score of Switzerland in 1989:

# In[3]:


filter = justEurovisionCountries["year"] == 1989
filter = filter & (justEurovisionCountries["country"] == "Switzerland")
switzerland1989Kofgi = justEurovisionCountries[filter]["KOFGI"]
print(switzerland1989Kofgi)


# #### Missing data 1970-1990:
# 
# A few countries, most from the former Soviet bloc, had only KOFGI scores only starting from 1991:
# 
# (Also, Lithuania and Latvia are the 2 countries who existed in 1970 but didn't have a KOGFI score in 1970 and also weren't part of the 1991-starting countries)

# In[4]:


filter1 = justEurovisionCountries["year"] == 1990
filter1 = filter1 & (pd.isna(justEurovisionCountries["KOFGI"]))
print(justEurovisionCountries[filter1]["country"])

filter1 = justEurovisionCountries["year"] == 1970
filter1 = filter1 & (pd.isna(justEurovisionCountries["KOFGI"]))
print(justEurovisionCountries[filter1]["country"])


# ## Exporting justEurovisionCountries

# In[5]:


justEurovisionCountries.to_csv(os.path.join('../data',r'KOF_globalization_modified.csv'))

# ####  I'm not sure if anything else is needed, but here is some more reformatting of the df in case it's useful:
# ============================================================================================
# 
# Next, we can reformat the dataframe so it has:
# - rows of years
# - columns of country names
# - cells are all specifically the values in the 'KOFGI' column of the original dataset

# In[6]:


pivoted_df = justEurovisionCountries[["year","country","KOFGI"]]
pivoted_df = pivoted_df.pivot(index="country",columns="year",values="KOFGI")
print("==============================================================================================")
print("Here are all the KOFGI values per year, indexed by country:\n")
print(pivoted_df)
print("==============================================================================================")


# #### Example of using pivoted_df:
# 
# (this seems harder than using justEurovisionCountries, but I'm keeping this here in case some operations might be easier with this format?
# Getting the KOFGI score of Switzerland in 1989:

# In[7]:


pivoted_df["country"] = pivoted_df.index
print (pivoted_df[pivoted_df["country"] == "Switzerland"][1989])


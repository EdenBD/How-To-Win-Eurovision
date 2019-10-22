#!/usr/bin/env python
# coding: utf-8

# ## Spotify Script
# 
# We want to get the audio features of the songs that did well in past Eurovisions.
# 
# We will assume that as input, we have 2 lists of strings: 1 with the song names and 1 with the artist names, where the element at the ith index of the song list is the song, and the element at the ith index of the artist list is the artist who sang that song.
# 
# The input is completely hard-coded for now.

# In[14]:


import json
import urllib.request
from urllib.request import Request
from pandas.io.json import json_normalize
from unidecode import unidecode
import pandas as pd
import os


# We now need to get a token to access the Spotify API. For now, I'm using a temporary token (so this string will need to be replaced very often) generated from the "Get Token" button here: https://developer.spotify.com/console/get-audio-features-track/?id=06AKEBrKUckW0KREUWRnvT

# In[15]:


current_token = 'BQDUqgTI688Fw7Fq87mVLuiAngFePetx9Ov7EwB0U3fjzdwaegZro9qZW_gUdRIRS8J4iMh1MPRzDB9HL6Vxoo1n6PLYHsPi24qyw3AIlhvrl2TPG1jpFHE4i2ciLQSkDOk81abTz-UrTy0zP7kFdMJjptPrIefoiw'


# Here are some hard-coded data inputs:

# In[28]:

eurovision_df = pd.read_csv(os.path.join(os.pardir,'data',r'cleaned_wikipedia_songs.csv'))

# songs = ['Euphoria', 'Rise Like a Phoenix']
# artists = ['Loreen','Conchita Wurst']
# print(eurovision_df.describe(include=['O']))
songs = eurovision_df['song'].tolist()
artists = eurovision_df['artist'].tolist()

print('len=',len(songs),len(artists))
# We also want to keep track of null-values (songs that aren't in the Spotify API):

# In[29]:


countNulls = 0


# Data is our result list that will keep all the JSONs we get:

# In[30]:


data = []
for i in range(len(songs)):
    
    # formatting spaces
    song = songs[i].replace(" ","%20")
    artist = artists[i].replace(" ","%20")

    # going from artist / song name to song URI (https://developer.spotify.com/documentation/web-api/reference/search/search/)
    request = Request('https://api.spotify.com/v1/search?q=track:' + song + '%20artist:' + artist + '&type=track&limit=1')
    request.add_header('Accept', 'application/json')
    request.add_header('Content-Type', 'application/json')
    request.add_header('Authorization', 'Bearer ' + current_token)
    res = urllib.request.urlopen(request)
    resObject = json.load(res)

    if (len(resObject["tracks"]["items"]) == 0):
        countNulls += 1
    else:
        songURI = resObject["tracks"]["items"][0]["id"]
        # name = resObject["tracks"]["items"][0]["name"]
        name = songs[i]

        # going from song URI -> audio features (https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)
        audioRequest = Request('https://api.spotify.com/v1/audio-features/' + songURI)
        audioRequest.add_header('Accept', 'application/json')
        audioRequest.add_header('Content-Type', 'application/json')
        audioRequest.add_header('Authorization', 'Bearer ' + current_token)
        audioRes = urllib.request.urlopen(audioRequest)
        jsonObject = json.load(audioRes)

        # adding the song name into JSON
        jsonObject["name"] = name

        data.append(jsonObject)

# converting the list of JSON objects -> a dataframe
df = json_normalize(data)
print(df)


# We then export our results from the dataframe into CSV:

# In[31]:

# requires running the file from within the data-wrangling directory
df.to_csv(os.path.join(os.pardir,'data',r'spotify_audio_features.csv'))


# ### # Nulls
# 
# We now see how many null values there were:

# In[32]:


print("Number of Nulls: ", countNulls)
print("Number of Songs: ", len(df))


# ### Miscellaneous Stuff
# 
# To see how a res object (where res = urllib.request.urlopen(request)) looks in a JSON format:
# 
#     print(res.read().decode())
# 
# Here's a dataset where they label what each Spotify track feature means: https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018

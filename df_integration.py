import pandas as pd
from pandas.api.types import is_numeric_dtype
import os
import string
from unidecode import unidecode


# cleaning wikipedia_songs after wrangling that happens in python 2
def update_cleaned_wikipedia_songs():
    def pre_proccesing_strings(obj):
        if isinstance(obj, str):
            # handling French special letters.
            fr_to_en = unidecode(obj)
            modified = fr_to_en.translate(str.maketrans('','',string.punctuation+string.digits))
            return modified
        return obj

    eurovision_df = pd.read_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))
    eurovision_df = eurovision_df[(eurovision_df.year > 1974) & (eurovision_df.year < 2017)]

    for column in ['song','artist','country','language']:
        eurovision_df[column] =  eurovision_df.apply(lambda row:  pre_proccesing_strings(row[column]), axis=1)
    for numeric_column in ['rank','points','year']:
        eurovision_df[numeric_column] = eurovision_df.apply(lambda row: 0 if row[numeric_column]=='-' else int(row[numeric_column]), axis=1)
    eurovision_df = eurovision_df[(eurovision_df['rank'] < 6) & (eurovision_df['rank'] > 0)]

    # fixing song with digit title
    index = eurovision_df.index[pd.isnull(eurovision_df.loc[:,'song'])]  
    eurovision_df.loc[index,'song'] = 1994  
    
    eurovision_df.to_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))

def integrate_databases():

    def replace_null(df_series, value):
        if pd.isnull(value):
            if is_numeric_dtype(df_series):
                return large_spotify[column].median()
            elif column == 'key':
                #equal C
                return 0 
            elif column == 'mode':
                # equal major
                return 1
            elif column == 'time_signature':
                # equal 4/4
                return 4
        return value

    # 50% null
    spotify = pd.read_csv(os.path.join('data',r'spotify_audio_features.csv'))
    spotify.rename({"name": "song"}, axis=1, inplace=True)
    wiki = pd.read_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))
    merged = pd.merge(spotify, wiki, how='right', on=['song'])
    
    merged = merged.loc[:, ~merged.columns.str.contains('^Unnamed')]
    merged.drop(columns=['type','id','uri','track_href','analysis_url','duration_ms'], inplace=True)
    # fill null values with median of larger spotify dataset
    large_spotify = pd.read_csv(os.path.join('data',r'large_spotify_songs.csv'))
    spotify_columns = ((set(merged.keys())).difference(set(wiki.keys()))) & set(large_spotify.keys())
    for column in spotify_columns: 
        merged[column] =  merged.apply(lambda row:  replace_null(large_spotify[column], row[column]), axis=1)  
   
    print('merged len',len(merged))
    merged.to_csv(os.path.join('data',r'merged_euro.csv'))


if __name__ == "__main__":
    # run python wrangling_wiki.py data/wikipedia_songs.txt data/cleaned_wikipedia_songs.csv 
    # to install python2 run: apt update && apt install -y python python-pip 
    # update_cleaned_wikipedia_songs()   
    integrate_databases() 
import pandas as pd
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
    eurovision_df =  eurovision_df.applymap(lambda x:  pre_proccesing_strings(x))
    eurovision_df.to_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))

def integrate_databases():
    spotify = pd.read_csv(os.path.join('data',r'spotify_audio_features.csv'))
    spotify.rename({"name": "song"}, axis=1, inplace=True)
    wiki = pd.read_csv(os.path.join('data',r'cleaned_wikipedia_songs.csv'))
    merged = pd.merge(spotify, wiki, how='inner', on=['song'])
    merged.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y'], inplace=True)
    merged.to_csv(os.path.join('data',r'merged_euro.csv'))



if __name__ == "__main__":
    # update_cleaned_wikipedia_songs()   
    integrate_databases() 
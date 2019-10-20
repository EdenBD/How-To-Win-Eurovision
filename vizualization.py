import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

integrated = pd.read_csv(os.path.join('data',r'merged_euro.csv'))
large_spotify = pd.read_csv(os.path.join('data',r'large_spotify_songs.csv'))
subset = large_spotify.sample(50)

music_columns = {'acousticness','instrumentalness', 'liveness', 'valence', 'energy', 'loudness', 'speechiness', 'danceability', 'tempo'}

for column in music_columns:
    plt.clf()
    p = sns.distplot(integrated[(integrated['rank'] == 1)][column], label='1st place', hist=True, rug=True)
    sns.distplot(integrated[(integrated['rank'] == 2)][column], label='2nd place', hist=True, rug=True)
    sns.distplot(integrated[(integrated['rank'] == 3)][column], label='3rd place', hist=True, rug=True)
    # sns.distplot(integrated[(integrated['rank'] == 4)][column], label='4th place', hist=True, rug=True)
    # sns.distplot(integrated[(integrated['rank'] == 5)][column], label='5th place', hist=True, rug=True)
    sns.distplot(subset[column], label='Larger dataset', hist=True, rug=True)


    p.set_title('{} distribution'.format(column))
    p.set_xlabel('')
    p.legend()
    plt.savefig('historgam {}.png'.format(column))
    plt.clf()

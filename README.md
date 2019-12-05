[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EdenBD/How-To-Win-Eurovision/master)
# How-To-Win-Eurovision
Our MIT 6.S080 final project: visualizating and analyzing data relating to Eurovision top-ranking country and song characteristics throughout the years.

Here are some of the files in our repo:

### data-wrangling scripts:
- `KOF_globalisation_index_script.ipynb`: creates KOF_globalization_modified.csv (our cleaned KOF index dataset) from KOF_Globalisation_Index.xlsx
- `spotify_script.ipynb`: creates spotify_audio_features.csv (our spotify datset) by gathering data via Spotify API calls
- `votes_dataset_script.ipynb`: creates votes_dataset_clean.csv from eurovision_song_contest_1975_2016.xlsx
- `wrangling_wiki.py`: we scraped Wikipedia to extract the top 5 wininning Eurovision songs at each year into a txt file, and then used Wrangle to clean/organize the data set. The wrangling script creates cleaned_wikipedia_songs.csv.

### data-integration-scripts:
- `countries_distance.ipynb`: adding a geographoc distance column between pairs of countries by integrating the countriesarea.csv and votes datasets.
- `spotify_wiki_integration.py`: creating merged_euro.csv, a file with the audio features corresponding to each of the songs in the wikipedia table. 
- `integrating_KOF_and_votes.ipnb`: to check the correlation between the votes that a country gets with its globaliztion index KOF. 

### data:
contains both our original and cleaned datasets

### visualuzations:
- `world_vs_eurviosion_songs_features.py` and `histograms.png`: a summary of the distributions of different audio features in Eurovision songs compared with general Spotify songs.
- `voting_2_countries_mutual.png`: an example of 2 countries that have given each other significanlty more points throughout the years than the average Eurovision country would give them
- `voting_cluster_map.png`: a map of counry clusters that tend to vote for each other
- `voting_map.png`: an illustration of country voting patterns on a map of Europe

### other:
- `votes_vs_country_dist_visualization.ipynb`: investigating and visualizing correlation between country distance and voting trends
- `votes_visualization.ipynb`: creates some of the visualizations of country pair voting patterns. The interactive visualization on the map is not rendered on Github: to see it, re-run the notebook in [Binder](https://mybinder.org/v2/gh/EdenBD/How-To-Win-Eurovision/4050b026639a67d4242224411b708bf63d8cbcf6). You can also modify parameters to show some visualizations for different pairs of countries.

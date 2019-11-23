# How-To-Win-Eurovision
Our MIT 6.S080 final project: visualizating and analyzing data relating to Eurovision top-ranking country and song characteristics throughout the years

Here are some of the files in our repo:

### data-wrangling scripts:
- KOF_globalisation_index_script.ipynb: creates KOF_globalization_modified.csv (our cleaned KOF index dataset) from KOF_Globalisation_Index.xlsx
- spotify_script.ipynb: creates spotify_audio_features.csv (our spotify datset) by gathering data via Spotify API calls
- votes_dataset_script.ipynb: creates votes_dataset_clean.csv from eurovision_song_contest_1975_2016.xlsx

### data:
contains both our original and cleaned datasets

### visualuzations:
- histogram.png: a summary of the distributions of different audio features in Eurovision songs compared with general Spotify songs
- voting_2_countries_mutual.png: an example of 2 countries that have given each other significanlty more points throughout the years than the average Euroviison country would give them
- voting_cluster_map.png: a map of counry clusters that tend to vote for each other

### other:
- countries_distance.ipynb / votes_vs_country_dist_visualization.ipynb: investigating and visualizing correlation between country distance and voting trends
- votes_visualization.ipynb: creates some of the visualizations of country pair voting patterns

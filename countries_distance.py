import pandas as pd
import os

# loading data sets
countries_names_to_code = pd.read_csv(os.path.join('data',r'countryarea.csv'))[['Country Name','Country Code']]

votes = pd.read_csv(os.path.join('data',r'votes_with_minorities.csv'))
votes.drop(columns=['Unnamed: 0'],inplace=True)
print(countries_names_to_code.head())
print(len(countries_names_to_code))
print(votes.head())
print(len(votes))

# adding code to FROM countries
votes_with_code = pd.merge(votes, countries_names_to_code, how='inner', left_on=['From country'], right_on=['Country Name'])
votes_with_code.drop(columns=['Country Name'],inplace=True)
votes_with_code.rename(columns={"Country Code": "From country code"},inplace=True)

# adding code to TO countries
votes_with_code = pd.merge(votes_with_code, countries_names_to_code, how='inner', left_on=['To country'], right_on=['Country Name'])
votes_with_code.drop(columns=['Country Name'],inplace=True)
votes_with_code.rename(columns={"Country Code": "To country code"},inplace=True)
votes_with_code = votes_with_code[['Year', '(semi-) final', 'Jury or Televoting','From country', 'From country code', 'To country', 
                   'To country code','Points', '2_minority_in_1']]
# loading distances 
countries_distw = pd.read_csv(os.path.join('data',r'countries_distw.csv'))[['iso_o','iso_d','distw']]

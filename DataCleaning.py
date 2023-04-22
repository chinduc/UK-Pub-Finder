import pandas as pd
import numpy as np

pubs = pd.read_csv('open_pubs.csv', header=None)
pubs.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']


pubs.head()

pubs = pubs.replace('\\N', np.nan)

pubs = pubs.dropna()

pubs['longitude'] = pd.to_numeric(pubs['longitude'], errors='coerce')
pubs['latitude'] = pd.to_numeric(pubs['latitude'], errors='coerce')

#Saving the cleaned dataset
pubs.to_csv('cleaned_pubs_data.csv')
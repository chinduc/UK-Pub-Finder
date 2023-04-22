import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static



pubs = pd.read_csv('cleaned_pubs_data.csv', index_col=0)
pubs.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']



st.markdown("<h1 style='text-align: center; color: BLACK; font-weight: bold;'>Pub Finder Application</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: BLUE;'>Pub List</h2>", unsafe_allow_html=True)


search_type = st.radio("Search by:", ('Postal Code', 'Local Authority'))


if search_type == 'Postal Code':
    search_list = pubs['postcode'].unique()
else:
    search_list = pubs['local_authority'].unique()


search_value = st.selectbox(f"Select a {search_type}:", search_list)


if search_type == 'Postal Code':
    newPubs = pubs[pubs['postcode'] == search_value]
else:
    newPubs = pubs[pubs['local_authority'] == search_value]


st.write(f"Displaying {len(newPubs)} pubs in {search_value}:")
st.dataframe(newPubs)


m = folium.Map(location=[newPubs['latitude'].mean(), newPubs['longitude'].mean()], zoom_start=13)


for index, row in newPubs.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(m)


folium_static(m)


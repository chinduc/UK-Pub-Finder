import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

pubs = pd.read_csv('cleaned_pubs_data.csv', index_col=0)


st.markdown("<h1 style='text-align: center; color: BLACK; font-weight: bold;'>Pub Finder Application</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: BLUE;'>Find the Nearest Pub</h2>", unsafe_allow_html=True)


lat = st.number_input("Enter your latitude:",value=50.95)
lon = st.number_input("Enter your longitude:",value=-3.94)


pubs['distance'] = pubs.apply(lambda record: np.sqrt((record['latitude']-lat)**2 + (record['longitude']-lon)**2), axis=1)


nearest_pubs = pubs.sort_values(by='distance').head(5)
st.write(f"Displaying 5 pubs near you(lat: {lat}, lon: {lon}):")
st.dataframe(nearest_pubs)


m = folium.Map(location=[lat, lon], zoom_start=13)


folium.Marker(location=[lat, lon], icon=folium.Icon(color='red'), popup='Your Location').add_to(m)


marker_cluster = MarkerCluster().add_to(m)
for index, record in nearest_pubs.iterrows():
    Marker([record['latitude'], record['longitude']], popup=record['name']).add_to(marker_cluster)


st.write("Map of the nearest pubs:")
folium_static(m)

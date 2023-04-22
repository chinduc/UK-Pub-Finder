import streamlit as st
import pandas as pd
import numpy as np


pubs = pd.read_csv('cleaned_pubs_data.csv', index_col=0)



st.markdown("<h1 style='text-align: center; color: BLACK; font-weight: bold;'>Pub Finder Application</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: BLUE;'>Welcome !</h2>", unsafe_allow_html=True)


st.image('pub.jpg', use_column_width=True)


st.write(f"Total pubs : **{len(pubs)}**")
st.write(f"Across **{len(pubs['local_authority'].unique())}** local authorities.")
 
st.markdown("<h3 style='text-align: center; color: BLUE;'>Pub Statistics</h3>", unsafe_allow_html=True)

stats = pubs.describe().T
stats['count'] = stats['count'].astype(int)
st.dataframe(stats)


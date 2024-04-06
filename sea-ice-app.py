import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
#import matplotlib.pyplot as plt
import numpy as np

st.title("Ice Area by Year")
st.header("Northern and Southern Hemisphere ")
st.subheader("from 1978 to 2013")



df = pd.read_csv("monthly_sea_ice_index.csv")

f1 = df["data-type"] != "-9999"
f2 = df["area"] > -9999
f3 = df["extent"] > -9999
fN = df["region"] == "N"
fS = df["region"] == "S"

df_north = df.loc[f1 & f2 & f3 & fN]
df_south = df.loc[f1 & f2 & f3 & fS]


col1, col2 = st.columns(2)
with col1:
    st.write(df_north.describe())
with col2:    
    st.write(df_south.describe())
    
# north 
df_north_area = df_north.groupby(["year"])["area"].mean()
df_north_area = df_north_area.to_frame().reset_index()

df_north_extent = df_north.groupby(["year"])["extent"].mean()
df_north_extent = df_north_extent.to_frame().reset_index()

# south
df_south_area = df_south.groupby(["year"])["area"].mean()
df_south_area = df_south_area.to_frame().reset_index()

df_south_extent = df_south.groupby(["year"])["extent"].mean()
df_south_extent = df_south_extent.to_frame().reset_index()

#############################
#
#############################
option = st.selectbox(
    'Select hemisphere',
    ('North', 'South')
)

if option == "North":
    header = '''
        ### Northern Hemisphere
        In millions of km<sup>2</sup>
    '''
    dfa = df_north_area
    dfe = df_north_extent
    
else:
    header = '''
        ### Southern Hemisphere
        In millions of km<sup>2</sup>
    '''
    dfa = df_south_area
    dfe = df_south_extent
    
st.markdown(header, unsafe_allow_html=True)



pxline = px.line(dfa, x="year", y="area", title='Yearly average ice area by year')
pxline

pxline = px.line(dfe, x="year", y="extent", title='Yearly average ice extend by year')
pxline
  

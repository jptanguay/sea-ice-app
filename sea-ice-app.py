import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
#import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("monthly_sea_ice_index.csv")

#st.table(df.describe())

#st.table(df.head(5))

f1 = df["data-type"] != "-9999"
f2 = df["region"] == "N"
f3 = df["area"] > -9999
f4 = df["extent"] > -9999

df_north = df.loc[f1 & f2 & f3 & f4]

st.title("Ice Area by Year")
st.header("Northern and Southern Hemisphere ")
st.subheader("from 1978 to 2013")
st.write(df_north.describe())


#st.dataframe(df_north)


df_north_area = df_north.groupby(["year"])["area"].mean()
df_north_area = df_north_area.to_frame().reset_index()
#st.write(df_north_area.head())


df_north_extent = df_north.groupby(["year"])["extent"].mean()
df_north_extent = df_north_extent.to_frame().reset_index()


col1, col2 = st.columns(2)

###with col1:
#st.line_chart( pd.DataFrame(df_north_area) )
#chart_df = alt.Chart( df_north_area ).mark_line().encode(
#    y=alt.Y('area', scale=alt.Scale(domain=[8, 12], clamp=True)),
#    #x=alt.X('year'),
#    x="year"
#    #color='type'
#)

st.write('''
    ### Northern Hemisphere
    In millions of km<sup>2</sup>
''')


pxline = px.line(df_north_area, x="year", y="area", title='Yearly average area by year')
pxline


    
    
#with col2:
pxline = px.line(df_north_extent, x="year", y="extent", title='Yearly average extend by year')
pxline
   
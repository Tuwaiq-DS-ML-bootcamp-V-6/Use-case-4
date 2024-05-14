import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
from scipy.stats import zscore
import dtale as dt
import plotly.graph_objects as go
df=pd.read_csv("data_saudi_used_cars.csv")
st.title("Looking to buy a used car in Saudi Arabia ?")

st.write("The used car market in Saudi Arabia is booming, and is expected to reach $8.69 billion by 2027. My colleagues and I were interested in finding  what brands of cars are being sold in Saudi Arabia and what regions in Saudi Arabia has the highest sales of used cars.")
st.write("We came across a website called  '' Sayarah "".Its a website that offers new and used cars from various brands and models in Saudi Arabia. On the Sayarah website, people can buy, sell, or exchange cars.")

st.write("Through the analysis of  datasets on website  '' Sayarah "" ,we aim to gain a better understanding of the variables, such as engine size, mileage, and year, that affect used car costs.")

numerical_columns = ['Year', 'Engine_Size', 'Mileage', 'Price']
corr_matrix = df[numerical_columns].corr()

# Create a heatmap using Plotly
fig1 = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.index,
    colorscale='Blues'
))

# Update layout for better visualization
fig1.update_layout(
    title='Count of Cars by Region and Make',
    xaxis_title='Year_Engine_Size',
    yaxis_title='Mileage_Price',
    width=800,
    height=800
)

# Display the heatmap
st.plotly_chart(fig1, use_container_width=True)

st.write("I began by counting all of the renters in each rental unit. For instance, there are more people renting cars in Riyadh than in other locations, which is to be expected given the city's population and status as a capital.")


fig = px.bar(
    df, 
    x='Region',  
    color='Region', 
    title='Make of Cars by Make and Region',
    color_discrete_sequence=['#0000FF', '#1E90FF', '#00BFFF']  )


fig.update_layout(
    width=500,
    height=500,
    title='Make of Cars by Make and Region'
)


st.plotly_chart(fig, use_container_width=True)
st.write("Our exploration dives into two key aspects of the Saudi used car market:")
st.write("Price Spectrum:")
st.write("We'll unveil the spread of used car prices in the dataset. This will show you the range of what you can expect to pay for a pre-owned vehicle in Saudi Arabia.")
st.write("Market Muscle: ")
st.write("We'll calculate the total value of all the used cars (excluding those listed for free). This will give you a sense of the overall size and economic power of the Saudi used car market.")

fig2 = px.bar(
    df, 
    x='Make',  
    color='Make', 
    title='Make of Cars by Make and Region',
    color_discrete_sequence=['#0000FF', '#1E90FF', '#00BFFF']  )


fig2.update_layout(
    width=500,
    height=500,
    title= 'Make of Cars by Make and Region'
)


st.plotly_chart(fig2, use_container_width=True)

st.write('Conclusion:')
st.write("There are two factors that affect the price of a price of a used car:")
st.write(".  Mileage")
st.write(".  Engine size")
st.write(".  Year of the car")
st.write("If we have low mileage in the car, that increases the price of the used car.")
st.write("Also, if the engine size is large, the price will increase.")
st.write("Don't forget that the year of the car has a significant effect on its price. ")


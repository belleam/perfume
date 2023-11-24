## Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests


## Load the data
perfume_df = pd.read_csv('perfume_df.csv')
csim = pd.read_csv('shape_csim_df.csv')
csim = csim.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
shape_indices = pd.Series(csim.index, index=perfume_df['Name']).drop_duplicates()


## Page configuration
st.set_page_config(page_title='Shape matcher', layout='wide')


## Function for the recommendation
def shape_recommendations(name):
    idx = shape_indices[name]
    nb_closest_images = 4
    closest_shapes = csim.loc[idx].sort_values(ascending=False)[1:nb_closest_images+1].index
    get_numbers = [float(i) for i in closest_shapes]
    st.write('Similar bottles')
    col1, col2 = st.columns(2)
    for i in get_numbers[0:2]:
        with col1:
            st.image(perfume_df['Image URL'].loc[i], width=150)
            st.write(perfume_df['Name'].loc[i])
            st.write(perfume_df['Brand'].loc[i])
    for i in get_numbers[2:5]:
        with col2:
            st.image(perfume_df['Image URL'].loc[i], width=150)
            st.write(perfume_df['Name'].loc[i])
            st.write(perfume_df['Brand'].loc[i])


## Page configuration
def main():

    ## Header
    scent_image = Image.open('shapes.png')
    col1, col2, col3 = st.columns([1, 1.5, 1])
    col2.image(scent_image, use_column_width=True)

    ## Get input from the user
    brands = perfume_df['Brand'].drop_duplicates()
    brand = st.selectbox('Select a brand', brands)
    names = perfume_df['Name'].loc[perfume_df['Brand'] == brand]
    name = st.selectbox('Select your fragrance', names)

    ## Display image  
    st.write('Bottle')
    idx = shape_indices[name]
    st.image(perfume_df['Image URL'].loc[idx], width=250)

    ## Launch recommendation function
    matchmake = ''
    ## Button
    if st.button('Meet your match'):
        matchmake = shape_recommendations(name)


if __name__ == '__main__':
    main()
## Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.neighbors import NearestNeighbors


## Load the data
perfume_df = pd.read_csv('perfume_df.csv')
sent_mat_df = pd.read_csv('sent_matrix_df.csv')
sent_indices = pd.Series(sent_mat_df.index, index=perfume_df['Name']).drop_duplicates()


## Page configuration
st.set_page_config(page_title='Sensation matcher', layout='wide')


## Function for the recommendation
def sensation_recommendations(name):
    idx = sent_indices[name]
    print('Selected fragrance:', perfume_df['Name'].iloc[idx])
    print('Notes:', perfume_df['Notes'].iloc[idx])
    knn_model = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors=6)
    knn_model.fit(sent_mat_df.values)
    distances, indices = knn_model.kneighbors(sent_mat_df.iloc[idx,:].values.reshape(1,-1))
    perfume_indices = indices.flatten()
    perfume_indices = perfume_indices[1:6]
    rec = perfume_df[['Name', 'Brand', 'Description']].iloc[perfume_indices]

    return st.dataframe(rec)


## Page configuration
def main():

    ## Header
    scent_image = Image.open('sentiments.png')
    col1, col2, col3 = st.columns([1, 1.5, 1])
    col2.image(scent_image, use_column_width=True)

    ## Get input from the user
    brands = perfume_df['Brand'].drop_duplicates()
    brand = st.selectbox('Select a brand', brands)
    names = perfume_df['Name'].loc[perfume_df['Brand'] == brand]
    name = st.selectbox('Select your fragrance', names)

    ## Display description
    st.write('Fragrance description')
    input_desc = perfume_df['Description'].loc[perfume_df['Name'] == name].values[0]
    st.write(input_desc)

    ## Launch recommendation function
    matchmake = ''
    ## Button
    if st.button('Meet your match'):
        matchmake = sensation_recommendations(name)


if __name__ == '__main__':
    main()
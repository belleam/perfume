## Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


## Load the data
perfume_df = pd.read_csv('perfume_df.csv')
cosine_sim_df = pd.read_csv('scent_csim_df.csv')
note_indices = pd.Series(cosine_sim_df.index, index=perfume_df['Name']).drop_duplicates()


## Page configuration
st.set_page_config(page_title='Scent matcher', page_icon='🫧', layout='wide')


## Function for the recommendation
def scent_recommendations(name, cosine_sim_df=cosine_sim_df):
    idx = note_indices[name]
    sim_scores = list(enumerate(cosine_sim_df.iloc[idx,:]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    perfume_indices = [i[0] for i in sim_scores]
    rec = perfume_df[['Name', 'Brand', 'Notes']].iloc[perfume_indices]
    st.dataframe(rec, hide_index=True)


## Page configuration
def main():

    ## Header
    scent_image = Image.open('scent.png')
    col1, col2, col3 = st.columns([1, 1.5, 1])
    col2.image(scent_image, use_column_width=True)

    ## Get input from the user
    brands = perfume_df['Brand'].drop_duplicates()
    brand = st.selectbox('Select a brand', brands)
    names = perfume_df['Name'].loc[perfume_df['Brand'] == brand]
    name = st.selectbox('Select your fragrance', names)

    ## Display notes
    st.write('Scent notes')
    input_notes = perfume_df['Notes'].loc[perfume_df['Name'] == name].values[0]
    st.write(input_notes)

    ## Launch recommendation function
    matchmake = ''
    ## Button
    if st.button('Meet your match'):
        matchmake = scent_recommendations(name)


if __name__ == '__main__':
    main()
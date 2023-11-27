## Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


## Page configuration
st.set_page_config(page_title='Fragrance Matcher', page_icon='🫧', layout='wide')


## Page configuration
def main():

    ## Header
    scent_image = Image.open('fragrance.png')
    col1, col2, col3 = st.columns([1, 1.5, 1])
    col2.image(scent_image, use_column_width=True)
    st.header('Welcome to the fragrance matchmaker')
    st.write('Head to the sidebar to select your matchmaker and discover your new favourite perfume')
    st.subheader('Scent Matcher')
    st.write('Matches by scent notes for favourite fragances')
    st.subheader('Sensation Matcher')
    st.write('Matches by emotions in the descriptions to fit the mood')
    st.subheader('Shape Matcher')
    st.write('Matches by bottle shape for desired aesthetics')


if __name__ == '__main__':
    main()
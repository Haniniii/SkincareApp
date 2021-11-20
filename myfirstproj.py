# read data into a DataFrame
import pandas as pd
import csv
import streamlit as st
from PIL import Image

st.write("""
# Simple Skincare Recommending App
This app recommend **product** from multiple brands :)
""")

if st.button('Click ME'): st.write('Please scroll down, thank you.')

else: st.write('You are beautiful just the way you are!')
#st.write("Click the play button!")
video_file = open('myvideo.mp4', 'rb')
video_bytes= video_file.read()

st.video(video_bytes)

st.write('Before you continue, please watch the video and read the [terms and conditions.](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')

data = pd.read_csv('skincare_products.csv')
if show:
    st.write("Please choose which product that you wish us to recommend on the **sidebar** button.")
    st.image('skincare.jpg')

#### RENAME THE COLUMNS
data.columns = ['Product Name','URL', 'Product Type','Ingredients','Price']
del data['URL']

#st.write(data)
option = st.sidebar.selectbox(
    'Select product type',
     ['Option','Moisturiser','Serum','Oil','Mist','Mask'])

if option=='Moisturiser':

    st.subheader('Recommended Moisturiser')
    del data['Product Type']
    data.iloc[0:10,0:5]

elif option=='Serum':

    
    st.subheader('Recommended Serum')
    del data['Product Type']
    data.iloc[11:21,0:5]


elif option=='Oil':

    
    st.subheader('Recommended Oil')
    del data['Product Type']
    data.iloc[21:31,0:5]

elif option=='Mist':

    
    st.subheader('Recommended Mist')
    del data['Product Type']
    data.iloc[31:41,0:5]

elif option=='Mask':

    
    st.subheader('Recommended Mask')
    del data['Product Type']
    data.iloc[41:51,0:5]

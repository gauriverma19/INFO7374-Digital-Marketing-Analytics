import streamlit as st
import numpy as np
import pandas as pd

add_selectbox = st.sidebar.radio(
    "Select a search method",
    ("Similarity Search", "Facebook AI")
)

if add_selectbox == 'Similarity Search' :
 st.title("**_Recommendations using similarity search_**")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('algo1.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Select an image from below :point_down:")
 pic = st.selectbox('Images:', images)
 st.write("**Image you selected:**")
 st.image(pic,width=None)


 z = st.slider('How many similar products would you like to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("YOU MAY ALSO LIKE:")
 #st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

elif add_selectbox == 'Facebook AI':
 st.title("Recommendations using facebook AI")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('algo2.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Select an image from below :point_down:")
 pic = st.selectbox('Images:', images)
 st.write("**Image you selected:**")
 st.image(pic,width=None)


 z = st.slider('How many similar products would you like to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("YOU MAY ALSO LIKE:")
 #st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

 





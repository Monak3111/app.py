import streamlit as st
import pandas as pd

st.title('Machine Learning App')
df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")

               

st.write('This app builds a machine learning model')

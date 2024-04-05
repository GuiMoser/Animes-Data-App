import pandas as pd
import streamlit as st
import plotly.express as px

animes_df = pd.read_csv('anime.csv')

st.title('Animes Recommendations App')


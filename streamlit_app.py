#Importing packages
import streamlit as st
import pandas as pd

data_url = "https://raw.githubusercontent.com/davis011235/ECON8320-Project/main/df.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

data = load_data(data_url)

st.title("ECON 8320 Project")

x = st.sidebar.selectbox(
    'x variable',
    ('Year', 'Hours Usually Worked', 'Household Income',
       'Household Members', 'HS or GED', 'Years of College',
       'Ever in Military', 'Currently in Military', 'Union Member', 'City')
)
y = st.sidebar.selectbox(
    'y variable',
    ('Year', 'Hours Usually Worked', 'Household Income',
       'Household Members', 'HS or GED', 'Years of College',
       'Ever in Military', 'Currently in Military', 'Union Member', 'City')
)

st.sidebar.checkbox(
    'Filter by City', False)

st.scatter_chart(data = data, x = x, y = y)


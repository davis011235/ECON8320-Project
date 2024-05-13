# Importing packages
import streamlit as st
import pandas as pd

data_url = "https://raw.githubusercontent.com/davis011235/ECON8320-Project/main/df.csv"

# Caching data so the dashboard runs faster
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

data = load_data(data_url)

# Adding title
st.title("ECON 8320 Project")

# Creating selectbox for x axis variable
x = st.sidebar.selectbox(
    'x variable',
    ('Year', 'Hours Usually Worked', 'Household Income',
       'Household Members', 'HS or GED', 'Years of College',
       'Ever in Military', 'Currently in Military', 'Union Member', 'City')
)
# Creating selectbox for y axis variable
y = st.sidebar.selectbox(
    'y variable',
    ('Year', 'Hours Usually Worked', 'Household Income',
       'Household Members', 'HS or GED', 'Years of College',
       'Ever in Military', 'Currently in Military', 'Union Member', 'City')
)
    
# Generating scatter plot of x and y variables
st.scatter_chart(data = data, x = x, y = y)


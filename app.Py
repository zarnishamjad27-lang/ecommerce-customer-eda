
import streamlit as st
import pandas as pd

st.title("E-commerce Customer Analysis")

df = pd.read_csv('Ecommerce Customers.csv')

st.write(df.head())

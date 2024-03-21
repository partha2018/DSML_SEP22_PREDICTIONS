import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

st.header('This is a header with a divider', divider='rainbow')
st.header('Partha is :blue[cool] :sunglasses:')
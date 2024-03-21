import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


def square(num):
    return num * num


number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.write("Result is: ",square(number))
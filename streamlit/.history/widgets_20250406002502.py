import streamlit  as st
import pandas as pd

st.title('Streamlit Text Input')

name = st.text_input('Enter you name')

age = st.slider('Select you age : ', 0, 100, 25)


st.write(f'Age is {age}')
options = ['Python', 'Java', 'C++', 'JS']

choice = st.selectbox('Choose you lang : ', options=options)
st.write(f'your choice is {choice}')

if name:
    st.write(f'Hello, {name}')
    

uploaded_file = st.file_uploader('Choose a CSV file : '  , type='csv')  

if uploaded_file is not None:
    df =  
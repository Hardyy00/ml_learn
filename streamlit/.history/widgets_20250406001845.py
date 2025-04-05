import streamlit  as st

st.title('Streamlit Text Input')

name = st.text_input('Enter you name')

age = st.slider('Select you age')

if name:
    st.write(f'Hello, {name}')
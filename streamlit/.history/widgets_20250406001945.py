import streamlit  as st

st.title('Streamlit Text Input')

name = st.text_input('Enter you name')

age = st.slider('Select you age : ', 0, 100, 25)

if name:
    st.write(f'Hello, {name}')
    st.write(f'Age is {age}')
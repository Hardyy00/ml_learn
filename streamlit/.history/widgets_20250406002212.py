import streamlit  as st

st.title('Streamlit Text Input')

name = st.text_input('Enter you name')

age = st.slider('Select you age : ', 0, 100, 25)


st.write(f'Age is {age}')
options = ['Python', 'Java', 'C++', 'JS']

choice = st.selectbox('Choose you lang : ', options=options)


if name:
    st.write(f'Hello, {name}')
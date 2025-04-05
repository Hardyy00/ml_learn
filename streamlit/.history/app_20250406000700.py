import streamlit as st
import pandas as pd
import numpy as np


## title of the application
st.title('Hello Hardik')

## display a simple text

st.write('This is a simple text')

## create a simple dataframe

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40,50]
})
import streamlit as st
import pandas as pd
import numpy as np
import duckdb


st.title("# SQL SRS Spaced Repetition System SQL Practice")
st.write("Hello world")

option = st.selectbox(
    'What would you like to review?',
    ['Join', 'GroupBy', 'Windows Functions'],
    index=None,
    placeholder="Select a theme...",
)

st.write("You've selected: ", option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)


tab1, tab2, tab3, tab4 = st.tabs(["Recherche", "Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="Entrez votre input")
    st.write("Vous avez entré la query suivante: " + str(sql_query))
    st.dataframe(duckdb.sql(sql_query).df())


   #result = duckdb.sql(sql_query).df()
   #st.write(f"Vous avez entré la query suivante: {sql_query}")
   #st.dataframe(result)

with tab2:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab3:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab4:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



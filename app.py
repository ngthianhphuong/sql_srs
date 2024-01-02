import streamlit as st
import pandas as pd
import numpy as np
import duckdb
import io

st.title("# SQL SRS Spaced Repetition System SQL Practice")

csv = """
beverage, price
orange juice, 2.5
expresso, 2 
tea, 3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food-item, food_price
cookie juice, 2.5
chocolatine, 2
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(csv2))

with st.sidebar:
    option = st.selectbox(
        'What would you like to review?',
        ['Join', 'GroupBy', 'Windows Functions'],
        index=None,
        placeholder="Select a theme...",
    )

    st.write("You've selected: ", option)

# la réponse que l'utilisateur doit donner
answer = """
SELECT * FROM beverages
CROSS JOIN 
food_items"""

# la solution = la dataframe créée à partir de la requête SQL
solution = duckdb.sql(answer).df()

st.header("Enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    # l'output de la requête de l'utilisateur
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("Expected output:")
    st.dataframe(solution)



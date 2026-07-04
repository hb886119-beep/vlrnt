import streamlit as st
import pandas as pd
import sqlite3

st.title("💰 무기 가격 분석")

def get_connection():
    return sqlite3.connect("valorant.db")

df = pd.read_sql_query("SELECT weapon, price FROM guns", get_connection())

df_unique = df.drop_duplicates()

st.bar_chart(df_unique.set_index("weapon"))
st.dataframe(df_unique.sort_values("price", ascending=False))

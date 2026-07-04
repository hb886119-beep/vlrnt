import streamlit as st
import pandas as pd
import sqlite3

st.title("🔥 사용률 TOP 무기")

def get_connection():
    return sqlite3.connect("valorant.db")

df = pd.read_sql_query("SELECT weapon, pick_rate FROM guns", get_connection())

df_unique = df.groupby("weapon").mean().sort_values("pick_rate", ascending=False)

st.bar_chart(df_unique)

st.dataframe(df_unique)

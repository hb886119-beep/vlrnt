import streamlit as st
import pandas as pd
import sqlite3

st.title("🔫 무기 데이터 (20개)")

def get_connection():
    return sqlite3.connect("valorant.db")

@st.cache_data
def load_data():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM guns", conn)
    conn.close()
    return df

df = load_data()

weapon = st.selectbox("무기 선택", df["weapon"].unique())

st.dataframe(df[df["weapon"] == weapon])

st.line_chart(
    df[df["weapon"] == weapon].set_index("range")[["damage_head", "damage_body", "damage_leg"]]
)

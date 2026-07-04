import streamlit as st
import pandas as pd
import sqlite3

st.title("📉 거리별 데미지 분석")

def get_connection():
    return sqlite3.connect("valorant.db")

df = pd.read_sql_query("SELECT * FROM guns", get_connection())

avg = df.groupby("range")[["damage_head", "damage_body", "damage_leg"]].mean()

st.subheader("전체 무기 평균 거리 데미지")
st.line_chart(avg)

weapon = st.selectbox("무기 선택", df["weapon"].unique())
st.line_chart(df[df["weapon"] == weapon].set_index("range")[["damage_head", "damage_body", "damage_leg"]])

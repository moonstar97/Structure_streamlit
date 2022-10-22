import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

df_agg = pd.read_csv("data/grade_num.csv", encoding="cp949")
df_agg["연도"] = df_agg["연도"].astype(int)

st.set_page_config(
    page_title="9조 streamlit_page",
    page_icon="🖍",
    layout="wide",
)

st.markdown("# 2. 연도별 과목별 학업성취도")

st.markdown("## 2.1. 학업성취도 우수학생 수")

st.sidebar.header('피처를 선택해주세요')

selected_school = st.sidebar.selectbox('중학교 / 고등학교',
   ["중학교", "고등학교"])

st.sidebar.write("9조 보고서 링크📌")
st.sidebar.markdown("[9조 보고서](https://www.notion.so/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9)")

if selected_school == "중학교":
    fig1_1 = px.line(df_agg, x="연도", y="3수준학생수(중)"
                , color="과목", markers=True)
    fig1_1.update_layout(autosize=False,
    width=1000,
    height=800)
    fig1_1.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig1_1)

elif selected_school == "고등학교":
    fig1_2 = px.line(df_agg, x="연도", y="3수준학생수(고)"
                , color="과목", markers=True)
    fig1_2.update_layout(autosize=False,
    width=1000,
    height=800)
    fig1_2.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig1_2)

st.markdown("## 2.2. 학업성취도 열등학생 수")

if selected_school == "중학교":
    fig2_1 = px.line(df_agg, x="연도", y="1수준학생수(중)"
                , color="과목", markers=True)
    fig2_1.update_layout(autosize=False,
    width=1000,
    height=800)
    fig2_1.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig2_1)

elif selected_school == "고등학교":
    fig2_2 = px.line(df_agg, x="연도", y="1수준학생수(고)"
                , color="과목", markers=True)
    fig2_2.update_layout(autosize=False,
    width=1000,
    height=800)
    fig2_2.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig2_2)

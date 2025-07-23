import streamlit as st
import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("universities.csv")

st.set_page_config(page_title="대학 추천기", page_icon="🎓")
st.title("🎓 대학 추천 시스템")
st.write("당신의 **모의고사 등급**을 입력하면, 지원 가능한 대학을 추천해드립니다.")

# 사용자 입력 받기
grade = st.slider("당신의 평균 등급은?", 1, 9, 5)

# 추천 대학 필터링
available_universities = df[df["최소등급"] >= grade]

# 결과 출력
if not available_universities.empty:
    st.subheader(f"✅ {grade}등급으로 지원 가능한 대학 리스트:")
    st.dataframe(available_universities.reset_index(drop=True))
else:
    st.warning("😥 해당 등급으로 지원 가능한 대학이 없습니다.")

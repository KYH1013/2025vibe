import streamlit as st
import random

st.set_page_config(page_title="점심메뉴 추천기", page_icon="🍱")
st.title("🍽️ 점심 메뉴 추천기")

# 메뉴 리스트
menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", "비빔밥",
    "라멘", "우동", "햄버거", "샐러드", "초밥",
    "파스타", "피자", "쌀국수", "냉면", "떡볶이"
]

# 버튼 누르면 바로 추천
if st.button("오늘 뭐 먹을까? 🍱"):
    choice = random.choice(menus)
    st.success(f"오늘의 추천 메뉴는 **{choice}** 입니다! 😋")

# 전체 메뉴 보기
with st.expander("📋 전체 메뉴 보기"):
    st.write(", ".join(menus))

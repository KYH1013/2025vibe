import streamlit as st
import random

st.set_page_config(page_title="점심 메뉴 추천기", page_icon="🍱")

st.title("🍱 오늘 뭐 먹지?")
st.write("메뉴가 고민될 땐 클릭 한 번으로 추천!")

menu_list = [
    "김치찌개", "된장찌개", "제육볶음", "비빔밥", "불고기",
    "라멘", "우동", "쌀국수", "햄버거", "샐러드", "파스타", "초밥", "치킨"
]

if st.button("메뉴 추천 받기 🎲"):
    choice = random.choice(menu_list)
    st.success(f"👉 오늘은 **{choice}** 어떠세요? 😋")

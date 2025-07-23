import streamlit as st
import random
import time

# 페이지 기본 설정
st.set_page_config(page_title="점심메뉴 룰렛", page_icon="🍱")

st.title("🎯 점심메뉴 룰렛 추천기")

# 기본 점심 메뉴 리스트
menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", "비빔밥",
    "라멘", "우동", "햄버거", "샐러드", "초밥",
    "파스타", "피자", "쌀국수", "냉면", "떡볶이"
]

# 룰렛 돌리기 버튼
if st.button("🎲 메뉴 돌리기"):
    with st.spinner("룰렛 돌리는 중..."):
        for _ in range(20):  # 회전 횟수 조절
            choice = random.choice(menus)
            st.markdown(
                f"<h3 style='text-align:center'>🍽️ {choice}</h3>",
                unsafe_allow_html=True
            )
            time.sleep(0.1)

        final = random.choice(menus)
        st.success(f"✅ 오늘의 점심은 **{final}** 어떠세요? 😋")

# 전체 메뉴 리스트 보기
with st.expander("📋 전체 메뉴 보기"):
    st.write(", ".join(menus))

import streamlit as st
import random

st.set_page_config(page_title="점심메뉴 추천기", page_icon="🍱")
st.title("🍽️ 점심 메뉴 추천기")

# 기본 메뉴
default_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", "비빔밥",
    "라멘", "우동", "햄버거", "샐러드", "초밥",
    "파스타", "피자", "쌀국수", "냉면", "떡볶이"
]

# 세션 상태로 전체 메뉴 관리
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()

# 🔤 사용자 입력
new_menu = st.text_input("메뉴를 추가해보세요 ✏️")
if st.button("➕ 메뉴 추가"):
    if not new_menu.strip():
        st.warning("⚠️ 메뉴를 입력해주세요.")
    elif new_menu.strip() in st.session_state.menus:
        st.info("이미 있는 메뉴입니다.")
    else:
        st.session_state.menus.append(new_menu.strip())
        st.success(f'"{new_menu.strip()}" 메뉴가 추가되었습니다!')

# 🎲 추천 버튼
if st.button("오늘 뭐 먹을까? 🍱"):
    choice = random.choice(st.session_state.menus)
    st.success(f"오늘의 추천 메뉴는 **{choice}** 입니다! 😋")

# 📋 전체 메뉴 리스트 출력
with st.expander("전체 메뉴 보기"):
    st.write(", ".join(st.session_state.menus))

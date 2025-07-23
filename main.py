import streamlit as st
import random

st.set_page_config(page_title="점심메뉴 추천기", page_icon="🍱")
st.title("🍽️ 점심 메뉴 추천기")

# 기본 메뉴 (삭제 불가)
default_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", "비빔밥",
    "라멘", "우동", "햄버거", "샐러드", "초밥",
    "파스타", "피자", "쌀국수", "냉면", "떡볶이"
]

# 세션 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()
if "user_added" not in st.session_state:
    st.session_state.user_added = []

# 🔤 사용자 메뉴 입력
new_menu = st.text_input("메뉴를 추가해보세요 ✏️")
if st.button("➕ 메뉴 추가"):
    new_menu = new_menu.strip()
    if not new_menu:
        st.warning("⚠️ 메뉴를 입력해주세요.")
    elif new_menu in st.session_state.menus:
        st.info("이미 있는 메뉴입니다.")
    else:
        st.session_state.menus.append(new_menu)
        st.session_state.user_added.append(new_menu)
        st.success(f'"{new_menu}" 메뉴가 추가되었습니다!')

# 🎲 추천
if st.button("오늘 뭐 먹을까? 🍱"):
    choice = random.choice(st.session_state.menus)
    st.success(f"오늘의 추천 메뉴는 **{choice}** 입니다! 😋")

# 📋 전체 메뉴 보기
with st.expander("전체 메뉴 보기"):
    st.write(", ".join(st.session_state.menus))

# ❌ 사용자 추가 메뉴 제거
st.subheader("🧹 사용자 추가 메뉴 제거")
if st.session_state.user_added:
    menu_to_remove = st.selectbox("삭제할 메뉴를 선택하세요", st.session_state.user_added)
    if st.button("❌ 메뉴 제거 요청"):
        st.session_state.menus.remove(menu_to_remove)
        st.session_state.user_added.remove(menu_to_remove)
        st.success(f'"{menu_to_remove}" 메뉴가 제거되었습니다.')
else:
    st.info("사용자가 추가한 메뉴가 없습니다.")

import streamlit as st
import streamlit.components.v1 as components
import json

# 초기 설정
st.set_page_config(page_title="귀여운 점심 룰렛", page_icon="🍙")
st.title("🎀 귀여운 점심메뉴 룰렛")

# 기본 메뉴
default_menus = [
    "김치찌개", "제육볶음", "돈까스", "라멘", "비빔밥",
    "우동", "햄버거", "샐러드", "초밥", "파스타"
]

# 세션 상태 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()
if "user_added" not in st.session_state:
    st.session_state.user_added = []

# ✅ 메뉴 추가
with st.form("add_form"):
    new_menu = st.text_input("🍽️ 메뉴 추가", placeholder="예: 순두부찌개")
    submitted = st.form_submit_button("➕ 추가하기")
    if submitted:
        new_menu = new_menu.strip()
        if not new_menu:
            st.warning("⚠️ 메뉴를 입력해주세요.")
        elif new_menu in st.session_state.menus:
            st.info("이미 있는 메뉴입니다.")
        else:
            st.session_state.menus.append(new_menu)
            st.session_state.user_added.append(new_menu)
            st.success(f'"{new_menu}" 메뉴가 추가되었습니다!')

# ✅ 메뉴 제거
st.subheader("🧹 사용자 추가 메뉴 제거")
if st.session_state.user_added:
    remove_target = st.selectbox("삭제할 메뉴 선택", st.session_state.user_added)
    if st.button("❌ 제거하기"):
        st.session_state.menus.remove(remove_target)
        st.session_state.user_added.remove(remove_target)
        st.success(f'"{remove_target}" 메뉴가 삭제되었습니다.')
else:
    st.info("사용자가

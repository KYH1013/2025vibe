import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="점심 룰렛", page_icon="🍱")
st.title("🎯 점심메뉴 원판 룰렛")

# 기본 고정 메뉴
default_menus = [
    "김치찌개", "제육볶음", "돈까스", "라멘", "비빔밥",
    "우동", "햄버거", "샐러드", "초밥", "파스타"
]

# 세션 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()
if "user_added" not in st.session_state:
    st.session_state.user_added = []

# ✅ 메뉴 추가 섹션
with st.form(key="menu_form"):
    new_menu = st.text_input("🍽️ 메뉴를 추가해보세요", placeholder="예: 순두부찌개")
    submitted = st.form_submit_button("➕ 추가하기")
    if submitted:
        cleaned = new_menu.strip()
        if not cleaned:
            st.warning("⚠️ 메뉴를 입력해주세요.")
        elif cleaned in st.session_state.menus:
            st.info("이미 있는 메뉴입니다.")
        else:
            st.session_state.menus.append(cleaned)
            st.session_state.user_added.append(cleaned)
            st.success(f'"{cleaned}" 메뉴가 추가되었습니다!')

# ✅ 사용자 추가 메뉴 제거
st.subheader("🧹 추가한 메뉴 제거")
if st.session_state.user_added:
    remove_target = st.selectbox("삭제할 메뉴 선택", st.session_state.user_added)
    if st.button("❌ 제거하기"):
        st.session_state.menus.remove(remove_target)
        st.session_state.user_added.remove(remove_target)
        st.success(f'"{remove_target}" 메뉴가 삭제되었습니다.')
else:
    st.info("사용자가 추가한 메뉴가 없습니다.")

# ✅ 룰렛 삽입 (PickerWheel)
menu_query = ",".join(st.session_state.menus)
iframe_code = f"""
<iframe src="https://pickerwheel.com/emb/?choices={menu_query}&mode=spin" 
width="100%" height="500" frameborder="0" scrolling="no"></iframe>
"""
components.html(iframe_code, height=520)

# 📋 전체 메뉴 보기
with st.expander("📋 현재 룰렛에 포함된 메뉴"):
    st.write(", ".join(st.session_state.menus))

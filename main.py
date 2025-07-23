import streamlit as st
import random
import time

st.set_page_config(page_title="점심 메뉴 룰렛", page_icon="🍱")
st.title("🎯 점심메뉴 룰렛 추천기")
    ]

# ✅ 사용자 메뉴 입력
new_menu = st.text_input("🍽️ 메뉴를 직접 추가해보세요!")
if st.button("➕ 메뉴 추가"):
    if new_menu.strip() == "":
        st.warning("메뉴를 입력해주세요.")
    elif new_menu in st.session_state.menus:
        st.info("이미 존재하는 메뉴입니다.")
    else:
        st.session_state.menus.append(new_menu.strip())
        st.success(f'"{new_menu.strip()}" 메뉴가 추가되었습니다!')

# ✅ 룰렛 돌리기
if st.button("🎲 메뉴 돌리기"):
    with st.spinner("룰렛 돌리는 중..."):
        for _ in range(15):
            choice = random.choice(st.session_state.menus)
            st.markdown(f"<h3 style='text-align:center'>🍽️ {choice}</h3>", unsafe_allow_html=True)
            time.sleep(0.1)
        final_choice = random.choice(st.session_state.menus)
        st.success(f"✅ 오늘의 점심은 **{final_choice}** 어떠세요? 😋")

# ✅ 전체 메뉴 보기
with st.expander("📋 전체 메뉴 보기"):
    st.write(", ".join(st.session_state.menus))

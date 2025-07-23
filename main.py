import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="PickerWheel 점심 룰렛", page_icon="🍱")
st.title("🎡 PickerWheel 점심 룰렛 + 광주 맛집 추천")

# 메뉴-맛집 매핑
restaurant_map = {
    "김치찌개": ["나산식당 - 동구", "궁전김치찌개 - 서구", "시골통돼지볶음 - 광산구"],
    "돈까스": ["무등왕돈까스 - 서구", "진심왕돈까스 - 광산구", "카츠앤맘 전대점 - 전대"],
    "제육볶음": ["대추골식당 - 북구", "함지박식당 - 남구"],
    "라멘": ["이로리라멘 - 동명동", "멘야하나비 - 수완지구"],
    "비빔밥": ["솔밭가든 - 북구", "돌솥밥집 - 동구"],
    "우동": ["사누끼우동 - 상무지구", "오모가리우동 - 봉선동"],
    "햄버거": ["버거스올마이티 - 전대", "버거스베로 - 수완"],
    "샐러드": ["샐러드마켓 - 상무지구", "그린키친 - 봉선동"],
    "초밥": ["초밥집이요 - 남구", "스시하루 - 동명동"],
    "파스타": ["더플레이트 - 봉선동", "트라토리아 - 중외공원"],
    "피자": ["피제리아다로마 - 전대후문", "더플레이버 - 상무지구"],
    "쌀국수": ["에머이 - 봉선동", "퍼싸이공 - 운암"],
    "냉면": ["을밀대 - 광천동", "봉평메밀막국수 - 동림동"],
    "떡볶이": ["엽기떡볶이 - 광주점", "떡볶이공방 - 운암"],
}

# 기본 메뉴
default_menus = list(restaurant_map.keys())

# 세션 상태
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()
if "user_added" not in st.session_state:
    st.session_state.user_added = []

# 메뉴 추가
with st.form("add_menu"):
    new_menu = st.text_input("🍽️ 메뉴 추가", placeholder="예: 국밥")
    if st.form_submit_button("➕ 추가"):
        new_menu = new_menu.strip()
        if new_menu and new_menu not in st.session_state.menus:
            st.session_state.menus.append(new_menu)
            st.session_state.user_added.append(new_menu)
            st.success(f'"{new_menu}" 메뉴가 추가되었습니다.')
        elif not new_menu:
            st.warning("메뉴를 입력해주세요.")
        else:
            st.info("이미 있는 메뉴입니다.")

# 메뉴 제거
st.subheader("🧹 사용자 메뉴 제거")
if st.session_state.user_added:
    to_remove = st.selectbox("삭제할 메뉴 선택", st.session_state.user_added)
    if st.button("❌ 제거"):
        st.session_state.menus.remove(to_remove)
        st.session_state.user_added.remove(to_remove)
        st.success(f'"{to_remove}" 메뉴가 삭제되었습니다.')

# ▶ PickerWheel iFrame 출력
menu_str = ",".join(st.session_state.menus)
iframe_code = f"""
<iframe src="https://pickerwheel.com/emb/?choices={menu_str}&mode=spin" 
width="100%" height="500" frameborder="0" scrolling="no"></iframe>
"""
st.components.v1.html(iframe_code, height=520)

# 추천 결과 뽑기 버튼
st.markdown("---")
st.subheader("🎯 선택된 메뉴로 광주 맛집 추천")

selected_menu = st.selectbox("✅ 룰렛에서 뽑힌 메뉴를 선택하세요", st.session_state.menus)
if st.button("📍 맛집 추천 보기"):
    if selected_menu in restaurant_map:
        st.success(f"🍴 **{selected_menu}**에 어울리는 광주 맛집:")
        for r in restaurant_map[selected_menu]:
            st.write(f"- {r}")
    else:
        st.warning("등록된 맛집 정보가 없는 메뉴입니다.")

# 전체 메뉴 보기
with st.expander("📋 현재 전체 메뉴 목록 보기"):
    st.write(", ".join(st.session_state.menus))

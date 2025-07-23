import streamlit as st

st.set_page_config(page_title="PickerWheel 점심 룰렛", page_icon="🍱")
st.title("🎡 PickerWheel 점심 룰렛 + 광주 맛집 추천")

# ✅ 기본 메뉴-맛집 매핑
if "restaurant_map" not in st.session_state:
    st.session_state.restaurant_map = {
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

# 유저 추가 메뉴/맛집 기록용
if "user_added_menus" not in st.session_state:
    st.session_state.user_added_menus = []
if "user_added_restaurants" not in st.session_state:
    st.session_state.user_added_restaurants = {}

# 메뉴 리스트
def get_all_menus():
    return list(st.session_state.restaurant_map.keys())

# 메뉴 추가
with st.form("add_menu"):
    st.subheader("🍽️ 메뉴 추가")
    new_menu = st.text_input("추가할 메뉴", placeholder="예: 국밥")
    if st.form_submit_button("➕ 메뉴 추가"):
        if new_menu and new_menu not in st.session_state.restaurant_map:
            st.session_state.restaurant_map[new_menu] = []
            st.session_state.user_added_menus.append(new_menu)
            st.success(f"'{new_menu}' 메뉴가 추가되었습니다.")
        else:
            st.warning("이미 있는 메뉴거나 입력이 비어있습니다.")

# 맛집 추가
with st.form("add_restaurant"):
    st.subheader("🏪 맛집 추가")
    menu_choice = st.selectbox("📌 메뉴 선택", get_all_menus())
    restaurant_name = st.text_input("맛집 이름", placeholder="예: 홍익국밥")
    restaurant_location = st.text_input("위치", placeholder="예: 동구")
    if st.form_submit_button("🏷️ 맛집 추가"):
        if restaurant_name and restaurant_location:
            full = f"{restaurant_name} - {restaurant_location}"
            if full not in st.session_state.restaurant_map[menu_choice]:
                st.session_state.restaurant_map[menu_choice].append(full)
                if menu_choice not in st.session_state.user_added_restaurants:
                    st.session_state.user_added_restaurants[menu_choice] = []
                st.session_state.user_added_restaurants[menu_choice].append(full)
                st.success(f"{full} 맛집이 '{menu_choice}'에 추가되었습니다.")
            else:
                st.info("이미 등록된 맛집입니다.")
        else:
            st.warning("맛집 이름과 위치를 모두 입력해주세요.")

# 맛집 제거
st.subheader("❌ 맛집 제거")
if st.session_state.user_added_restaurants:
    menu_for_remove = st.selectbox("삭제할 맛집의 메뉴", list(st.session_state.user_added_restaurants.keys()))
    restaurant_to_remove = st.selectbox("삭제할 맛집", st.session_state.user_added_restaurants[menu_for_remove])
    if st.button("🗑️ 맛집 제거"):
        st.session_state.restaurant_map[menu_for_remove].remove(restaurant_to_remove)
        st.session_state.user_added_restaurants[menu_for_remove].remove(restaurant_to_remove)
        st.success(f"{restaurant_to_remove} 맛집이 제거되었습니다.")
else:
    st.info("사용자가 추가한 맛집이 없습니다.")

# 메뉴 제거
st.subheader("🧹 메뉴 제거")
if st.session_state.user_added_menus:
    menu_to_remove = st.selectbox("삭제할 사용자 메뉴", st.session_state.user_added_menus)
    if st.button("❌ 메뉴 완전 제거"):
        del st.session_state.restaurant_map[menu_to_remove]
        st.session_state.user_added_menus.remove(menu_to_remove)
        if menu_to_remove in st.session_state.user_added_restaurants:
            del st.session_state.user_added_restaurants[menu_to_remove]
        st.success(f"'{menu_to_remove}' 메뉴와 관련 맛집이 삭제되었습니다.")
else:
    st.info("사용자가 추가한 메뉴가 없습니다.")

# 룰렛 iFrame
st.subheader("🎰 룰렛으로 추천받기")
menu_str = ",".join(get_all_menus())
iframe_code = f"""
<iframe src="https://pickerwheel.com/emb/?choices={menu_str}&mode=spin" 
width="100%" height="500" frameborder="0" scrolling="no"></iframe>
"""
st.components.v1.html(iframe_code, height=520)

# 결과 보기
st.markdown("---")
st.subheader("📍 룰렛 결과로 맛집 보기")
selected_menu = st.selectbox("🎯 선택된 메뉴", get_all_menus())
if st.button("🍴 맛집 추천"):
    restaurants = st.session_state.restaurant_map.get(selected_menu, [])
    if restaurants:
        st.success(f"{selected_menu}에 어울리는 광주 맛집 추천:")
        for r in restaurants:
            st.write(f"- {r}")
    else:
        st.warning("등록된 맛집이 없습니다.")

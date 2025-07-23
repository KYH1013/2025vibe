import streamlit as st
import streamlit.components.v1 as components
import json

# Streamlit 설정
st.set_page_config(page_title="점심 룰렛", page_icon="🍙")
st.title("🎯 점심메뉴 룰렛 + 광주 맛집 추천")

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

# 세션 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()
if "user_added" not in st.session_state:
    st.session_state.user_added = []
if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = None

# 메뉴 추가
with st.form("add_menu_form"):
    new_menu = st.text_input("🍽️ 메뉴 추가", placeholder="예: 국밥")
    if st.form_submit_button("➕ 추가하기"):
        new_menu = new_menu.strip()
        if new_menu and new_menu not in st.session_state.menus:
            st.session_state.menus.append(new_menu)
            st.session_state.user_added.append(new_menu)
            st.success(f'"{new_menu}" 메뉴가 추가되었습니다!')
        elif not new_menu:
            st.warning("메뉴를 입력해주세요.")
        else:
            st.info("이미 있는 메뉴입니다.")

# 메뉴 제거
st.subheader("🧹 사용자 추가 메뉴 제거")
if st.session_state.user_added:
    remove_target = st.selectbox("삭제할 메뉴", st.session_state.user_added)
    if st.button("❌ 제거하기"):
        st.session_state.menus.remove(remove_target)
        st.session_state.user_added.remove(remove_target)
        st.success(f'"{remove_target}" 메뉴가 삭제되었습니다.')

# JSON 메뉴 리스트
menu_json = json.dumps(st.session_state.menus)

# HTML 룰렛 + 결과 JS 연결
html_code = f"""
<div id="arrow" style="width:0;height:0;border-left:20px solid transparent;
  border-right:20px solid transparent;border-bottom:30px solid #ff3385;margin:20px auto;"></div>
<div id="wheel" style="width:400px;height:400px;border-radius:50%;
  border:8px solid #ff66b2;margin:auto;overflow:hidden;position:relative;"></div>
<div style="text-align:center;margin-top:20px;">
  <button id="spinBtn" style="background:#ff66b2;color:#fff;padding:10px 20px;
    font-size:18px;border:none;border-radius:10px;cursor:pointer;">🎡 룰렛 돌리기</button>
  <div id="result" style="font-size:24px;margin-top:10px;color:#ff3399;"></div>
</div>
<script>
  const items = {menu_json};
  const wheel = document.getElementById("wheel");

  function createWheel() {{
    wheel.innerHTML = "";
    const angle = 360 / items.length;
    items.forEach((item, i) => {{
      const seg = document.createElement("div");
      seg.className = "segment";
      seg.style.width = "50%";
      seg.style.height = "50%";
      seg.style.position = "absolute";
      seg.style.top = "50%";
      seg.style.left = "50%";
      seg.style.transformOrigin = "0% 0%";
      seg.style.transform = `rotate(${{angle * i}}deg) skewY(${{90 - angle}}deg)`;
      seg.style.background = `hsl(${{i * (360/items.length)}}, 100%, 90%)`;
      seg.innerHTML = `<div style="transform:skewY(-${{90 - angle}}deg) rotate(-${{angle * i}}deg);
        width:100px;text-align:center;padding-top:5px;">${{item}}</div>`;
      wheel.appendChild(seg);
    }});
  }}

  createWheel();

  document.getElementById("spinBtn").onclick = () => {{
    const spinDeg = 3600 + Math.floor(Math.random() * 360);
    wheel.style.transition = "transform 4s ease-out";
    wheel.style.transform = `rotate(${{spinDeg}}deg)`;
    const idx = (items.length - Math.floor((spinDeg % 360) / (360 / items.length))) % items.length;
    const selected = items[idx];
    document.getElementById("result").innerText = `🎉 오늘의 메뉴는 "${{selected}}"!`;
    fetch("/_process_result", {{
      method: "POST",
      body: JSON.stringify({{ menu: selected }}),
      headers: {{ "Content-Type": "application/json" }}
    }});
  }};
</script>
"""

# 클라이언트에서 선택된 결과를 받을 수 있는 구성
def handle_result():
    import streamlit.web.server.websocket_headers
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    from streamlit.runtime.state import get_session_state

    ctx = get_script_run_ctx()
    session_id = ctx.session_id
    result = st.experimental_get_query_params().get("result")
    if result:
        st.session_state.selected_menu = result[0]

components.html(html_code, height=600)

# 결과에 따른 맛집 출력
if st.session_state.selected_menu and st.session_state.selected_menu in restaurant_map:
    st.markdown(f"### 📍 광주 맛집 추천: **{st.session_state.selected_menu}**")
    for place in restaurant_map[st.session_state.selected_menu]:
        st.write(f"- {place}")

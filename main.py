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
    st.info("사용자가 추가한 메뉴가 없습니다.")

# ✅ 메뉴 JSON 변환
menu_data = json.dumps(st.session_state.menus)

# ✅ 룰렛 HTML 코드 (Google Fonts + CSS 애니메이션 포함)
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    * {{
      font-family: 'Jua', sans-serif;
    }}
    #wheel {{
      width: 400px;
      height: 400px;
      border-radius: 50%;
      border: 8px solid #ff66b2;
      position: relative;
      margin: auto;
      overflow: hidden;
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }}
    .segment {{
      width: 50%;
      height: 50%;
      position: absolute;
      top: 50%;
      left: 50%;
      transform-origin: 0% 0%;
      background-color: #ffe6f0;
      border: 1px solid #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      text-align: center;
      padding: 5px;
    }}
    #arrow {{
      width: 0;
      height: 0;
      border-left: 20px solid transparent;
      border-right: 20px solid transparent;
      border-bottom: 30px solid #ff3385;
      margin: 20px auto;
    }}
    #spinBtn {{
      background-color: #ff66b2;
      color: white;
      border: none;
      padding: 10px 20px;
      font-size: 18px;
      border-radius: 10px;
      cursor: pointer;
    }}
    #result {{
      text-align: center;
      margin-top: 10px;
      font-size: 24px;
      color: #ff3399;
    }}
  </style>
</head>
<body>

<div id="arrow"></div>
<div id="wheel"></div>
<div style="text-align:center; margin-top:20px;">
  <button id="spinBtn">🍭 룰렛 돌리기</button>
  <div id="result"></div>
</div>

<script>
  const items = {menu_data};
  const wheel = document.getElementById("wheel");

  function createWheel(items) {{
    wheel.innerHTML = "";
    const len = items.length;
    const angle = 360 / len;
    items.forEach((item, i) => {{
      const segment = document.createElement("div");
      segment.className = "segment";
      segment.style.transform = `rotate(${{angle * i}}deg) skewY(${{90 - angle}}deg)`;
      segment.style.background = `hsl(${{i * (360 / len)}}, 100%, 90%)`;
      segment.innerHTML = `<div style="transform: skewY(-${{90 - angle}}deg) rotate(-${{angle * i}}deg); width:100px;">${{item}}</div>`;
      wheel.appendChild(segment);
    }});
  }}

  createWheel(items);

  document.getElementById("spinBtn").onclick = () => {{
    const angle = 3600 + Math.floor(Math.random() * 360);
    wheel.style.transition = "transform 4s ease-out";
    wheel.style.transform = `rotate(${{angle}}deg)`;

    const selected = items[(items.length - Math.floor((angle % 360) / (360 / items.length))) % items.length];
    setTimeout(() => {{
      document.getElementById("

import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="생활 습관 체크", page_icon="👟")
st.title("👟 생활 습관 체크 앱 (내장 차트 사용)")

# 초기 데이터
if "habit_data" not in st.session_state:
    today = date.today()
    st.session_state.habit_data = pd.DataFrame({
        "날짜": [today - timedelta(days=i) for i in reversed(range(7))],
        "물(잔)": [0]*7,
        "운동": [0]*7,
        "수면(시간)": [0]*7
    })

# 오늘 기록
today_str = date.today().strftime("%Y-%m-%d")
st.subheader(f"📅 오늘 ({today_str}) 기록")

water = st.slider("💧 물 마신 양 (잔)", 0, 15, 0)
exercise = st.checkbox("🏃 운동했나요?")
sleep = st.slider("🛌 수면 시간 (시간)", 0, 12, 0)

if st.button("✅ 오늘 기록 저장"):
    idx = st.session_state.habit_data[st.session_state.habit_data["날짜"] == date.today()].index
    if not idx.empty:
        i = idx[0]
        st.session_state.habit_data.at[i, "물(잔)"] = water
        st.session_state.habit_data.at[i, "운동"] = int(exercise)
        st.session_state.habit_data.at[i, "수면(시간)"] = sleep
        st.success("오늘 기록이 저장되었습니다!")

# 📊 시각화
st.subheader("📊 최근 7일간 습관 리포트")

df = st.session_state.habit_data.copy()

# ✅ 날짜 열을 datetime 형식으로 변환한 후 MM/DD 표시
df["날짜"] = pd.to_datetime(df["날짜"])
df["날짜"] = df["날짜"].dt.strftime("%m/%d")

# 물 그래프
st.markdown("### 💧 물 마신 양")
st.line_chart(data=df.set_index("날짜")[["물(잔)"]])

# 운동 그래프
st.markdown("### 🏃 운동 여부")
st.bar_chart(data=df.set_index("날짜")[["운동"]])

# 수면 그래프
st.markdown("### 🛌 수면 시간")
st.line_chart(data=df.set_index("날짜")[["수면(시간)"]])

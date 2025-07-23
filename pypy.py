import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

st.set_page_config(page_title="생활 습관 체크", page_icon="👟")

st.title("👟 생활 습관 체크 앱")
st.markdown("매일 **물 섭취량 / 운동 여부 / 수면 시간**을 기록하고, 일주일 동안의 습관을 추적해보세요!")

# 초기 데이터 설정
if "habit_data" not in st.session_state:
    today = date.today()
    st.session_state.habit_data = pd.DataFrame({
        "날짜": [today - timedelta(days=i) for i in reversed(range(7))],
        "물(잔)": [0]*7,
        "운동": [False]*7,
        "수면(시간)": [0]*7
    })

# 오늘 날짜만 입력 받기
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
        st.session_state.habit_data.at[i, "운동"] = exercise
        st.session_state.habit_data.at[i, "수면(시간)"] = sleep
        st.success("오늘 기록이 저장되었습니다!")
    else:
        st.warning("오늘은 기록할 수 없습니다. 하루에 한 번만 저장 가능합니다.")

# 시각화
st.subheader("📊 최근 7일간 습관 리포트")

df = st.session_state.habit_data.copy()
df["운동"] = df["운동"].astype(int)

# 차트 그리기
fig1, ax1 = plt.subplots()
ax1.plot(df["날짜"], df["물(잔)"], marker="o", label="물(잔)")
ax1.set_ylabel("물(잔)")
ax1.set_title("💧 물 마신 양")

fig2, ax2 = plt.subplots()
ax2.bar(df["날짜"], df["운동"], label="운동 여부", color="orange")
ax2.set_ylabel("운동 (1=했음)")
ax2.set_title("🏃 운동 여부")

fig3, ax3 = plt.subplots()
ax3.plot(df["날짜"], df["수면(시간)"], marker="s", color="green", label="수면 시간")
ax3.set_ylabel("수면 시간 (시간)")
ax3.set_title("🛌 수면 시간")

st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)

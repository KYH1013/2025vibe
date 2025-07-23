import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="생활 습관 체크", page_icon="👟")
st.title("👟 생활 습관 체크 앱 (건강 점수 포함)")

# 초기 데이터 설정
if "habit_data" not in st.session_state:
    today = date.today()
    st.session_state.habit_data = pd.DataFrame({
        "날짜": [today - timedelta(days=i) for i in reversed(range(7))],
        "물(잔)": [0]*7,
        "운동": [0]*7,
        "수면(시간)": [0]*7
    })

today = date.today()
today_str = today.strftime("%Y-%m-%d")
st.subheader(f"📅 오늘 ({today_str}) 기록")

# 사용자 입력
water = st.slider("💧 물 마신 양 (잔)", 0, 15, 0)
exercise = st.checkbox("🏃 운동했나요?")
sleep = st.slider("🛌 수면 시간 (시간)", 0, 12, 0)

# 점수 계산 함수
def calculate_score(w, e, s):
    score = 0
    if w >= 6:
        score += 1
    if e:
        score += 1
    if 7 <= s <= 9:
        score += 1
    return score

today_score = calculate_score(water, exercise, sleep)

# 점수 기준 안내 및 오늘 점수 출력
st.markdown("### 🧮 오늘의 건강 점수 기준")
st.markdown("""
- 💧 물을 6잔 이상 마시면 **+1점**  
- 🏃 운동을 하면 **+1점**  
- 🛌 수면 시간이 7~9시간이면 **+1점**
""")
st.metric("🟢 오늘의 건강 점수 (0~3)", f"{today_score}/3")

# 점수에 따른 피드백
if today_score == 3:
    st.success("🎯 완벽한 하루! 건강 습관 만점입니다!")
elif today_score == 2:
    st.info("👍 잘하고 있어요! 물이나 수면을 조금 더 챙겨보면 좋겠어요.")
elif today_score == 1:
    st.warning("🙂 노력은 좋은 시작! 조금만 더 신경 써봐요.")
else:
    st.error("💡 오늘은 관리가 부족했어요. 내일부터 다시 시작해봐요!")

# 기록 저장
if st.button("✅ 오늘 기록 저장"):
    idx = st.session_state.habit_data[st.session_state.habit_data["날짜"] == today].index
    if not idx.empty:
        i = idx[0]
        st.session_state.habit_data.at[i, "물(잔)"] = water
        st.session_state.habit_data.at[i, "운동"] = int(exercise)
        st.session_state.habit_data.at[i, "수면(시간)"] = sleep
        st.success("오늘 기록이 저장되었습니다!")

# 리포트
st.subheader("📊 최근 7일간 습관 리포트")

df = st.session_state.habit_data.copy()
df["날짜"] = pd.to_datetime(df["날짜"])
df["날짜"] = df["날짜"].dt.strftime("%m/%d")

# 그래프를 작게 표시
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 💧 물 마신 양")
    st.line_chart(df.set_index("날짜")[["물(잔)"]], use_container_width=False)

with col2:
    st.markdown("#### 🏃 운동 여부")
    st.bar_chart(df.set_index("날짜")[["운동"]], use_container_width=False)

st.markdown("#### 🛌 수면 시간")
st.line_chart(df.set_index("날짜")[["수면(시간)"]], use_container_width=False)

# 주간 리포트
st.subheader("🧾 건강 리포트 요약 (최근 7일 기준)")

# 주간 점수 계산
def row_score(row):
    score = 0
    if row["물(잔)"] >= 6:
        score += 1
    if row["운동"] == 1:
        score += 1
    if 7 <= row["수면(시간)"] <= 9:
        score += 1
    return score

df["점수"] = df.apply(row_score, axis=1)
avg_score = df["점수"].mean()

# 주간 피드백
if avg_score >= 2.5:
    msg = "🎉 완벽한 건강 습관! 지금처럼만 유지해보세요!"
elif avg_score >= 1.5:
    msg = "🙂 좋은 흐름이에요! 물 섭취나 수면을 조금 더 챙겨보면 더 좋아요."
else:
    msg = "💡 최근 관리를 놓치셨나요? 오늘부터 다시 작게 시작해보세요!"

st.metric("최근 7일 평균 건강 점수 (0~3)", f"{avg_score:.2f}")
st.info(msg)

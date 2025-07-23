import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="습관 트래커", page_icon="👟")
st.title("👟 생활 습관 체크 앱")

# 초기 데이터 프레임
if "habit_data" not in st.session_state:
    st.session_state.habit_data = pd.DataFrame(columns=["날짜", "물(잔)", "운동", "수면(시간)", "점수"])

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

# 입력 섹션
st.subheader("📅 날짜와 건강 습관 입력")

input_date = st.date_input("기록할 날짜", value=date.today())
water = st.slider("💧 물 마신 양 (잔)", 0, 15, 0)
exercise = st.checkbox("🏃 운동했나요?", value=False)
sleep = st.slider("🛌 수면 시간 (시간)", 0, 12, 0)

# 점수 계산 및 출력
score = calculate_score(water, exercise, sleep)
st.metric("📊 입력일 건강 점수", f"{score}/3")

# 점수 기준
st.markdown("### 🧮 건강 점수 기준")
st.markdown("""
- 💧 물 6잔 이상 → +1점  
- 🏃 운동 했음 → +1점  
- 🛌 수면 7~9시간 → +1점
""")

# 피드백 메시지
if score == 3:
    st.success("🎯 완벽한 하루! 건강 습관 만점입니다!")
elif score == 2:
    st.info("👍 잘하고 있어요! 부족한 부분을 조금 더 챙겨보면 좋겠어요.")
elif score == 1:
    st.warning("🙂 노력은 좋은 시작! 조금만 더 신경 써봐요.")
else:
    st.error("💡 오늘은 관리가 부족했어요. 내일부터 다시 시작해봐요!")

# 저장 버튼
if st.button("✅ 기록 저장"):
    new_entry = {
        "날짜": input_date,
        "물(잔)": water,
        "운동": int(exercise),
        "수면(시간)": sleep,
        "점수": score
    }
    st.session_state.habit_data = pd.concat([
        st.session_state.habit_data[st.session_state.habit_data["날짜"] != input_date],
        pd.DataFrame([new_entry])
    ], ignore_index=True)
    st.success(f"{input_date.strftime('%Y-%m-%d')} 기록이 저장되었습니다!")

# 기록 요약 테이블
st.subheader("📋 기록 요약")
if not st.session_state.habit_data.empty:
    df = st.session_state.habit_data.copy()
    df["날짜"] = pd.to_datetime(df["날짜"]).dt.strftime("%m/%d")

    # 점수 컬럼 없을 경우 계산해서 추가
    if "점수" not in df.columns:
        df["점수"] = df.apply(
            lambda row: calculate_score(row["물(잔)"], row["운동"], row["수면(시간)"]),
            axis=1
        )

    st.dataframe(df.set_index("날짜"))
    avg_score = df["점수"].mean()
    st.metric("📈 평균 건강 점수", f"{avg_score:.2f}")
else:
    st.info("아직 기록이 없습니다. 날짜를 선택하고 기록을 시작해보세요.")

    # 평균 점수 피드백
    st.markdown("### 💬 건강 피드백")
    if avg_score >= 2.5:
        st.success("🎉 훌륭해요! 건강 습관이 아주 잘 유지되고 있어요.")
    elif avg_score >= 1.5:
        st.info("🙂 괜찮은 흐름이에요. 물/수면/운동 중 한 가지만 더 챙겨봐요.")
    else:
        st.warning("⚠️ 습관 관리가 조금 부족해요. 지금부터 하나씩 다시 시작해보세요!")


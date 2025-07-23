import streamlit as st

st.set_page_config(page_title="이거 살까 말까 도우미", page_icon="🛍️")
st.title("🛍️ 이거 살까 말까? 소비 결정 도우미 (GPT 없음 버전)")

# 입력
st.subheader("1️⃣ 사고 싶은 물건이나 서비스를 입력하세요")
item = st.text_input("예: 갤럭시 워치7, 명상 앱 1년 구독")

st.subheader("2️⃣ 구매하려는 이유는 무엇인가요?")
reason = st.text_area("예: 운동할 때 쓰려고요. 집중에 도움이 될 것 같아요.")

st.subheader("3️⃣ 지금 가진 비슷한 물건이 있나요?")
has_similar = st.radio("예 / 아니요", ["예", "아니요"], horizontal=True)

st.subheader("4️⃣ 얼마나 자주 사용할 것 같나요?")
frequency = st.selectbox("예상 사용 빈도", ["거의 안 쓸 듯", "가끔", "자주", "매일"])

st.subheader("5️⃣ 가격에 대해 어떻게 느끼나요?")
cost_feeling = st.radio("부담됨 / 괜찮음", ["부담됨", "괜찮음"], horizontal=True)

st.subheader("6️⃣ 지금 감정 상태는 어떤가요?")
emotion = st.selectbox("지금 기분", ["기분 좋음", "지침", "우울함", "충동적인 느낌", "평온함"])

if st.button("🤔 판단 결과 보기"):
    st.markdown("### 🧠 소비 판단 리포트")

    # 간단한 규칙 기반 판단
    flags = []

    if has_similar == "예":
        flags.append("- 이미 비슷한 물건이 있어요.")
    if frequency in ["거의 안 쓸 듯", "가끔"]:
        flags.append("- 자주 쓰지 않을 가능성이 있어요.")
    if cost_feeling == "부담됨":
        flags.append("- 가격이 부담된다고 느끼고 있어요.")
    if emotion in ["우울함", "충동적인 느낌"]:
        flags.append("- 지금 감정 상태가 구매에 영향을 줄 수 있어요.")

    if flags:
        st.write("다음과 같은 점을 고려해보세요:")
        for f in flags:
            st.write(f)

        st.warning("💡 잠깐 기다려보고 다시 생각해보는 것도 좋을 것 같아요!")
    else:
        st.success("🎉 괜찮은 소비일 가능성이 높아요! 가치 있는 소비가 되길 바랍니다.")

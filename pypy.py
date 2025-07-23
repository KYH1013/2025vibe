import streamlit as st
import openai

# 🔑 OpenAI API 키 설정
openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

st.set_page_config(page_title="이거 살까 말까 도우미", page_icon="🛍️")
st.title("🛍️ 이거 살까 말까? 소비 결정 도우미")

# 입력 받기
st.subheader("1️⃣ 사고 싶은 물건이나 서비스를 알려주세요")
item = st.text_input("예: 갤럭시 워치7, 명상 앱 1년 구독")

st.subheader("2️⃣ 구매 배경/상황을 알려주세요 (선택)")
context = st.text_area("예: 운동 시작하려고요. 현재 스마트워치는 없습니다.")

if st.button("🤔 살까 말까 판단 도와줘"):
    if not item:
        st.warning("물건 또는 서비스명을 입력해주세요!")
    else:
        with st.spinner("AI가 당신의 소비를 도와주는 중..."):
            # GPT 프롬프트 구성
            prompt = f"""
너는 소비 결정을 도와주는 조언자야. 사용자가 어떤 물건을 사고 싶어할 때,
충동구매를 줄이고 가치소비를 할 수 있도록 현실적이고 따뜻한 질문을 해줘.
마지막엔 구매 여부에 대한 판단을 내려주되, 사용자가 스스로 결정할 수 있도록 유도해.

[사고 싶은 항목]
{item}

[배경/상황]
{context if context else "없음"}

1. 사고 싶은 이유를 물어봐줘.
2. 비슷한 걸 이미 갖고 있는지 확인해줘.
3. 그 물건이 얼마나 자주 쓰일지 물어봐.
4. 기분에 따른 충동인지도 고려해줘.
5. 3일 뒤에도 여전히 원할지 스스로 생각하게 해줘.
6. 마지막으로 구매해도 괜찮을지 한 문장으로 조언해줘.
            """

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "당신은 절제 있고 따뜻한 소비 조언자입니다."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.markdown("### 🧠 소비 판단 리포트")
                st.write(answer)
            except Exception as e:
                st.error("GPT 응답 중 문제가 발생했습니다. API 키 또는 연결 상태를 확인하세요.")


import streamlit as st
import openai

st.set_page_config(page_title="이거 살까 말까? GPT 소비 도우미", page_icon="🛍️")
st.title("🛍️ 이거 살까 말까? GPT 소비 결정 도우미")

# 사용자에게 OpenAI API 키 입력 받기
api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# 사용자 입력
item = st.text_input("1️⃣ 사고 싶은 물건이나 서비스", placeholder="예: 갤럭시 워치7")
context = st.text_area("2️⃣ 구매하려는 이유나 상황", placeholder="선택 사항입니다.")

if st.button("🤔 GPT에게 조언받기"):
    if not api_key:
        st.warning("OpenAI API 키를 입력해주세요.")
    elif not item:
        st.warning("사고 싶은 항목을 입력해주세요.")
    else:
        with st.spinner("GPT가 고민을 정리 중입니다..."):
            try:
                openai.api_key = api_key

                prompt = f"""
너는 소비 결정을 도와주는 조언자야. 사용자가 사고 싶은 물건이나 서비스에 대해,
충동구매가 아닌 가치 소비를 할 수 있도록 도와줘. 현실적이고 따뜻한 질문을 해줘.
마지막엔 신중한 한 문장 조언을 해줘.

[사고 항목] {item}
[배경 설명] {context if context else '없음'}

1. 왜 사고 싶은지 질문해줘.
2. 비슷한 걸 이미 갖고 있는지 물어봐.
3. 얼마나 자주 쓸지, 얼마나 필요한지 점검해줘.
4. 감정 상태에 따른 충동 소비 가능성도 물어봐.
5. 스스로 판단을 내릴 수 있도록 유도하는 조언으로 마무리해줘.
                """

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "당신은 친절하고 절제 있는 소비 도우미입니다."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

                result = response.choices[0].message.content
                st.markdown("### 💬 GPT의 소비 판단 조언")
                st.write(result)

            except Exception as e:
                st.error("❌ GPT 응답 중 문제가 발생했어요. API 키가 잘못되었거나 연결이 안 된 것 같아요.")

commit

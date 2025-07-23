import streamlit as st
import random
import time

st.set_page_config(page_title="점심 메뉴 룰렛", page_icon="🍱")
st.title("🎯 점심메뉴 룰렛 추천기")

# 메뉴-이미지 매핑
menu_images = {
    "김치찌개": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Kimchi_Jjigae.jpg/640px-Kimchi_Jjigae.jpg",
    "된장찌개": "https://www.maangchi.com/wp-content/uploads/2007/06/Doenjangjjigae.jpg",
    "제육볶음": "https://recipe1.ezmember.co.kr/cache/recipe/2018/10/27/171b38de9d0785cb8028e7c530fbec6d1.jpg",
    "돈까스": "https://cdn.imweb.me/upload/S202107069cd4df60a8ef0/225f01e5d42a5.png",
    "비빔밥": "https://www.maangchi.com/wp-content/uploads/2008/02/bibimbap.jpg",
    "라멘": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tonkotsu_ramen_by_ayustety_in_Tokyo.jpg/640px-Tonkotsu_ramen_by_ayustety_in_Tokyo.jpg",
    "우동": "https://recipe1.ezmember.co.kr/cache/recipe/2015/06/30/1b258b8997aa54cb504bcd7614a5bc4f1.jpg",
    "햄버거": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Various_hamburgers.jpg",
    "샐러드": "https://www.simplyrecipes.com/thmb/jckKJ8zQGQbW6dYvwL6mXxQvWco=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Greek-Salad-LEAD-1-96e3e1dc19e84e579a3d0903f8789e44.jpg",
    "초밥": "https://upload.wikimedia.org/wikipedia/commons/6/60/Sushi_platter.jpg",
    "파스타": "https://upload.wikimedia.org/wikipedia/commons/0/09/Spaghetti_al_Pomodoro.JPG",
    "피자": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Supreme_pizza.jpg",
    "쌀국수": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Pho-Beef-Noodles-2008.jpg"
}

menus = list(menu_images.keys())

if st.button("🎲 메뉴 돌리기"):
    with st.spinner("룰렛 돌리는 중..."):
        for _ in range(15):
            choice = random.choice(menus)
            st.markdown(f"<h3 style='text-align:center'>🍽️ {choice}</h3>", unsafe_allow_html=True)
            time.sleep(0.1)

        # 최종 선택
        final_choice = random.choice(menus)
        st.success(f"✅ 오늘의 점심은 **{final_choice}** 어떠세요? 😋")
        st.image(menu_images[final_choice], caption=final_choice, use_column_width=True)

# 전체 메뉴
with st.expander("📋 전체 메뉴 보기"):
    st.write(", ".join(menus))

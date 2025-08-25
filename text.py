import streamlit as st
import pandas as pd

# 미래 식량 후보 데이터 (예시)
food_data = pd.DataFrame([
    {"name": "곤충 단백질", "taste": "고소함", "texture": "바삭함", "nutrition": "단백질 풍부", "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Edible_insects.jpg"},
    {"name": "해조류", "taste": "짭짤함", "texture": "쫄깃함", "nutrition": "미네랄 풍부", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Seaweed_on_shore.jpg"},
    {"name": "인공육", "taste": "고기맛", "texture": "부드러움", "nutrition": "단백질 풍부", "image": "https://upload.wikimedia.org/wikipedia/commons/3/35/Lab-grown_meat.jpg"},
    {"name": "배양육", "taste": "고기맛", "texture": "쫄깃함", "nutrition": "단백질 풍부", "image": "https://upload.wikimedia.org/wikipedia/commons/2/23/Cultured_meat.jpg"},
    {"name": "곡물 기반 식품", "taste": "담백함", "texture": "부드러움", "nutrition": "탄수화물 풍부", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Grain_on_plate.jpg"},
])

st.title("나만의 미래 식량 찾기 🥗🤖")

st.write("아래 질문에 답하면 AI가 당신의 입맛에 맞는 미래 식량을 추천해줍니다!")

# 질문
taste_pref = st.selectbox("좋아하는 맛을 선택하세요:", ["고소함", "짭짤함", "고기맛", "담백함"])
texture_pref = st.selectbox("좋아하는 식감은?", ["바삭함", "쫄깃함", "부드러움"])
nutrition_pref = st.multiselect("중요하게 생각하는 영양소는?", ["단백질 풍부", "미네랄 풍부", "탄수화물 풍부"])

# 추천 점수 계산
def recommend_food(taste, texture, nutrition_list):
    scores = []
    for _, row in food_data.iterrows():
        score = 0
        if row["taste"] == taste:
            score += 1
        if row["texture"] == texture:
            score += 1
        for n in nutrition_list:
            if row["nutrition"] == n:
                score += 1
        scores.append(score)
    food_data["score"] = scores
    return food_data.sort_values(by="score", ascending=False).head(3)

if st.button("추천 받기"):
    recommendations = recommend_food(taste_pref, texture_pref, nutrition_pref)
    st.subheader("🍽 추천 미래 식량 Top 3")
    for _, food in recommendations.iterrows():
        st.markdown(f"**{food['name']}**")
        st.image(food['image'], use_container_width=True)
        st.write(f"맛: {food['taste']} | 식감: {food['texture']} | 특징: {food['nutrition']}")

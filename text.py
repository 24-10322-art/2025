import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌱 OX 퀴즈로 찾는 나만의 미래 식량 (확장판)")

st.write("각 질문에 O(맞다)/X(틀리다)로 답하면 AI가 당신에게 가장 잘 맞는 미래 식량을 추천합니다!")

# OX 퀴즈 질문 10개
quiz_questions = {
    "고소한 맛을 좋아한다": "taste_high",
    "짭짤한 맛을 좋아한다": "taste_salty",
    "단맛을 좋아한다": "taste_sweet",
    "쫄깃한 식감을 좋아한다": "texture_chewy",
    "부드러운 식감을 좋아한다": "texture_soft",
    "단백질이 풍부한 식품을 선호한다": "nutrition_protein",
    "저칼로리 식품을 좋아한다": "nutrition_lowcal",
    "가공식품 형태를 선호한다": "form_processed",
    "자연 상태 그대로 식품을 좋아한다": "form_natural",
    "음료/액체 형태를 선호한다": "form_liquid"
}

# 사용자 OX 선택
user_answers = {}
for q in quiz_questions:
    user_answers[quiz_questions[q]] = st.radio(q, ["O", "X"], horizontal=True)

# 미래 식량 후보 데이터
food_data = pd.DataFrame([
    {"name": "귀뚜라미 단백질", "taste_high": True, "taste_salty": False, "taste_sweet": False, 
     "texture_chewy": False, "texture_soft": False, "nutrition_protein": True, "nutrition_lowcal": False,
     "form_processed": True, "form_natural": False, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Edible_insects.jpg"},
    
    {"name": "해조류(김, 다시마 등)", "taste_high": False, "taste_salty": True, "taste_sweet": False,
     "texture_chewy": True, "texture_soft": False, "nutrition_protein": False, "nutrition_lowcal": True,
     "form_processed": False, "form_natural": True, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Seaweed_on_shore.jpg"},
    
    {"name": "배양육", "taste_high": False, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": False, "texture_soft": True, "nutrition_protein": True, "nutrition_lowcal": False,
     "form_processed": True, "form_natural": False, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/2/23/Cultured_meat.jpg"},
    
    {"name": "곤약 기반 대체 식품", "taste_high": False, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": True, "texture_soft": False, "nutrition_protein": False, "nutrition_lowcal": True,
     "form_processed": True, "form_natural": False, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Konjac_jelly.jpg"},
    
    {"name": "곡물 기반 미래 식품", "taste_high": False, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": False, "texture_soft": True, "nutrition_protein": False, "nutrition_lowcal": False,
     "form_processed": False, "form_natural": True, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Grain_on_plate.jpg"},
    
    {"name": "곤충 단백질 바", "taste_high": True, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": False, "texture_soft": True, "nutrition_protein": True, "nutrition_lowcal": False,
     "form_processed": True, "form_natural": False, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/1/19/Cricket_energy_bar.jpg"},
    
    {"name": "미래 식용 버섯", "taste_high": False, "taste_salty": True, "taste_sweet": False,
     "texture_chewy": True, "texture_soft": False, "nutrition_protein": True, "nutrition_lowcal": False,
     "form_processed": False, "form_natural": True, "form_liquid": False,
     "image": "https://upload.wikimedia.org/wikipedia/commons/1/11/Mushrooms.jpg"},
])

# 추천 점수 계산
def recommend_food():
    scores = []
    for _, row in food_data.iterrows():
        score = 0
        for key, answer in user_answers.items():
            if (answer == "O" and row[key]) or (answer == "X" and not row[key]):
                score += 1
        scores.append(score)
    food_data["score"] = scores
    top_food = food_data.sort_values(by="score", ascending=False).iloc[0]
    return top_food

# 추천 결과 표시
if st.button("추천 받기"):
    top_food = recommend_food()
    
    # 카드형 UI
    st.markdown("### 🌟 당신에게 가장 잘 맞는 미래 식량 🌟")
    st.image(top_food['image'], use_container_width=True)
    st.markdown(f"### {top_food['name']}")
    st.markdown("**특징:**")
    for key, val in top_food.items():
        if val and key not in ["name", "image", "score"]:
            # 질문 텍스트로 매핑
            question_text = [q for q, k in quiz_questions.items() if k == key][0]
            st.markdown(f"- {question_text}")

    # 점수 시각화 (OX 적합도)
    st.markdown("### 점수 시각화")
    fig, ax = plt.subplots()
    ax.barh([top_food['name']], [top_food['score']], color='green')
    ax.set_xlim(0, len(quiz_questions))
    ax.set_xlabel("OX 적합 점수")
    st.pyplot(fig)

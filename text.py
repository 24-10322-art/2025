import streamlit as st
import pandas as pd

st.title("🌱 OX 퀴즈로 찾는 나만의 미래 식량")
st.write("각 질문에 O(맞다)/X(틀리다)로 답하면 AI가 당신에게 맞는 미래 식량을 추천합니다!")

# 세션 상태 초기화
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# OX 퀴즈 질문
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

# 사용자 OX 선택 저장
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {k: "X" for k in quiz_questions.values()}

# 설문 화면
if not st.session_state.show_result:
    for q in quiz_questions:
        st.session_state.user_answers[quiz_questions[q]] = st.radio(q, ["O", "X"], horizontal=True, key=q)

    if st.button("추천 받기"):
        st.session_state.show_result = True

# 미래 식량 후보 데이터 (로컬 이미지 사용)
food_data = pd.DataFrame([
    {"name": "배양육", "taste_high": False, "taste_salty": False, "taste_sweet": False, 
     "texture_chewy": False, "texture_soft": True, "nutrition_protein": True, "nutrition_lowcal": False,
     "form_processed": True, "form_natural": False, "form_liquid": False,
    },
    
    {"name": "귀뚜라미바", "taste_high": True, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": False, "texture_soft": True, "nutrition_protein": True, "nutrition_lowcal": True,
     "form_processed": True, "form_natural": False, "form_liquid": False,
    },
    
    {"name": "아마란스", "taste_high": False, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": False, "texture_soft": True, "nutrition_protein": False, "nutrition_lowcal": False,
     "form_processed": False, "form_natural": True, "form_liquid": False,
     },
    
    {"name": "굼벵이 호두파이", "taste_high": True, "taste_salty": False, "taste_sweet": True,
     "texture_chewy": True, "texture_soft": True, "nutrition_protein": True, "nutrition_lowcal": False,
     "form_processed": True, "form_natural": False, "form_liquid": False,
    },
    
    {"name": "스피루리나", "taste_high": False, "taste_salty": False, "taste_sweet": False,
     "texture_chewy": False, "texture_soft": False, "nutrition_protein": True, "nutrition_lowcal": True,
     "form_processed": True, "form_natural": True, "form_liquid": True,
     },
])

# 추천 점수 계산
def recommend_food(user_answers):
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

# 결과 화면
if st.session_state.show_result:
    top_food = recommend_food(st.session_state.user_answers)
    st.subheader("🌟 당신에게 가장 잘 맞는 미래 식량 🌟")
    st.image(f"./{top_food['image']}", use_container_width=True)
    st.markdown(f"### {top_food['name']}")
    st.markdown("**특징:**")
    for key, val in top_food.items():
        if val and key not in ["name", "image", "score"]:
            question_text = [q for q, k in quiz_questions.items() if k == key][0]
            st.markdown(f"- {question_text}")
    
    if st.button("다시 퀴즈 풀기"):
        st.session_state.show_result = False

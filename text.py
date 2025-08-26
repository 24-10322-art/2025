import streamlit as st
import pandas as pd

st.title("🌱 선호도 퀴즈로 찾는 나만의 미래 식량")
st.write("각 질문에 대해 얼마나 해당되는지 선택하면 AI가 당신에게 맞는 미래 식량을 추천합니다!")

# 세션 상태 초기화
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# 선호도 퀴즈 질문
quiz_questions = {
    "1. 고기 맛이 나는 단백질 식품을 좋아한다": "pref_meat_like",
    "2. 달콤한 간식/디저트 종류를 선호한다": "pref_dessert",
    "3. 곡물이나 씨앗류처럼 알갱이 형태의 식감을 좋아한다": "texture_grainy",
    "4. 바삭하거나 씹는 맛이 있는 식감을 선호한다": "texture_crunchy",
    "5. 곤충을 재료로 한 식품에 대한 거부감이 없다": "pref_insect",
    "6. 건강 보조식품처럼 간편하게 섭취하는 것을 좋아한다": "pref_supplement_form",
    "7. 물에 타 먹거나 음료 형태로 마시는 것이 편하다": "form_liquid",
    "8. 자연에서 온 원물 그대로의 식품을 선호한다": "form_natural",
    "9. 새로운 재료나 식감에 도전하는 것을 즐긴다": "pref_novelty",
    "10. 비교적 칼로리가 낮고 가벼운 식품을 찾는다": "nutrition_lowcal"
}

# 설문 화면
if not st.session_state.show_result:
    for q_text, q_key in quiz_questions.items():
        if q_key not in st.session_state.user_answers:
            st.session_state.user_answers[q_key] = 3  # 초기값: 중립
        
        st.session_state.user_answers[q_key] = st.slider(
            q_text, 1, 5, st.session_state.user_answers[q_key],
            format="%d (1=전혀 아니다, 5=매우 그렇다)"
        )
        
    if st.button("추천 받기"):
        st.session_state.show_result = True
        st.rerun()

# 미래 식량 후보 데이터
food_data = pd.DataFrame([
    {"name": "배양육",
     "pref_meat_like": 5, "pref_dessert": 1, "texture_grainy": 1, "texture_crunchy": 1, "pref_insect": 1,
     "pref_supplement_form": 1, "form_liquid": 1, "form_natural": 1, "pref_novelty": 5, "nutrition_lowcal": 2,
     "appearance_description": "인공적으로 배양된 고기로, 실제 고기와 흡사한 외형을 가지고 있습니다."},
    
    {"name": "귀뚜라미바",
     "pref_meat_like": 1, "pref_dessert": 4, "texture_grainy": 2, "texture_crunchy": 5, "pref_insect": 5,
     "pref_supplement_form": 4, "form_liquid": 1, "form_natural": 2, "pref_novelty": 4, "nutrition_lowcal": 4,
     "appearance_description": "에너지바 형태로 갈색이며, 곤충 분말이 포함되어 있습니다."},
    
    {"name": "아마란스",
     "pref_meat_like": 1, "pref_dessert": 2, "texture_grainy": 5, "texture_crunchy": 2, "pref_insect": 1,
     "pref_supplement_form": 1, "form_liquid": 1, "form_natural": 5, "pref_novelty": 2, "nutrition_lowcal": 2,
     "appearance_description": "작은 알갱이 곡물 형태로 노란색 또는 붉은색을 띱니다."},
    
    {"name": "굼벵이 호두파이",
     "pref_meat_like": 1, "pref_dessert": 5, "texture_grainy": 2, "texture_crunchy": 2, "pref_insect": 5,
     "pref_supplement_form": 2, "form_liquid": 1, "form_natural": 1, "pref_novelty": 4, "nutrition_lowcal": 2,
     "appearance_description": "일반 호두파이와 유사하지만 곤충 가루가 포함된 디저트입니다."},
    
    {"name": "스피루리나",
     "pref_meat_like": 1, "pref_dessert": 1, "texture_grainy": 2, "texture_crunchy": 1, "pref_insect": 1,
     "pref_supplement_form": 5, "form_liquid": 5, "form_natural": 5, "pref_novelty": 3, "nutrition_lowcal": 5,
     "appearance_description": "짙은 초록색 미세 조류로 분말이나 정제 형태로 섭취합니다."},
])

# 추천 점수 계산 함수 (유사도 기반)
def recommend_food(user_answers):
    scores = []
    for index, row in food_data.iterrows():
        score = 0
        for key, answer in user_answers.items():
            score += 5 - abs(answer - row[key])  # 가까울수록 높은 점수
        scores.append(score)
    
    food_data_with_scores = food_data.copy()
    food_data_with_scores["score"] = scores
    top_food = food_data_with_scores.sort_values(by="score", ascending=False).iloc[0]
    return top_food

# 결과 화면
if st.session_state.show_result:
    top_food = recommend_food(st.session_state.user_answers)
    
    st.subheader("🌟 당신에게 가장 잘 맞는 미래 식량 🌟")
    st.write(f"**{top_food['name']}**")
    st.markdown(f"**생김새 묘사:** *{top_food['appearance_description']}*")
    
    st.markdown("---")
    st.markdown("**당신의 선택과 가까운 특징:**")
    for key, answer in st.session_state.user_answers.items():
        if abs(answer - top_food[key]) <= 1:  # 유사성이 높은 특징만 표시
            st.markdown(f"- {quiz_questions.get(key, key)} (당신의 선택: {answer}/5)")
    
    st.markdown("---")
    
    if st.button("다시 퀴즈 풀기"):
        st.session_state.show_result = False
        st.session_state.user_answers = {k: 3 for k in quiz_questions.values()}
        st.rerun()

import streamlit as st
import pandas as pd

st.title("🌱 OX 퀴즈로 찾는 나만의 미래 식량")
st.write("각 질문에 O(맞다)/X(틀리다)로 답하면 AI가 당신에게 맞는 미래 식량을 추천합니다!")

# 세션 상태 초기화
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# OX 퀴즈 질문 10개 (미래 식량의 특징을 더 잘 반영하도록 변경!)
quiz_questions = {
    "1. 고기 맛이 나는 단백질 식품을 좋아한다": "pref_meat_like", # 배양육
    "2. 달콤한 간식/디저트 종류를 선호한다": "pref_dessert", # 귀뚜라미바, 굼벵이 호두파이
    "3. 곡물이나 씨앗류처럼 알갱이 형태의 식감을 좋아한다": "texture_grainy", # 아마란스
    "4. 바삭하거나 씹는 맛이 있는 식감을 선호한다": "texture_crunchy", # 귀뚜라미바 (이전보다 강조)
    "5. 곤충을 재료로 한 식품에 대한 거부감이 없다": "pref_insect", # 귀뚜라미바, 굼벵이 호두파이 (핵심 구분점!)
    "6. 건강 보조식품처럼 간편하게 섭취하는 것을 좋아한다": "pref_supplement_form", # 스피루리나, 귀뚜라미바
    "7. 물에 타 먹거나 음료 형태로 마시는 것이 편하다": "form_liquid", # 스피루리나
    "8. 자연에서 온 원물 그대로의 식품을 선호한다": "form_natural", # 아마란스, 스피루리나
    "9. 새로운 재료나 식감에 도전하는 것을 즐긴다": "pref_novelty", # 배양육, 곤충 식품 전반
    "10. 비교적 칼로리가 낮고 가벼운 식품을 찾는다": "nutrition_lowcal" # 귀뚜라미바, 스피루리나
}

# 설문 화면
if not st.session_state.show_result:
    # 퀴즈 질문 표시 및 답변 받기
    for q_text, q_key in quiz_questions.items():
        # Session State에 답변이 없으면 "X"로 초기값 설정 (새로운 퀴즈 시작 시)
        if q_key not in st.session_state.user_answers:
            st.session_state.user_answers[q_key] = "X"
        
        st.session_state.user_answers[q_key] = st.radio(q_text, ["O", "X"], horizontal=True, key=q_key)
        
    if st.button("추천 받기"):
        st.session_state.show_result = True
        st.rerun() # 결과 화면으로 바로 전환을 위해 rerun

# 미래 식량 후보 데이터 (변경된 질문에 맞춰 특성 재조정)
food_data = pd.DataFrame([
    {"name": "배양육",
     "pref_meat_like": True, "pref_dessert": False, "texture_grainy": False, "texture_crunchy": False, "pref_insect": False, 
     "pref_supplement_form": False, "form_liquid": False, "form_natural": False, "pref_novelty": True, "nutrition_lowcal": False,
     "appearance_description": "인공적으로 배양된 고기로, 일반 육류와 유사한 붉은색 또는 옅은 분홍색을 띠며, 다진 고기나 스테이크 형태로 가공될 수 있습니다. 실제 고기와 흡사한 마블링이나 근섬유를 구현하기도 합니다."},
    
    {"name": "귀뚜라미바",
     "pref_meat_like": False, "pref_dessert": True, "texture_grainy": False, "texture_crunchy": True, "pref_insect": True, # 바삭한 식감
     "pref_supplement_form": True, "form_liquid": False, "form_natural": False, "pref_novelty": True, "nutrition_lowcal": True,
     "appearance_description": "곡물 에너지바와 유사한 형태로, 주로 갈색을 띠고 있으며 귀뚜라미 가루가 포함되어 있어 미세한 점박이가 보이거나 부드러운 질감을 가집니다. 간혹 귀뚜라미 형태가 살짝 드러나기도 합니다."},
    
    {"name": "아마란스",
     "pref_meat_like": False, "pref_dessert": False, "texture_grainy": True, "texture_crunchy": False, "pref_insect": False,
     "pref_supplement_form": False, "form_liquid": False, "form_natural": True, "pref_novelty": False, "nutrition_lowcal": False,
     "appearance_description": "매우 작은 알갱이 형태로, 색상은 옅은 노란색, 갈색, 붉은색 등 다양합니다. 조리 시 퀴노아처럼 알갱이가 톡톡 터지는 식감을 가지며, 밥이나 샐러드에 섞어 먹기 좋습니다."},
    
    {"name": "굼벵이 호두파이",
     "pref_meat_like": False, "pref_dessert": True, "texture_grainy": False, "texture_crunchy": False, "pref_insect": True, # 굼벵이
     "pref_supplement_form": False, "form_liquid": False, "form_natural": False, "pref_novelty": True, "nutrition_lowcal": False,
     "appearance_description": "일반 호두파이와 외형은 유사하나, 굼벵이가 재료로 사용되어 파이 내부에 흰색 또는 미색의 굼벵이 가루가 섞여 있거나, 부드럽게 갈린 형태로 들어가 있어 육안으로는 일반 호두파이와 크게 다르지 않아 보일 수 있습니다."},
    
    {"name": "스피루리나",
     "pref_meat_like": False, "pref_dessert": False, "texture_grainy": False, "texture_crunchy": False, "pref_insect": False,
     "pref_supplement_form": True, "form_liquid": True, "form_natural": True, "pref_novelty": False, "nutrition_lowcal": True,
     "appearance_description": "짙은 초록색 또는 푸른색을 띠는 미세 조류로, 주로 건조된 분말 형태로 유통됩니다. 물에 타거나 다른 식품에 섞으면 녹색으로 변하며, 미세한 입자감과 특유의 해조류 향이 있습니다. 정제 형태로도 섭취 가능합니다."},
])

# 추천 점수 계산 함수
def recommend_food(user_answers):
    scores = []
    for index, row in food_data.iterrows():
        score = 0
        for key, answer in user_answers.items():
            if (answer == "O" and row[key]) or (answer == "X" and not row[key]):
                score += 1
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
    
    st.markdown("---") # 구분선 추가
    st.markdown("**이유 (당신의 선택과 일치하는 특징):**")
    matched_features = []
    # quiz_questions 딕셔너리에서 key 값을 찾기 위한 역방향 맵 생성 (성능 향상)
    question_key_to_text = {v: k for k, v in quiz_questions.items()}

    for key, answer in st.session_state.user_answers.items():
        if (answer == "O" and top_food[key]) or (answer == "X" and not top_food[key]):
            # 퀴즈 질문 원문이 있으면 추가 (예: '1. 고기 맛이 나는 단백질 식품을 좋아한다')
            if key in question_key_to_text:
                matched_features.append(f"- {question_key_to_text[key]}")
    
    if matched_features:
        for feature in matched_features:
            st.markdown(feature)
    else:
        st.markdown("- 당신의 답변과 잘 맞는 특징을 찾지 못했습니다. 😢") # 매칭되는 특징이 없을 경우

    st.markdown("---")
    
    if st.button("다시 퀴즈 풀기"):
        st.session_state.show_result = False
        st.session_state.user_answers = {k: "X" for k in quiz_questions.values()} # 답변 초기화
        st.rerun() # 설문 화면으로 전환을 위해 rerun

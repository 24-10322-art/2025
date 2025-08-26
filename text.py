import streamlit as st
import pandas as pd

st.title("🌱 OX 퀴즈로 찾는 나만의 미래 식량")
st.write("각 질문에 O(맞다)/X(틀리다)로 답하면 AI가 당신에게 맞는 미래 식량을 추천합니다!")

# 세션 상태 초기화
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# OX 퀴즈 질문
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
            st.session_state.user_answers[q_key] = "X"
        
        st.session_state.user_answers[q_key] = st.radio(
            q_text, ["O", "X"], horizontal=True, key=q_key
        )
        
    if st.button("추천 받기"):
        st.session_state.show_result = True
        st.rerun()

# 미래 식량 후보 데이터 (extra_description 추가)
food_data = pd.DataFrame([
    {"name": "배양육",
     "pref_meat_like": True, "pref_dessert": False, "texture_grainy": False, "texture_crunchy": False, "pref_insect": False, 
     "pref_supplement_form": False, "form_liquid": False, "form_natural": False, "pref_novelty": True, "nutrition_lowcal": False,
     "appearance_description": "인공적으로 배양된 고기로, 실제 고기와 흡사한 외형을 가지고 있습니다.",
     "extra_description": "배양육은 동물 도살 없이 세포 배양으로 만들어진 고기로, 환경 부담을 줄이고 윤리적인 대안으로 주목받고 있습니다. 단백질 함량이 높고 기존 육류와 비슷한 맛과 식감을 제공하지만, 아직은 가격이 높다는 한계가 있습니다."},
    
    {"name": "귀뚜라미바",
     "pref_meat_like": False, "pref_dessert": True, "texture_grainy": False, "texture_crunchy": True, "pref_insect": True,
     "pref_supplement_form": True, "form_liquid": False, "form_natural": False, "pref_novelty": True, "nutrition_lowcal": True,
     "appearance_description": "에너지바 형태로 갈색이며, 곤충 분말이 포함되어 있습니다.",
     "extra_description": "귀뚜라미는 단백질과 아미노산이 풍부하고, 소고기 대비 훨씬 적은 환경 자원을 사용합니다. 에너지바 형태로 가볍게 먹기 좋아 간식이나 운동 후 보충식으로 적합합니다."},
    
    {"name": "아마란스",
     "pref_meat_like": False, "pref_dessert": False, "texture_grainy": True, "texture_crunchy": False, "pref_insect": False,
     "pref_supplement_form": False, "form_liquid": False, "form_natural": True, "pref_novelty": False, "nutrition_lowcal": False,
     "appearance_description": "작은 알갱이 곡물 형태로 노란색 또는 붉은색을 띱니다.",
     "extra_description": "아마란스는 고대 곡물로, 글루텐이 없으면서 단백질과 칼슘, 철분이 풍부합니다. 밥에 섞거나 샐러드, 죽, 시리얼 등으로 다양하게 활용 가능합니다."},
    
    {"name": "굼벵이 호두파이",
     "pref_meat_like": False, "pref_dessert": True, "texture_grainy": False, "texture_crunchy": False, "pref_insect": True,
     "pref_supplement_form": False, "form_liquid": False, "form_natural": False, "pref_novelty": True, "nutrition_lowcal": False,
     "appearance_description": "일반 호두파이와 유사하지만 곤충 가루가 포함된 디저트입니다.",
     "extra_description": "굼벵이는 단백질과 불포화지방산이 풍부해 영양가가 높습니다. 디저트와 결합하면 거부감을 줄이면서 새로운 맛을 경험할 수 있습니다."},
    
    {"name": "스피루리나",
     "pref_meat_like": False, "pref_dessert": False, "texture_grainy": False, "texture_crunchy": False, "pref_insect": False,
     "pref_supplement_form": True, "form_liquid": True, "form_natural": True, "pref_novelty": False, "nutrition_lowcal": True,
     "appearance_description": "짙은 초록색 미세 조류로 분말이나 정제 형태로 섭취합니다.",
     "extra_description": "스피루리나는 단백질 비율이 높고, 비타민과 미네랄이 풍부한 슈퍼푸드입니다. 분말은 스무디, 요거트, 빵 반죽 등에 활용할 수 있습니다."},
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
    st.markdown(f"**추가 설명:** {top_food['extra_description']}")  # 🔥 설명 추가
    
    st.markdown("---")
    st.markdown("**당신의 선택과 일치하는 특징:**")
    matched_features = []
    question_key_to_text = {v: k for k, v in quiz_questions.items()}

    for key, answer in st.session_state.user_answers.items():
        if (answer == "O" and top_food[key]) or (answer == "X" and not top_food[key]):
            if key in question_key_to_text:
                matched_features.append(f"- {question_key_to_text[key]}")
    
    if matched_features:
        for feature in matched_features:
            st.markdown(feature)
    else:
        st.markdown("- 당신의 답변과 잘 맞는 특징을 찾지 못했습니다. 😢")

    st.markdown("---")
    
    if st.button("다시 퀴즈 풀기"):
        st.session_state.show_result = False
        st.session_state.user_answers = {k: "X" for k in quiz_questions.values()}
        st.rerun()

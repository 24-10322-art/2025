import streamlit as st
import pandas as pd

st.title("🌱 나만의 미래 식량 추천")

st.write("아래 설문에 답하면 AI가 당신에게 가장 잘 맞는 미래 식량을 추천합니다!")

# 사용자 입력
taste_pref = st.radio("1. 좋아하는 맛은?", ["고소함", "짭짤함", "단맛", "고기맛", "담백함"])
texture_pref = st.radio("2. 좋아하는 식감은?", ["바삭함", "쫄깃함", "부드러움", "살짝 씹히는 맛"])
nutrition_pref = st.multiselect("3. 중요하게 생각하는 영양소는?", ["단백질 풍부", "미네랄 풍부", "저칼로리", "탄수화물 풍부", "비타민 풍부"])
eco_pref = st.slider("4. 환경과 지속 가능성을 얼마나 중요하게 생각하나요?", 1, 5, 3)
form_pref = st.selectbox("5. 선호하는 식량 형태는?", ["자연 상태 그대로", "가공식품 형태", "스낵/바 형태", "음료/액체 형태"])

# 미래 식량 후보 데이터
food_data = pd.DataFrame([
    {"name": "귀뚜라미 단백질", "taste": "고소함", "texture": "바삭함", "nutrition": "단백질 풍부", "eco": 5, "form": "스낵/바 형태", "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Edible_insects.jpg"},
    {"name": "해조류(김, 다시마 등)", "taste": "짭짤함", "texture": "쫄깃함", "nutrition": "미네랄 풍부", "eco": 4, "form": "자연 상태 그대로", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Seaweed_on_shore.jpg"},
    {"name": "배양육(실험실에서 배양한 고기)", "taste": "고기맛", "texture": "부드러움", "nutrition": "단백질 풍부", "eco": 3, "form": "가공식품 형태", "image": "https://upload.wikimedia.org/wikipedia/commons/2/23/Cultured_meat.jpg"},
    {"name": "곤약 기반 대체 식품", "taste": "담백함", "texture": "쫄깃함", "nutrition": "저칼로리", "eco": 4, "form": "가공식품 형태", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Konjac_jelly.jpg"},
    {"name": "곡물 기반 미래 식품(퀴노아, 아마란스 등)", "taste": "담백함", "texture": "부드러움", "nutrition": "탄수화물 풍부", "eco": 4, "form": "자연 상태 그대로", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Grain_on_plate.jpg"},
    {"name": "곤충 단백질 바(밀웜, 귀뚜라미 포함)", "taste": "고소함", "texture": "부드러움", "nutrition": "단백질 풍부", "eco": 5, "form": "스낵/바 형태", "image": "https://upload.wikimedia.org/wikipedia/commons/1/19/Cricket_energy_bar.jpg"},
    {"name": "미래 식용 버섯(재배형 고단백 버섯)", "taste": "짭짤함", "texture": "쫄깃함", "nutrition": "단백질/미네랄", "eco": 5, "form": "자연 상태 그대로", "image": "https://upload.wikimedia.org/wikipedia/commons/1/11/Mushrooms.jpg"},
])

# 추천 점수 계산 (Top 1)
def recommend_food():
    scores = []
    for _, row in food_data.iterrows():
        score = 0
        if row["taste"] == taste_pref:
            score += 2
        if row["texture"] == texture_pref:
            score += 2
        for n in nutrition_pref:
            if n in row["nutrition"]:
                score += 1
        score += min(eco_pref, row["eco"])
        if row["form"] == form_pref:
            score += 1
        scores.append(score)
    food_data["score"] = scores
    top_food = food_data.sort_values(by="score", ascending=False).iloc[0]
    return top_food

# 추천 결과 표시
if st.button("추천 받기"):
    top_food = recommend_food()
    st.subheader("🌟 당신에게 가장 잘 맞는 미래 식량 🌟")
    # 이미지 표시
    st.image(top_food['image'], use_container_width=True)
    # 주요 특징 표시
    st.markdown(f"### {top_food['name']}")
    st.markdown(f"- **맛:** {top_food['taste']}")
    st.markdown(f"- **식감:** {top_food['texture']}")
    st.markdown(f"- **영양 특징:** {top_food['nutrition']}")
    st.markdown(f"- **선호 형태:** {top_food['form']}")
    st.markdown(f"- **지속 가능성 점수:** {top_food['eco']}")

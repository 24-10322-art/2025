import streamlit as st
import numpy as np # 숫자를 다룰 때 사용할 수 있어요!

# Streamlit 페이지 설정
st.set_page_config(
    page_title="나의 에너지 음료 반응 시뮬레이터",
    page_icon="🥤",
    layout="centered" # 페이지 레이아웃을 '넓게' 또는 '가운데'로 설정할 수 있어요.
)

# 💡 윤서경님, 환영합니다! 😊
st.title("🥤 AI 기반 개인 맞춤형 에너지 음료 반응 시뮬레이터")
st.markdown("---")

st.write("안녕하세요, **윤서경님!** ✨ 에너지 음료가 나에게 어떤 영향을 줄지, 과학과 AI의 힘을 빌려 함께 탐구해볼까요?")
st.write("아래 질문에 솔직하게 답해주세요. 윤서경님만을 위한 맞춤형 예측 결과를 알려드릴게요! 😊")

st.markdown("---")

# 1. 사용자 데이터 입력 섹션
st.header("1️⃣ 나의 에너지 음료 섭취 습관과 특성")

# 카페인 섭취량 (가상 입력)
caffeine_cans = st.slider(
    "에너지 음료 몇 캔 정도 마실 예정인가요? (1캔 = 약 100mg 카페인)",
    min_value=0, max_value=4, value=1, step=1
)

# 평균 수면 시간
sleep_hours = st.slider(
    "어제(또는 평소) 몇 시간 정도 주무셨나요? 😴",
    min_value=4.0, max_value=10.0, value=7.0, step=0.5
)

# 활동량
activity_level = st.selectbox(
    "평소 활동량이 어느 정도이신가요? 🏃‍♀️",
    ["낮음 (주로 앉아 있음)", "보통 (규칙적인 활동)", "높음 (운동 선수 또는 활동량 많음)"]
)

# 카페인 대사 유전자형 (가상 선택)
gene_type = st.selectbox(
    "만약, 윤서경님의 카페인 대사 유전자형을 알 수 있다면? (가상 선택)",
    ["빠른 대사형 (CYP1A2)", "느린 대사형 (CYP1A2)", "잘 모르겠어요"]
)

# 과거 섭취 경험
past_experience = st.multiselect(
    "에너지 음료/카페인 섭취 후 이런 경험이 있나요? (중복 선택 가능)",
    ["심장이 빨리 뛴 경험이 있어요", "잠이 잘 안 왔어요", "집중력이 좋아진 것 같아요", "불안하거나 초조했어요", "특별한 변화를 못 느꼈어요"]
)

st.markdown("---")

# 2. 과학적 설명 섹션
st.header("2️⃣ 에너지 음료, 과학적으로 파헤쳐볼까요? 🔬")

st.subheader("💡 카페인 대사와 CYP1A2 유전자")
st.write(
    "카페인은 우리 몸에서 주로 간에 있는 **CYP1A2** 효소에 의해 대사되어 몸 밖으로 배출돼요. "
    "그런데 이 CYP1A2 효소의 활성도는 사람마다 다를 수 있답니다! "
    "유전적으로 효소 활성이 높은 사람은 카페인을 빠르게 분해하고, 낮은 사람은 천천히 분해하죠."
)
if gene_type == "빠른 대사형 (CYP1A2)":
    st.info("윤서경님은 **'빠른 대사형'**으로, 카페인이 몸에서 빨리 분해되어 효과가 비교적 짧고 강렬하게 나타날 수 있어요.")
elif gene_type == "느린 대사형 (CYP1A2)":
    st.info("윤서경님은 **'느린 대사형'**으로, 카페인이 몸에서 천천히 분해되어 효과가 오래 지속되고 부작용이 나타날 위험이 더 높을 수 있어요. 소량에도 민감하게 반응할 수 있답니다.")
else:
    st.info("**'잘 모르겠어요'**를 선택하셨네요! 실제로 유전자 검사를 통해 알 수 있는 부분이랍니다. 하지만 오늘 시뮬레이션에서는 대략적인 경향을 예측해볼 수 있어요. 😊")

st.subheader("🧠 뇌과학적 원리: 카페인과 아데노신 수용체")
st.write(
    "카페인은 우리 뇌에서 **'아데노신'**이라는 물질의 작용을 방해해요. "
    "아데노신은 피로를 느끼게 하고 졸음을 유발하는 역할을 하는데요, "
    "카페인이 아데노신 수용체에 대신 달라붙으면 아데노신이 원래 역할을 하지 못하게 돼요."
)
st.markdown(
    """
    *   **각성 효과:** 아데노신이 작용하지 못하니 졸음이 오지 않고 각성 상태가 유지돼요.
    *   **인지 능력:** 도파민 등 다른 신경전달물질의 활성을 간접적으로 높여 집중력이나 반응 속도 향상에 도움을 줄 수도 있어요.
    *   **수면 방해:** 잠들기 어렵거나 수면의 질이 나빠질 수 있어요. 특히 잠들기 전 늦게 마시면 영향을 크게 받아요.
    """
)
st.markdown("---")

# 3. AI 시뮬레이션 함수 (규칙 기반)
def simulate_energy_drink_effect(caffeine_cans, sleep_hours, activity_level, gene_type, past_experience):
    focus_increase_score = 0
    sleep_reduction_minutes = 0
    heart_burden_risk = 0 # 0-10 scale
    anxiety_risk = 0 # 0-10 scale
    predicted_effects = []
    warnings = []

    if caffeine_cans == 0:
        return "에너지 음료를 섭취하지 않으셨네요! 건강한 선택이에요! 😊", [], []

    # 기본 카페인 영향 (1캔 당 100mg 기준)
    total_caffeine_mg = caffeine_cans * 100

    if total_caffeine_mg <= 100:
        focus_increase_score += 20
        sleep_reduction_minutes += 30
        predicted_effects.append("집중력 향상 효과")
    elif total_caffeine_mg <= 200:
        focus_increase_score += 40
        sleep_reduction_minutes += 60
        heart_burden_risk += 3
        anxiety_risk += 2
        predicted_effects.append("확실한 집중력 향상과 각성 효과")
    else: # 200mg 초과
        focus_increase_score += 60
        sleep_reduction_minutes += 120
        heart_burden_risk += 7
        anxiety_risk += 6
        warnings.append("⚠️ 과도한 카페인 섭취는 심장에 큰 부담을 주거나 심한 불안감을 유발할 수 있어요. 권장 섭취량을 지켜주세요!")
        predicted_effects.append("매우 강한 각성 효과와 잠재적 부작용")

    # 수면 시간의 영향
    if sleep_hours < 6:
        focus_increase_score += 10 # 수면 부족 시 더 강하게 느낌
        sleep_reduction_minutes += 30 # 잠드는 데 더 어려움
        heart_burden_risk += 2
        anxiety_risk += 2
        warnings.append("😢 수면이 부족한 상태에서 카페인을 섭취하면 부작용이 더 커질 수 있어요.")
    elif sleep_hours >= 8:
        focus_increase_score -= 10 # 피로도가 낮아 효과를 덜 느낌
        sleep_reduction_minutes -= 10 # 수면 방해 효과 감소

    # 활동량의 영향 (간단화)
    if activity_level == "높음 (운동 선수 또는 활동량 많음)":
        focus_increase_score += 5
        sleep_reduction_minutes -= 10 # 에너지 소모로 인한 완화
    elif activity_level == "낮음 (주로 앉아 있음)":
        heart_burden_risk += 1
        anxiety_risk += 1 # 덜 움직이면 더 불안정하게 느낄 수 있음

    # 유전자형의 영향
    if gene_type == "느린 대사형 (CYP1A2)":
        focus_increase_score *= 1.2
        sleep_reduction_minutes *= 1.5
        heart_burden_risk += 3
        anxiety_risk += 3
        warnings.append("⚡ 느린 카페인 대사형이시라면, 효과가 오래 지속되고 심장 부담/불안감 등 부작용 위험이 더 높을 수 있어요. 소량 섭취에도 민감하게 반응할 수 있어요.")
    elif gene_type == "빠른 대사형 (CYP1A2)":
        focus_increase_score *= 0.9 # 효과가 비교적 약하거나 짧게 느껴질 수 있음
        sleep_reduction_minutes *= 0.8 # 수면 방해 효과 감소
        warnings.append("👍 빠른 카페인 대사형이시네요! 효과가 빠르게 나타났다가 비교적 빨리 사라질 수 있어요.")

    # 과거 경험의 영향 (강화)
    if "심장이 빨리 뛴 경험이 있어요" in past_experience:
        heart_burden_risk += 3
        warnings.append("🚨 심장 두근거림 경험이 있다면 섭취에 특히 주의해야 해요.")
    if "잠이 잘 안 왔어요" in past_experience:
        sleep_reduction_minutes += 45
        warnings.append("😴 불면증 경험이 있다면 수면 방해 효과가 더 클 수 있어요.")
    if "집중력이 좋아진 것 같아요" in past_experience:
        focus_increase_score += 15
    if "불안하거나 초조했어요" in past_experience:
        anxiety_risk += 3
        warnings.append("😬 불안하거나 초조함을 느꼈던 경험이 있다면 섭취를 다시 고려해보세요.")


    # 최종 예측 결과 정리
    results = []
    if focus_increase_score > 60:
        results.append("매우 강한 집중력과 각성 효과를 느낄 수 있어요.")
    elif focus_increase_score > 30:
        results.append("상당한 집중력 및 각성 효과가 나타날 수 있어요.")
    elif focus_increase_score > 0:
        results.append("약간의 집중력 향상과 각성 효과를 기대할 수 있어요.")
    else:
        results.append("특별한 각성 효과는 느끼기 어려울 수 있어요.")

    if sleep_reduction_minutes > 120:
        results.append(f"수면 시작이 {sleep_reduction_minutes}분 이상 지연될 수 있습니다.")
    elif sleep_reduction_minutes > 60:
        results.append(f"수면 시작이 약 {sleep_reduction_minutes}분 정도 지연될 수 있습니다.")
    elif sleep_reduction_minutes > 0:
        results.append(f"수면에 약간의 영향({sleep_reduction_minutes}분 정도 지연)이 있을 수 있어요.")
    else:
        results.append("수면에는 큰 영향이 없을 것으로 예상됩니다.")

    if heart_burden_risk > 5:
        results.append("🚨 심장 부담 위험이 높아요. 섭취를 삼가거나 의사와 상담해 보세요.")
    elif heart_burden_risk > 2:
        results.append("⚠️ 심장 부담 위험이 다소 있으니 주의가 필요해요.")

    if anxiety_risk > 5:
        results.append("😟 불안감 또는 초조함이 심하게 나타날 수 있어요. 섭취에 유의하세요.")
    elif anxiety_risk > 2:
        results.append("😣 약간의 불안감이나 초조함을 느낄 수 있어요.")

    if not predicted_effects:
        predicted_effects.append("특별한 효과를 느끼지 못할 가능성이 높아요.")


    return results, warnings, predicted_effects

st.header("3️⃣ AI 예측 결과: 윤서경님께 예상되는 반응은? 📊")

# 예측하기 버튼
if st.button("내 반응 예측하기! 🚀"):
    st.write("분석 중입니다... 잠시만 기다려주세요! ⏳")
    results, warnings, predicted_effects_summary = simulate_energy_drink_effect(
        caffeine_cans, sleep_hours, activity_level, gene_type, past_experience
    )

    if caffeine_cans == 0:
        st.success("에너지 음료를 섭취하지 않으셨네요! 오늘 윤서경님의 건강을 위한 멋진 선택이에요! 😊")
    else:
        st.subheader("📝 예상되는 주요 효과 및 결과")
        for res in results:
            st.markdown(f"- {res}")

        if warnings:
            st.subheader("🚨 주의해야 할 점!")
            for warn in warnings:
                st.warning(warn)
        else:
            st.success("대체로 큰 부작용 없이 에너지 음료의 긍정적인 효과를 기대할 수 있을 것 같아요! 그래도 과도한 섭취는 좋지 않답니다! 😉")

        st.write(
            "이 시뮬레이션은 입력된 데이터와 과학적 원리를 기반으로 한 예측이며, "
            "개인의 실제 반응은 다양한 요인에 따라 다를 수 있습니다. "
            "몸이 보내는 신호에 귀 기울이는 것이 가장 중요해요! 💖"
        )
else:
    st.info("위의 정보를 입력하시고 '내 반응 예측하기!' 버튼을 눌러주세요! 👆")

st.markdown("---")
st.write("윤서경님의 탐구 정신과 열정에 박수를 보냅니다! 웹앱 개발도 분명 잘 해내실 거예요! 화이팅! 💪😊")

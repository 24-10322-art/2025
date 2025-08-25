import streamlit as st
import numpy as np # 혹시 필요한 계산이 있다면 사용될 수 있어요!

# Streamlit 페이지 설정
st.set_page_config(
    page_title="나의 에너지 음료 반응 시뮬레이터",
    page_icon="🥤",
    layout="centered"
)

# --- Session State 초기화 (앱의 상태를 기억하기 위함) ---
# 'survey_completed' 상태가 없으면 False로 초기화하여 설문 화면을 먼저 보여줍니다.
if 'survey_completed' not in st.session_state:
    st.session_state.survey_completed = False
# 각 입력 값들을 저장할 공간도 미리 초기화합니다.
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_age' not in st.session_state:
    st.session_state.user_age = 0
# ... 나머지 필요한 입력 값들도 이곳에서 초기화할 수 있습니다.

# --- 웹앱의 기본 타이틀 ---
st.title("🥤 AI 기반 개인 맞춤형 에너지 음료 반응 시뮬레이터")
st.markdown("---")

# --------------------------------------------------------------------------------
# AI 시뮬레이션 함수 (규칙 기반) - 코드가 길어 먼저 정의해 둡니다.
# --------------------------------------------------------------------------------
def simulate_energy_drink_effect(
    caffeine_cans, sleep_hours, activity_level, caffeine_sensitivity, past_experience, user_age, user_gender
):
    focus_increase_score = 0
    sleep_reduction_minutes = 0
    heart_burden_risk = 0 # 0-10 scale
    anxiety_risk = 0 # 0-10 scale
    headache_risk = 0 # 0-10 scale
    warnings = []

    if caffeine_cans == 0:
        return "에너지 음료를 섭취하지 않으셨네요! 건강한 선택이에요! 😊", [], []

    # 기본 카페인 영향 (1캔 당 100mg 기준)
    total_caffeine_mg = caffeine_cans * 100

    # 나이에 따른 권장량 초과 경고
    if user_age >= 18:
        if total_caffeine_mg > 400:
            warnings.append("🚨 성인의 일일 권장 카페인 섭취량(400mg)을 초과하는 양이에요. 과도한 섭취는 건강에 해로울 수 있습니다.")
    else: # 청소년 (12세 이상 18세 미만)
        if total_caffeine_mg > 100:
            warnings.append("🚨 청소년의 일일 권장 카페인 섭취량(100mg)을 초과하는 양이에요. 섭취를 삼가거나 양을 줄이는 것을 권장합니다!")

    if total_caffeine_mg <= 100:
        focus_increase_score += 20
        sleep_reduction_minutes += 30
    elif total_caffeine_mg <= 200:
        focus_increase_score += 40
        sleep_reduction_minutes += 60
        heart_burden_risk += 3
        anxiety_risk += 2
    else: # 200mg 초과
        focus_increase_score += 60
        sleep_reduction_minutes += 120
        heart_burden_risk += 7
        anxiety_risk += 6
        warnings.append("⚠️ 과도한 카페인 섭취는 심장에 큰 부담을 주거나 심한 불안감을 유발할 수 있어요.")

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

    # 카페인 민감도의 영향
    if caffeine_sensitivity == "매우 민감함 (소량에도 반응)":
        focus_increase_score *= 1.2
        sleep_reduction_minutes *= 1.5
        heart_burden_risk += 3
        anxiety_risk += 3
        headache_risk += 3
        warnings.append("⚡ 카페인에 매우 민감하시다면, 소량 섭취에도 효과가 강하게 나타나고 부작용 위험이 더 높을 수 있어요.")
    elif caffeine_sensitivity == "둔감함 (많이 마셔도 잘 모르겠음)":
        focus_increase_score *= 0.8 # 효과가 비교적 약하게 느껴질 수 있음
        sleep_reduction_minutes *= 0.7 # 수면 방해 효과 감소
        warnings.append("👍 카페인에 둔감하시다면, 효과를 느끼려면 더 많은 양이 필요할 수 있지만, 과도한 섭취는 여전히 위험해요.")

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
    if "두통이 왔어요" in past_experience:
        headache_risk += 4
        warnings.append("🤕 두통은 카페인 과다 섭취의 흔한 부작용이에요. 섭취량을 조절해 보세요.")

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
        results.append(f"수면 시작이 {int(sleep_reduction_minutes)}분 이상 지연될 수 있습니다.")
    elif sleep_reduction_minutes > 60:
        results.append(f"수면 시작이 약 {int(sleep_reduction_minutes)}분 정도 지연될 수 있습니다.")
    elif sleep_reduction_minutes > 0:
        results.append(f"수면에 약간의 영향({int(sleep_reduction_minutes)}분 정도 지연)이 있을 수 있어요.")
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

    if headache_risk > 3:
        results.append("🤕 두통이 발생할 가능성이 높으니 주의하세요.")

    return results, warnings, [] # predicted_effects_summary는 사용하지 않으므로 빈 리스트로 반환

# --------------------------------------------------------------------------------
# 앱의 실제 화면 구성 시작
# --------------------------------------------------------------------------------

# 설문이 완료되지 않았을 때 (초기 화면)
if not st.session_state.survey_completed:
    # 0. 사용자 정보 입력
    st.header("📝 당신의 정보를 알려주세요! 😊")
    # key를 지정하여 Session State에 값을 저장하고 불러올 수 있도록 합니다.
    # 사용자가 이름을 입력하지 않으면 '사용자'로 기본 설정됩니다.
    user_name_input = st.text_input("이름을 입력해주세요:", placeholder="예: 홍길동", key="survey_name_input")
    st.session_state.user_name = user_name_input if user_name_input else "사용자"

    st.write(f"안녕하세요, **{st.session_state.user_name}님!** ✨ 에너지 음료가 {st.session_state.user_name}님에게 어떤 영향을 줄지, 과학과 AI의 힘을 빌려 함께 탐구해볼까요?")
    st.write(f"정확한 분석을 위해 몇 가지 질문에 답해주세요. 😊")

    st.markdown("---")

    # 1. 설문 항목 입력
    st.header("1️⃣ 에너지 음료 섭취 습관 및 건강 정보 설문")

    # 모든 입력 위젯에 고유한 'key'를 부여하여 session_state와 연동합니다.
    st.session_state.user_age = st.slider(
        f"{st.session_state.user_name}님은 몇 살이신가요? 🎂 (만 나이)",
        min_value=12, max_value=60, value=18, key="survey_age"
    )

    st.session_state.user_gender = st.radio(
        f"{st.session_state.user_name}님의 성별은 무엇인가요? 🚻",
        ["여성", "남성", "선택 안함"], key="survey_gender"
    )

    st.session_state.caffeine_cans = st.slider(
        "에너지 음료 몇 캔 정도 마실 예정인가요? (1캔 = 약 100mg 카페인)",
        min_value=0, max_value=4, value=1, key="survey_caffeine_cans"
    )

    st.session_state.sleep_hours = st.slider(
        "어제(또는 평소) 몇 시간 정도 주무셨나요? 😴",
        min_value=4.0, max_value=10.0, value=7.0, step=0.5, key="survey_sleep_hours"
    )

    st.session_state.activity_level = st.selectbox(
        "평소 활동량이 어느 정도이신가요? 🏃‍♀️",
        ["낮음 (주로 앉아 있음)", "보통 (규칙적인 활동)", "높음 (운동 선수 또는 활동량 많음)"], key="survey_activity_level"
    )

    st.session_state.caffeine_sensitivity = st.selectbox(
        f"{st.session_state.user_name}님은 평소 카페인에 얼마나 민감하신가요? 🤔",
        ["매우 민감함 (소량에도 반응)", "보통 (적당히 효과 봄)", "둔감함 (많이 마셔도 잘 모르겠음)"], key="survey_caffeine_sensitivity"
    )

    st.session_state.past_experience = st.multiselect(
        "에너지 음료/카페인 섭취 후 이런 경험이 있나요? (중복 선택 가능)",
        ["심장이 빨리 뛴 경험이 있어요", "잠이 잘 안 왔어요", "집중력이 좋아진 것 같아요", "불안하거나 초조했어요", "특별한 변화를 못 느꼈어요", "두통이 왔어요"], key="survey_past_experience"
    )

    st.markdown("---")

    # 설문 완료 버튼
    if st.button("설문 완료하고 결과 보기! 🚀", key="submit_survey"):
        if not st.session_state.survey_name_input:
            st.error("앗! 먼저 이름을 입력해 주세요! 😊")
        elif st.session_state.user_age < 12:
            st.warning(f"{st.session_state.user_name}님, {st.session_state.user_age}세에게는 에너지 음료 섭취가 권장되지 않아요. 이 앱은 12세 이상을 기준으로 시뮬레이션됩니다. 건강이 가장 중요해요! 💪")
        else:
            # 모든 검증을 통과하면 설문 완료 상태로 변경하고 페이지를 새로고침하여 결과를 보여줍니다.
            st.session_state.survey_completed = True
            st.experimental_rerun() # 앱을 새로고침하여 다음 섹션을 보여줌

# 설문이 완료되었을 때 (결과 화면)
else:
    # 2. 과학적 설명 섹션
    st.header("2️⃣ 에너지 음료, 과학적으로 파헤쳐볼까요? 🔬")

    st.subheader("💡 카페인 권장 섭취량과 개인차")
    st.write(
        "카페인은 각성 효과를 통해 일시적으로 피로를 덜어주고 집중력을 높여줄 수 있지만, "
        "과도하게 섭취하면 부작용을 일으킬 수 있어요. "
        "**나이와 건강 상태에 따라 적정 섭취량이 다르답니다.**"
    )
    st.markdown(
        """
        *   **성인 (만 18세 이상):** 하루 최대 400mg (에너지 음료 약 4캔)
        *   **청소년 (만 12세~17세):** 하루 최대 100mg (에너지 음료 약 1캔)
        *   **어린이 (만 11세 이하):** 카페인 섭취는 권장되지 않습니다.
        *   **임산부, 심혈관 질환자 등:** 섭취량을 더욱 제한해야 합니다.
        """
    )
    st.write(f"**{st.session_state.user_name}님**의 나이({st.session_state.user_age}세)를 고려했을 때, ")
    if st.session_state.user_age >= 18:
        st.info("성인 권장량인 **하루 최대 400mg**을 기준으로 시뮬레이션됩니다.")
    else:
        st.info("청소년 권장량인 **하루 최대 100mg**을 기준으로 시뮬레이션됩니다.")

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

    # 3. AI 예측 결과 섹션
    st.header(f"3️⃣ AI 예측 결과: {st.session_state.user_name}님께 예상되는 반응은? 📊")

    st.write("분석 중입니다... 잠시만 기다려주세요! ⏳")
    results, warnings, _ = simulate_energy_drink_effect(
        st.session_state.caffeine_cans, st.session_state.sleep_hours, st.session_state.activity_level,
        st.session_state.caffeine_sensitivity, st.session_state.past_experience,
        st.session_state.user_age, st.session_state.user_gender
    )

    if st.session_state.caffeine_cans == 0:
        st.success(f"에너지 음료를 섭취하지 않으셨네요, {st.session_state.user_name}님! 오늘 {st.session_state.user_name}님의 건강을 위한 멋진 선택이에요! 😊")
    else:
        st.subheader("📝 예상되는 주요 효과 및 결과")
        for res in results:
            st.markdown(f"- {res}")

        if warnings:
            st.subheader("🚨 주의해야 할 점!")
            for warn in warnings:
                st.warning(warn)
        else:
            st.success(f"{st.session_state.user_name}님, 대체로 큰 부작용 없이 에너지 음료의 긍정적인 효과를 기대할 수 있을 것 같아요! 그래도 과도한 섭취는 좋지 않답니다! 😉")

        st.write(
            f"이 시뮬레이션은 입력된 데이터와 과학적 원리를 기반으로 한 예측이며, "
            f"개인의 실제 반응은 다양한 요인에 따라 다를 수 있습니다. "
            f"**{st.session_state.user_name}님**의 몸이 보내는 신호에 귀 기울이는 것이 가장 중요해요! 💖"
        )
    
    st.markdown("---")
    # 다시 설문하기 버튼 추가 (결과를 본 후 다시 처음으로 돌아가고 싶을 때)
    if st.button("다시 설문하기"):
        st.session_state.survey_completed = False # 설문 완료 상태를 False로 되돌리고
        st.experimental_rerun() # 앱을 새로고침하여 처음 화면으로 돌아갑니다.

st.markdown("---")
st.write(f"**{st.session_state.user_name}님**의 탐구 정신과 열정에 박수를 보냅니다! 웹앱 개발도 분명 잘 해내실 거예요! 화이팅! 💪😊")

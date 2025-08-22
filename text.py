import streamlit as st
import pandas as pd

# 학생들이 자주 마시는 에너지 음료 데이터 (mg 단위로 정리)
energy_drinks = {
    "핫식스 오리지널": {
        "카페인(mg)": 60,
        "타우린(mg)": 1000,
        "칼로리(kcal)": 120,
        "효과": "피로 회복, 집중력 향상 ⚡",
        "용량": "250ml"
    },
    "핫식스 더킹": {
        "카페인(mg)": 150,
        "타우린(mg)": 2000,
        "칼로리(kcal)": 170,
        "효과": "강력한 각성 효과 🚀",
        "용량": "355ml"
    },
    "몬스터 에너지 오리지널": {
        "카페인(mg)": 160,
        "타우린(mg)": 1000,
        "칼로리(kcal)": 210,
        "효과": "집중력 강화, 피로 감소 🔥",
        "용량": "473ml"
    },
    "몬스터 울트라(제로)": {
        "카페인(mg)": 140,
        "타우린(mg)": 1000,
        "칼로리(kcal)": 0,
        "효과": "칼로리 부담 없이 에너지 공급 💨",
        "용량": "355ml"
    }
}

# 하루 카페인 권장량
DAILY_LIMIT = 400  

# Streamlit UI
st.title("🥤 학생들이 자주 마시는 에너지 음료 성분 & 효과")
st.write("🔥 핫식스와 몬스터의 성분과 효과를 확인해보세요!")
st.info("💡 성인 기준 하루 카페인 권장량은 400mg입니다.")

# 음료 선택
selected_drink = st.selectbox("에너지 음료를 선택하세요:", list(energy_drinks.keys()))

# 선택한 음료 데이터 표시
drink_info = energy_drinks[selected_drink]

st.subheader(f"📌 {selected_drink}")
st.write(f"**용량:** {drink_info['용량']}")
st.write(f"**카페인:** {drink_info['카페인(mg)']}mg")
st.write(f"**타우린:** {drink_info['타우린(mg)']}mg")
st.write(f"**칼로리:** {drink_info['칼로리(kcal)']}kcal")
st.success(f"✨ 효과: {drink_info['효과']}")

# 카페인 권장량 대비 퍼센트 계산
percent = (drink_info['카페인(mg)'] / DAILY_LIMIT) * 100

# ✅ st.progress()는 0~1 사이 값만 허용 → percent / 100
st.progress(min(1.0, percent / 100))  
st.write(f"☕ 하루 권장량 대비 **{percent:.1f}%** 섭취")

# 경고 메시지
if percent >= 100:
    st.error("🚨 하루 권장량을 초과했습니다! 주의하세요.")
elif percent >= 70:
    st.warning("⚠️ 권장량의 70% 이상 섭취했습니다. 조심하세요!")

# 테이블로 전체 음료 보기
if st.checkbox("📊 모든 음료 성분 비교하기"):
    df = pd.DataFrame(energy_drinks).T
    st.dataframe(df)

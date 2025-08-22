import streamlit as st
import pandas as pd

# 에너지 음료 데이터
energy_drinks = {
    "핫식스 오리지널": {
        "카페인": "60mg / 250ml",
        "타우린": "1000mg",
        "칼로리": "120kcal",
        "효과": "피로 회복, 집중력 향상 ⚡"
    },
    "핫식스 더킹": {
        "카페인": "150mg / 355ml",
        "타우린": "2000mg",
        "칼로리": "170kcal",
        "효과": "강력한 각성 효과 🚀"
    },
    "몬스터 에너지 오리지널": {
        "카페인": "160mg / 473ml",
        "타우린": "1000mg",
        "칼로리": "210kcal",
        "효과": "집중력 강화, 피로 감소 🔥"
    },
    "몬스터 울트라(제로)": {
        "카페인": "140mg / 355ml",
        "타우린": "1000mg",
        "칼로리": "0kcal",
        "효과": "칼로리 부담 없이 에너지 공급 💨"
    },
    "레드불 오리지널": {
        "카페인": "80mg / 250ml",
        "타우린": "1000mg",
        "칼로리": "110kcal",
        "효과": "피로 회복, 운동 전후 활력 ⚡"
    },
    "레드불 슈가프리": {
        "카페인": "80mg / 250ml",
        "타우린": "1000mg",
        "칼로리": "0kcal",
        "효과": "저칼로리 에너지 부스터 💎"
    }
}

# Streamlit UI
st.title("🥤 에너지 음료 성분 & 효과 조회")
st.write("대표적인 에너지 음료들의 성분과 효과를 확인해보세요!")

# 음료 선택
selected_drink = st.selectbox("에너지 음료를 선택하세요:", list(energy_drinks.keys()))

# 선택한 음료 데이터 표시
drink_info = energy_drinks[selected_drink]

st.subheader(f"📌 {selected_drink}")
st.write(f"**카페인 함량:** {drink_info['카페인']}")
st.write(f"**타우린 함량:** {drink_info['타우린']}")
st.write(f"**칼로리:** {drink_info['칼로리']}")
st.success(f"✨ 효과: {drink_info['효과']}")

# 테이블로 전체 음료 보기
if st.checkbox("📊 모든 에너지 음료 성분 보기"):
    df = pd.DataFrame(energy_drinks).T
    st.dataframe(df)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 학생들이 자주 마시는 에너지 음료 데이터 (mg 단위 + 이미지 URL)
energy_drinks = {
    "핫식스 오리지널": {
        "카페인(mg)": 60,
        "타우린(mg)": 1000,
        "칼로리(kcal)": 120,
        "효과": "피로 회복, 집중력 향상 ⚡",
        "용량": "250ml",
        "이미지": "https://shopping-phinf.pstatic.net/main_8249771/82497719041.1.jpg"
    },
    "핫식스 더킹": {
        "카페인(mg)": 150,
        "타우린(mg)": 2000,
        "칼로리(kcal)": 170,
        "효과": "강력한 각성 효과 🚀",
        "용량": "355ml",
        "이미지": "https://shopping-phinf.pstatic.net/main_8249768/82497682733.2.jpg"
    },
    "몬스터 에너지 오리지널": {
        "카페인(mg)": 160,
        "타우린(mg)": 1000,
        "칼로리(kcal)": 210,
        "효과": "집중력 강화, 피로 감소 🔥",
        "용량": "473ml",
        "이미지": "https://shopping-phinf.pstatic.net/main_8249773/82497737464.2.jpg"
    },
    "몬스터 울트라(제로)": {
        "카페인(mg)": 140,
        "타우린(mg)": 1000,
        "칼로리(kcal)": 0,
        "효과": "칼로리 부담 없이 에너지 공급 💨",
        "용량": "355ml",
        "이미지": "https://shopping-phinf.pstatic.net/main_8249772/82497725342.1.jpg"
    }
}

# 고2 학생 기준 하루 카페인 권장량
DAILY_LIMIT = 120  

# Streamlit UI
st.title("🥤 학생들이 자주 마시는 에너지 음료 성분 & 효과")
st.write("🔥 핫식스와 몬스터의 성분과 효과를 확인해보세요!")
st.info(f"💡 18세 학생 기준 하루 카페인 권장량은 {DAILY_LIMIT}mg입니다.")

# 음료 선택
selected_drink = st.selectbox("에너지 음료를 선택하세요:", list(energy_drinks.keys()))
drink_info = energy_drinks[selected_drink]

st.subheader(f"📌 {selected_drink}")
st.image(drink_info['이미지'], caption=selected_drink, width=200)
st.write(f"**용량:** {drink_info['용량']}")
st.write(f"**카페인:** {drink_info['카페인(mg)']}mg")
st.write(f"**타우린:** {drink_info['타우린(mg)']}mg")
st.write(f"**칼로리:** {drink_info['칼로리(kcal)']}kcal")
st.success(f"✨ 효과: {drink_info['효과']}")

# 카페인 권장량 대비 퍼센트 계산
percent = (drink_info['카페인(mg)'] / DAILY_LIMIT) * 100
st.write(f"☕ 하루 권장량 대비 **{percent:.1f}%** 섭취")

# 원그래프 시각화
labels = ['섭취한 카페인', '남은 권장량']
sizes = [min(drink_info['카페인(mg)'], DAILY_LIMIT), max(0, DAILY_LIMIT - drink_info['카페인(mg)'])]
colors = ['#ff6347', '#90ee90']  # 빨강=섭취, 초록=남은
explode = (0.1, 0)  # 첫 조각 강조

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, wedgeprops={'edgecolor':'white'})
ax.axis('equal')  # 원형 유지
st.pyplot(fig)

# 경고 메시지 (학생 기준)
if percent >= 100:
    st.error("🚨 하루 권장량을 초과했습니다! 주의하세요.")
elif percent >= 70:
    st.warning("⚠️ 권장량의 70% 이상 섭취했습니다. 조심하세요!")

# 테이블에 이미지 포함
if st.checkbox("📊 모든 음료 성분 + 이미지 보기"):
    st.markdown("### 전체 음료 비교")
    table_html = "<table style='width:100%; border-collapse: collapse;'>"
    table_html += "<tr><th>이미지</th><th>음료</th><th>카페인</th><th>타우린</th><th>칼로리</th><th>효과</th><th>용량</th></tr>"
    
    for name, info in energy_drinks.items():
        table_html += f"<tr style='border-bottom:1px solid #ddd;'>"
        table_html += f"<td><img src='{info['이미지']}' width='60'></td>"
        table_html += f"<td>{name}</td>"
        table_html += f"<td>{info['카페인(mg)']} mg</td>"
        table_html += f"<td>{info['타우린(mg)']} mg</td>"
        table_html += f"<td>{info['칼로리(kcal)']} kcal</td>"
        table_html += f"<td>{info['효과']}</td>"
        table_html += f"<td>{info['용량']}</td>"
        table_html += "</tr>"
    table_html += "</table>"
    
    st.markdown(table_html, unsafe_allow_html=True)

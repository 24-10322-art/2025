import streamlit as st
import pandas as pd
import random
import pydeck as pdk

# --- 데이터 정의 ---
destinations = {
    "파리": {"국가": "프랑스", "lat": 48.8566, "lon": 2.3522, "이미지": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg"},
    "도쿄": {"국가": "일본", "lat": 35.6762, "lon": 139.6503, "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Tokyo_Tower_and_around_Skyscrapers.jpg/640px-Tokyo_Tower_and_around_Skyscrapers.jpg"},
    "뉴욕": {"국가": "미국", "lat": 40.7128, "lon": -74.0060, "이미지": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Lower_Manhattan_from_Jersey_City_November_2014_panorama_3.jpg"},
    "런던": {"국가": "영국", "lat": 51.5074, "lon": -0.1278, "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/London_Montage_L.jpg/640px-London_Montage_L.jpg"}
}

# --- 앱 UI ---
st.title("🌏 가상 세계 여행 시뮬레이터")

# --- 지구본 시각화 ---
df = pd.DataFrame([
    {"city": city, "lat": data["lat"], "lon": data["lon"]}
    for city, data in destinations.items()
])

st.subheader("지구본에서 도시를 확인하세요")
st.write("도시 마커를 클릭하거나, 아래 선택 박스로 도시를 선택하세요")

deck = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v10',
    initial_view_state=pdk.ViewState(latitude=20, longitude=0, zoom=0, pitch=30),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200000,
            pickable=True
        )
    ],
    tooltip={"text": "{city}"}
)

st.pydeck_chart(deck)

# --- 도시 선택 ---
city = st.selectbox("여행할 도시를 선택하세요:", list(destinations.keys()))

if city:
    data = destinations[city]
    st.subheader(f"{city} 여행 시작!")
    st.image(data["이미지"], use_container_width=True)

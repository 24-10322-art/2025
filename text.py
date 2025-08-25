import streamlit as st
import pydeck as pdk

# 도시 데이터
cities = [
    {
        "name": "London",
        "lat": 51.5074,
        "lon": -0.1278,
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/cd/London_Montage_L.jpg",
        "desc": "런던은 영국의 수도로, 버킹엄 궁전, 빅벤, 런던 아이 등으로 유명합니다."
    },
    {
        "name": "Tokyo",
        "lat": 35.6895,
        "lon": 139.6917,
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Tokyo_Skyline_Roppongi_Hills.jpg",
        "desc": "도쿄는 일본의 수도로, 첨단 기술과 전통 문화가 공존하는 도시입니다."
    },
    {
        "name": "Paris",
        "lat": 48.8566,
        "lon": 2.3522,
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Paris_as_seen_from_the_Tour_Saint-Jacques_2011_03.jpg",
        "desc": "파리는 프랑스의 수도이자 패션, 예술, 미식의 중심지입니다."
    },
    {
        "name": "New York",
        "lat": 40.7128,
        "lon": -74.0060,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Lower_Manhattan_from_Jersey_City_November_2014_panorama_3.jpg",
        "desc": "뉴욕은 미국 최대의 도시로, 자유의 여신상과 타임스퀘어가 유명합니다."
    },
]

# 사이드바에서 도시 선택
st.title("가상 세계 여행 시뮬레이터")
selected_city = st.sidebar.radio("여행할 도시를 선택하세요", [c["name"] for c in cities])

city = next((c for c in cities if c["name"] == selected_city), None)

# 지구본 마커 시각화
layer = pdk.Layer(
    "ScatterplotLayer",
    data=[{"position": [c["lon"], c["lat"]], "name": c["name"]} for c in cities],
    get_position="position",
    get_radius=200000,
    get_fill_color=[255, 0, 0],
    pickable=True,
)

view_state = pdk.ViewState(latitude=20, longitude=0, zoom=0.8, pitch=0)
r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"})

st.pydeck_chart(r, use_container_width=True)

# 선택한 도시 정보 표시
if city:
    st.subheader(f"📍 {city['name']}")
    st.image(city["image"], caption=city["name"], use_container_width=True)
    st.write(city["desc"])

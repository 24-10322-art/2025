import streamlit as st
import pydeck as pdk
import time

# 도시 데이터
cities = [
    {
        "name": "London",
        "lat": 51.5074,
        "lon": -0.1278,
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d6/London_Skyline_%28cropped%29.jpg",
        "desc": "런던은 영국의 수도로, 역사와 현대가 공존하는 도시이며 세계적인 금융과 문화 중심지입니다."
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

st.set_page_config(layout="wide")
st.title("가상 세계 여행 시뮬레이터")

# 도시 선택
selected_city = st.sidebar.radio("여행할 도시를 선택하세요", ["전체 보기"] + [c["name"] for c in cities])

# 데이터 준비
layer = pdk.Layer(
    "ScatterplotLayer",
    data=[{"position": [c["lon"], c["lat"]], "name": c["name"]} for c in cities],
    get_position="position",
    get_radius=200000,
    get_fill_color=[255, 0, 100],
    pickable=True,
)

if selected_city == "전체 보기":
    # 초기 회전 애니메이션 (단순 구현: 위도 고정, 경도만 변화)
    for lon in range(-180, 181, 30):
        view_state = pdk.ViewState(latitude=20, longitude=lon, zoom=0.8, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"})
        st.pydeck_chart(r, use_container_width=True)
        time.sleep(0.1)
else:
    # 선택된 도시로 줌인
    city = next((c for c in cities if c["name"] == selected_city), None)
    if city:
        view_state = pdk.ViewState(latitude=city["lat"], longitude=city["lon"], zoom=6, pitch=45)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"})
        st.pydeck_chart(r, use_container_width=True)
        st.subheader(f"📍 {city['name']}")
        st.image(city["image"], caption=city["name"], use_container_width=True)
        st.write(city["desc"])

import streamlit as st
import random
import pandas as pd

# --- 데이터 정의 ---
destinations = {
    "파리": {
        "국가": "프랑스",
        "명소": ["에펠탑", "루브르 박물관", "노트르담 대성당"],
        "음식": ["크루아상", "에스카르고", "마카롱"],
        "날씨": ["맑음", "비", "흐림"],
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg",
        "위도": 48.8566,
        "경도": 2.3522
    },
    "도쿄": {
        "국가": "일본",
        "명소": ["도쿄 타워", "센소지", "시부야 교차로"],
        "음식": ["스시", "라멘", "타코야끼"],
        "날씨": ["맑음", "비", "눈"],
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/1/11/Tokyo_Tower_and_around_Skyscrapers.jpg",
        "위도": 35.6762,
        "경도": 139.6503
    },
    "뉴욕": {
        "국가": "미국",
        "명소": ["자유의 여신상", "타임스 스퀘어", "센트럴 파크"],
        "음식": ["핫도그", "피자", "베이글"],
        "날씨": ["맑음", "비", "눈"],
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Lower_Manhattan_from_Jersey_City_November_2014_panorama_3.jpg",
        "위도": 40.7128,
        "경도": -74.0060
    },
    "런던": {
        "국가": "영국",
        "명소": ["빅벤", "타워 브리지", "버킹엄 궁전"],
        "음식": ["피쉬 앤 칩스", "애프터눈 티", "요크셔 푸딩"],
        "날씨": ["맑음", "비", "흐림", "안개"],
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/c/cd/London_Montage_L.jpg",
        "위도": 51.5074,
        "경도": -0.1278
    }
}

# --- 앱 UI ---
st.title("🌏 가상 세계 여행 시뮬레이터")

# 도시 선택
city = st.selectbox("여행할 도시를 선택하세요:", list(destinations.keys()))

if city:
    data = destinations[city]
    
    st.subheader(f"여행 도시: {city}, 국가: {data['국가']}")
    
    # 이미지 표시 (최신 문법: use_container_width)
    st.image(data["이미지"], caption=city, use_container_width=True)
    
    # 랜덤 날씨
    weather = random.choice(data["날씨"])
    st.write(f"오늘의 날씨: **{weather}**")
    
    # 랜덤 명소
    attraction = random.choice(data["명소"])
    st.write(f"추천 명소: **{attraction}**")
    
    # 랜덤 음식
    food = random.choice(data["음식"])
    st.write(f"추천 음식: **{food}**")
    
    # 랜덤 이벤트
    events = [
        "현지인과 사진 찍기 성공!",
        "기념품 가게에서 할인 받음!",
        "갑작스러운 소나기! 우산 준비 필수",
        "길을 잘못 들어 새로운 골목 발견"
    ]
    event = random.choice(events)
    st.info(f"오늘의 이벤트: {event}")
    
    # 지도 표시
    st.subheader("📍 여행 위치")
    st.map(pd.DataFrame({
        'lat': [data["위도"]],
        'lon': [data["경도"]]
    }, columns=['lat', 'lon']))

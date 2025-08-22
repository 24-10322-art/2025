import streamlit as st

st.set_page_config(page_title="상황별 음악 추천", page_icon="🎶", layout="wide")

st.title("🎧 상황별 음악 추천 웹앱")
st.write("오늘 당신이 겪은 상황에 딱 맞는 음악을 추천해드릴게요! 🏫🍔📚🌧️🏃")

# 상황별 옵션
situations = [
    "🏫 학교 선생님한테 혼났을 때",
    "🍔 야식이 너무 땡길 때",
    "📚 시험공부 해야 하는데 집중이 안 될 때",
    "🏃 운동할 때 텐션 올리고 싶을 때",
    "🌧️ 비 오는 날 혼자 걸을 때"
]
choice = st.selectbox("👉 지금 상황에 가장 가까운 걸 골라주세요", situations)

# 상황별 음악 추천 (곡명, 링크, 앨범이미지)
music_dict = {
    "🏫 학교 선생님한테 혼났을 때": [
        ("Linkin Park - Numb", "https://www.youtube.com/watch?v=kXYiU_JCYtU",
         "https://upload.wikimedia.org/wikipedia/en/6/64/Linkin_Park_-_Numb_CD_cover.jpg"),
        ("Eminem - Not Afraid", "https://www.youtube.com/watch?v=j5-yKhDd64s",
         "https://upload.wikimedia.org/wikipedia/en/9/92/Eminem_-_Not_Afraid.jpg"),
        ("Green Day - Boulevard of Broken Dreams", "https://www.youtube.com/watch?v=Soa3gO7tL-c",
         "https://upload.wikimedia.org/wikipedia/en/f/f3/Green_Day_-_Boulevard_of_Broken_Dreams_cover.jpg")
    ],
    "🍔 야식이 너무 땡길 때": [
        ("Bruno Mars - Treasure", "https://www.youtube.com/watch?v=nPvuNsRccVw",
         "https://upload.wikimedia.org/wikipedia/en/1/18/Bruno_Mars_-_Treasure.png"),
        ("Maroon 5 - Sugar", "https://www.youtube.com/watch?v=09R8_2nJtjg",
         "https://upload.wikimedia.org/wikipedia/en/0/0e/Maroon_5_Sugar_cover.png"),
        ("TWICE - What is Love?", "https://www.youtube.com/watch?v=i0p1bmr0EmE",
         "https://upload.wikimedia.org/wikipedia/en/7/7d/Twice_-_What_Is_Love.png")
    ],
    "📚 시험공부 해야 하는데 집중이 안 될 때": [
        ("Lo-Fi Beats - Study Session", "https://www.youtube.com/watch?v=jfKfPfyJRdk",
         "https://lofigirl.com/wp-content/uploads/2020/06/lofi-study-girl.jpg"),
        ("Chillhop Essentials", "https://www.youtube.com/watch?v=5yx6BWlEVcY",
         "https://chillhop.com/wp-content/uploads/2020/09/chillhop-fall-essentials.jpg"),
        ("Rainy Jazz for Study", "https://www.youtube.com/watch?v=Dx5qFachd3A",
         "https://i.scdn.co/image/ab67616d0000b27389409d857ae11404be53d9c3")
    ],
    "🏃 운동할 때 텐션 올리고 싶을 때": [
        ("Survivor - Eye of the Tiger", "https://www.youtube.com/watch?v=btPJPFnesV4",
         "https://upload.wikimedia.org/wikipedia/en/3/39/Eye_of_the_Tiger_Single.jpg"),
        ("Eminem - Lose Yourself", "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
         "https://upload.wikimedia.org/wikipedia/en/8/8f/Lose_Yourself.jpg"),
        ("Kanye West - Stronger", "https://www.youtube.com/watch?v=PsO6ZnUZI0g",
         "https://upload.wikimedia.org/wikipedia/en/7/70/Stronger_Kanye_West.jpg")
    ],
    "🌧️ 비 오는 날 혼자 걸을 때": [
        ("Coldplay - The Scientist", "https://www.youtube.com/watch?v=RB-RcX5DS5A",
         "https://upload.wikimedia.org/wikipedia/en/b/bf/Coldplay_-_The_Scientist.png"),
        ("Radiohead - Creep", "https://www.youtube.com/watch?v=XFkzRNyygfk",
         "https://upload.wikimedia.org/wikipedia/en/0/02/Radioheadcreep.png"),
        ("Taeyeon - Rain", "https://www.youtube.com/watch?v=tF27TNC_4pc",
         "https://upload.wikimedia.org/wikipedia/en/0/0a/Taeyeon_Rain_single_cover.jpg")
    ]
}

# 선택된 상황에 맞는 음악 출력
if choice:
    st.subheader(f"{choice} 🎶 이런 음악 어때요?")
    cols = st.columns(3)  # 3열 정렬
    for idx, (title, link, img) in enumerate(music_dict[choice]):
        with cols[idx % 3]:
            st.image(img, use_column_width=True)
            st.markdown(f"**[{title}]({link})**")

# 배경 스타일
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #f9d423, #ff4e50);
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

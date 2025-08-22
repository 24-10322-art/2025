import streamlit as st

# 제목
st.title("🎵 기분별 음악 추천 웹앱")
st.write("당신의 기분에 맞는 음악을 추천해드릴게요! 😆🥲😡😴")

# 기분 옵션
moods = ["😊 행복해요", "🥲 슬퍼요", "😡 화나요", "😴 피곤해요", "🤔 집중하고 싶어요"]
choice = st.selectbox("현재 기분을 선택해주세요 👇", moods)

# 기분별 음악 추천 딕셔너리
music_dict = {
    "😊 행복해요": [
        ("Pharrell Williams - Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Justin Timberlake - Can't Stop The Feeling", "https://www.youtube.com/watch?v=ru0K8uYEZWw")
    ],
    "🥲 슬퍼요": [
        ("Adele - Someone Like You", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Sam Smith - Too Good at Goodbyes", "https://www.youtube.com/watch?v=J_ub7Etch2U")
    ],
    "😡 화나요": [
        ("Linkin Park - Numb", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
        ("Eminem - Lose Yourself", "https://www.youtube.com/watch?v=_Yhyp-_hX2s")
    ],
    "😴 피곤해요": [
        ("Coldplay - Fix You", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("Lauv - I Like Me Better", "https://www.youtube.com/watch?v=BcqxLCWn-CE")
    ],
    "🤔 집중하고 싶어요": [
        ("Lo-Fi Beats - Study/Work", "https://www.youtube.com/watch?v=jfKfPfyJRdk"),
        ("Chillhop Music - Relax/Focus", "https://www.youtube.com/watch?v=5yx6BWlEVcY")
    ]
}

# 선택된 기분의 음악 출력
if choice:
    st.subheader(f"{choice} 기분에 추천하는 음악 🎧")
    for title, link in music_dict[choice]:
        st.markdown(f"- [{title}]({link})")

# 배경 꾸미기
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(to right, #fbc2eb, #a6c1ee);
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


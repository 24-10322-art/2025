import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(
    page_title="오늘의 기분, 음악으로 채워줄게요!",
    page_icon="🎶",
    layout="centered"
)

# --- Session State 초기화 (앱의 상태를 기억하기 위함) ---
if 'survey_completed' not in st.session_state:
    st.session_state.survey_completed = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
# 설문 답변을 저장할 딕셔너리 초기화
if 'mood_answers' not in st.session_state:
    st.session_state.mood_answers = {}
# 최종 기분 점수 및 분류 초기화
if 'mood_score' not in st.session_state:
    st.session_state.mood_score = 0
if 'identified_mood' not in st.session_state:
    st.session_state.identified_mood = ""

# --- 음악 추천 로직 (감정 분류 및 추천) ---
# 이 부분은 나중에 더 정교하게 다듬을 수 있어요!
def get_music_recommendation(mood_score):
    if mood_score >= 8:
        mood_label = "최고의 활기찬 기분"
        music_info = {
            "mood": "활기찬",
            "desc": "하늘을 날아갈 듯한 최고의 활기찬 기분이시네요! 이 에너지를 음악과 함께 더욱 빛내보세요!",
            "tracks": [
                {"title": "Happy", "artist": "Pharrell Williams", "youtube_link": "https://www.youtube.com/watch?v=y6Sxv-sUYtM"},
                {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "youtube_link": "https://www.youtube.com/watch?v=OPf0cE4Xk04"},
                {"title": "Dynamite", "artist": "BTS", "youtube_link": "https://www.youtube.com/watch?v=gdZLi9oWNZg"}
            ]
        }
    elif mood_score >= 4:
        mood_label = "긍정적이고 활기찬 기분"
        music_info = {
            "mood": "긍정적",
            "desc": "기분 좋고 활기찬 하루를 보내고 계시군요! 긍정적인 에너지를 유지할 수 있는 음악을 추천해 드려요.",
            "tracks": [
                {"title": "Good Day", "artist": "IU", "youtube_link": "https://www.youtube.com/watch?v=jeWd71N-d_U"},
                {"title": "Walking On Sunshine", "artist": "Katrina & The Waves", "youtube_link": "https://www.youtube.com/watch?v=iPix7oE2-T8"},
                {"title": "Feel Special", "artist": "TWICE", "youtube_link": "https://www.youtube.com/watch?v=3ymwXLvyiHw"}
            ]
        }
    elif mood_score >= 0:
        mood_label = "차분하거나 평온한 기분"
        music_info = {
            "mood": "차분한",
            "desc": "복잡하지 않고 차분한 마음 상태이시군요. 편안하게 휴식을 취하거나 집중할 수 있는 음악이 필요하실 것 같아요.",
            "tracks": [
                {"title": "고민보다 GO", "artist": "방탄소년단", "youtube_link": "https://www.youtube.com/watch?v=d_ZfB6jWvXo"}, # 평온하거나 휴식을 위할 때 듣는 곡으로 변경 필요
                {"title": "River Flows in You", "artist": "Yiruma", "youtube_link": "https://www.youtube.com/watch?v=7M7b0eYf06c"},
                {"title": "Clair de Lune", "artist": "Claude Debussy", "youtube_link": "https://www.youtube.com/watch?v=EAJdCgU6D0I"}
            ]
        }
    elif mood_score >= -4:
        mood_label = "조금 지치거나 답답한 기분"
        music_info = {
            "mood": "위로",
            "desc": "조금 지치고 답답한 기분이시군요. 따뜻한 위로가 필요할 때 들으면 좋은 음악들을 준비했어요.",
            "tracks": [
                {"title": "지친 하루", "artist": "윤종신 (with 곽진언, 김필)", "youtube_link": "https://www.youtube.com/watch?v=84vS34kGk5c"},
                {"title": "Fix You", "artist": "Coldplay", "youtube_link": "https://www.youtube.com/watch?v=k4Dnt6nB7bY"},
                {"title": "숨", "artist": "박효신", "youtube_link": "https://www.youtube.com/watch?v=J32V42oH79k"}
            ]
        }
    else: # mood_score < -4
        mood_label = "매우 우울하거나 힘든 기분"
        music_info = {
            "mood": "공감",
            "desc": "지금 많이 힘든 기분이시군요... 괜찮아요. 혼자가 아니에요. 이 음악들이 작은 위안이 되기를 바라요.",
            "tracks": [
                {"title": "Into the Unknown", "artist": "Idina Menzel, Aurora", "youtube_link": "https://www.youtube.com/watch?v=nrD7yE6yLzY"},
                {"title": "Mad World", "artist": "Gary Jules", "youtube_link": "https://www.youtube.com/watch?v=4N3N1MlmPLw"},
                {"title": "고백", "artist": "Melomance", "youtube_link": "https://www.youtube.com/watch?v=eEaYs-S_YFw"}
            ]
        }
    
    st.session_state.identified_mood = mood_label
    return music_info

# --- 웹앱의 기본 타이틀 ---
st.title("🎶 AI 기반 오늘의 기분 맞춤형 음악 추천")
st.markdown("---")

# --------------------------------------------------------------------------------
# 앱의 실제 화면 구성 시작
# --------------------------------------------------------------------------------

# 설문이 완료되지 않았을 때 (초기 화면 및 설문)
if not st.session_state.survey_completed:
    st.header("📝 당신의 이름을 알려주세요! 😊")
    user_name_input = st.text_input("이름을 입력해주세요:", placeholder="예: 윤서경", key="mood_survey_name_input")
    st.session_state.user_name = user_name_input if user_name_input else "사용자"
    
    st.write(f"안녕하세요, **{st.session_state.user_name}님!** ✨")
    st.write("오늘 기분이 어떠신가요? 10가지 질문에 답하고, 기분에 딱 맞는 음악을 추천받으세요!")
    st.markdown("---")

    st.header("1️⃣ 오늘의 기분 설문")
    st.write("솔직하게 답해주세요. 뇌과학 기반 AI가 {name}님을 위한 음악을 찾아낼 거예요!".format(name=st.session_state.user_name))

    # 설문 질문과 점수 매핑 (dictionary for options and scores)
    questions = [
        {"q": "1. 전반적인 기분은 어떠신가요?",
         "options": {"매우 좋음 😊": 2, "좋음 🙂": 1, "보통 😐": 0, "조금 안 좋음 🙁": -1, "매우 안 좋음 😔": -2}},
        {"q": "2. 현재 활력이 넘치나요, 아니면 피곤한가요?",
         "options": {"활력이 넘쳐요! 💪": 2, "적당히 힘이 있어요.": 1, "그저 그래요.": 0, "좀 피곤해요. 😩": -1, "많이 지쳤어요. 😴": -2}},
        {"q": "3. 마음이 차분하신가요, 아니면 조금 들떠 있으신가요?",
         "options": {"매우 차분해요. 🧘‍♀️": -1, "차분한 편이에요.": -0.5, "보통이에요.": 0, "조금 들떠 있어요.": 0.5, "매우 들떠 있어요! 🎉": 1}},
        {"q": "4. 무언가에 집중하고 싶은 마음이 있나요?",
         "options": {"네, 매우 집중하고 싶어요. 🤓": 1, "어느 정도요.": 0.5, "별로요.": 0, "아니요, 산만해요.": -0.5}},
        {"q": "5. 요즘 스트레스를 얼마나 받고 있다고 느끼시나요?",
         "options": {"매우 높음 😫": -2, "높음": -1, "보통": 0, "낮음": 1, "전혀 없음 😊": 2}},
        {"q": "6. 세상 모든 것이 아름답게 보이나요, 아니면 회색빛인가요?",
         "options": {"세상이 아름다워요! ✨": 2, "긍정적인 편이에요.": 1, "그냥 그래요.": 0, "조금 부정적이에요.": -1, "세상이 회색빛이에요. 🌫️": -2}},
        {"q": "7. 오늘 새로운 것에 도전하고 싶은 마음이 드나요?",
         "options": {"네, 매우 도전적이에요! 🚀": 1, "조금 흥미가 있어요.": 0.5, "별로요.": 0, "아니요, 쉬고 싶어요. 🛋️": -0.5}},
        {"q": "8. 몸은 가벼운가요, 아니면 무겁게 느껴지나요?",
         "options": {"매우 가벼워요! 🤸‍♂️": 1, "가벼운 편이에요.": 0.5, "보통이에요.": 0, "조금 무거워요.": -0.5, "매우 무거워요. 😴": -1}},
        {"q": "9. 주변 환경이 평화롭게 느껴지나요, 아니면 소란스럽게 느껴지나요?",
         "options": {"매우 평화로워요. 😌": 1, "평화로운 편이에요.": 0.5, "그저 그래요.": 0, "조금 소란스러워요.": -0.5, "매우 소란스러워요. 😡": -1}},
        {"q": "10. 지금 당장 하고 싶은 일은 무엇인가요?",
         "options": {"활기찬 활동 (운동, 외출 등)": 1, "생산적인 활동 (공부, 일 등)": 0.5, "편안한 휴식 (영화, 독서 등)": -0.5, "아무것도 안 하고 싶어요. 😑": -1}}
    ]

    # 사용자 답변을 저장할 딕셔너리
    st.session_state.mood_answers = {}
    
    # 각 질문 표시 및 답변 받기
    for i, q_data in enumerate(questions):
        # 라디오 버튼의 옵션 순서 유지 (dictionary는 순서가 보장되지 않을 수 있으므로)
        options_list = list(q_data["options"].keys())
        selected_option = st.radio(q_data["q"], options_list, key=f"q_{i}")
        st.session_state.mood_answers[f"q_{i}"] = q_data["options"][selected_option]
        st.markdown("---") # 질문 사이에 구분선 추가

    if st.button("내 기분 분석하고 음악 추천받기! 🎶", key="submit_mood_survey"):
        if not st.session_state.user_name:
            st.error("앗! 먼저 이름을 입력해 주세요! 😊")
        else:
            # 모든 질문의 점수를 합산
            st.session_state.mood_score = sum(st.session_state.mood_answers.values())
            
            # 설문 완료 상태로 변경하고 페이지 새로고침
            st.session_state.survey_completed = True
            st.rerun()

# 설문이 완료되었을 때 (결과 화면)
else:
    display_user_name = st.session_state.user_name if st.session_state.user_name else "사용자"

    st.header(f"2️⃣ {display_user_name}님의 기분 분석 결과 🧠")
    st.write("뇌과학 AI가 분석한 {name}님의 기분과 맞춤형 음악 추천입니다!".format(name=display_user_name))
    st.markdown("---")

    music_recommendation = get_music_recommendation(st.session_state.mood_score)

    st.subheader(f"✨ 오늘의 기분: {st.session_state.identified_mood}")
    st.write(music_recommendation["desc"])
    
    st.markdown("---")
    st.subheader("🎵 추천 음악 리스트")
    for track in music_recommendation["tracks"]:
        st.write(f"**{track['title']}** - {track['artist']}")
        st.markdown(f"[Youtube에서 듣기]({track['youtube_link']})") # 링크로 제공
        st.markdown("---")

    st.markdown("---")
    st.header("3️⃣ 뇌과학적 원리: 음악이 기분에 미치는 영향 뇌 활동 변화 🔬")
    st.write(
        "음악은 단순히 소리의 조합이 아니라, 우리 뇌의 다양한 영역에 직접적으로 영향을 미쳐 감정을 조절하고, "
        "기억을 활성화하며, 심지어 신체 반응까지 변화시킬 수 있는 강력한 도구랍니다."
    )
    
    if st.session_state.identified_mood == "최고의 활기찬 기분" or st.session_state.identified_mood == "긍정적이고 활기찬 기분":
        st.info(
            "이런 활기찬 음악은 뇌의 **도파민 보상 시스템**을 활성화시켜 즐거움과 만족감을 높여줍니다. "
            "또한, **청각 피질**과 연결된 **운동 피질**도 자극하여 신체 활동을 촉진하고 에너지를 증진시키는 데 도움을 줍니다. "
            "빠른 템포와 밝은 멜로디는 **뇌의 베타파**를 증가시켜 집중력과 각성 상태를 유지하는 데도 기여할 수 있어요."
        )
    elif st.session_state.identified_mood == "차분하거나 평온한 기분":
        st.info(
            "차분한 음악은 **뇌의 전전두피질** 활동을 도와 감정 조절 능력을 향상시키고, **알파파** 생성을 촉진하여 "
            "마음을 안정시키고 스트레스를 줄이는 데 효과적입니다. "
            "부교감 신경계를 활성화하여 심박수와 혈압을 낮추는 등 신체적 이완에도 도움을 줍니다."
        )
    elif st.session_state.identified_mood == "조금 지치거나 답답한 기분" or st.session_state.identified_mood == "매우 우울하거나 힘든 기분":
        st.info(
            "이러한 위로와 공감의 음악은 뇌의 **변연계**와 **전전두피질**을 자극하여 감정적인 처리와 회복을 돕습니다. "
            "슬픈 음악이 오히려 마음을 편안하게 하는 '카타르시스' 효과는 **옥시토신**과 같은 호르몬 분비와도 관련이 있어요. "
            "또한, 공감을 유발하는 가사는 **사회적 뇌 영역**을 활성화하여 고립감을 줄이는 데 도움을 줄 수 있습니다."
        )
    
    st.markdown("---")
    # 다시 설문하기 버튼 추가 (결과를 본 후 다시 처음으로 돌아가고 싶을 때)
    if st.button("다시 기분 분석하기"):
        st.session_state.survey_completed = False # 설문 완료 상태를 False로 되돌리고
        st.session_state.mood_answers = {} # 답변 초기화
        st.session_state.mood_score = 0 # 점수 초기화
        st.session_state.identified_mood = "" # 기분 초기화
        st.rerun()

st.markdown("---")
st.write(f"**{st.session_state.user_name}님**의 탐구 정신과 감성에 박수를 보냅니다! 웹앱 개발도 분명 잘 해내실 거예요! 화이팅! 💪😊")

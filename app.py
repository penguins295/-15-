import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="환영 앱",
    page_icon="🎆",
    layout="wide"
)

# 스타일 설정: 형광 노란색 배경, 중앙 배치, 버튼 색상 분리
st.markdown(
    """
    <style>
    /* 전체 배경 형광 노란색 */
    .stApp {
        background-color: #CCFF00;
    }

    /* 화면 세로/가로 중앙 정렬 */
    .block-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 85vh;
    }

    /* 환영합니다 문구: 중앙 초대형 빨간 글씨 */
    .welcome-title {
        color: #FF0000 !important;
        font-size: 5.5rem;
        font-weight: 900;
        text-align: center;
        margin-top: 2rem;
        line-height: 1.2;
        word-break: keep-all;
    }

    /* 버튼 컨테이너 중앙 정렬 */
    div.stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* 버튼 디자인: 배경과 확실히 구분되는 검정 배경 + 흰색/형광노랑 글씨 */
    div.stButton > button {
        background-color: #111111 !important;
        border: 4px solid #FF0000 !important;
        border-radius: 16px;
        padding: 1rem 3.5rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
        transition: transform 0.15s ease;
    }

    /* 버튼 내부 텍스트 색상 및 크기 강제 지정 */
    div.stButton > button p {
        color: #FFFFFF !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
    }

    div.stButton > button:hover {
        background-color: #FF0000 !important;
        border-color: #111111 !important;
        transform: scale(1.05);
    }

    /* 불꽃놀이 캔버스가 전체 화면을 덮도록 설정 */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        pointer-events: none !important;
        z-index: 9999 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 버튼만 먼저 중앙에 표시
clicked = st.button("들어가기")

# 버튼을 눌렀을 때만 '환영합니다!' 표시 + 불꽃놀이 폭죽 실행
if clicked:
    st.markdown('<div class="welcome-title">환영합니다!</div>', unsafe_allow_html=True)

    # 실제 불꽃놀이 효과 (canvas-confetti) 및 음성 출력
    components.html(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
        <script>
        // 브라우저 음성 출력 ("환영합니다!")
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();

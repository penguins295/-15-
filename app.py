import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="환영 앱",
    page_icon="🎉",
    layout="centered"
)

# 형광 노란색 배경 및 빨간색 글씨 커스텀 CSS 적용
st.markdown(
    """
    <style>
    /* 전체 앱 배경을 형광 노란색(#CCFF00)으로 설정 */
    .stApp {
        background-color: #CCFF00;
    }

    /* 모든 텍스트 색상을 빨간색으로 강제 적용 */
    h1, h2, h3, p, span, div {
        color: #FF0000 !important;
    }

    /* 버튼 스타일 커스텀 */
    div.stButton > button {
        background-color: #FF0000 !important;
        color: #CCFF00 !important;
        font-weight: bold;
        border: 2px solid #FF0000 !important;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-size: 1.1rem;
    }

    div.stButton > button:hover {
        background-color: #CC0000 !important;
        border-color: #CC0000 !important;
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 메인 타이틀
st.markdown("<h1>웹앱 방문을 환영합니다</h1>", unsafe_allow_html=True)
st.markdown("<p>아래 버튼을 눌러보세요!</p>", unsafe_allow_html=True)

# '들어가기' 버튼 클릭 처리
if st.button("들어가기"):
    # 폭죽 효과 실행
    st.balloons()
    
    # 환영 문구 출력
    st.markdown("<h2>환영합니다!</h2>", unsafe_allow_html=True)

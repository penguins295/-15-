import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="환영 앱", page_icon="🎆", layout="wide")

css_code = (
    "<style>"
    ".stApp { background-color: #CCFF00; }"
    ".block-container { display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 85vh; }"
    ".welcome-title { color: #FF0000 !important; font-size: 5.5rem; font-weight: 900; text-align: center; margin-top: 2rem; line-height: 1.2; word-break: keep-all; }"
    "div.stButton { display: flex; justify-content: center; width: 100%; }"
    "div.stButton > button { background-color: #111111 !important; border: 4px solid #FF0000 !important; border-radius: 16px; padding: 1rem 3.5rem; box-shadow: 0 8px 20px rgba(0,0,0,0.25); }"
    "div.stButton > button p { color: #FFFFFF !important; font-size: 2rem !important; font-weight: 800 !important; margin: 0 !important; }"
    "div.stButton > button:hover { background-color: #FF0000 !important; border-color: #111111 !important; transform: scale(1.05); }"
    "iframe { position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; pointer-events: none !important; z-index: 9999 !important; }"
    "</style>"
)

st.markdown(css_code, unsafe_allow_html=True)

if st.button("들어가기"):
    st.markdown('<div class="welcome-title">환영합니다!</div>', unsafe_allow_html=True)

    js_code = (
        '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>'
        "<script>"
        "if ('speechSynthesis' in window) {"
        "  window.speechSynthesis.cancel();"
        '  const msg = new SpeechSynthesisUtterance("환영합니다!");'
        '  msg.lang = "ko-KR";'
        "  window.speechSynthesis.speak(msg);"
        "}"
        "const duration = 4000;"
        "const animationEnd = Date.now() + duration;"
        "const defaults = { startVelocity: 35, spread: 360, ticks: 70, zIndex: 9999 };"
        "const interval = setInterval(function() {"
        "  const timeLeft = animationEnd - Date.now();"
        "  if (timeLeft <= 0) { return clearInterval(interval); }"
        "  const particleCount = 70 * (timeLeft / duration);"
        "  confetti(Object.assign({}, defaults, { particleCount, origin: { x: Math.random() * 0.3 + 0.1, y: Math.random() - 0.2 } }));"
        "  confetti(Object.assign({}, defaults, { particleCount, origin: { x: Math.random() * 0.3 + 0.6, y: Math.random() - 0.2 } }));"
        "}, 250);"
        "</script>"
    )
    components.html(js_code, height=0, width=0)

import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임", page_icon="✌️", layout="centered")

css_code = (
    "<style>"
    ".title-text { font-size: 3.5rem; font-weight: 900; text-align: center; margin-bottom: 2rem; }"
    ".result-box { font-size: 2rem; font-weight: 800; text-align: center; margin-top: 2.5rem; padding: 2rem; border-radius: 16px; background-color: #f0f2f6; color: #111111; line-height: 1.6; }"
    "div.stButton > button { width: 100%; height: 5rem; border-radius: 12px; border: 3px solid #111111 !important; background-color: #111111 !important; }"
    "div.stButton > button p { color: #FFFFFF !important; font-size: 1.8rem !important; font-weight: 800 !important; margin: 0 !important; }"
    "div.stButton > button:hover { background-color: #FF0000 !important; border-color: #FF0000 !important; }"
    "</style>"
)
st.markdown(css_code, unsafe_allow_html=True)

st.markdown('<div class="title-text">가위 바위 보!</div>', unsafe_allow_html=True)

choices = ["가위", "바위", "보"]
user_choice = None

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️ 가위"):
        user_choice = "가위"
with col2:
    if st.button("✊ 바위"):
        user_choice = "바위"
with col3:
    if st.button("🖐️ 보"):
        user_choice = "보"

if user_choice:
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        outcome = "비겼습니다."
    elif (
        (user_choice == "가위" and comp_choice == "보")
        or (user_choice == "바위" and comp_choice == "가위")
        or (user_choice == "보" and comp_choice == "바위")
    ):
        outcome = "당신이 이겼습니다!"
    else:
        outcome = "당신이 졌습니다."

    result_html = (
        f'<div class="result-box">'
        f"컴퓨터는 <b>{comp_choice}</b>를 골랐습니다.<br>"
        f'<span style="color: #FF0000; font-size: 2.8rem;">{outcome}</span>'
        f"</div>"
    )
    st.markdown(result_html, unsafe_allow_html=True)

"""
Сайт-візитка "Механічна Інженерія" — Python/Streamlit-версія.

Та сама структура, що й у index.html (hero, про мене, послуги, інструменти,
проєкти, процес, контакти), але побудована на ідіоматичному Streamlit
замість статичного HTML/CSS/JS. Дані винесені в content.py.
"""

from datetime import date
from pathlib import Path

import streamlit as st

import content

APP_DIR = Path(__file__).parent


def load_css(path: str) -> None:
    """Читає файл стилів і вставляє його в сторінку."""
    with open(APP_DIR / path, encoding="utf-8") as f:
        st.html(f"<style>{f.read()}</style>")


st.set_page_config(
    page_title=content.NAME,
    page_icon="⚙️",
    layout="wide",
)

load_css("streamlit_style.css")


# --- Hero -------------------------------------------------------------
st.markdown(f"<p class='eyebrow'>{content.TAGLINE}</p>", unsafe_allow_html=True)
st.title(content.NAME, anchor=False)
st.write(content.HERO_LEAD)

cols = st.columns(len(content.STATS))
for col, (number, label) in zip(cols, content.STATS):
    with col:
        st.markdown(
            f"<div style='font-size:1.6rem;font-weight:800;color:#1d5fe0'>{number}</div>"
            f"<div style='color:#5b6b85;font-size:0.85rem'>{label}</div>",
            unsafe_allow_html=True,
        )

st.divider()


# --- Про мене -----------------------------------------------------------
st.header("Про мене", anchor=False)
st.write(content.ABOUT_TEXT)

for point in content.ABOUT_POINTS:
    st.markdown(
        f"<div style='border-left:3px solid #1d5fe0;background:#f3f6fb;"
        f"padding:10px 14px;margin-bottom:8px;border-radius:8px'>{point}</div>",
        unsafe_allow_html=True,
    )

st.divider()


# --- Послуги ------------------------------------------------------------
st.header("Послуги", anchor=False)

for row_start in range(0, len(content.SERVICES), 3):
    row = content.SERVICES[row_start : row_start + 3]
    cols = st.columns(3)
    for col, (icon, title, text) in zip(cols, row):
        with col:
            with st.container(border=True):
                st.markdown(f"### {icon}")
                st.markdown(f"**{title}**")
                st.write(text)

st.divider()


# --- Інструменти ----------------------------------------------------------
st.header("Інструменти", anchor=False)
st.markdown(
    "".join(f"<span class='pill'>{skill}</span>" for skill in content.SKILLS),
    unsafe_allow_html=True,
)

st.divider()


# --- Проєкти ------------------------------------------------------------
st.header("Проєкти", anchor=False)
st.caption("Демонстраційні приклади для портфоліо — деталі проєктів надаються за запитом.")

for row_start in range(0, len(content.PROJECTS), 2):
    row = content.PROJECTS[row_start : row_start + 2]
    cols = st.columns(2)
    for col, (title, text, tag) in zip(cols, row):
        with col:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.write(text)
                st.markdown(f"<span class='pill'>{tag}</span>", unsafe_allow_html=True)

st.divider()


# --- Процес роботи --------------------------------------------------------
st.header("Як будується співпраця", anchor=False)

for number, title, text in content.PROCESS:
    left, right = st.columns([1, 6])
    with left:
        st.markdown(f"<span class='step-num'>{number}</span>", unsafe_allow_html=True)
    with right:
        st.markdown(f"**{title}**")
        st.write(text)

st.divider()


# --- Контакти -----------------------------------------------------------
st.header("Обговоримо ваш проєкт?", anchor=False)
st.caption("Напишіть кілька слів про задачу — відповім і запропоную наступні кроки.")

form_col, info_col = st.columns([3, 2])

with form_col:
    with st.form("contact_form"):
        st.text_input("Ім'я", placeholder="Як до вас звертатися")
        st.text_input("Email", placeholder="you@example.com")
        st.text_area("Повідомлення", placeholder="Коротко опишіть задачу")
        submitted = st.form_submit_button("Надіслати")
        if submitted:
            st.success("Дякую! Це демонстраційна форма — повідомлення нікуди не надсилається.")

with info_col:
    st.markdown(f"**Email**  \n{content.CONTACT_EMAIL}")
    st.markdown(f"**Телефон**  \n{content.CONTACT_PHONE}")
    st.markdown(f"**Локація**  \n{content.CONTACT_LOCATION}")

st.divider()
st.caption(f"© {date.today().year} {content.NAME}. Всі права захищено. · {content.FOOTER_NOTE}")

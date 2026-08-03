"""
Точка входу застосунку "Механічна Інженерія".
Тут лише налаштування сторінки + навігація. Контент — у views/, тексти — у content.py.
"""

import functools
from pathlib import Path

import streamlit as st

import content
from views.about import show_about
from views.contact import show_contact
from views.gallery import show_gallery
from views.home import show_home
from views.projects import show_projects
from views.services import show_services

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


# --- Сторінки ---------------------------------------------------------
# Домашній сторінці потрібні посилання на інші сторінки (для st.page_link),
# тому її callable отримує вже готові StreamlitPage-об'єкти через functools.partial.
page_about = st.Page(show_about, title="Про мене", url_path="about", icon=":material/person:")
page_services = st.Page(show_services, title="Послуги", url_path="services", icon=":material/settings:")
page_gallery = st.Page(show_gallery, title="Галерея", url_path="gallery", icon=":material/photo_library:")
page_projects = st.Page(show_projects, title="Проєкти", url_path="projects", icon=":material/work:")
page_contact = st.Page(show_contact, title="Контакти", url_path="contact", icon=":material/mail:")
page_home = st.Page(
    functools.partial(show_home, page_about, page_services, page_gallery, page_projects, page_contact),
    title="Головна",
    url_path="home",
    icon=":material/home:",
    default=True,
)

pages = st.navigation(
    {
        "": [page_home],
        "Про сайт": [page_about, page_services, page_gallery],
        "Роботи": [page_projects],
        "Зв'язок": [page_contact],
    },
    position="sidebar",
)

pages.run()

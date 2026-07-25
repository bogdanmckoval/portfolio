import streamlit as st

EMAIL = ''
GITHUB_URL = 'https://github.com/bogdanmckoval'


def show_about_page():
    st.title("Богдан Коваль")

    st.subheader("Мої проєкти")

    with st.container(border=True):
        st.subheader("Калькулятор режимів різання")
        st.write(
            "Вебзастосунок для підбору швидкості різання, подачі та частоти "
            "обертання за матеріалом заготовки й типом інструмента."
        )
        st.write("Технології: Python, Streamlit, pandas")

    with st.container(border=True):
        st.subheader("Довідник посадок і допусків")
        st.write(
            "Пошук по системі ISO: за номінальним розміром і полем допуску "
            "видає граничні відхилення та тип посадки."
        )
        st.write("Технології: Python, Streamlit, JSON")

    with st.container(border=True):
        st.subheader("Каталог різального інструменту")
        st.write(
            "База фрез і свердел з фільтрами за діаметром, кількістю зубів "
            "і матеріалом. Дані зберігаються у JSON."
        )
        st.write("Технології: Python, Streamlit, JSON")

    st.subheader("Мої контакти")
    with st.container(border=True):
        st.write(f"Email: {EMAIL}")
        st.write(f"Github: {GITHUB_URL}")

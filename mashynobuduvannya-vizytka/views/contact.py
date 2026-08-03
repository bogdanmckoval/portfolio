import streamlit as st

import content


def show_contact() -> None:
    """Сторінка «Контакти» — форма звʼязку та контактні дані."""

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

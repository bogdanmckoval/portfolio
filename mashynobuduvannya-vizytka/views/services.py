import streamlit as st

import content


def show_services() -> None:
    """Сторінка «Послуги» + інструменти."""

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

    st.header("Інструменти", anchor=False)
    st.markdown(
        "".join(f"<span class='pill'>{skill}</span>" for skill in content.SKILLS),
        unsafe_allow_html=True,
    )

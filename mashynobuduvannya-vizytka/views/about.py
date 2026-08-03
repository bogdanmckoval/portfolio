import streamlit as st

import content


def show_about() -> None:
    """Сторінка «Про мене» + процес роботи."""

    st.header("Про мене", anchor=False)
    st.write(content.ABOUT_TEXT)

    for point in content.ABOUT_POINTS:
        st.markdown(
            f"<div style='border-left:3px solid #1d5fe0;background:#f3f6fb;"
            f"padding:10px 14px;margin-bottom:8px;border-radius:8px'>{point}</div>",
            unsafe_allow_html=True,
        )

    st.divider()

    st.header("Як будується співпраця", anchor=False)
    for number, title, text in content.PROCESS:
        left, right = st.columns([1, 6])
        with left:
            st.markdown(f"<span class='step-num'>{number}</span>", unsafe_allow_html=True)
        with right:
            st.markdown(f"**{title}**")
            st.write(text)

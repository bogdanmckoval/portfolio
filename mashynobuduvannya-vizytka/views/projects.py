import streamlit as st

import content


def show_projects() -> None:
    """Сторінка «Проєкти» — приклади робіт."""

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

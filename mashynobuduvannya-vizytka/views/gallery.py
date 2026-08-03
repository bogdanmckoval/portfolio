import streamlit as st

import content


def show_gallery() -> None:
    """Сторінка «Галерея» — фото на тему машинобудування."""

    st.header("Галерея", anchor=False)
    st.caption("Фото з відкритих джерел (Pexels) — ілюструють тематику розділу.")

    for row_start in range(0, len(content.GALLERY), 3):
        row = content.GALLERY[row_start : row_start + 3]
        cols = st.columns(3)
        for col, (url, caption) in zip(cols, row):
            with col:
                st.image(url, caption=caption, width="stretch")

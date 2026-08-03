import streamlit as st

import content


def show_home(page_about, page_services, page_gallery, page_projects, page_contact) -> None:
    """Головна сторінка: hero + швидкі посилання на решту сайту."""

    st.markdown(f"<p class='eyebrow'>{content.TAGLINE}</p>", unsafe_allow_html=True)
    st.title(content.NAME, anchor=False)
    st.write(content.HERO_LEAD)

    cta_col, ghost_col, _ = st.columns([1, 1, 2])
    with cta_col:
        st.page_link(page_contact, label="Обговорити проєкт", icon=":material/forum:", width="stretch")
    with ghost_col:
        st.page_link(page_projects, label="Дивитись роботи", icon=":material/work:", width="stretch")

    stat_cols = st.columns(len(content.STATS))
    for col, (number, label) in zip(stat_cols, content.STATS):
        with col:
            st.markdown(
                f"<div style='font-size:1.6rem;font-weight:800;color:#1d5fe0'>{number}</div>"
                f"<div style='color:#5b6b85;font-size:0.85rem'>{label}</div>",
                unsafe_allow_html=True,
            )

    st.divider()
    st.header("Розділи сайту", anchor=False)

    quick_links = [
        (page_about, "Чим займаюсь і як підходжу до інженерних задач."),
        (page_services, "3D-моделювання, CAM/CNC, розрахунки, документація."),
        (page_gallery, "Фото з теми машинобудування."),
        (page_projects, "Приклади робіт для портфоліо."),
        (page_contact, "Форма звʼязку та контактні дані."),
    ]
    cols = st.columns(len(quick_links))
    for col, (page, description) in zip(cols, quick_links):
        with col:
            with st.container(border=True):
                st.page_link(page, label=f"**{page.title}**", icon=page.icon, width="stretch")
                st.caption(description)

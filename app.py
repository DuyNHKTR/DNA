import streamlit as st

from ui_sections import (
    apply_styles,
    render_demo_section,
    render_footer_section,
    render_intro_section,
    render_method_section,
    render_paper_context_section,
    render_results_section,
    render_sidebar,
)


st.set_page_config(
    page_title="DNA Sequence Classification Demo",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()
locale = render_sidebar()
render_intro_section(locale)
render_paper_context_section(locale)
render_method_section(locale)
render_results_section(locale)
render_demo_section(locale)
render_footer_section(locale)

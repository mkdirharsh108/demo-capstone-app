import os
import streamlit as st


def get_logo_path():
    path = os.path.join(os.path.dirname(__file__), "..", "img", "logo.png")
    if os.path.exists(path):
        return path
    return "https://i.ibb.co/YTYGn5qV/logo.png"


def header_home():
    logo = get_logo_path()

    st.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 0.5rem; margin-top: 0.2rem;">
            <div style="display: inline-flex; align-items: center; gap: 6px; padding: 3px 12px; border-radius: 9999px; background: rgba(24, 119, 242, 0.08); border: 1px solid rgba(24, 119, 242, 0.2); color: #1877F2; font-size: 0.74rem; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase;">
                <span style="width: 6px; height: 6px; border-radius: 50%; background: #00A86B; box-shadow: 0 0 6px #00A86B;"></span>
                Next-Gen Biometric Attendance
            </div>
        </div>
    """, unsafe_allow_html=True)

    _, col_img, _ = st.columns([1, 0.22, 1])
    with col_img:
        st.image(logo, width=64)

    st.markdown("""
        <div style="text-align: center; margin-top: -0.3rem; margin-bottom: 1.1rem;">
            <h1 style="font-size: 1.85rem; font-weight: 800; letter-spacing: -0.03em; margin: 0; line-height: 1.15; color: #1C1E21;">
                OmniAttend
            </h1>
            <p style="color: #65676B; font-size: 0.88rem; margin: 4px 0 0 0; line-height: 1.4;">
                Frictionless classroom attendance via Computer Vision & Voice AI
            </p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo = get_logo_path()

    col1, col2 = st.columns([3, 1], vertical_alignment="center")
    with col1:
        col_img, col_text = st.columns([0.16, 0.84], vertical_alignment="center")
        with col_img:
            st.image(logo, width=38)
        with col_text:
            st.markdown("""
                <div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 1.1rem; color: #1C1E21; line-height: 1.2;">OmniAttend</div>
                    <div style="font-size: 0.72rem; color: #65676B; font-weight: 500;">AI Campus Suite</div>
                </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="text-align: right;">
                <div style="display: inline-flex; align-items: center; gap: 6px; padding: 3px 10px; border-radius: 9999px; background: rgba(0, 168, 107, 0.1); border: 1px solid rgba(0, 168, 107, 0.25); color: #00A86B; font-size: 0.72rem; font-weight: 600;">
                    <span style="width: 6px; height: 6px; border-radius: 50%; background: #00A86B; box-shadow: 0 0 6px #00A86B;"></span>
                    AI Active
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

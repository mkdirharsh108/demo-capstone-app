import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #FFFFFF; 
                    border: 1px solid #E4E6EB; 
                    border-left: 4px solid #1877F2; 
                    border-radius: 16px; 
                    padding: 18px 20px; 
                    margin-bottom: 14px; 
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);">
            <h3 style="margin: 0; color: #1C1E21; font-size: 1.2rem; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif;">{name}</h3>
            <div style="display: flex; align-items: center; gap: 8px; margin: 6px 0 10px 0; font-size: 0.82rem; color: #65676B;">
                <span>Code: <span style="background: rgba(24, 119, 242, 0.08); color: #1877F2; border: 1px solid rgba(24, 119, 242, 0.2); padding: 2px 7px; border-radius: 6px; font-weight: 600;">{code}</span></span>
                <span style="color: #CCD0D5;">•</span>
                <span>Section: <span style="color: #1C1E21; font-weight: 600;">{section}</span></span>
            </div>
    """

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px;">'
        for icon, label, value in stats:
            html += f'<div style="background: #F0F2F5; border: 1px solid #E4E6EB; padding: 4px 10px; border-radius: 8px; font-size: 0.8rem; color: #4B5563;">{icon} <b style="color: #1C1E21;">{value}</b> <span style="color: #65676B;">{label}</span></div>'
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

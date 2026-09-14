import streamlit as st


def footer_home():
    logo_url = "https://static.vecteezy.com/system/resources/thumbnails/045/593/130/small/esport-ape-logo-free-png.png"

    st.markdown(f""" 
        <div style="margin-top:1.2rem; padding-top:0.8rem; border-top:1px solid #E4E6EB; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px;">
            <div style="display:flex; align-items:center; gap:6px;">
                <span style="color:#65676B; font-size:0.8rem; font-weight:500;">Engineered with precision by</span>
                <img src='{logo_url}' style='max-height:18px;' alt='Author' />
            </div>
            <div style="display:flex; align-items:center; gap:10px; font-size:0.72rem; color:#8C939D;">
                <span>FaceID (MobileNet & ResNet)</span>
                <span>•</span>
                <span>Voice2Vec Embeddings</span>
                <span>•</span>
                <span>Edge Analytics</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://static.vecteezy.com/system/resources/thumbnails/045/593/130/small/esport-ape-logo-free-png.png"

    st.markdown(f"""
        <div style="margin-top:1.5rem; padding-top:0.8rem; border-top:1px solid #E4E6EB; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
            <div style="display:flex; align-items:center; gap:6px;">
                <span style="color:#65676B; font-size:0.78rem;">Crafted by</span>
                <img src='{logo_url}' style='max-height:18px;' alt='Author' />
            </div>
            <div style="font-size:0.74rem; color:#8C939D;">
                OmniAttend AI Biometrics Suite
            </div>
        </div>
    """, unsafe_allow_html=True)

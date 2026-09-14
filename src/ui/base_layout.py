import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            /* Root App Background - Meta Signature Clean Canvas */
            .stApp {
                background: #F0F2F5 !important;
                background-image: 
                    radial-gradient(circle at 50% 0%, rgba(24, 119, 242, 0.05) 0%, transparent 50%),
                    radial-gradient(circle at 85% 85%, rgba(0, 168, 107, 0.04) 0%, transparent 40%) !important;
                background-attachment: fixed !important;
                color: #1C1E21 !important;
            }

            /* Home Portal Column Cards - Pure White Elevated Surfaces */
            .stApp div[data-testid="stColumn"] {
                background: #FFFFFF !important;
                border: 1px solid #E4E6EB !important;
                border-radius: 20px !important;
                padding: 1.25rem 1.4rem !important;
                box-shadow: 0 4px 18px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.03) !important;
                transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), 
                            border-color 0.25s ease, 
                            box-shadow 0.25s ease !important;
            }

            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-3px) !important;
                border-color: rgba(24, 119, 242, 0.35) !important;
                box-shadow: 0 10px 28px rgba(24, 119, 242, 0.12), 0 2px 6px rgba(0, 0, 0, 0.04) !important;
            }

            /* Home Mascot Wrapper - Compact Pedestal */
            .mascot-halo {
                width: 95px;
                height: 95px;
                margin: 0.4rem auto 0.7rem auto;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(24, 119, 242, 0.08) 0%, rgba(24, 119, 242, 0.01) 70%, transparent 75%);
                display: flex;
                align-items: center;
                justify-content: center;
                border: 1px solid rgba(24, 119, 242, 0.12);
                transition: transform 0.3s ease;
            }

            .mascot-halo:hover {
                transform: scale(1.04);
            }

            /* Role Badge inside Portal Card */
            .portal-badge {
                display: inline-flex;
                align-items: center;
                gap: 5px;
                padding: 3px 12px;
                border-radius: 9999px;
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                margin-bottom: 0.3rem;
            }

            .portal-badge-student {
                background: rgba(24, 119, 242, 0.08);
                color: #1877F2;
                border: 1px solid rgba(24, 119, 242, 0.22);
            }

            .portal-badge-teacher {
                background: rgba(231, 111, 81, 0.1);
                color: #E76F51;
                border: 1px solid rgba(231, 111, 81, 0.25);
            }

            /* Micro Features Chips */
            .feature-pill-list {
                display: flex;
                flex-wrap: wrap;
                gap: 5px;
                justify-content: center;
                margin: 0.8rem 0 1rem 0;
            }

            .feature-pill {
                background: #F0F2F5;
                border: 1px solid #E4E6EB;
                border-radius: 6px;
                padding: 3px 8px;
                font-size: 0.74rem;
                color: #4B5563;
                font-weight: 500;
                display: inline-flex;
                align-items: center;
                gap: 4px;
            }
        </style>  
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #F0F2F5 !important;
                background-image: 
                    radial-gradient(circle at 50% 0%, rgba(24, 119, 242, 0.04) 0%, transparent 45%) !important;
                background-attachment: fixed !important;
                color: #1C1E21 !important;
            }

            /* Reset dashboard columns to normal clean layout */
            .stApp div[data-testid="stColumn"] {
                background: transparent !important;
                padding: 0.3rem !important;
                border-radius: 0px !important;
                box-shadow: none !important;
                border: none !important;
            }
        </style>  
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            /* Modern Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

            html, body, [class*="css"] {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
                color: #1C1E21;
            }

            /* Hide Top Bar of streamlit */
            #MainMenu, footer, header {
                visibility: hidden !important;
            }

            /* 13-Inch Laptop Screen Fit Constraints */
            .block-container {
                padding-top: 0.8rem !important;
                padding-bottom: 0.8rem !important;
                max-width: 860px !important;
            }

            /* Typography Hierarchy */
            h1, h2, h3, h4 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.02em !important;
                color: #1C1E21 !important;
            }

            h1 {
                font-size: 1.9rem !important;
                line-height: 1.2 !important;
                margin-bottom: 0.3rem !important;
            }

            h2 {
                font-size: 1.45rem !important;
                line-height: 1.25 !important;
                margin-bottom: 0.3rem !important;
            }

            h3 {
                font-size: 1.15rem !important;
                margin-bottom: 0.2rem !important;
            }

            p, span, label {
                color: #65676B;
            }

            /* Clean Dividers */
            hr {
                border-color: #E4E6EB !important;
                margin: 0.8rem 0 !important;
            }

            /* Meta-Style Smooth Button System */
            button {
                border-radius: 10px !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.92rem !important;
                padding: 0.55rem 1.2rem !important;
                border: none !important;
                transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 6px !important;
            }

            /* Primary Button - Meta Blue with Pure White Text */
            button[kind="primary"],
            button[kind="primary"] *,
            button[kind="primary"] p,
            button[kind="primary"] span,
            button[kind="primary"] div,
            button[data-testid="stBaseButton-primary"],
            button[data-testid="stBaseButton-primary"] *,
            button[data-testid="stBaseButton-primary"] p,
            button[data-testid="stBaseButton-primary"] span,
            button[data-testid="stBaseButton-primary"] div {
                background-color: #1877F2 !important;
                color: #FFFFFF !important;
                -webkit-text-fill-color: #FFFFFF !important;
                font-weight: 600 !important;
            }

            button[kind="primary"],
            button[data-testid="stBaseButton-primary"] {
                box-shadow: 0 2px 8px rgba(24, 119, 242, 0.3) !important;
            }

            button[kind="primary"]:hover,
            button[kind="primary"]:hover *,
            button[data-testid="stBaseButton-primary"]:hover,
            button[data-testid="stBaseButton-primary"]:hover * {
                background-color: #166FE5 !important;
                color: #FFFFFF !important;
                -webkit-text-fill-color: #FFFFFF !important;
                box-shadow: 0 4px 14px rgba(24, 119, 242, 0.45) !important;
                transform: translateY(-1px) !important;
            }

            /* Secondary Button - Meta Soft Gray with Dark Text */
            button[kind="secondary"],
            button[kind="secondary"] *,
            button[kind="secondary"] p,
            button[kind="secondary"] span,
            button[data-testid="stBaseButton-secondary"],
            button[data-testid="stBaseButton-secondary"] *,
            button[data-testid="stBaseButton-secondary"] p,
            button[data-testid="stBaseButton-secondary"] span {
                background-color: #E4E6EB !important;
                color: #050505 !important;
                -webkit-text-fill-color: #050505 !important;
                font-weight: 600 !important;
            }

            button[kind="secondary"]:hover,
            button[kind="secondary"]:hover *,
            button[data-testid="stBaseButton-secondary"]:hover,
            button[data-testid="stBaseButton-secondary"]:hover * {
                background-color: #D8DADF !important;
                color: #050505 !important;
                -webkit-text-fill-color: #050505 !important;
                transform: translateY(-1px) !important;
            }

            /* Tertiary Button - Meta Green for Account Actions with Pure White Text */
            button[kind="tertiary"],
            button[kind="tertiary"] *,
            button[kind="tertiary"] p,
            button[kind="tertiary"] span,
            button[data-testid="stBaseButton-tertiary"],
            button[data-testid="stBaseButton-tertiary"] *,
            button[data-testid="stBaseButton-tertiary"] p,
            button[data-testid="stBaseButton-tertiary"] span {
                background-color: #42B72A !important;
                color: #FFFFFF !important;
                -webkit-text-fill-color: #FFFFFF !important;
                font-weight: 600 !important;
            }

            button[kind="tertiary"],
            button[data-testid="stBaseButton-tertiary"] {
                box-shadow: 0 2px 8px rgba(66, 183, 42, 0.25) !important;
            }

            button[kind="tertiary"]:hover,
            button[kind="tertiary"]:hover *,
            button[data-testid="stBaseButton-tertiary"]:hover,
            button[data-testid="stBaseButton-tertiary"]:hover * {
                background-color: #36A420 !important;
                color: #FFFFFF !important;
                -webkit-text-fill-color: #FFFFFF !important;
                box-shadow: 0 4px 12px rgba(66, 183, 42, 0.4) !important;
                transform: translateY(-1px) !important;
            }

            /* Inputs and Form Controls - Crisp Meta Style */
            input[type="text"], input[type="password"], textarea {
                background: #FFFFFF !important;
                border: 1px solid #CCD0D5 !important;
                border-radius: 10px !important;
                color: #1C1E21 !important;
                font-family: 'Inter', sans-serif !important;
                padding: 9px 12px !important;
                box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.04) !important;
                transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
            }

            input[type="text"]:focus, input[type="password"]:focus, textarea:focus {
                border-color: #1877F2 !important;
                box-shadow: 0 0 0 2px rgba(24, 119, 242, 0.2) !important;
            }

            input::placeholder, textarea::placeholder {
                color: #8C939D !important;
                opacity: 1 !important;
            }

            /* Selectbox */
            div[data-baseweb="select"] > div {
                background: #FFFFFF !important;
                border: 1px solid #CCD0D5 !important;
                border-radius: 10px !important;
                color: #1C1E21 !important;
            }

            /* Elevated Containers */
            div[data-testid="stVerticalBlockBorderWrapper"] {
                background: #FFFFFF !important;
                border: 1px solid #E4E6EB !important;
                border-radius: 16px !important;
                padding: 1.2rem !important;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04) !important;
            }

            /* Dialogs */
            div[data-testid="stDialog"] > div {
                background: #FFFFFF !important;
                border: 1px solid #E4E6EB !important;
                border-radius: 20px !important;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15) !important;
            }

            /* Toasts and Alerts */
            div[data-testid="stToast"] {
                background: #1C1E21 !important;
                color: #FFFFFF !important;
                border-radius: 12px !important;
            }

            /* Dataframes */
            div[data-testid="stDataFrame"] {
                border: 1px solid #E4E6EB !important;
                border-radius: 12px !important;
                overflow: hidden !important;
                background: #FFFFFF !important;
            }

            /* Camera Input */
            div[data-testid="stCameraInput"] {
                border: 1px solid #CCD0D5 !important;
                border-radius: 14px !important;
                overflow: hidden !important;
                background: #FFFFFF !important;
            }
        </style>  
    """, unsafe_allow_html=True)
import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
            <div style="text-align: center;">
                <div class="portal-badge portal-badge-student">⚡ Student Access</div>
                <h2 style="font-size: 1.35rem; font-weight: 700; color: #1C1E21; margin: 0.2rem 0 0.15rem 0;">I'm a Student</h2>
                <p style="color: #65676B; font-size: 0.82rem; margin: 0 0 0.35rem 0;">Fast biometric check-in & attendance tracking</p>
                <div class="mascot-halo">
                    <img src="https://static.vecteezy.com/system/resources/previews/045/546/305/non_2x/boy-wear-graduation-hat-and-holding-book-3d-mascot-free-png.png" style="height: 72px; width: auto;" alt="Student Mascot" />
                </div>
                <div class="feature-pill-list">
                    <span class="feature-pill">⚡ FaceID Check-in</span>
                    <span class="feature-pill">🎙️ Voice AI</span>
                    <span class="feature-pill">📊 My Attendance</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Enter Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch', key='btn_home_student'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <div class="portal-badge portal-badge-teacher">🎓 Faculty Access</div>
                <h2 style="font-size: 1.35rem; font-weight: 700; color: #1C1E21; margin: 0.2rem 0 0.15rem 0;">I'm an Educator</h2>
                <p style="color: #65676B; font-size: 0.82rem; margin: 0 0 0.35rem 0;">Multi-student camera scans & class analytics</p>
                <div class="mascot-halo">
                    <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" style="height: 76px; width: auto;" alt="Teacher Mascot" />
                </div>
                <div class="feature-pill-list">
                    <span class="feature-pill">📸 Multi-Face Scan</span>
                    <span class="feature-pill">👥 Subject Admin</span>
                    <span class="feature-pill">📈 Instant Reports</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Enter Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch', key='btn_home_teacher'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()

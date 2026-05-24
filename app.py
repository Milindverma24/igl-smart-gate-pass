import streamlit as st
from streamlit_option_menu import option_menu

from pages.visitor_form import show_visitor_form
from pages.login import login
from pages.admin_dashboard import show_admin_dashboard
from pages.approvals import show_approvals
from pages.visitor_logs import show_visitor_logs
from pages.manual_pass import show_manual_pass
from pages.analytics import show_analytics
from pages.export_reports import show_export_reports

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="IGL Gate Pass",

    page_icon="🛡️",

    layout="wide",

    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATES
# =========================================================

if "page" not in st.session_state:

    st.session_state.page = "home"

if "admin" not in st.session_state:

    st.session_state.admin = False

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
HIDE STREAMLIT DEFAULTS
========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background-color: transparent;
}

[data-testid="stSidebarNav"] {
    display: none;
}

/* =========================================================
APP BACKGROUND
========================================================= */

.stApp {

    background-color: #050816;

    color: white;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background-color: #111827;

    border-right: 2px solid #00FFAA;
}

/* =========================================================
COLLAPSED SIDEBAR
========================================================= */

section[data-testid="stSidebar"][aria-expanded="false"] {

    min-width: 70px !important;

    max-width: 70px !important;
}

/* =========================================================
EXPANDED SIDEBAR
========================================================= */

section[data-testid="stSidebar"][aria-expanded="true"] {

    min-width: 300px !important;

    max-width: 300px !important;
}

/* =========================================================
SIDEBAR TOGGLE BUTTON
========================================================= */

[data-testid="collapsedControl"] {

    display: flex !important;

    color: #00FFAA !important;

    padding-top: 15px;
}

/* =========================================================
BUTTONS
========================================================= */

.stButton > button {

    width: 100%;

    height: 52px;

    border-radius: 12px;

    border: none;

    background: linear-gradient(
        90deg,
        #00FFAA,
        #00C896
    );

    color: black;

    font-size: 18px;

    font-weight: bold;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.02);

    background: linear-gradient(
        90deg,
        #00C896,
        #00FFAA
    );
}

/* =========================================================
INPUT BOXES
========================================================= */

.stTextInput input,
.stTextArea textarea {

    border-radius: 10px;

    border: 1px solid #00FFAA;

    background-color: #111827;

    color: white;
}

/* =========================================================
DATAFRAME
========================================================= */

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

    border: 1px solid rgba(0,255,170,0.2);
}

/* =========================================================
METRIC CARDS
========================================================= */

div[data-testid="metric-container"] {

    background-color: #111827;

    border: 1px solid rgba(0,255,170,0.2);

    padding: 20px;

    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    # =====================================================
    # HERO SECTION
    # =====================================================

    col1, col2 = st.columns([1,2])

    # =====================================================
    # LEFT LOGO
    # =====================================================

    with col1:

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.image(
            "assets/logo.png",
            width=260
        )

    # =====================================================
    # RIGHT CONTENT
    # =====================================================

    with col2:

        st.markdown("""

        <div style='padding-top:80px;'>

        <h1 style='
        color:#00FFAA;
        font-size:72px;
        font-weight:900;
        line-height:1.1;
        margin-bottom:10px;
        '>

        IGL GATE PASS SYSTEM

        </h1>

        <p style='
        color:#D1D5DB;
        font-size:24px;
        margin-top:10px;
        '>

        Smart Visitor Management Platform

        </p>

        <div style='
        width:180px;
        height:4px;
        background:#00FFAA;
        border-radius:20px;
        margin-top:20px;
        '></div>

        </div>

        """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # =====================================================
    # PORTALS
    # =====================================================

    col3, col4 = st.columns(2)

    # =====================================================
    # VISITOR PORTAL
    # =====================================================

    with col3:

        st.markdown("""

        <div style='
        background:linear-gradient(
        145deg,
        #111827,
        #0F172A
        );
        padding:45px;
        border-radius:25px;
        border:1px solid rgba(0,255,170,0.25);
        text-align:center;
        min-height:340px;
        box-shadow:0px 0px 20px rgba(0,255,170,0.08);
        '>

        <div style='font-size:90px;'>👤</div>

        <h1 style='
        color:#00FFAA;
        font-size:38px;
        margin-top:15px;
        '>

        Visitor Portal

        </h1>

        <p style='
        color:#D1D5DB;
        font-size:18px;
        margin-top:15px;
        '>

        Register Visitors & Generate Smart Gate Passes

        </p>

        </div>

        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "🚀 Open Visitor Portal",
            key="visitor_portal"
        ):

            st.session_state.page = "visitor"

            st.rerun()

    # =====================================================
    # ADMIN PORTAL
    # =====================================================

    with col4:

        st.markdown("""

        <div style='
        background:linear-gradient(
        145deg,
        #111827,
        #0F172A
        );
        padding:45px;
        border-radius:25px;
        border:1px solid rgba(0,255,170,0.25);
        text-align:center;
        min-height:340px;
        box-shadow:0px 0px 20px rgba(0,255,170,0.08);
        '>

        <div style='font-size:90px;'>🔐</div>

        <h1 style='
        color:#00FFAA;
        font-size:38px;
        margin-top:15px;
        '>

        Admin Portal

        </h1>

        <p style='
        color:#D1D5DB;
        font-size:18px;
        margin-top:15px;
        '>

        Security, Analytics & Visitor Monitoring

        </p>

        </div>

        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "🔐 Open Admin Portal",
            key="admin_portal"
        ):

            st.session_state.page = "admin_login"

            st.rerun()

    st.write("")
    st.write("")

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""

    <div style='
    text-align:center;
    color:#9CA3AF;
    font-size:15px;
    margin-top:25px;
    '>

    © 2026 India Glycols Limited • Smart Security Infrastructure

    </div>

    """, unsafe_allow_html=True)
# =========================================================
# VISITOR PAGE
# =========================================================

elif st.session_state.page == "visitor":

    col1, col2 = st.columns([1,5])

    with col1:

        if st.button("⬅ Back"):

            st.session_state.page = "home"

            st.rerun()

    with col2:

        st.markdown("""

        <h1 style='
        color:#00FFAA;
        text-align:center;
        font-size:42px;
        font-weight:800;
        '>

        Visitor Registration Form

        </h1>

        """, unsafe_allow_html=True)

    show_visitor_form()

# =========================================================
# ADMIN LOGIN PAGE
# =========================================================

elif st.session_state.page == "admin_login":

    col1, col2 = st.columns([1,5])

    with col1:

        if st.button("⬅ Back"):

            st.session_state.page = "home"

            st.rerun()

    with col2:

        st.markdown("""

        <h1 style='
        color:#00FFAA;
        text-align:center;
        font-size:42px;
        font-weight:800;
        '>

        Admin Login

        </h1>

        """, unsafe_allow_html=True)

    login()

# =========================================================
# ADMIN PANEL
# =========================================================

elif st.session_state.page == "admin_panel":

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.image(
            "assets/logo.png",
            width=180
        )

        st.markdown("""

        <h2 style='
        text-align:center;
        color:#00FFAA;
        '>

        ADMIN PANEL

        </h2>

        """, unsafe_allow_html=True)

        selected = option_menu(

            menu_title=None,

            options=[

                "Dashboard",

                "Approvals",

                "Visitor Logs",

                "Manual Pass",

                "Analytics",

                "Export Reports",

                "Logout"
            ],

            icons=[

                "speedometer2",

                "check-circle-fill",

                "file-earmark-text-fill",

                "person-plus-fill",

                "bar-chart-fill",

                "download",

                "box-arrow-right"
            ],

            default_index=0,

            styles={

                "container": {

                    "padding": "5px",
                    "background-color": "#111827"
                },

                "icon": {

                    "color": "#00FFAA",
                    "font-size": "18px"
                },

                "nav-link": {

                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#1E293B",
                    "border-radius": "10px"
                },

                "nav-link-selected": {

                    "background-color": "#00C896",
                    "color": "black",
                    "font-weight": "bold"
                }
            }
        )

    # =====================================================
    # DASHBOARD
    # =====================================================

    if selected == "Dashboard":

        show_admin_dashboard()

    # =====================================================
    # APPROVALS
    # =====================================================

    elif selected == "Approvals":

        show_approvals()

    # =====================================================
    # VISITOR LOGS
    # =====================================================

    elif selected == "Visitor Logs":

        show_visitor_logs()
    
    elif selected == "Manual Pass":

        show_manual_pass()

    # =====================================================
    # ANALYTICS
    # =====================================================

    elif selected == "Analytics":

        show_analytics()

    elif selected == "Export Reports":

        show_export_reports()
    # =====================================================
    # LOGOUT
    # =====================================================

    
    elif selected == "Logout":

        st.session_state.admin = False

        st.session_state.page = "home"

        st.rerun()
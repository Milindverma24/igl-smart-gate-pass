import streamlit as st

# =========================
# ADMIN LOGIN
# =========================

def login():

    st.markdown("""

    <div style='
    max-width:450px;
    margin:auto;
    background-color:#111827;
    padding:40px;
    border-radius:20px;
    border:1px solid rgba(0,255,170,0.2);
    '>

    <h2 style='
    text-align:center;
    color:#00FFAA;
    margin-bottom:30px;
    '>

    🔐 Admin Authentication

    </h2>

    </div>

    """, unsafe_allow_html=True)

    username = st.text_input(
        "Admin ID"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    st.write("")

    if st.button(
        "Login"
    ):

        # =========================
        # VALID LOGIN
        # =========================

        if (

            username == "admin"

            and

            password == "igl123"

        ):

            st.session_state.admin = True

            # =========================
            # MOVE TO ADMIN PANEL
            # =========================

            st.session_state.page = "admin_panel"

            st.success(
                "Login Successful"
            )

            st.rerun()

        # =========================
        # INVALID LOGIN
        # =========================

        else:

            st.error(
                "Invalid Credentials"
            )
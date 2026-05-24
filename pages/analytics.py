import streamlit as st
import pandas as pd
import plotly.express as px

from database.database import fetch_visitors

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================

def show_analytics():

    st.markdown("""

    <h1 style='
    color:#00FFAA;
    text-align:center;
    font-size:42px;
    font-weight:800;
    '>

    📊 Visitor Analytics Dashboard

    </h1>

    """, unsafe_allow_html=True)

    visitors = fetch_visitors()

    if len(visitors) == 0:

        st.warning(
            "No Data Found"
        )

        return

    # =================================================
    # DATAFRAME
    # =================================================

    data = []

    for visitor in visitors:

        data.append({

            "Visitor ID": visitor[1],

            "Name": visitor[2],

            "Company": visitor[5],

            "Status": visitor[11]
        })

    df = pd.DataFrame(data)

    # =================================================
    # STATUS COUNTS
    # =================================================

    status_chart = px.pie(

        df,

        names="Status",

        title="Approval Rates"
    )

    st.plotly_chart(

        status_chart,

        use_container_width=True
    )

    # =================================================
    # COMPANY VISITS
    # =================================================

    company_chart = px.histogram(

        df,

        x="Company",

        title="Top Companies Visiting"
    )

    st.plotly_chart(

        company_chart,

        use_container_width=True
    )
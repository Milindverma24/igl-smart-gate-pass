import streamlit as st
import pandas as pd

from database.database import fetch_visitors

# =====================================================
# EXPORT REPORTS
# =====================================================

def show_export_reports():

    st.markdown("""

    <h1 style='
    color:#00FFAA;
    text-align:center;
    font-size:42px;
    font-weight:800;
    '>

    📁 Export Reports

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

            "Phone": visitor[3],

            "Email": visitor[4],

            "Company": visitor[6],

            "Purpose": visitor[7],

            "Status": visitor[11]
        })

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

    # =================================================
    # CSV EXPORT
    # =================================================

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        label="⬇ Download CSV",

        data=csv,

        file_name="visitor_report.csv",

        mime="text/csv"
    )

    # =================================================
    # EXCEL EXPORT
    # =================================================

    excel_path = "visitor_report.xlsx"

    df.to_excel(

        excel_path,

        index=False
    )

    with open(excel_path, "rb") as file:

        st.download_button(

            label="⬇ Download Excel",

            data=file,

            file_name="visitor_report.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
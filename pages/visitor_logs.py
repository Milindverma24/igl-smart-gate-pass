import streamlit as st
import pandas as pd

from database.database import fetch_visitors

def show_visitor_logs():

    st.title(
        "📋 Visitor Logs"
    )

    visitors = fetch_visitors()

    data = []

    for visitor in visitors:

        data.append({

            "Visitor ID": visitor[1],
            "Name": visitor[2],
            "Phone": visitor[3],
            "Company": visitor[5],
            "Status": visitor[11]

        })

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )
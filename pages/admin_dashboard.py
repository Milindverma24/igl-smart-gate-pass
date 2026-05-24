import streamlit as st
import pandas as pd

from database.database import fetch_visitors

def show_admin_dashboard():

    st.title(
        "📊 Admin Dashboard"
    )

    visitors = fetch_visitors()

    data = []

    for visitor in visitors:

        data.append({

            "ID": visitor[0],
            "Visitor ID": visitor[1],
            "Name": visitor[2],
            "Phone": visitor[3],
            "Email": visitor[4],
            "Company": visitor[5],
            "Purpose": visitor[6],
            "Meeting Person": visitor[7],
            "Status": visitor[11]

        })

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )
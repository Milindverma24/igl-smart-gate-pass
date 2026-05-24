import streamlit as st

from database.database import (
    fetch_visitors,
    approve_visitor,
    update_visitor_status
)

from utils.id_generator import generate_visitor_id
from utils.qr_generator import generate_qr
from utils.pdf_generator import generate_pdf
from utils.email_sender import send_email
from utils.voice_alert import speak_alert

import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# =========================================================
# REJECTION EMAIL
# =========================================================

def send_rejection_email(

    receiver_email,
    visitor_name

):

    sender_email = "YOUR_EMAIL@gmail.com"

    sender_password = "YOUR_APP_PASSWORD"

    subject = "IGL Visitor Request Rejected"

    body = f"""

Hello {visitor_name},

Your visitor gate pass request has been rejected by the administration.

Please contact IGL Security Department for more information.

Regards,
IGL Security Team

"""

    msg = MIMEText(body)

    msg["Subject"] = subject

    msg["From"] = sender_email

    msg["To"] = receiver_email

    try:

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        return True

    except Exception as e:

        print(f"Email Error: {e}")

        return False

# =========================================================
# APPROVALS PAGE
# =========================================================

def show_approvals():

    st.markdown("""

    <h1 style='
    color:#00FFAA;
    text-align:center;
    font-size:42px;
    font-weight:800;
    '>

    ✅ Visitor Approval Center

    </h1>

    """, unsafe_allow_html=True)

    visitors = fetch_visitors()

    # =====================================================
    # SEARCH + FILTERS
    # =====================================================

    col_search, col_filter = st.columns(2)

    with col_search:

        search = st.text_input(

            "🔍 Search Visitor",

            placeholder="Search by Visitor ID, name, phone, company"
        )

    with col_filter:

        status_filter = st.selectbox(

            "📌 Filter By Status",

            [

                "All",

                "Pending",

                "Approved",

                "Checked In",

                "Checked Out",

                "Expired",

                "Rejected"
            ]
        )

    st.divider()

    # =====================================================
    # NO VISITORS
    # =====================================================

    if len(visitors) == 0:

        st.warning(
            "No visitor requests found."
        )

        return

    # =====================================================
    # LOOP VISITORS
    # =====================================================

    for visitor in visitors:

        # =================================================
        # DATABASE INDEXES
        # =================================================
        #
        # 0  id
        # 1  visitor_id
        # 2  name
        # 3  phone
        # 4  email
        # 5  employee_email
        # 6  company
        # 7  purpose
        # 8  person_to_meet
        # 9  photo_path
        # 10 qr_path
        # 11 pdf_path
        # 12 status
        # 13 expiry_time
        #
        # =================================================

        # =================================================
        # AUTO EXPIRE PASSES
        # =================================================

        if visitor[12] == "Approved":

            if len(visitor) > 13 and visitor[13]:

                try:

                    expiry_time = datetime.strptime(

                        visitor[13],

                        "%Y-%m-%d %H:%M:%S.%f"
                    )

                    if datetime.now() > expiry_time:

                        update_visitor_status(

                            visitor[0],

                            "Expired"
                        )

                        st.rerun()

                except Exception as e:

                    print(e)

        # =================================================
        # SEARCH FILTER
        # =================================================

        search_match = (

            search.lower() in str(visitor[1]).lower()

            or

            search.lower() in str(visitor[2]).lower()

            or

            search.lower() in str(visitor[3]).lower()

            or

            search.lower() in str(visitor[6]).lower()
        )

        # =================================================
        # STATUS FILTER
        # =================================================

        status_match = (

            status_filter == "All"

            or

            visitor[12] == status_filter
        )

        # =================================================
        # SKIP NON MATCHING
        # =================================================

        if not (search_match and status_match):

            continue

        # =================================================
        # CARD START
        # =================================================

        st.markdown("""
        <div style='
        background-color:#111827;
        padding:25px;
        border-radius:18px;
        border:1px solid rgba(0,255,170,0.15);
        margin-bottom:25px;
        '>
        """, unsafe_allow_html=True)

        # =================================================
        # TOP SECTION
        # =================================================

        col1, col2 = st.columns([1,3])

        # =================================================
        # VISITOR IMAGE
        # =================================================

        with col1:

            try:

                st.image(
                    visitor[9],
                    width=180
                )

            except:

                st.warning(
                    "Visitor image not found"
                )

        # =================================================
        # VISITOR DETAILS
        # =================================================

        with col2:

            st.subheader(
                visitor[2]
            )

            st.write(
                f"🆔 Visitor ID: {visitor[1]}"
            )

            st.write(
                f"📧 Email: {visitor[4]}"
            )

            st.write(
                f"📱 Phone: {visitor[3]}"
            )

            st.write(
                f"🏢 Company: {visitor[6]}"
            )

            st.write(
                f"📝 Purpose: {visitor[7]}"
            )

            st.write(
                f"👤 Person To Meet: {visitor[8]}"
            )

            st.write(
                f"📌 Status: {visitor[12]}"
            )

        st.write("")

        # =================================================
        # ACTION BUTTONS
        # =================================================

        col3, col4, col5 = st.columns(3)

        # =================================================
        # APPROVE
        # =================================================

        if visitor[12] == "Pending":

            if col3.button(
                f"✅ Approve {visitor[0]}"
            ):

                generated_id = generate_visitor_id()

                qr_path = generate_qr(
                    generated_id
                )

                visitor_data = {

                    "visitor_id": generated_id,

                    "name": visitor[2],

                    "phone": visitor[3],

                    "company": visitor[6],

                    "purpose": visitor[7],

                    "person_to_meet": visitor[8]

                }

                pdf_path = generate_pdf(

                    visitor_data,

                    visitor[9],

                    qr_path
                )

                expiry = datetime.now() + timedelta(hours=24)

                approve_visitor(

                    visitor[0],

                    generated_id,

                    qr_path,

                    pdf_path,

                    expiry
                )

                email_sent = send_email(

                    visitor[4],

                    visitor[2],

                    generated_id,

                    pdf_path
                )

                if email_sent:

                    st.success(
                        "✅ Visitor Approved & Pass Sent"
                    )

                    speak_alert(
                        "Visitor approved successfully"
                    )

                else:

                    st.error(
                        "❌ Email Sending Failed"
                    )

                st.rerun()

        # =================================================
        # GENERATE PASS
        # =================================================

        if col4.button(
            f"🪪 Generate Pass {visitor[0]}"
        ):

            generated_id = generate_visitor_id()

            qr_path = generate_qr(
                generated_id
            )

            visitor_data = {

                "visitor_id": generated_id,

                "name": visitor[2],

                "phone": visitor[3],

                "company": visitor[6],

                "purpose": visitor[7],

                "person_to_meet": visitor[8]

            }

            pdf_path = generate_pdf(

                visitor_data,

                visitor[9],

                qr_path
            )

            email_sent = send_email(

                visitor[4],

                visitor[2],

                generated_id,

                pdf_path
            )

            if email_sent:

                st.success(
                    "✅ Gate Pass Generated & Sent To Visitor Email"
                )

            else:

                st.error(
                    "❌ Email Sending Failed"
                )

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(

                    label="🖨 Print Gate Pass",

                    data=pdf_file,

                    file_name=f"{generated_id}.pdf",

                    mime="application/pdf"
                )

        # =================================================
        # REJECT
        # =================================================

        if visitor[12] == "Pending":

            if col5.button(
                f"❌ Reject {visitor[0]}"
            ):

                rejection_sent = send_rejection_email(

                    visitor[4],

                    visitor[2]
                )

                if rejection_sent:

                    update_visitor_status(

                        visitor[0],

                        "Rejected"
                    )

                    st.error(
                        "❌ Visitor Rejected & Email Sent"
                    )

                else:

                    st.error(
                        "❌ Rejection Email Failed"
                    )

                st.rerun()

        # =================================================
        # CHECK IN
        # =================================================

        if visitor[12] == "Approved":

            if st.button(
                f"🟢 Check In {visitor[0]}"
            ):

                update_visitor_status(

                    visitor[0],

                    "Checked In"
                )

                st.success(
                    "✅ Visitor Checked In"
                )

                speak_alert(
                    "Visitor checked in"
                )

                st.rerun()

        # =================================================
        # CHECK OUT
        # =================================================

        if visitor[12] == "Checked In":

            if st.button(
                f"🔴 Check Out {visitor[0]}"
            ):

                update_visitor_status(

                    visitor[0],

                    "Checked Out"
                )

                st.success(
                    "✅ Visitor Checked Out"
                )

                speak_alert(
                    "Visitor checked out"
                )

                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        st.divider()
import streamlit as st
from PIL import Image
from datetime import datetime
import os
import re

from database.database import insert_visitor

from utils.id_generator import generate_visitor_id
from utils.qr_generator import generate_qr
from utils.pdf_generator import generate_pdf
from utils.email_sender import send_email

# =========================================================
# VALID EMAIL
# =========================================================

def valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(
        pattern,
        email
    )

# =========================================================
# VALID PHONE
# =========================================================

def valid_phone(phone):

    return (

        phone.isdigit()

        and

        len(phone) == 10
    )

# =========================================================
# MANUAL PASS PAGE
# =========================================================

def show_manual_pass():

    st.markdown("""

    <h1 style='
    color:#00FFAA;
    text-align:center;
    font-size:42px;
    font-weight:800;
    '>

    ➕ Manual Visitor Pass Entry

    </h1>

    """, unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns(2)

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with col1:

        visitor_name = st.text_input(
            "Visitor Name"
        )

        phone = st.text_input(
            "Phone Number"
        )

        email = st.text_input(
            "Email Address"
        )

        company = st.text_input(
            "Company Name"
        )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with col2:

        purpose = st.text_input(
            "Purpose"
        )

        person_to_meet = st.text_input(
            "Person To Meet"
        )

        visit_date = st.date_input(
            "Visit Date"
        )

    st.divider()

    # =====================================================
    # PHOTO UPLOAD
    # =====================================================

    visitor_photo = st.file_uploader(

        "Upload Visitor Photo",

        type=["jpg", "jpeg", "png"]
    )

    st.divider()

    # =====================================================
    # GENERATE PASS
    # =====================================================

    if st.button(
        "🪪 Generate Visitor Pass"
    ):

        # =================================================
        # VALIDATION
        # =================================================

        if (

            visitor_name.strip() == ""

            or

            phone.strip() == ""

            or

            email.strip() == ""

            or

            company.strip() == ""

            or

            purpose.strip() == ""

            or

            person_to_meet.strip() == ""

        ):

            st.error(
                "Please fill all fields"
            )

            return

        # =================================================
        # PHONE VALIDATION
        # =================================================

        if not valid_phone(phone):

            st.error(
                "Enter valid 10-digit phone number"
            )

            return

        # =================================================
        # EMAIL VALIDATION
        # =================================================

        if not valid_email(email):

            st.error(
                "Enter valid email address"
            )

            return

        # =================================================
        # IMAGE VALIDATION
        # =================================================

        if visitor_photo is None:

            st.error(
                "Upload Visitor Photo"
            )

            return

        # =================================================
        # GENERATE ID
        # =================================================

        visitor_id = generate_visitor_id()

        # =================================================
        # CREATE FOLDER
        # =================================================

        os.makedirs(
            "visitor_photos",
            exist_ok=True
        )

        # =================================================
        # SAVE PHOTO
        # =================================================

        image = Image.open(
            visitor_photo
        )

        # =================================================
        # CONVERT RGBA TO RGB
        # =================================================

        if image.mode == "RGBA":

            image = image.convert(
                "RGB"
            )

        photo_path = f"visitor_photos/{visitor_id}.jpg"

        image.save(
            photo_path
        )

        # =================================================
        # GENERATE QR
        # =================================================

        qr_path = generate_qr(
            visitor_id
        )

        # =================================================
        # VISITOR DATA
        # =================================================

        visitor_data = {

            "visitor_id": visitor_id,

            "name": visitor_name,

            "phone": phone,

            "company": company,

            "purpose": purpose,

            "person_to_meet": person_to_meet
        }

        # =================================================
        # GENERATE PDF
        # =================================================

        pdf_path = generate_pdf(

            visitor_data,

            photo_path,

            qr_path
        )

        # =================================================
        # SAVE DATABASE
        # =================================================

        insert_visitor(

            visitor_name,

            phone,

            email,

            "",

            company,

            purpose,

            person_to_meet,

            photo_path
        )

        # =================================================
        # SEND EMAIL
        # =================================================

        email_sent = send_email(

            email,

            visitor_name,

            visitor_id,

            pdf_path
        )

        # =================================================
        # SUCCESS
        # =================================================

        if email_sent:

            st.success(
                "✅ Pass Generated & Email Sent Successfully"
            )

        else:

            st.warning(
                "⚠ Pass Generated But Email Failed"
            )

        st.balloons()

        # =================================================
        # PRINT PASS
        # =================================================

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(

                label="🖨 Print Visitor Pass",

                data=pdf_file,

                file_name=f"{visitor_id}.pdf",

                mime="application/pdf"
            )
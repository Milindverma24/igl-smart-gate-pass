import streamlit as st
from PIL import Image
import os
import re

from database.database import insert_visitor

# =========================================================
# VALIDATE EMAIL
# =========================================================

def valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(
        pattern,
        email
    )

# =========================================================
# VALIDATE PHONE
# =========================================================

def valid_phone(phone):

    return (

        phone.isdigit()

        and

        len(phone) == 10
    )

# =========================================================
# VISITOR FORM
# =========================================================

def show_visitor_form():

    st.markdown("""

    <h1 style='
    text-align:center;
    color:#00FFAA;
    font-size:42px;
    font-weight:800;
    '>

    🪪 IGL Visitor Registration

    </h1>

    """, unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns(2)

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with col1:

        name = st.text_input(
            "Visitor Name"
        )

        phone = st.text_input(
            "Mobile Number"
        )

        email = st.text_input(
            "Email Address"
        )

        employee_email = st.text_input(
            "Employee Email (Optional)"
        )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with col2:

        company = st.text_input(
            "Company Name"
        )

        purpose = st.text_area(
            "Purpose of Visit"
        )

        person_to_meet = st.text_input(
            "Person To Meet"
        )

    st.divider()

    # =====================================================
    # PHOTO OPTIONS
    # =====================================================

    st.subheader(
        "📸 Visitor Photo"
    )

    photo_option = st.radio(

        "Select Photo Method",

        [

            "Upload Image",

            "Capture From Camera"
        ]
    )

    visitor_photo = None

    # =====================================================
    # UPLOAD IMAGE
    # =====================================================

    if photo_option == "Upload Image":

        visitor_photo = st.file_uploader(

            "Upload Visitor Image",

            type=[

                "jpg",
                "jpeg",
                "png"
            ]
        )

    # =====================================================
    # CAMERA INPUT
    # =====================================================

    elif photo_option == "Capture From Camera":

        visitor_photo = st.camera_input(

            "Capture Visitor Photo"
        )

    st.divider()

    # =====================================================
    # SUBMIT BUTTON
    # =====================================================

    if st.button(
        "📨 Submit Request"
    ):

        # =================================================
        # CLEAN VALUES
        # =================================================

        name_value = name.strip()

        phone_value = phone.strip()

        email_value = email.strip()

        employee_email_value = employee_email.strip()

        company_value = company.strip()

        purpose_value = purpose.strip()

        person_value = person_to_meet.strip()

        # =================================================
        # REQUIRED FIELD VALIDATION
        # =================================================

        if (

            name_value == ""

            or

            phone_value == ""

            or

            email_value == ""

            or

            company_value == ""

            or

            purpose_value == ""

            or

            person_value == ""

        ):

            st.error(
                "Please fill all fields"
            )

            return

        # =================================================
        # PHONE VALIDATION
        # =================================================

        if not valid_phone(phone_value):

            st.error(
                "Enter valid 10-digit mobile number"
            )

            return

        # =================================================
        # EMAIL VALIDATION
        # =================================================

        if not valid_email(email_value):

            st.error(
                "Enter valid email address"
            )

            return

        # =================================================
        # OPTIONAL EMPLOYEE EMAIL VALIDATION
        # =================================================

        if employee_email_value != "":

            if not valid_email(employee_email_value):

                st.error(
                    "Enter valid employee email"
                )

                return

        # =================================================
        # PHOTO VALIDATION
        # =================================================

        if visitor_photo is None:

            st.error(
                "Please upload or capture visitor photo"
            )

            return

        # =================================================
        # SAVE PHOTO
        # =================================================

        os.makedirs(
            "visitor_photos",
            exist_ok=True
        )

        image = Image.open(
            visitor_photo
        )

        safe_name = name_value.replace(
            " ",
            "_"
        )

        photo_path = f"visitor_photos/{safe_name}.jpg"

        image.save(
            photo_path
        )

        # =================================================
        # SAVE DATABASE
        # =================================================

        insert_visitor(

            name_value,

            phone_value,

            email_value,

            employee_email_value,

            company_value,

            purpose_value,

            person_value,

            photo_path
        )

        # =================================================
        # SUCCESS
        # =================================================

        st.success(
            "✅ Visitor Request Submitted Successfully"
        )

        st.balloons()
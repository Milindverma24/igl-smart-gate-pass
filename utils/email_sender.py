import smtplib
import os

from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

load_dotenv()

# =========================================================
# SEND EMAIL
# =========================================================

def send_email(

    receiver_email,
    visitor_name,
    visitor_id,
    pdf_path

):

    # =====================================================
    # EMAIL CONFIG
    # =====================================================

    sender_email = os.getenv("EMAIL_USER")

    sender_password = os.getenv("EMAIL_PASS")

    # =====================================================
    # CHECK ENV VARIABLES
    # =====================================================

    if not sender_email or not sender_password:

        print("EMAIL ENV VARIABLES NOT FOUND")

        return False

    # =====================================================
    # CREATE MESSAGE
    # =====================================================

    msg = MIMEMultipart()

    msg["From"] = sender_email

    msg["To"] = receiver_email

    msg["Subject"] = "IGL Visitor Gate Pass Approved"

    # =====================================================
    # EMAIL BODY
    # =====================================================

    body = f"""

Hello {visitor_name},

Your gate pass request has been approved successfully.

Visitor ID:
{visitor_id}

Please find the attached gate pass PDF.

Regards,
IGL Security Team

"""

    msg.attach(

        MIMEText(
            body,
            "plain"
        )
    )

    # =====================================================
    # ATTACH LOGO
    # =====================================================

    try:

        with open(
            "assets/logo.png",
            "rb"
        ) as logo_file:

            logo = MIMEImage(
                logo_file.read()
            )

            logo.add_header(
                "Content-ID",
                "<igl_logo>"
            )

            msg.attach(logo)

    except Exception as e:

        print(f"Logo Error: {e}")

    # =====================================================
    # ATTACH PDF
    # =====================================================

    try:

        with open(
            pdf_path,
            "rb"
        ) as attachment:

            part = MIMEBase(
                "application",
                "octet-stream"
            )

            part.set_payload(
                attachment.read()
            )

        encoders.encode_base64(part)

        part.add_header(

            "Content-Disposition",

            f"attachment; filename={visitor_id}.pdf"
        )

        msg.attach(part)

    except Exception as e:

        print(f"PDF Error: {e}")

        return False

    # =====================================================
    # SEND EMAIL
    # =====================================================

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

        text = msg.as_string()

        server.sendmail(

            sender_email,
            receiver_email,
            text
        )

        server.quit()

        print("Email Sent Successfully")

        return True

    except Exception as e:

        print(f"Email Error: {e}")

        return False
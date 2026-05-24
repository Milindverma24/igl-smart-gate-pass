from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

import os

# =========================
# GENERATE PDF
# =========================

def generate_pdf(

    visitor_data,
    photo_path,
    qr_path

):

    # =========================
    # CREATE FOLDER
    # =========================

    os.makedirs(
        "generated_passes",
        exist_ok=True
    )

    # =========================
    # PDF PATH
    # =========================

    pdf_path = f"""

generated_passes/{visitor_data['visitor_id']}.pdf

""".replace("\n", "")

    # =========================
    # PDF DOCUMENT
    # =========================

    doc = SimpleDocTemplate(

        pdf_path,

        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # =========================
    # IGL LOGO
    # =========================

    logo = Image(

        "assets/logo.png",

        width=120,

        height=120
    )

    elements.append(logo)

    elements.append(Spacer(1, 20))

    # =========================
    # TITLE
    # =========================

    title = Paragraph(

        "<b>IGL VISITOR GATE PASS</b>",

        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 30))

    # =========================
    # VISITOR INFO
    # =========================

    info = f"""

    <b>Visitor ID:</b> {visitor_data['visitor_id']}<br/><br/>

    <b>Name:</b> {visitor_data['name']}<br/><br/>

    <b>Phone:</b> {visitor_data['phone']}<br/><br/>

    <b>Company:</b> {visitor_data['company']}<br/><br/>

    <b>Purpose:</b> {visitor_data['purpose']}<br/><br/>

    <b>Meeting Person:</b> {visitor_data['person_to_meet']}<br/><br/>

    """

    elements.append(

        Paragraph(

            info,

            styles['BodyText']
        )
    )

    elements.append(Spacer(1, 30))

    # =========================
    # VISITOR PHOTO
    # =========================

    visitor_image = Image(

        photo_path,

        width=140,

        height=140
    )

    elements.append(visitor_image)

    elements.append(Spacer(1, 30))

    # =========================
    # QR CODE
    # =========================

    qr_image = Image(

        qr_path,

        width=140,

        height=140
    )

    elements.append(qr_image)

    elements.append(Spacer(1, 20))

    # =========================
    # FOOTER
    # =========================

    footer = Paragraph(

        "<b>IGL SECURITY DEPARTMENT</b><br/>Authorized Visitor Pass",

        styles['BodyText']
    )

    elements.append(footer)

    # =========================
    # BUILD PDF
    # =========================

    doc.build(elements)

    return pdf_path
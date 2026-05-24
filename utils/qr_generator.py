import qrcode
import os

def generate_qr(visitor_id):

    os.makedirs(
        "qr_codes",
        exist_ok=True
    )

    qr = qrcode.make(visitor_id)

    qr_path = f"qr_codes/{visitor_id}.png"

    qr.save(qr_path)

    return qr_path
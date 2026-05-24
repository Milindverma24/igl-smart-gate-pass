import sqlite3

conn = sqlite3.connect(
    "database/gatepass.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS visitors (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    visitor_id TEXT,

    name TEXT,

    phone TEXT,

    email TEXT,

    employee_email TEXT,

    company TEXT,

    purpose TEXT,

    person_to_meet TEXT,

    photo_path TEXT,

    qr_path TEXT,

    pdf_path TEXT,

    status TEXT,

    expiry_time TEXT

)

""")

conn.commit()

# =========================
# INSERT VISITOR
# =========================

def insert_visitor(

    name,
    phone,
    email,
    employee_email,
    company,
    purpose,
    person_to_meet,
    photo_path

):

    cursor.execute("""

    INSERT INTO visitors (

        name,
        phone,
        email,
        employee_email,
        company,
        purpose,
        person_to_meet,
        photo_path,
        status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        name,
        phone,
        email,
        employee_email,
        company,
        purpose,
        person_to_meet,
        photo_path,
        "Pending"

    ))

    conn.commit()

# =========================
# FETCH VISITORS
# =========================

def fetch_visitors():

    cursor.execute(
        "SELECT * FROM visitors"
    )

    return cursor.fetchall()
def update_visitor_status(

    visitor_id,
    status

):

    conn = sqlite3.connect(
        "database/gatepass.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """

        UPDATE visitors

        SET status=?

        WHERE id=?

        """,

        (

            status,
            visitor_id
        )
    )

    conn.commit()

    conn.close()
# =========================================================
# UPDATE VISITOR STATUS
# =========================================================

def update_visitor_status(

    visitor_id,
    status

):

    conn = sqlite3.connect(
        "database/gatepass.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """

        UPDATE visitors

        SET status=?

        WHERE id=?

        """,

        (

            status,
            visitor_id
        )
    )

    conn.commit()

    conn.close()
# =========================
# APPROVE VISITOR
# =========================

def approve_visitor(

    row_id,
    visitor_id,
    qr_path,
    pdf_path,
    expiry_time

):

    cursor.execute("""

    UPDATE visitors

    SET

        visitor_id = ?,
        qr_path = ?,
        pdf_path = ?,
        status = ?,
        expiry_time = ?

    WHERE id = ?

    """, (

        visitor_id,
        qr_path,
        pdf_path,
        "Approved",
        str(expiry_time),
        row_id

    ))

    conn.commit()
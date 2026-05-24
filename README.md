# igl-smart-gate-pass
# 🛡️ Smart Gate Pass System

AI-powered Smart Visitor Management & Gate Pass Automation System built using **Python**, **Streamlit**, and **SQLite**.

---

# 📌 Overview

The **Smart Gate Pass System** is a modern digital visitor management platform developed to automate and secure the visitor entry process for organizations, institutions, and industries.

The system replaces manual registers with a smart automated platform that supports:

✅ Visitor Registration  
✅ Admin Approval System  
✅ QR-Based Gate Passes  
✅ PDF Pass Generation  
✅ Email Notifications  
✅ Analytics Dashboard  
✅ Voice Alerts  
✅ Manual Pass Generation  
✅ Visitor Tracking  

---

# 🚀 Features

# 👤 Visitor Portal

- Visitor Registration Form
- Upload Visitor Image
- Camera Capture Support
- Mobile Number Validation
- Email Validation
- Optional Employee Email
- Purpose of Visit
- Person To Meet
- Visitor Request Submission

---

# 🔐 Admin Portal

- Secure Admin Login
- Visitor Approval System
- Visitor Rejection System
- Manual Pass Generation
- Search Visitors
- Filter Visitors
- Visitor Logs
- Check-In / Check-Out
- Auto Pass Expiry

---

# 🪪 Smart Gate Pass Generation

- Automatic Visitor ID Generation
- QR Code Generation
- PDF Gate Pass Creation
- Email Delivery of Pass
- Print Visitor Pass

---

# 📊 Analytics Dashboard

- Daily Visitors
- Monthly Visitors
- Visitor Status Analysis
- Approval Tracking
- Visitor Insights

---

# 📧 Email Automation

- Approval Emails
- Rejection Emails
- PDF Gate Pass Attachments
- Automated Notifications

---

# 🔊 Security Features

- Voice Alert System
- Visitor Tracking
- Auto Pass Expiry Detection
- Check-In / Check-Out Monitoring

---

# 📁 Export Reports

- Export CSV Reports
- Export Excel Reports
- Export PDF Reports

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Logic |
| Streamlit | Web Application |
| SQLite | Database |
| PIL | Image Processing |
| QRCode | QR Generation |
| smtplib | Email Automation |
| ReportLab | PDF Generation |
| Pandas | Data Analysis |
| Matplotlib | Charts & Analytics |

---

# 📂 Project Structure

```bash
SMART_GATE_PASS_SYSTEM/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── logo.png
│
├── database/
│   └── database.py
│
├── pages/
│   ├── visitor_form.py
│   ├── approvals.py
│   ├── admin_dashboard.py
│   ├── visitor_logs.py
│   ├── analytics.py
│   ├── manual_pass.py
│   └── export_reports.py
│
├── utils/
│   ├── email_sender.py
│   ├── id_generator.py
│   ├── pdf_generator.py
│   ├── qr_generator.py
│   └── voice_alert.py
│
└── visitor_photos/

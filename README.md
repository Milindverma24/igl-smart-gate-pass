Smart Gate Pass System

AI-powered Smart Visitor Management & Gate Pass Automation System built using Streamlit, Python, and SQLite.

⸻

📌 Project Overview

The Smart Gate Pass System is a modern visitor management platform designed to automate and digitize the complete gate entry process for organizations, institutions, and industries.

The system provides:

* Visitor registration
* Admin approvals
* QR-based gate passes
* PDF pass generation
* Email automation
* Visitor tracking
* Analytics dashboard
* Manual pass generation
* Voice alerts
* Security-focused management

This project eliminates manual register entries and improves security, efficiency, and visitor monitoring.

⸻

🚀 Features

👤 Visitor Portal

* Visitor Registration Form
* Upload Visitor Image
* Camera Capture Support
* Email Validation
* Phone Validation
* Optional Employee Email
* Purpose of Visit
* Person to Meet

⸻

🔐 Admin Portal

* Secure Admin Login
* Visitor Approval System
* Visitor Rejection System
* Search Visitors
* Filter Visitors
* Check-In / Check-Out
* Auto Pass Expiry

⸻

🪪 Smart Gate Pass Generation

* Automatic Visitor ID Generation
* QR Code Generation
* PDF Gate Pass Creation
* Email Delivery of Pass
* Manual Pass Generation
* Print Visitor Pass

⸻

📊 Analytics Dashboard

* Daily Visitors
* Monthly Visitors
* Visitor Status Tracking
* Approval Analytics
* Visitor Insights

⸻

📧 Email Automation

* Visitor Approval Emails
* Gate Pass Email Attachments
* Rejection Notifications

⸻

🔊 Security Features

* Voice Alert System
* Auto Visitor Tracking
* Pass Expiry Detection
* Check-In / Check-Out Monitoring

⸻

📁 Export Reports

* CSV Export
* Excel Export
* PDF Report Export

⸻

🛠️ Tech Stack

Technology	Usage
Python	Backend Logic
Streamlit	Web Application
SQLite	Database
PIL	Image Processing
QRCode	QR Generation
smtplib	Email Automation
ReportLab	PDF Generation
Pandas	Data Handling
Matplotlib	Analytics Charts

⸻

📂 Project Structure

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

⸻

⚙️ Installation Guide

1️⃣ Clone Repository

git clone https://github.com/Milindverma24/igl-smart-gate-pass.git

⸻

2️⃣ Navigate to Project

cd igl-smart-gate-pass

⸻

3️⃣ Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Mac/Linux

python3 -m venv venv
source venv/bin/activate

⸻

4️⃣ Install Dependencies

pip install -r requirements.txt

⸻

🔐 Environment Variables

Create a .env file in root directory:

EMAIL_USER=yourgmail@gmail.com
EMAIL_PASS=your_gmail_app_password

⸻

▶️ Run Application

streamlit run app.py

⸻

📸 Screenshots

🏠 Home Page

(Add Screenshot Here)

⸻

👤 Visitor Registration

(Add Screenshot Here)

⸻

🔐 Admin Dashboard

(Add Screenshot Here)

⸻

📊 Analytics Dashboard

(Add Screenshot Here)

⸻

🪪 Generated Gate Pass

(Add Screenshot Here)

⸻

🔄 Workflow

1. Visitor fills registration form
2. Admin receives request
3. Admin approves/rejects visitor
4. System generates:
    * Visitor ID
    * QR Code
    * PDF Gate Pass
5. Pass sent to visitor email
6. Visitor checks in/out
7. System tracks logs and analytics

⸻

🔒 Security Features

* Secure Admin Portal
* Email Authentication
* QR-based Verification
* Pass Expiry Mechanism
* Visitor Activity Tracking

⸻

📈 Future Enhancements

* Face Recognition
* Vehicle Number Plate Recognition
* WhatsApp Pass Delivery
* AI Suspicious Visitor Detection
* Cloud Database Integration
* RFID Integration
* Mobile Application
* Employee Approval Workflow
* CCTV Integration

⸻

👨‍💻 Author

Milind Verma

Student Coordinator — Null Community, VIT Bhopal

⸻

📄 License

This project is licensed under the MIT License.

⸻

⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

⸻

📬 Contact

For suggestions or collaborations:

📧 Email: your_email@gmail.com

⸻

🌟 Project Status

✅ Active Development
✅ GitHub Ready
✅ Deployment Ready
✅ Portfolio Ready

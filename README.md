# Patient Data Management System

**Final Semester Project – 6th Semester B.Tech CSE**  
**Course: Software Engineering**  
**SRM University – AP, Andhra Pradesh**  
**May 2024**

A secure web-based application built with Django to manage patient data, medical billing, and insurance claim verification while preventing fraud through role-based access and transparent record handling.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Now-brightgreen)](https://basheershaik.pythonanywhere.com)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green)](https://www.djangoproject.com/)

## 🚀 Live Demo

The complete working system is deployed and publicly available:  
👉 **https://basheershaik.pythonanywhere.com**

**How to explore the live site immediately:**

1. Open the link above
2. On the landing page, **scroll down a little** → you will see three login buttons at the bottom:
   - **Admin Login**
   - **Medical Login**
   - **Insurance Login**
3. Click any of them and use the test credentials below to log in and explore the system.

**Test Login Credentials** (created for reviewers / examiners / visitors):

| Role       | Username     | Password         |
|------------|--------------|------------------|
| Admin / Hospital | Hospital93   | Hospital@93      |
| Medical    | Medical93    | Medical@93       |
| Insurance  | Insurance93  | Insurance@93     |

**Important:** These are demo accounts with limited data. Feel free to explore, add test patients/bills, and verify the workflow.

## 📖 What Each Role Can Do After Login

### 1. Admin / Hospital Department (Hospital93)
- Register new patients and generate unique **Patient IDs**
- View and manage patient basic details
- Access all patient records and bills (read-only for most parts)
- Monitor overall system activity

### 2. Medical Department (Medical93)
- Search patients using their **Patient ID**
- Add treatment details, diagnoses, and **medical bills** for the patient
- Update existing records (if permitted)
- View history of bills and treatments added by them

### 3. Insurance Company (Insurance93)
- Search any patient using their **Patient ID**
- View all hospital-uploaded bills and medical records for that patient
- Cross-verify bills submitted by the hospital against patient claims
- Detect discrepancies or potential manipulation
- Approve / flag claims based on the transparent data

This role-based access ensures secure, auditable, and fraud-resistant processing of medical bills and insurance claims.

## ✨ Features

- Role-based authentication (3 user types)
- Patient registration with unique ID generation
- Secure medical bill entry and retrieval
- Cross-verification of hospital vs. patient-submitted bills
- Responsive and user-friendly interface
- SQLite database (easy for demo & portability)

## 🛠️ Tech Stack

- **Backend**: Django 5.0 (Python 3.10)
- **Frontend**: Django Templates, HTML5, CSS3, Bootstrap
- **Database**: SQLite (development & demo)
- **Deployment**: PythonAnywhere (free tier)

## 📁 Project Structure

Patient-Data-Management-System-using-Django/
├── HospitalAdmin/              # Django project root
│   ├── DemoApp/                # Main application (models, views, forms)
│   ├── HospitalAdmin/          # Settings, urls, wsgi
│   ├── manage.py
│   ├── Templates/              # HTML templates (html/ subfolder)
│   ├── static/                 # CSS, JS, images
│   └── db.sqlite3              # Database (not committed)
├── requirements.txt
└── README.md


## 🏁 Local Setup Instructions

1. Clone the repository (bash)
   git clone https://github.com/Basheershaik93/Patient-Data-Management-System-using-Django.git
   cd Patient-Data-Management-System-using-Django/HospitalAdmin
2. Create & activate virtual environment
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate   # macOS/Linux
3. Install dependencies and apply migrations
   pip install django
   python manage.py migrate
4. Run the server
   python manage.py runserver
## NOTE: Use the same test credentials above to log in locally.

## 📄 Full Project Report

The complete final report (including abstract, DFDs, ER diagram, use case diagrams, class/sequence diagrams, data dictionary, etc.) is available here:  
[Final Report - Patient Data Management System (DOCX/PDF)](https://1drv.ms/w/c/2978854f35982d77/IQCuAODgQPIWSY55AAe2KG8eAfMr8SrWpeQ6bhGIEnnnqhY?e=PIJPDn)

- Submitted to: SRM University – AP  
- For: Software Engineering Course (6th Semester Final Project)

## Acknowledgements

Guide: Mr. Hema Kumar Yarnagula, SRM University – AP
Team Members:
Shaik Basheer (AP21110011000)
Avanendra Sai (AP21110010997)
Kavya Bellamkonda (AP21110010990)
Khizar Ali (AP21110011003)


Special thanks to SRM University – AP for the opportunity to build this project as part of the Software Engineering course.
## Note
This is an academic project developed in the 6th semester (May 2024).
The live demo is hosted on a free PythonAnywhere account and may require monthly activity to remain online (takes ~10 seconds to extend).
Feel free to explore, test

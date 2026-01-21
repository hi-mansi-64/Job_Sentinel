#  JobSentinel
## Smart Job Authenticity & Scam Detection Platform

---

##  System Overview
JobSentinel is a smart web-based application designed to analyze job descriptions and determine whether a job posting is **Genuine**, **Suspicious**, or a **Likely Scam**.  
The system uses a **hybrid detection approach**, combining **Machine Learning**, **keyword-based risk analysis**, and **company verification logic** to generate accurate and explainable results.

---

##  Problem Statement
With the rapid growth of online job portals and social media hiring, fake job postings have become increasingly common.  
Many job seekers fall victim to scams involving:
- Registration fees  
- No interview selection  
- WhatsApp-only communication  
- Unrealistic salary promises  

Traditional verification methods are manual, time-consuming, and unreliable.

---

## 💡 Proposed Solution
JobSentinel provides an automated solution that:
- Analyzes job descriptions using a trained ML model  
- Detects high-risk and medium-risk scam keywords  
- Calculates a trust score  
- Verifies company presence  
- Displays a clear verdict with visual indicators  

This makes job verification **fast, reliable, and user-friendly**.

---

##  Tools & Technologies

### Frontend
- HTML5  
- CSS3  
- Bootstrap 5  
- JavaScript  

### Backend
- Python  
- Flask Framework  

### Machine Learning
- scikit-learn  
- TF-IDF Vectorizer  
- Trained Job Scam Classification Model  

### Database
- Microsoft SQL Server  
- pyodbc  

### Development Tools
- Visual Studio Code  
- Git (optional)

---

##  Detection Techniques

### Machine Learning Approach

Vectorization: TF-IDF

Model Used: Trained classification model (job scam detector)

Prediction Output: Probability of job being fake

Trust Score: Converted probability (0–100%)

### Risk Analysis Logic

High Risk Keywords: registration fee, no interview, whatsapp, pay to start

Medium Risk Keywords: earn, immediate, work from home, no experience


## 🏢 Company Verification Logic
The system checks for the presence of trusted company names such as:
TCS
Infosys
Wipro
Accenture
IBM

yaml
Copy code

### Verification Status
| Condition | Status |
|--------|--------|
| Trusted company detected | Verified |
| No company mentioned | Not Verified |
| Neutral case | Partially Verified |

---

## 🖥️ Application Features
- Job description input form  
- Animated circular trust score  
- Risk level classification  
- Company verification status  
- Keyword highlighting in job text  
- Clear verdict display  
- Database logging of job analysis  

---

## 🧾 Database Design

JobSentinel uses Microsoft SQL Server to store job analysis results securely.
Each job checked by the system is saved for verification and future reference.

### Database Schema (JobScamDB)

| Column Name   | Data Type  | Description                                           |
|---------------|-----------|-------------------------------------------------------|
| job_text      | NVARCHAR  | Original job description submitted by the user       |
| trust_score   | INT       | ML + keyword-based trust score (0–100)              |
| result        | NVARCHAR  | Final verdict (Genuine / Suspicious / Likely Scam)  |
| created_at    | DATETIME  | Timestamp when the job was analyzed (default: now)  |

### Purpose of Database

Each row = one job analysis request

Data stored automatically in SQL Server

Helps in audit, reporting, and future ML improvements

---

## How To Run

Download or clone the project repository from GitHub.

Ensure that Python is installed on your system.

Open the project folder in Command Prompt, PowerShell, or Terminal.

Install all required dependencies mentioned in the requirements.txt file.

Run the application using the main Python file.

Once the server starts, open any web browser.

Enter the local server address shown in the terminal (http://127.0.0.1:5000
).

The JobSentinel web interface will open and is ready to use.

---

## Why This Project Is Useful

Hybrid ML + rule-based detection approach

Visual trust score representation

Real-world scam pattern analysis

Explainable and transparent results

Easily extendable for major project

---
## Limitations

Model accuracy depends on training data quality

New scam patterns may require retraining

Company verification is keyword-based

##  Future Enhancements

Detailed reasoning engine & Advanced deep learning models

Job history dashboard

Export analysis reports

URL and domain credibility checking

Real-time web scraping

Cloud database integration

Online deployment

---

## Conclusion
JobSentinel is a practical, real-world focused project that helps users identify fake job postings efficiently.
Its hybrid detection approach makes it accurate, explainable, and suitable for academic as well as real-world use.

👩‍💻 Developed By

Himanshi Tripathi
(BCA Student)




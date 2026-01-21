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

### 1️⃣ Machine Learning Analysis
- Job descriptions are converted into numerical features using **TF-IDF Vectorization**.
- A trained ML model predicts the probability of the job being a scam.
- The output is converted into a percentage score.

---

### 2️⃣ Keyword Risk Analysis

#### 🔴 High Risk Keywords
registration fee
pay registration
no interview
whatsapp
bonus check
pay to start

#### 🟡 Medium Risk Keywords
earn
immediate
work from home
no experience

High-risk keywords strongly indicate scam behavior, while medium-risk keywords indicate suspicious intent.

---

### 3️⃣ Trust Score Calculation

Final Trust Score =
ML Prediction Score

(15 × High Risk Keywords)

(5 × Medium Risk Keywords)

(Maximum capped at 100%)

#### Example
- ML Score: 32%  
- High Risk Keywords: 4 → 60%  
- Medium Risk Keywords: 1 → 5%  
- **Final Trust Score: 97%**

This logic ensures that obvious scam jobs always appear as high risk.

---

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

---

## 🧾 Database Design

### Table: JobChecks

| Column Name | Description |
|------------|-------------|
| job_text | Job description |
| trust_score | Final trust score (%) |
| result | Verdict |

---

## Why This Project Is Unique
Hybrid ML + rule-based detection approach

Visual trust score representation

Real-world scam pattern analysis

Explainable and transparent results

Easily extendable for major project

---

##  Future Enhancements
Detailed reasoning engine

Job history dashboard

Export analysis reports

Cloud database integration

Online deployment

---

## Conclusion
JobSentinel is a practical, real-world focused project that helps users identify fake job postings efficiently.
Its hybrid detection approach makes it accurate, explainable, and suitable for academic as well as real-world use.

👩‍💻 Developed By

 Himanshi Tripathi

  (BCA Student)



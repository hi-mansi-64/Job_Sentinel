from flask import Flask, render_template, request
import joblib
import pyodbc
import re

app = Flask(__name__)

# 1 Load ML model & vectorizer
model = joblib.load("model/job_scam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# 2 Database connection
def get_db_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-86TT8PD;"
        "DATABASE=JobScamDB;"
        "Trusted_Connection=yes;"
    )

# 3 Risk keywords (weighted)
HIGH_RISK = [
    "registration fee",
    "pay registration",
    "no interview",
    "whatsapp",
    "bonus check",
    "pay to start"
]

MEDIUM_RISK = [
    "earn",
    "immediate",
    "work from home",
    "no experience"
]

# 4 Trusted companies list
TRUSTED_COMPANIES = [
    "tcs", "infosys", "wipro", "accenture", "ibm"
]

# 5 Routes
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/check', methods=['POST'])
def check():
    job_text = request.form['job_text']
    text = job_text.lower()

    # ---------- Keyword Detection ----------
    high_hits = [k for k in HIGH_RISK if k in text]
    medium_hits = [k for k in MEDIUM_RISK if k in text]
    detected_keywords = high_hits + medium_hits

    # ---------- ML Prediction ----------
    X = vectorizer.transform([job_text])
    prob = model.predict_proba(X)[0][1]   # Fake probability
    score = int(prob * 100)               # base score

    # ---------- Boost score with keywords ----------
    score += len(high_hits) * 15
    score += len(medium_hits) * 5
    score = min(score, 100)  # cap at 100%

    # ---------- FINAL VERDICT LOGIC ----------
    if len(high_hits) >= 1 or score >= 60:
        verdict = "Likely Scam"
        risk_level = "High Risk"
    elif len(medium_hits) >= 2 or 40 <= score < 60:
        verdict = "Suspicious"
        risk_level = "Medium Risk"
    elif score < 30 and len(detected_keywords) == 0:
        verdict = "Genuine"
        risk_level = "Low Risk"
    else:
        verdict = "Mostly Genuine (Be Cautious)"
        risk_level = "Medium Risk"

    # ---------- Company Verification ----------
    company_verified = "Partially Verified"  # default

    # 1 Check for trusted company names
    if any(c.lower() in text for c in TRUSTED_COMPANIES):
        company_verified = "Verified"
    # 2 Check if company is mentioned at all (simple heuristic: capitalized words > 2 letters)
    elif not re.search(r'\b[A-Z][a-zA-Z]{2,}\b', job_text):
        company_verified = "Company Not Mentioned"
    # 3 Suspicious contact info
    elif "whatsapp" in text or "gmail.com" in text:
        company_verified = "Not Verified"

    # 4 Save to Database ----------
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO JobChecks (job_text, trust_score, result) VALUES (?, ?, ?)",
            job_text, score, verdict
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("DB Error:", e)

    # 5 Render Result Page ----------
    return render_template(
        "result.html",
        score=score,
        verdict=verdict,
        risk_level=risk_level,
        company_status=company_verified,
        detected_high=high_hits,
        detected_medium=medium_hits,
        job_text=job_text
    )

# 6️ Run App
if __name__ == "__main__":
    app.run(debug=True)

import joblib

# Load ML model & vectorizer at the top
ml_model = joblib.load("model/job_scam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

@app.route('/check', methods=['POST'])
def check():
    text = request.form['job_text'].lower()
    
    # ML Prediction
    ml_vec = vectorizer.transform([text])
    prob_fake = ml_model.predict_proba(ml_vec)[0][1]  # fake probability
    ml_result = "Fake" if prob_fake >= 0.5 else "Genuine"
    ml_score = int(prob_fake * 100)
    
    # Keyword scoring (existing)
    score = sum(KEYWORDS[k] for k in KEYWORDS if k in text)
    
    # Combine logic (you can average or weight them)
    combined_score = int((ml_score + score) / 2)  # example
    if combined_score >= 50:
        result = "Fake"
    elif combined_score >= 30:
        result = "Caution"
    else:
        result = "Genuine"
    
    # Company verification
    company_keywords = ["inc", "pvt", "ltd", "llc", "corporation", "company"]
    company_name_present = any(k in text for k in company_keywords)
    company_status = "Verified" if company_name_present else "Not Verified"

    # Save to DB
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO JobChecks (job_text, trust_score, result) VALUES (?, ?, ?)",
            text, combined_score, result
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("DB Error:", e)

    return render_template(
        'result.html',
        score=combined_score,
        result=result,
        company_status=company_status
    )

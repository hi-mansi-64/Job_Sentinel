import pandas as pd
import re
import joblib
import numpy as np

feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

top_fake = sorted(zip(coefficients, feature_names), reverse=True)[:15]
top_genuine = sorted(zip(coefficients, feature_names))[:15]

print("Top Fake Indicators:")
for c, f in top_fake:
    print(f)

print("\nTop Genuine Indicators:")
for c, f in top_genuine:
    print(f)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
with open("model_report.txt", "w") as f:
    f.write(report)

# 1. Load dataset (FIXED: encoding + bad lines)
df = pd.read_csv("data/job_scam_clean.csv",
encoding="latin1",
on_bad_lines="skip",
engine="python"
)
df = df.fillna("")

# 2. Combine useful text fields
df["text"] = (
    df["title"] + " " +
    df["description"] + " " +
    df["requirements"] + " " +
    df["company_profile"]
)

# 3. Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\S+@\S+', ' email ', text)
    text = re.sub(r'http\S+', ' url ', text)
    text = re.sub(r'[^a-z ]', ' ', text)
    return text

df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["fraudulent"]

# 4. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    max_features=6000,
    stop_words="english",
    ngram_range=(1, 2)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 6. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# 7. Evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 8. Save model & vectorizer
joblib.dump(model, "model/job_scam_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

print("Model & Vectorizer saved successfully!")

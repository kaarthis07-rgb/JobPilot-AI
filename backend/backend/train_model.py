import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Sample training data
data = {
    "text": [
        "Python Machine Learning Data Science",
        "Java Spring Boot SQL",
        "Fake job earn money quickly no interview",
        "Immediate payment required to get job"
    ],
    "label": [1, 1, 0, 0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/job_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("AI Model trained successfully!")

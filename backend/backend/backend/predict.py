import joblib

model = joblib.load("model/job_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_job(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    if prediction == 1:
        return "Real Job"
    else:
        return "Fake Job"

if __name__ == "__main__":
    text = input("Enter job description: ")
    print(predict_job(text))

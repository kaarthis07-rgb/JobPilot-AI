from fastapi import FastAPI

app = FastAPI(title="JobPilot AI API")

@app.get("/")
def home():
    return {
        "message": "Welcome to JobPilot AI",
        "author": "Kaarthi S",
        "version": "1.0"
    }

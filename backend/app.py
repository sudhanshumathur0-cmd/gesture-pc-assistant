# backend/app.py

from fastapi import FastAPI

app = FastAPI(
    title="AI Gesture Assistant",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message":
        "AI Gesture Assistant Running"
    }


@app.get("/status")
def status():

    return {
        "status": "running"
    }

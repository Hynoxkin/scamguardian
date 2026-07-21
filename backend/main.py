from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Backend is working!"}


@app.post("/analyze")
def analyze(data: dict):
    message = data.get("message", "")

    return {
        "risk": 95,
        "type": "Bank Impersonation",
        "reason": f"You entered: {message}",
        "advice": "Do not click suspicious links."
    }
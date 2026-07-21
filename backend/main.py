from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv
import json # for result generated
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT")
)

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("EMAIL_ADDRESS"),
    MAIL_PASSWORD=os.getenv("EMAIL_PASSWORD"),
    MAIL_FROM=os.getenv("EMAIL_ADDRESS"),
    MAIL_PORT=465,
    MAIL_SERVER="smtp.mail.yahoo.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True
)

app = FastAPI()

# Allow React frontend to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is working!"}


@app.post("/analyze")
async def analyze(data: dict):
    message = data.get("message", "")

    # The message sent to AI model
    response = client.responses.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        input=f"""
    Return ONLY valid JSON.

    {{
    "risk": 94,
    "level": "HIGH",
    "type": "Bank Impersonation",
    "summary": "This SMS impersonates DBS to steal banking credentials.",
    "flags": [
        "Creates urgency",
        "Suspicious URL",
        "Threatens account suspension"
    ],
    "advice": [
        "Do not click the link.",
        "Open the official DBS app instead.",
        "Contact the bank if unsure."
    ]
    }}

    SMS:
    {message}
    """
    )

    # getting result from json
    result = json.loads(response.output_text)

    # advice email layout
    advice_text = "\n".join(f"• {item}" for item in result["advice"])

    # Message sent to caregiver email
    message = MessageSchema(
        subject="⚠️ ScamGuardian Alert",
        recipients=[os.getenv("CARETAKER_EMAIL")],
        body=f"""
    A potential scam has been detected.

    Risk: {result['risk']}
    Type: {result['type']}

    Flags:
    {', '.join(result['flags'])}

    Advice:
    {advice_text}
    """,
        subtype="plain"
    )

    fm = FastMail(conf)

    if result["level"] == "HIGH":
        await fm.send_message(message)

    # outputing result
    return {
    "analysis": result
}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    purpose: str
    tone: str
    recipient: str
    details: str

@app.get("/")
def home():
    return {"message": "Email Writer API running"}

@app.post("/generate-email")
def generate_email(data: EmailRequest):
    prompt = f"""
You are a professional email writer.

Generate:
- Subject
- Email body

Details:
Purpose: {data.purpose}
Tone: {data.tone}
Recipient: {data.recipient}
Context: {data.details}

Rules:
- Keep it clear and concise
- Use natural language
- Format properly
- Avoid repetition

Return format:

Subject: <subject line>

Body:
<email body>
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3.5:4b",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return {
            "success": True,
            "output": result.get("response", "")
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
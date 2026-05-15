from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask(req: PromptRequest):
    prompt = req.prompt
    try:
        resp = openai.responses.create(
            model="gpt-4o-mini",
            input=f'Return ONLY valid JSON with width and height for: "{prompt}"\nExample: {{"width": 100, "height": 100}}'
        )
        text = resp.output[0].content[0].text
        parsed = json.loads(text)  # safer than eval
    except Exception as e:
        print("OpenAI error:", e)
        parsed = {"width": 100, "height": 100}

    return parsed
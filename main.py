import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import uvicorn
from dotenv import load_dotenv

# Load secret environment variables from .env
load_dotenv()

app = FastAPI(title="OmniScript AI Engine")

# Fetch key from environment safely
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

class ScreenData(BaseModel):
    screen_text: str
    app_package_name: str

@app.post("/analyze-screen")
async def analyze_screen(data: ScreenData):
    try:
        prompt = f"Analyze this screen text from the Android app '{data.app_package_name}': {data.screen_text}. What exact button or text should the bot click next?"
        response = model.generate_content(prompt)
        return {"status": "success", "ai_decision": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

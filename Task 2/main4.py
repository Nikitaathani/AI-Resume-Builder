from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptData(BaseModel):
    project: str
    skills: str

@app.post("/build-prompt")
def build_prompt(data: PromptData):

    prompt = f"""
Generate ATS friendly bullet points.

Project:
{data.project}

Skills:
{data.skills}
"""

    return {
        "prompt": prompt
    }
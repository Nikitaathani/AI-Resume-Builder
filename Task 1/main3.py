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

class ResumeData(BaseModel):
    name: str
    role: str
    skills: str

@app.post("/generate")
def generate(data: ResumeData):
    return {
        "response": f"{data.name} is a {data.role} with skills in {data.skills}. Passionate about building innovative and scalable applications."
    }
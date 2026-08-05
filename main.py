from backend.schemas.syllabus import Syllabus
from backend.schemas.syllabus import Topics
from backend.weeklyOverview import weekOverview 
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os 
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API = os.getenv("DEEPSEEK_API")

app = FastAPI()

@app.post("/syllabus")
async def createOverview(syllabus: Syllabus):

    weeks = weekOverview(syllabus)
    return weeks

@app.post("/studyGuide")
async def createOverview(topics: Topics, DEEPSEEK_API):

    studyGuides = weekOverview(topics, DEEPSEEK_API)
    return studyGuides


app.mount("/", StaticFiles(directory = ".", html=True), name = "static")


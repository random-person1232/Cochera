from backend.schemas.syllabus import Syllabus
from backend.schemas.syllabus import Topics
from backend.weeklyOverview import weekOverview 
from backend.studyGuide import createGuide
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os 
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API = os.getenv("DEEPSEEK_API")
TAVILY_API = os.getenv("TAVILY_API")

app = FastAPI()

@app.post("/syllabus")
def createOverview(syllabus: Syllabus):

    weeks = weekOverview(syllabus, DEEPSEEK_API)
    return weeks

@app.post("/studyGuide")
def generateGuide(topics: Topics):

    materials = createGuide(topics, DEEPSEEK_API, TAVILY_API)
    return materials


app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

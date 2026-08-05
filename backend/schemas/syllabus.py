from pydantic import BaseModel

class Syllabus(BaseModel):
    subject: str
    length: int
    weeks: int = 8
    goal: str 

class Topics(BaseModel):
    weeks: list
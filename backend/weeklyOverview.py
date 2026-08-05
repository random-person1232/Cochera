from openai import OpenAI
from backend.schemas.syllabus import Syllabus
import json



def weekOverview(syllabus: Syllabus, DEEPSEEK_API):
    
    subject = syllabus.subject
    weeks = syllabus.weeks
    goal = syllabus.goal

    client = OpenAI(api_key=DEEPSEEK_API,  base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-v4-flash", 
        messages=[
            {"role": "system", "content": "You are a teacher with "
            "40+ years of experience teaching " + subject},
{       
    "role": "user",
    "content":
        f"""Generate a week-by-week study plan overview.

The subject is: {subject}
Duration: {weeks} weeks
Goal: {goal}

Return exactly {weeks} topics, one topic for each week. Each week's topic should
be a unique sub-topic of the subject, by the end of the course, the learner has
a comprehensive understanding of the subject.

Return ONLY valid JSON.
Do not include markdown, explanations, or code fences.

The output must have this format:
[
"Week 1 topic",
"Week 2 topic",
"Week 3 topic"
]

A example will be the following:

The subject is: JavaScript
Duration: Six weeks
Goal: Client Side JavaScript

Output:

[
"The DOM",
"Events",
"User Inputs",
"Backend Communication",
"Async JavaScript",
"Browser APIs"
]
"""
}
        ],
        temperature=0.7,
        stream=False
    )

    topicList = json.loads(response.choices[0].message.content)
    return topicList
from openai import OpenAI
import json
from backend.schemas.syllabus import Topics
from backend.webSearch import websearch
def createGuide(topics: Topics, DEEPSEEK_API, TAVILY_API):

    client = OpenAI(api_key=DEEPSEEK_API,  base_url="https://api.deepseek.com")

    weeklyTopics = topics.weeks

    for week in weeklyTopics:
        response = client.chat.completions.create(
            model="deepseek-v4-flash", 
            messages=[
                {"role": "system", "content": "You are a Google power searcher with extensive knowledge on "+week},
    {       
        "role": "user",
        "content": """
    I want to find high quality learning materials about {week}. I want you to generate a list of 
    search keywords that point to reliable articles and videos about the topic. I will run
    the keywords through Tavily, a search API to grab sources. Output the key phrases in a list.
    There should be around five key phrases.

    Reference the example below:
    Input: Javascript DOM
    Output: [
    "JavaScript DOM manipulation MDN",
    "JavaScript DOM events tutorial",
    "JavaScript DOM structure",
    "querySelector vs getElementById JavaScript",
    "JavaScript event delegation"
    ]
    """
    }
    ],
        temperature=0.7,
        stream=False
    )        
    keywords = json.loads(response.choices[0].message.content)
    URLs = websearch(keywords, DEEPSEEK_API, TAVILY_API)
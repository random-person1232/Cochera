from openai import OpenAI
import json
from backend.schemas.syllabus import Topics
from backend.webSearch import websearch
def createGuide(topics: Topics, DEEPSEEK_API, TAVILY_API):

    client = OpenAI(api_key=DEEPSEEK_API,  base_url="https://api.deepseek.com")

    materials = {}
    for week in topics.weeks:
        prompt = (
            f"I want to find high-quality learning materials about {week}. "
            "Generate around five search keyword phrases that point to reliable "
            "articles and videos about the topic. I will run them through Tavily, "
            "a search API.\n\n"
            "Respond ONLY with a JSON object in this exact structure:\n"
            '{"keywords": ["phrase 1", "phrase 2", "phrase 3", "phrase 4", "phrase 5"]}\n\n'
            "Example — input: JavaScript DOM\n"
            '{"keywords": ["JavaScript DOM manipulation MDN", '
            '"JavaScript DOM events tutorial", "JavaScript DOM structure", '
            '"querySelector vs getElementById JavaScript", "JavaScript event delegation"]}'
        )
        response = client.chat.completions.create(
            model="deepseek-v4-flash", 
            messages=[
                {"role": "system", "content": "You are a Google power searcher with extensive knowledge on "+week},
                {       
                    "role": "user",
                    "content": prompt
                }
                    ],
                temperature=0.7,
                stream=False,
                response_format= {"type":"json_object"}
            )        
        keywords = json.loads(response.choices[0].message.content)["keywords"]
        URLs = websearch(week, keywords, DEEPSEEK_API, TAVILY_API)

        materials.update({week: URLs})
    return materials


# Returns {week1: [URLs], week2: [URLs], ...}

from tavily import TavilyClient
from openai import OpenAI
import json

def websearch(week, keywords, DEEPSEEK_API, TAVILY_API):
    tavily = TavilyClient(api_key=TAVILY_API)

    URLs = []
    
    for keyword in keywords:
        response = tavily.search(
            query = keyword,
            max_results = 5
        )
        client = OpenAI(api_key=DEEPSEEK_API,  base_url="https://api.deepseek.com")
        prompt = (
            f"I want to learn about {week}. Below are search results from a scraper. "
            "Read each snippet and its source, and pick the TWO URLs that would help me "
            "learn the most. Prioritize reliable, high-quality content. You may consider "
            "the Tavily relevance score but do not rely on it solely.\n\n"
            "Respond ONLY with a JSON object in exactly this structure, no other text:\n"
            '{"results": [{"title": "...", "url": "...", "content": "..."}, '
            '{"title": "...", "url": "...", "content": "..."}]}\n\n'
            f"Here are the search results:\n{json.dumps(response, indent=2)}"
        )

        selections = client.chat.completions.create(
            model="deepseek-v4-flash", 
            messages=[
                {"role": "system", "content": "You are a experienced text analyzer"},
                {       
                    "role": "user",
                    "content": prompt
                }
                ],
                    temperature=0.7,
                    stream=False,
                    response_format={"type":"json_object"}
                )      
        raw = selections.choices[0].message.content
        picked = json.loads(raw)["results"]
        URLs.append(picked)

    return URLs


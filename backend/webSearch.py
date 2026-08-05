from tavily import TavilyClient
from openai import OpenAI

def websearch(keywords, DEEPSEEK_API, TAVILY_API):
    tavily = TavilyClient(api_key=TAVILY_API)

    for keyword in keywords:
        response = tavily.search(keyword)

        client = OpenAI(api_key=DEEPSEEK_API,  base_url="https://api.deepseek.com")


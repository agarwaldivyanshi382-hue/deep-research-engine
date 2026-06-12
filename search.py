from tavily import TavilyClient
from dotenv import load_dotenv

import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_sources(query):

    results = client.search(
        query=f"{query} research paper",
        search_depth="advanced",
        max_results=10,
        include_answer=True
    )

    return results
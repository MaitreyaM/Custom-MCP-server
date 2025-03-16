from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import asyncio
import httpx
from bs4 import BeautifulSoup
from brave_search_python_client import BraveSearch, WebSearchRequest

load_dotenv()

user_agent = "docs-app/1.0"
docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
}

mcp = FastMCP("docs")

async def search_web(query: str):
    """
    Use the Brave Search API to perform a web search.
    """
    brave_api_key = os.getenv("BRAVE_SEARCH_API_KEY")
    if not brave_api_key:
        raise ValueError("BRAVE_SEARCH_API_KEY not set in environment")
    
    brave_client = BraveSearch(api_key=brave_api_key)
    request = WebSearchRequest(q=query, count=5, search_lang="en")
    result = await brave_client.web(request)
    return result.dict()

async def fetch_url(url: str):
    """
    Fetch the content of a URL and return its text.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            content_div = soup.find("div", class_="main-content")
            return content_div.get_text() if content_div else soup.get_text()
        except httpx.TimeoutException:
            return "Timeout error"

@mcp.tool()
async def get_docs(query: str, library: str):
    """
    Search the latest docs for a given query and library.
    Supports langchain, openai, and llama-index.

    Args:
        query: The query to search for (e.g. "Chroma DB")
        library: The library to search in (e.g. "langchain")

    Returns:
        Text from the docs.
    """
    if library not in docs_urls:
        raise ValueError(f"Library {library} not supported by current docs_mcp")
    
    # Append a space between site URL and query.
    search_query = f"site:{docs_urls[library]} {query}"
    results = await search_web(search_query)
    
    
    if not results.get("web", {}).get("results"):
        return "No results found"

    text = ""
    for result in results["web"]["results"]:
        # The URL is likely in the "url" field rather than "link"
        text += await fetch_url(result["url"])
        return text

if __name__ == "__main__":
    mcp.run(transport="stdio")
from langchain.tools import tool
from tools.web.search_internet_tools import SearchInternetTools


@tool("Search instagram")
def search_instagram(query):
    """Useful to search for instagram post about a given topic and return relevant
    results."""
    query = f"site:instagram.com {query}"
    return SearchInternetTools.search_google_new(query)
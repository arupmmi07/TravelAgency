from crewai import Agent
from textwrap import dedent

from llm.llm_manager import LLMManager
from tools.web.search_internet_tools import SearchInternetTools


class CityExpertAgent:
    def __init__(self):
        pass

    def city_expert_agent():
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchInternetTools.search_internet],
            verbose=True,
            allow_delegation=True,
            max_iter=15,
            llm=LLMManager(
                llm_name="llama2"
            ).connect()
        )
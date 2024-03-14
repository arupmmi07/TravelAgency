from crewai import Agent
from textwrap import dedent
from lms.openai import openai_model

from tools.search_tools import SearchTools


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
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=openai_model('gpt-4'),
        )
from crewai import Agent
from textwrap import dedent

from tools.search_tools import SearchTools


class LocalGuideAgent:
    def __init__(self):
        pass

    def local_tour_guide_agent():
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information
        about the city, it's attractions and customs"""),
            goal=dedent(
                f"""Provide the BEST insights about the selected city"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
            max_iter=15
        )
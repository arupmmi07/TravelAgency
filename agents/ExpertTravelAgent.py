from crewai import Agent
from textwrap import dedent

from tools.web.search_internet_tools import SearchInternetTools
from tools.others.calculator_tools import CalculatorTools


class ExpertTravelAgent:
    def __init__(self):
        pass

    def expert_travel_agent(noofdays=7):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                f"""Expert in travel planning and logistics. 
                I have decades of expereince making travel iteneraries."""),
            goal=dedent(f"""
                        Create a {noofdays}-day travel itinerary with detailed per-day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[
                SearchInternetTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            allow_delegation=True,
            max_iter=15
        )
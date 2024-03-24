"""Test Agent creation and execution basic functionality."""

from unittest.mock import MagicMock, patch

from pydantic import BaseModel, Field
from pydantic_core import ValidationError

from crewai import Agent, Crew, Process, Task
from crewai_tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

from llm.llm_manager import LLMManager

from textwrap import dedent
from crewai_tools import SerperDevTool
from langchain.tools import tool
import os
from tools.web.search_internet_tools import SearchInternetTools

from dotenv import load_dotenv
load_dotenv()


# search_tool = SerperDevTool()

class Output(BaseModel):
    agent: str = Field(
        description="Name of the agent"
    )
    tasks: list[str] = Field(
        description="list of tasks performed by the agent"
    )


agency_type = "Travel Planner"
agency_description = dedent(
            f"""I want to create a {agency_type} agency, give me a list of agents and their 
            respective roles and tasks in a jason format, try to create roles and tasks as fine-grained as possible""")

def agencyAnalyser(type, agency_description):

    researcher = Agent(
        role="Researcher",
        goal="Make the best research and analysis on content about {type}",
        backstory=dedent(
            f"""You're an expert researcher, specialized in {agency_type}. You work as a freelancer
            who help customer to setup their own {agency_type} agency
            and is now working on doing research and analysis for a new customer."""
        ),
        tools=[SearchInternetTools.search_internet],
        allow_delegation=False,
        # output_json=Output,
        # output_pydantic=Output,
        verbose=True,
        llm=LLMManager(
            llm_name="mistral"
        ).connect()
    )

    task = Task(
        description=agency_description,
        expected_output="Give results in json format",
        agent=researcher,
    )

    crew = Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.hierarchical,
        verbose=2,
        manager_llm=LLMManager(
            llm_name="llama2"
        ).connect()
    )

    result=crew.kickoff()

    print("********************************")
    print(result)


agencyAnalyser(agency_type, agency_description)
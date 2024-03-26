"""Test Agent creation and execution basic functionality."""

from unittest.mock import MagicMock, patch
import uuid

from pydantic import UUID4, BaseModel, Field
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
    role: str = Field(
        description="Role of the agent"
    )
    tasks: list[str] = Field(
        description="list of tasks performed by the agent"
    )
    id: UUID4 = Field(
        default_factory=uuid.uuid4,
        frozen=True,
        description="Unique identifier for the object, not set by user.",
    )


agency_type = "IAS IPS Coaching"
agency_description = dedent(
            f"""I want to create a {agency_type} agency, give me a list of agents and their 
            respective roles and tasks in a jason format, try to create roles and tasks as fine-grained as possible""")

def agencyAnalyser(type, agency_description):

    researcher = Agent(
        role="Researcher",
        goal="Make the best research and analysis on content about {type}",
        backstory=dedent(
            f"""You're specialized in {agency_type} agency setup. You work as a freelancer
            who help customer to setup their own {agency_type} agency
            and is now working on doing research and analysis for a new customer that how many 
            agents they need and what should be role of these agents and what tasks they should perform."""
        ),
        tools=[SearchInternetTools.search_internet],
        allow_delegation=True,
        verbose=True,
        llm=LLMManager(
            llm_name="gpt-3.5-turbo"
        ).connect()
    )

    task = Task(
        description=agency_description,
        expected_output='',
        agent=researcher,
        # output_json=Output,
        output_pydantic=Output,
        output_file="output.json"
    )

    crew = Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.hierarchical,
        verbose=2,
        allow_delegation=True,
        manager_llm=LLMManager(
            llm_name="gpt-4"
        ).connect()
    )

    result=crew.kickoff()

    print("********************************")
    print(result)


agencyAnalyser(agency_type, agency_description)
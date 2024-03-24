from textwrap import dedent
from TravelAgency import TravelAgency

import os

from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Our Travel Planner Agency ##")
    print('-------------------------------')
    origin = input(
        dedent("""
      From where will you be traveling from?
    """))
    cities = input(
        dedent("""
      What are the cities options you are interested in visiting?
    """))
    date_range = input(
        dedent("""
      What is the date range you are interested in traveling?
    """))
    noofdays = input(
        dedent("""
      For how many day you are interested in traveling?
    """))
    interests = input(
        dedent("""
      What are some of your high level interests and hobbies?
    """))

    travel_agency = TravelAgency(origin, cities, date_range, interests)
    result = travel_agency.run()
    print("\n\n########################")
    print("## Here is you Travel Plan")
    print("########################\n")
    print(result)
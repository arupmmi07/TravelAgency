from agents.ExpertTravelAgent import ExpertTravelAgent
from agents.CityExpertAgent import CityExpertAgent
from agents.LocalGuideAgent import LocalGuideAgent
from llm.llm_manager import LLMManager

from tasks import TravelTasks
from crewai import Crew, Process



class TravelAgency:
    def __init__(self, origin, cities, date_range, interests, noofdays=7):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests
        self.noofdays = noofdays

    def run(self):
        # Define your custom agents and tasks under agents and tasks modules
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = ExpertTravelAgent.expert_travel_agent(self.noofdays)
        city_selection_agent = CityExpertAgent.city_expert_agent()
        local_tour_guide_agent = LocalGuideAgent.local_tour_guide_agent()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests,
            self.noofdays
        )

        identify_city = tasks.identify_city(
            city_selection_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                    expert_travel_agent,
                    city_selection_agent,
                    local_tour_guide_agent
                    ],
            tasks=[
                plan_itinerary,
                identify_city,
                gather_city_info
            ],
            process=Process.hierarchical,
            verbose=2,
            manager_llm=LLMManager(
                llm_name="llama2"
            ).connect()
        )

        result = crew.kickoff()
        return result
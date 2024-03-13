from agents.agents import TravelAgents
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
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent(self.noofdays)
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests,
            self.noofdays
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent,
                    city_selection_expert,
                    local_tour_guide
                    ],
            tasks=[
                plan_itinerary,
                identify_city,
                gather_city_info
            ],
            process=Process.HIGH_ACCURACY,
            verbose=True,
        )

        result = crew.kickoff()
        return result
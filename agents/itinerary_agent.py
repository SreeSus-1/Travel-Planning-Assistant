from agents.base_agent import BaseAgent

class ItineraryBuilderAgent(BaseAgent):
    def run(self, destination: str, budget: str, interests: str, days: int) -> str:
        prompt = f"""
        You are an Itinerary Builder Agent.

        Create a clear day-by-day travel plan for:
        Destination: {destination}
        Budget: {budget}
        Interests: {interests}
        Number of Days: {days}

        For each day, include:
        - morning
        - afternoon
        - evening

        Keep the itinerary realistic and aligned with the budget.
        """
        return self.call_ollama(prompt)
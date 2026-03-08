from agents.base_agent import BaseAgent

class CostEstimatorAgent(BaseAgent):
    def run(self, destination: str, budget: str, itinerary: str) -> str:
        prompt = f"""
        You are a Cost Estimator Agent.

        Estimate the likely travel cost for this trip.

        Destination: {destination}
        Budget: {budget}
        Itinerary:
        {itinerary}

        Break down:
        - stay
        - food
        - local transport
        - attraction/activity costs
        - overall estimate

        Mention whether the trip seems within budget.
        """
        return self.call_ollama(prompt)
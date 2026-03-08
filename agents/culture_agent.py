from agents.base_agent import BaseAgent

class LocalCultureCoachAgent(BaseAgent):
    def run(self, destination: str, interests: str) -> str:
        prompt = f"""
        You are a Local Culture Coach Agent.

        Provide helpful cultural and travel advice for:
        Destination: {destination}
        Interests: {interests}

        Include:
        - local etiquette
        - food recommendations
        - transport tips
        - safety suggestions
        - cultural experiences relevant to the interests
        """
        return self.call_ollama(prompt)
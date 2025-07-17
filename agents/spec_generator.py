from .base_agent import BaseAgent

class SpecGenerator(BaseAgent):
    def generate_spec(self, user_description: str) -> str:
        prompt = f"""
        You are an expert API architect. Based on this description, generate an OpenAPI 3.0 specification:

        "{user_description}"

        Return only the YAML.
        """
        return self.run_prompt(prompt)
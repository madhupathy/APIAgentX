from .base_agent import BaseAgent

class TestGenAgent(BaseAgent):
    def generate_tests(self, openapi_spec: str) -> str:
        prompt = f"""
        Create pytest unit tests for the API endpoints defined in the following OpenAPI spec:

        {openapi_spec}
        """
        return self.run_prompt(prompt)
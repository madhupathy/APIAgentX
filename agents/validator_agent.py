from .base_agent import BaseAgent

class ValidatorAgent(BaseAgent):
    def validate_spec(self, openapi_spec: str) -> str:
        prompt = f"""
        Validate the following OpenAPI spec. List any issues, improvements or missing components:

        {openapi_spec}
        """
        return self.run_prompt(prompt)
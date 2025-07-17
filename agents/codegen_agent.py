from .base_agent import BaseAgent

class CodeGenAgent(BaseAgent):
    def generate_code(self, openapi_spec: str) -> str:
        prompt = f"""
        Convert this OpenAPI 3.0 spec into Python FastAPI server code with endpoints and request models:

        {openapi_spec}
        """
        return self.run_prompt(prompt)
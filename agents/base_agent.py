import os
from langchain.llms import HuggingFaceHub

class BaseAgent:
    def __init__(self, model="mistralai/Mistral-7B-Instruct-v0.1"):
        self.llm = HuggingFaceHub(
            repo_id=model,
            model_kwargs={"temperature": 0.7, "max_new_tokens": 800},
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )

    def run_prompt(self, prompt):
        return self.llm(prompt)
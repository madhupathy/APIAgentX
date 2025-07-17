from agents.spec_generator import SpecGenerator
from agents.validator_agent import ValidatorAgent
from agents.codegen_agent import CodeGenAgent
from agents.testgen_agent import TestGenAgent

class APILifecycleChain:
    def __init__(self):
        self.spec_agent = SpecGenerator()
        self.validate_agent = ValidatorAgent()
        self.codegen_agent = CodeGenAgent()
        self.testgen_agent = TestGenAgent()

    def run(self, input_description: str):
        spec = self.spec_agent.generate_spec(input_description)
        validation = self.validate_agent.validate_spec(spec)
        code = self.codegen_agent.generate_code(spec)
        tests = self.testgen_agent.generate_tests(spec)

        return {
            "spec": spec,
            "validation": validation,
            "code": code,
            "tests": tests
        }
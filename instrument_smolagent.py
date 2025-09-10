from openinference.instrumentation.smolagents import SmolagentsInstrumentor

SmolagentsInstrumentor().instrument()

from smolagents import CodeAgent, InferenceClientModel

agent = CodeAgent(tools=[], model=InferenceClientModel())
alfred_agent = agent.from_hub("sergiopaniego/AlfredAgent", trust_remote_code=True)
alfred_agent.run(
    "Give me the best playlist for a party at Wayne's mansion. The party idea is a 'villain masquerade' theme"
)

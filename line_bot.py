from strands import Agent
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
bedrock_model = BedrockModel(
    region_name="us-west-2",
    model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
)
agent = Agent(
    model=bedrock_model,
    system_prompt="You are a helpful AI assistant"
 )

@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    user_message = payload.get("prompt","Hello")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()

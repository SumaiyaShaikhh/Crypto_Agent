# pip install openai-agents
# pip install python-dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Crypto Agent
crypto_agent = Agent(
    name = 'Crypto Agent',
    instructions= 
    """You are a cryptocurrency price assistant.

- When a user asks about a coin (e.g., Bitcoin, ETH), fetch and return the **current price in USD**.
- Mention the **source** (e.g., CoinGecko, CoinMarketCap) and the **time of the data**.
- If the user asks for trends, provide **7-day and 30-day changes**.
- Only use reliable APIs, and return results cleanly (no explanation unless asked)."""
)

# Color codes
CYAN = "\033[96m"
RESET = "\033[0m"

print("Hi there! I'm your smart guide to the Crypto Universe.")
print("Type EXIT when done ")


while True:
    user_input = input("Got Crypto Questions? Get Answers Here: ")
    
    if user_input == "exit":
        break
    
    else:
        response = Runner.run_sync(
    crypto_agent,
    input=user_input,
    run_config=config
)
    print(f"{CYAN}{response.final_output}{RESET}\n")
import asyncio
import os

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from dotenv import load_dotenv

load_dotenv()

agent1 = Agent(
    OpenAIChatModel("deepseek-flash",provider=DeepSeekProvider(api_key=os.getenv("DEEPSEEK_API_KEY"))),
)

async def main():
    result = await agent1.run("hello!")
    print(result)



if __name__ == "__main__":
    asyncio.run(main())

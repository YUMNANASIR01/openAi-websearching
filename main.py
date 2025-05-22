from dotenv import load_dotenv
from agents import Agent, FileSearchTool,Runner, WebSearchTool
load_dotenv()  # Yeh .env file ko load kareg
import chainlit as cl

# ---------------------------------------------------------------------
agent= Agent(
    model="gpt-4.1-mini" ,
    name= "my_agent",
    # instructions= "you are a helpful assistant,always search in file for information",
    tools=[
           WebSearchTool(),
           FileSearchTool(
            max_num_results=3,
            vector_store_ids=["vs_682f21a9eccc8191a5cf6198681860ec"],),
    ]
)
# -------------------------------------------------------------
@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    res = Runner.run_sync(agent, user_input)
    await cl.Message(content=res.final_output).send()




  
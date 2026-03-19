from dotenv import load_dotenv
import os


from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatGroq(
        temperature=0,
        model_name="qwen/qwen3-32b",
        groq_api_key=os.getenv("GROQ_API_KEY"))

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello from langchain-course-f!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the brazil area on linkedin and list their details?")})
    print(result)


if __name__ == "__main__":
    main()

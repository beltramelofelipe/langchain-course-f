from dotenv import load_dotenv
import os


from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result    
    """
    print(f"Search for {query}")
    return "Tokyo weather is sunny"

llm = ChatGroq(
        temperature=0, 
        model_name="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"))

tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello from langchain-course-f!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokio?")})
    print(result)


if __name__ == "__main__":
    main()

from .tools import search
from langgraph.prebuilt import create_react_agent
from load_llm import load_model

llm = load_model()

technical_agent = create_react_agent(llm, tools=[search],
                                     prompt = (
        "You are a helpful technical support agent. The user is having a technical issue. "
        "Use available tools or your knowledge to assist them. If needed, ask follow-up questions. "
       
    ))
product_info_agent = create_react_agent(llm, tools=[search], 
                                        prompt = (
        "You are a customer service agent providing product information. "
        "The user wants to know more about a product. "
        "Use the search tool to find relevant information if necessary. "
        
    ))
general_support_agent = create_react_agent(llm, tools=[search],
                                           prompt = (
        "You are a general customer support assistant. Help the user with their question or request. "
        "Be friendly and concise. Use search if needed. "
        
    ))


from langgraph.prebuilt import create_react_agent
from load_llm import load_model
from .state import NonRefundState, RequestType
from .agents import technical_agent, product_info_agent, general_support_agent



llm = load_model()

def define_request(state: NonRefundState) -> NonRefundState:
    message = state.get("messages", "")

    request_type = llm.with_structured_output(RequestType).invoke(message)
    state["request_type"] = request_type["type"]
    return state
    

def route_request(state: NonRefundState) -> str:
    request_type = state.get("request_type", "")
    print("ROUTE REQUEST got:", request_type, state)

    if request_type == "technical_support":
        return "technical_support_node"
    elif request_type == "product_info":
        return "product_info_node"
    else:
        return "general_support_node"

def technical_support_node(state: NonRefundState) -> dict:
    
    response = technical_agent.invoke({"messages": state['messages']})
    return {"messages": [response['messages'][-1]]}

def product_info_node(state: NonRefundState) -> dict:
    
    response = product_info_agent.invoke({"messages": state['messages']})
    print(response,"\n\n")
    return {"messages": [response['messages'][-1]]}


def general_support_node(state: NonRefundState) -> dict:
    
    response = general_support_agent.invoke({"messages": state['messages']})
    return {"messages": [response['messages'][-1]]}        
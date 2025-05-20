from refund_agent.graph import create_refund_graph
from non_refund_agent.graph import create_non_refund_agent
from langgraph.graph import StateGraph, START
from nodes import classifier, route_when_refundable
from state import SomeState
from langgraph.checkpoint.memory import MemorySaver
from load_llm import _set_env
import os


def create_customer_support_agent():
    """
    Creates and compiles a customer support agent graph for handling user complaints.

    This agent uses LangGraph to route incoming user messages through a classification step
    and dispatches them to the appropriate sub-agent depending on whether the complaint is refundable
    or not.

    Workflow:
        1. The user message enters at the START node.
        2. The `classifier` node determines whether the message qualifies for a refund.
        3. Based on the classifier's result:
            - If refundable, the message is routed to the `refund_agent` graph.
            - Otherwise, it is routed to the `complaint_agent` graph for non-refund assistance.

    Returns:
        A compiled LangGraph instance with in-memory checkpointing enabled.
    """
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "customer support_agent"
    _set_env("LANGSMITH_API_KEY")

    # Create subgraphs for handling refund and non-refund cases
    refund_graph = create_refund_graph()
    non_refund_graph = create_non_refund_agent()
    
    # Initialize the main graph with the expected state structure
    graph = StateGraph(SomeState)
    graph.add_node("classifier", classifier) 
    graph.add_node("refund_agent", refund_graph)
    graph.add_node("complaint_agent", non_refund_graph)

    graph.add_edge(START, "classifier")
    graph.add_conditional_edges(
        "classifier",
        route_when_refundable,
        {
            "refund_agent": "refund_agent",
            "complaint_agent": "complaint_agent",
        },
    )
    return graph.compile(checkpointer=MemorySaver())

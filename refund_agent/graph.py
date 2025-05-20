from .state import RefundState
from .nodes import (get_receipt_node, financial_manager, update_user_node,
                    process_refund, route_refund, 
                    route_refund_based_on_financial_manager)

from langgraph.graph import StateGraph, START



def create_refund_graph():
    '''
    create a refund graph
    '''
    graph = StateGraph(RefundState)
    graph.add_node("get_receipt_node", get_receipt_node)
    graph.add_node("financial_manager", financial_manager)
    graph.add_node("process_refund", process_refund)
    graph.add_node("update_user_node", update_user_node)

    # Define edges
    graph.add_edge(START, "get_receipt_node")
    graph.add_conditional_edges(
        "get_receipt_node",
        route_refund,  # Pass the callable function here
        {
            "financial_manager": "financial_manager",
            "update_user_node": "update_user_node",
        },
    )
    graph.add_conditional_edges(
        "financial_manager",
        route_refund_based_on_financial_manager,
        {
            "process_refund": "process_refund",
            "update_user_node": "update_user_node",
        },
    )
    return graph.compile(interrupt_before=['financial_manager'])
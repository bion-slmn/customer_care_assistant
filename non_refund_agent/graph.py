from .nodes import (define_request, technical_support_node, 
                    product_info_node, general_support_node, route_request)
from langgraph.graph import StateGraph, START
from .state import NonRefundState



def create_non_refund_agent():
    graph = StateGraph(NonRefundState)

    graph.add_node("define_request", define_request)
    graph.add_node("technical_support_node", technical_support_node)
    graph.add_node("product_info_node", product_info_node)
    graph.add_node("general_support_node", general_support_node)  # Fixed

    graph.add_edge(START, "define_request")
    graph.add_conditional_edges(
        "define_request",
        route_request,
        {
            "technical_support_node": "technical_support_node",
            "product_info_node": "product_info_node",
            "general_support_node": "general_support_node",  # Fixed key
        },
    )

    return graph.compile()
    
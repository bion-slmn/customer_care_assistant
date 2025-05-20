from typing import Literal, TypedDict
from langgraph.graph import MessagesState

class NonRefundState(MessagesState):
    """
    Represents the state of a non-refundable request in the conversation flow.

    Attributes:
        request_type (Literal["technical_support", "product_info", "general"]):
            The type of support request identified from the user message.
            - "technical_support": Issues related to technical problems.
            - "product_info": Inquiries about product specifications or details.
            - "general": Other non-specific general inquiries.
    """
    request_type: Literal["technical_support", "product_info", "general"]


class RequestType(TypedDict):
    """
    Structured output schema used to classify non-refundable user requests.

    Attributes:
        type (Literal["technical_support", "product_info", "general"]):
            The classified type of the request, used to guide appropriate handling.
    """
    type: Literal["technical_support", "product_info", "general"]

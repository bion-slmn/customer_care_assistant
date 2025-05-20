from typing import TypedDict, Optional
from langgraph.graph import MessagesState


class Approve(TypedDict):
    approved: bool


class RefundState(MessagesState):
    """
    Represents the state of a refund request during the conversation flow.

    Attributes:
        reciept_image (str): URL or path to the image of the receipt provided by the user.
        verified (bool): Indicates whether the receipt has been verified as valid.
        reason (str): A textual history or explanation related to the refund request.
        refund_amount (Optional[int]): The amount eligible for refund, if applicable.
        refund_prdct (Optional[str]): Name of the product associated with the refund.
        authorised_by (str): Identifier or name of the person/system authorizing the refund.
        authorised (bool): Indicates whether the refund has been approved.
    """
    reciept_image: str
    verified: bool
    reason: str
    refund_amount: Optional[int]
    refund_prdct: Optional[str]
    authorised_by: str
    authorised: bool


class Refund(TypedDict):
    """
    Structured output schema for the refund verification step.

    Attributes:
        reciept_image (str): URL or path to the receipt image.
        verified (bool): Whether the receipt is valid for a refund.
        refund_amount (Optional[int]): Amount eligible for refund.
        refund_prdct (Optional[str]): Product name identified from the receipt.
    """
    reciept_image: str
    verified: bool
    refund_amount: Optional[int]
    refund_prdct: Optional[str]

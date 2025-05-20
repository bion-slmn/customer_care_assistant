from langgraph.graph import MessagesState
from typing import Optional, Literal, TypedDict

class SomeState(MessagesState):
    user_first_message: str   # Their original complaint
    verified: bool            # Has their issue been verified with proof?
    classification: str       # Is it "refundable" or "non_refundable"?
    resolved: bool            # Has the issue been resolved?
    notes: str                # History of the conversation
    refund_amount: Optional[int]  # Amount to refund (if applicable)
    refund_prdct: Optional[str]   # Product name for the refund
    image_problem_path: Optional[str]  # Path to proof image
    image_bill_path: Optional[str]     # Path to receipt image

class ComplaintStatus(TypedDict):
    status: Literal['refundable', 'non_refundable']
    reason: str
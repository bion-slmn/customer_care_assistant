from .state import RefundState, Refund, Approve
from langchain.schema import HumanMessage
from load_llm import load_model


llm = load_model()

def get_receipt_node(state: RefundState) -> RefundState:
    """Get the receipt image from the user and extract refund info using LLM."""
    RECEIPT_PROMPT = """
    You are a refund assistant.

    Given the user message, confirm if the user has provided a valid receipt.
    Only if you are confident the image is an actual receipt, extract the following:
    - verified (true/false)
    - refund_amount (numeric, or 0.0 if not applicable)
    - refund_prdct (product name, or 'none')
    - receipt_image (the image URL or path)

    DO NOT mark the receipt as verified unless it clearly contains typical receipt features (like store name, date, item list, total, etc.).

    User message:
    {user_message}
    """


    user_input = input("Enter the path to the receipt image file: ")
    image_file_path = user_input.strip()

    #with open(image_file_path, "rb") as image_file:
    #    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    # Create the HumanMessage with image and text
    message = HumanMessage(
        content=[
            {"type": "text", "text": "Please verify this receipt."},
            {"type": "image_url", "image_url": {"url": image_file_path}},
        ]
    )

    # Prompt to LLM, assuming llm.with_structured_output(Refund) is defined
    prompt = RECEIPT_PROMPT.format(user_message=message)
    receipt = llm.with_structured_output(Refund).invoke(prompt)
    print(receipt, "\n\n\n")
    # Update state
    state["reciept_image"] = image_file_path
    state["verified"] = receipt["verified"]
    state["refund_amount"] = receipt["refund_amount"]
    state["refund_prdct"] = receipt["refund_prdct"]

    return state


def route_refund(state: RefundState) -> str:
    """Route based on verification."""
    return "financial_manager" if state.get("verified") else "update_user_node"




def financial_manager(state: RefundState) -> str:
    """Ask the manager (human or LLM) if we should proceed with the refund."""

    manager_message = state['messages'][-1].content

    prompt = f"""
    Based on the following message, determine whether the refund is approved.
    Respond with `approved: true` or `approved: false`.

    Message:
    "{manager_message}"
    """
    response = llm.with_structured_output(Approve).invoke(prompt)
    is_approved = response["approved"]
    return {"authorised": is_approved}


def route_refund_based_on_financial_manager(state: RefundState) -> str:
    """Route based on financial manager's approval."""
    return "process_refund" if state.get("authorised") else "update_user_node"


def process_refund(state: RefundState) -> RefundState:
    """Process the refund."""
    print(f"✅ Processing your refund of amount {state['refund_amount']} for product '{state['refund_prdct']}'.", '\n\n')
    return state


def update_user_node(state: RefundState) -> RefundState:
    """Update user with refund or receipt verification result."""
    if state.get("verified"):
        print(f"❌ The refund of amount {state['refund_amount']} for product '{state['refund_prdct']}' has been rejected.", '\n\n')
    else:
        print("⚠️ The receipt could not be read properly or was invalid.", '\n\n')
    return state

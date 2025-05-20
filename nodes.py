from state import SomeState, ComplaintStatus
from load_llm import load_model


llm = load_model()

def classifier(state: SomeState) -> dict:
    """Determine if a complaint is refundable."""
    user_message = state.get("messages", "")

    print(state, user_message, '\n\n')


    prompt = f"""
    Classify the following complaint as 'refundable' or 'non_refundable':
    "{user_message}"

    Refundable issues include:
    - Damaged items
    - Cold food that should be hot
    - Missing items
    - Orders that never arrived

    Non-refundable issues include:
    - Asking about delivery time
    - Rude delivery staff
    - Minor service complaints
    """

    classification = llm.with_structured_output(ComplaintStatus).invoke(prompt)
    print(classification)
    state["classification"] = classification["status"]
    return state


def route_when_refundable(state: SomeState):
  classification = state.get("classification", "")
  if classification == "refundable":
    return 'refund_agent'
  else:
    return 'complaint_agent'
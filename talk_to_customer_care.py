from langchain.schema import HumanMessage
from graph import create_customer_support_agent


def interact_with_customer_assistant(customer_assistant):
    """
    Continuously interact with a customer assistant agent using a threaded conversation.

    Args:
        customer_assistant: A compiled LangGraph agent supporting `.stream()`, `.get_state()`, and `.update_state()` methods.
    """
    thread = {"configurable": {"thread_id": "5"}}

    # Initial user input (text + image)
    content = [
        {"type": "text", "text": "look at what you delivered, can i get a refund"},
        {"type": "image_url", "image_url": "https://ceramike.com/wp-content/uploads/2022/08/Broken-Ceramic-Mug.jpg"},
    ]
    initial_input = {"messages": HumanMessage(content=content)}

    # Start initial conversation
    for event in customer_assistant.stream(initial_input, thread, stream_mode="values"):
        event["messages"][-1].pretty_print()

    while True:
        next = customer_assistant.get_state(thread).next
        print(f"\nNext step in the graph: {next}")

        if not next:
            print("No further actions required.")
            break

        # If the next node requires user input (like 'financial_manager'), prompt user
        if next[-1] == 'financial_manager':
            user_input = input("\n[financial_manager] Enter update for the state: ")
            customer_assistant.update_state(thread, {"messages": user_input})

        # Continue streaming the conversation
        for event in customer_assistant.stream(None, thread, stream_mode="values"):
            event["messages"][-1].pretty_print()


customer_asistant = create_customer_support_agent()
interact_with_customer_assistant(customer_asistant)
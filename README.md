
# 🛠️ Customer Support Assistant

This is a conversational AI agent built using [LangGraph](https://docs.langchain.com/langgraph/) to handle customer complaints and determine whether they are refundable or not. It supports multi-modal inputs (text + image) and routes complaints to the appropriate handling agents.

## ✨ Features

- Classifies complaints as **refundable** or **non-refundable**
- Supports messages with **images and text**
- Routes refundable issues to a `refund_agent` and ask manager to confirm the refund
- Routes non-refundable/general issues to a `complaint_agent`
- Handles threaded conversations using LangGraph
- Interactive user flow in the terminal

---

## 📦 Installation

Make sure you have Python 3.8+ and the following dependencies:

```bash
pip install -r requirements.txt

````


## 🚀 Usage

1. Clone the repository:

   ```bash
   git clone git@github.com:bion-slmn/customer_care_assistant.git
   cd customer-support-assistant
   ```

2. Create a `.env` file with your credentials:

   ```env
   GOOGLE_API_KEY=your_google_api_key

   ```

3. Run the main script:

   ```bash
   python main.py
   ```

4. When prompted:

   * Enter a message describing your issue
   * Optionally provide an image URL (e.g., a broken product image)

---

## 🧠 Example Interaction

```text
Enter your message: look at what you delivered, can I get a refund
Enter image URL (optional, press enter to skip): https://example.com/broken-cup.jpg

[assistant]
I'm sorry to hear that! It looks like your complaint is eligible for a refund. Let me escalate this to our refund team...

Next step in the graph: ['financial_manager']
[financial_manager] Enter update for the state: The refund amount should be $10

[assistant]
Your refund has been approved and will be processed shortly!
```

---

## 🧩 Project Structure

```text
.
├── graph/
│   ├── __init__.py
│   ├── create_customer_support_agent.py
│   ├── nodes.py
│   ├── state.py
│   ├── refund_agent/
│   │   └── graph.py
│   └── non_refund_agent/
│       └── graph.py
├── main.py
├── .env
└── README.md
```

---

## 🤖 Agent Design

This assistant uses LangGraph to define a graph-based agent architecture with:

* `classifier`: Classifies complaint type
* `refund_agent`: Handles valid refund scenarios
* `complaint_agent`: Handles general inquiries
* Conditional routing based on classification result

---

## 🔐 Environment Variables


## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

```

---


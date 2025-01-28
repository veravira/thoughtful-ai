# from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
#
# agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())
#
# agent.run("How long doe sit take a person from kyiv to london by train?")

from smolagents import CodeAgent, HfApiModel

###############################################################################
# 1) Hardcoded Q&A data for Thoughtful AI
###############################################################################
THOUGHTFUL_QA_DATA = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

###############################################################################
# 2) Helper Function: Retrieve a local Q&A answer if there's a match
###############################################################################
def get_thoughtful_answer(user_query: str) -> str:
    """
    Simple matching: if the user's question strongly overlaps
    any of our hardcoded Q&A questions, return that answer.
    Otherwise, return an empty string.
    """
    question_lower = user_query.lower()
    for qa in THOUGHTFUL_QA_DATA["questions"]:
        # A simple check if any key phrase matches
        # You could do more advanced partial or fuzzy matching here
        if qa["question"].lower() in question_lower or question_lower in qa["question"].lower():
            return qa["answer"]
    return ""  # No match

###############################################################################
# 3) Create an Agent with no external Tools, just an LLM fallback
###############################################################################
# HfApiModel() uses Hugging Face for LLM. Adjust if you want a different model.
agent = CodeAgent(
    tools=[],            # No extra tools like DuckDuckGoSearch
    model=HfApiModel()   # Generic fallback LLM
)

###############################################################################
# 4) Simple CLI flow
###############################################################################
def customer_support_flow():
    """
    Accept user input, check if there's a local Q&A match, otherwise fallback.
    """
    while True:
        user_input = input("\n[User] Ask a question about Thoughtful AI (or type 'exit'): ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Exiting. Have a nice day!")
            break

        # Check local Q&A
        local_match = get_thoughtful_answer(user_input)
        if local_match:
            # Return the known response
            print(f"[Agent] {local_match}")
        else:
            # Fallback to the LLM
            llm_response = agent.run(user_input)
            print(f"[Agent] {llm_response}")

###############################################################################
# 5) Main Execution
###############################################################################
if __name__ == "__main__":
    print("Welcome to Thoughtful AI Support!")
    customer_support_flow()

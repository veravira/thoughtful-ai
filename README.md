# thoughtful-ai

# Thoughtful AI - Customer Support Agent

## Objective
The Thoughtful AI Customer Support Agent is a conversational AI tool designed to assist users with basic questions about Thoughtful AI. It utilizes a predefined dataset of frequently asked questions (FAQs) and answers to provide instant responses. For questions outside the predefined dataset, the agent leverages a large language model (LLM) as a fallback.

---

## Features
- **Predefined Q&A Matching**: Hardcoded questions and answers about Thoughtful AI to ensure accurate responses for common queries.
- **Fallback to LLM**: For questions not covered in the dataset, the agent uses a Hugging Face-powered language model to generate responses.
- **User-Friendly CLI Interface**: A simple and interactive command-line interface for users to ask questions.

---

## Rules
The agent follows these guidelines:
1. Accepts user input and answers questions conversationally.
2. Retrieves the most relevant answer from the hardcoded dataset when possible.
3. Provides fallback responses using an LLM for unsupported queries.

---

## Predefined Dataset
The agent uses the following dataset to answer questions about Thoughtful AI:
```json
{
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
```
## How to Run

### Clone the Repository
```bash
git clone https://github.com/your-username/thoughtful_ai.git
cd thoughtful_ai
```

Install Dependencies
Ensure you have Python installed. Then, install the required packages
```bash
pip install smolagents
```

## Run the Application
```bash
python main.py
```
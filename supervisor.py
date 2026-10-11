
import ollama

from agents import BankingAgent, FraudAgent, CreditAgent


class SupervisorAgent:
    def __init__(self):
        self.banking_agent = BankingAgent()
        self.fraud_agent = FraudAgent()
        self.credit_agent = CreditAgent()

    def process_query(self, query):
        text = query.lower().strip()

        # Route requests to the correct specialist agent
        fraud_words = [
            "fraud", "suspicious", "scam",
            "unauthorized", "unusual transaction"
        ]

        credit_words = [
            "loan", "credit", "eligibility",
            "monthly debt", "monthly income",
            "borrow", "emi"
        ]

        banking_words = [
            "balance", "transaction", "account",
            "deposit", "withdraw", "transfer",
            "statement", "bank"
        ]

        try:
            if any(word in text for word in fraud_words):
                return self.fraud_agent.run(query)

            if any(word in text for word in credit_words):
                return self.credit_agent.run(query)

            if any(word in text for word in banking_words):
                return self.banking_agent.run(query)

            # Use Ollama for general questions
            response = ollama.chat(
                model="llama3.2:1b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful AI Banking Assistant. "
                            "Answer general questions clearly. "
                            "Never invent account balances, transactions, "
                            "fraud findings, or loan eligibility results. "
                            "For banking operations, direct the user to "
                            "the relevant banking feature."
                        ),
                    },
                    {"role": "user", "content": query},
                ],
            )

            return response["message"]["content"]

        except Exception as error:
            return (
                f"Request could not be completed: {error}\n"
                "Please try again."
            )

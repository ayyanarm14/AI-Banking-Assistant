
from banking_tools import (
    get_balance,
    get_transactions,
    detect_fraud,
    calculate_loan_eligibility
)


class BankingAgent:
    """Handles customer balance and transaction queries."""

    def run(self, request):
        request = request.lower()

        if "balance" in request:
            return get_balance()

        if "transaction" in request or "history" in request:
            return get_transactions()

        return "Banking Agent: I can help with balance and transactions."


class FraudAgent:
    """Checks transactions using a simple demo rule."""

    def run(self, request):
        return detect_fraud()


class CreditAgent:
    """Calculates the customer's debt-to-income ratio."""

    def run(self, request):
        # Demo values; these are not real customer financial details.
        monthly_income = 30000
        monthly_debt = 10000

        return calculate_loan_eligibility(
            monthly_income,
            monthly_debt
        )

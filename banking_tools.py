
# Simulated banking tools
# All customer information is fictional.

CUSTOMER = {
    "name": "Arun",
    "account": "XXXX1234",
    "balance": 25000
}

TRANSACTIONS = [
    {"date": "2026-10-10", "description": "Grocery", "amount": 1500},
    {"date": "2026-10-09", "description": "Electricity Bill", "amount": 2200},
    {"date": "2026-10-08", "description": "Online Transfer", "amount": 80000},
]

def get_balance():
    return (
        f"Customer: {CUSTOMER['name']}\n"
        f"Account: {CUSTOMER['account']}\n"
        f"Balance: ₹{CUSTOMER['balance']:,}"
    )

def get_transactions():
    return "\n".join(
        f"{t['date']} | {t['description']} | ₹{t['amount']:,}"
        for t in TRANSACTIONS
    )

def detect_fraud():
    suspicious = [t for t in TRANSACTIONS if t["amount"] >= 75000]

    if not suspicious:
        return "No suspicious transactions detected."

    return "\n".join(
        f"Potentially suspicious: {t['description']} "
        f"- ₹{t['amount']:,} on {t['date']}"
        for t in suspicious
    )

def calculate_loan_eligibility(monthly_income, monthly_debt):
    if monthly_income <= 0 or monthly_debt < 0:
        return "Enter a valid income and non-negative debt."

    ratio = (monthly_debt / monthly_income) * 100

    if ratio <= 40:
        status = "Lower debt burden under this demo rule."
    else:
        status = "High debt burden under this demo rule."

    return (
        f"Debt-to-income ratio: {ratio:.1f}%\n"
        f"Result: {status}"
    )

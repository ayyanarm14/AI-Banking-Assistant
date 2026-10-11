
def show_balance():
    print("\n--- Customer Banking Agent ---")
    print("Customer: Arun")
    print("Account: XXXX1234")
    print("Available balance: Rs. 25000.00")


def show_transactions():
    print("\n--- Transaction History ---")

    transactions = [
        ("Credit", "Salary", 15000.00),
        ("Debit", "Shopping", 2500.00),
        ("Debit", "Food", 500.00)
    ]

    for number, transaction in enumerate(transactions, start=1):
        kind, description, amount = transaction
        print(f"{number}. {kind}: {description} - Rs. {amount:.2f}")


def check_suspicious_transactions():
    print("\n--- Risk / Fraud Detection Agent ---")

    transactions = [
        ("Grocery shopping", 1200),
        ("Online purchase", 8500),
        ("Unusual large transfer", 75000)
    ]

    flagged = 0

    for description, amount in transactions:
        if amount >= 50000:
            print(
                f"{description}: Rs. {amount:.2f} "
                "-> REVIEW - High amount"
            )
            flagged += 1
        else:
            print(
                f"{description}: Rs. {amount:.2f} "
                "-> No alert from this rule"
            )

    print(f"\nTransactions flagged for review: {flagged}")
    print("Demo only: These are not real bank alerts.")


def check_loan_debt_burden():
    print("\n--- Credit / Loan Agent ---")

    try:
        income = float(input("Enter monthly income (Rs.): "))
        debt = float(input("Enter monthly debt payments (Rs.): "))

        if income <= 0 or debt < 0:
            print("Income must be above zero and debt cannot be negative.")
            return

        ratio = (debt / income) * 100

        print(f"\nDebt-to-income ratio: {ratio:.2f}%")

        if ratio <= 30:
            print("Demo assessment: Low debt burden.")
        elif ratio <= 40:
            print("Demo assessment: Moderate debt burden.")
        else:
            print("Demo assessment: High debt burden.")

        print("This is an educational estimate, not a bank decision.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


def main():
    print("=" * 42)
    print("       AI BANKING ASSISTANT")
    print("=" * 42)
    print("Demo mode: fictional data only.")

    while True:
        print("\n1. Check Account Balance")
        print("2. View Transaction History")
        print("3. Check Suspicious Transactions")
        print("4. Estimate Loan Debt Burden")
        print("5. Exit")

        try:
            choice = input("\nEnter your choice (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram stopped safely.")
            break

        if not choice:
            print("No input received. Please type a number from 1 to 5.")
            continue

        if choice == "1":
            show_balance()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            check_suspicious_transactions()
        elif choice == "4":
            check_loan_debt_burden()
        elif choice == "5":
            print("Thank you for using AI Banking Assistant!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

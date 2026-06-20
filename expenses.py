expenses = []

def add_expense(name, amount):
    # Validation added
    if not name or not name.strip():
        print("Error: expense name cannot be empty")
        return False
    if not isinstance(amount, (int, float)) or amount <= 0:
        print("Error: amount must be a positive number")
        return False

    expenses.append({"name": name.strip(), "amount": round(amount, 2)})
    print(f"Added: {name} - ${amount:.2f}")
    return True

def total():
    return round(sum(e["amount"] for e in expenses), 2)

def list_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['name']} - ${e['amount']:.2f}")
    print(f"Total: ${total():.2f}")
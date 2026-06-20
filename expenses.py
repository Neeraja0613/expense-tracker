expenses = []

def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})
    print(f"Added: {name} - ${amount}")

def total():
    return sum(e["amount"] for e in expenses)
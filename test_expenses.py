from expenses import add_expense, total, expenses

def test_valid_expense():
    expenses.clear()
    result = add_expense("Coffee", 4.50)
    assert result == True
    assert len(expenses) == 1

def test_empty_name_rejected():
    expenses.clear()
    result = add_expense("", 10)
    assert result == False
    assert len(expenses) == 0

def test_negative_amount_rejected():
    expenses.clear()
    result = add_expense("Coffee", -5)
    assert result == False

def test_total_calculation():
    expenses.clear()
    add_expense("Coffee", 4.50)
    add_expense("Lunch", 12.00)
    assert total() == 16.50

print("All tests passed!")
test_valid_expense()
test_empty_name_rejected()
test_negative_amount_rejected()
test_total_calculation()
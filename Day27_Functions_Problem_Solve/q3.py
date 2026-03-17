# Q. Expense Tracker

expenses = {
    "food": 1200,
    "travel": 800,
    "shopping": 1500,
    "bills": 1000
}


def expense_tracker(expences):

    total_value = 0
    Highest_value = 0
    count = 0


    for key,value in expences.items():
        count += 1
        total_value += value
        if value > Highest_value:
            Highest_value = value
            Highest_value_key = key

    average = total_value / count

    print('Total =',total_value)
    print(f"Highest: {Highest_value_key} - {Highest_value}")
    print('Average =',average)
        

expense_tracker(expenses)
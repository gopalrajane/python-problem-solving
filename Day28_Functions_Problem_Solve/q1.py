# Q. Mini Bank Account

def create_account(name, balance):
    return {"Name": name, "Balance": balance}


def deposit(account, amount):
    account['Balance'] += amount
    print("Deposited:", amount)
    print("Balance:", account['Balance'])


def withdraw(account, amount):
    if account['Balance'] >= amount:
        account['Balance'] -= amount
        print("Withdrawn:", amount)
        print("Balance:", account['Balance'])
    else:
        print("Insufficient Balance")


def check_balance(account):
    print("Current Balance:", account['Balance'])


name = input("Enter Name: ")
balance = int(input("Enter Balance: "))

account = create_account(name, balance)

deposit(account, 1000)
withdraw(account, 500)
check_balance(account)






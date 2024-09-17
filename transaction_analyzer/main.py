data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]


def print_transactions(transactions):
    for transaction in transactions:
        amount, statement = transaction
        print(f"${amount} - {statement}")

#print_transactions(data)

def print_summary(transactions):
    deposits = [transaction[0] for transaction in transactions
    if transaction[0] >= 0]
    total_deposited = sum(deposits)
    print(f"Total Deposited: {total_deposited}")
    withdrawals = [transaction[0] for transaction in transactions
    if transaction[0] < 0]
    total_withdrawn = sum(withdrawals)
    print(f"Total Withdrawn: {total_withdrawn}")
    balance = total_deposited + total_withdrawn
    print(f"Total Balance: {balance}")

#print_summary(data)


def analyze_transactions(transactions):
    transactions.sort()
    largest_withdrawal = transactions[0]
    largest_deposit = transactions[-1]
    deposits = [transaction[0] for transaction in transactions
    if transaction[0] >= 0]
    total_deposited = sum(deposits)
    withdrawals = [transaction[0] for transaction in transactions
    if transaction[0] < 0]
    total_withdrawn = sum(withdrawals)
    average_deposit = total_deposited / len(deposits) if deposits else 0
    average_withdrawal = total_withdrawn / len(withdrawals) if withdrawals else 0
    print(f"Largest Withdrawal: {largest_withdrawal}")
    print(f"Largest Deposit: {largest_deposit}")
    print(f"Average Deposit: {average_deposit}")
    print(f"Average Withdrawal: {average_withdrawal}")

#analyze_transactions(data)

while True:
    print("print?")
    print("analyze?")
    print("stop?")
    choice = input("Choose Option").lower()
    
    if choice == "print":
        print_summary(data)
    elif choice == "analyze":
        analyze_transactions(data)
    elif choice == "stop":
        break
    else:
        print("Invalid choice")

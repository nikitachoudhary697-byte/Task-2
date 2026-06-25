import csv

def add_expense():
    item = input("Enter expense name: ")
    amount = input("Enter amount: ")

    file = open("expenses.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow([item, amount])
    file.close()

    print("Expense added successfully.")

def show_expenses():
    try:
        file = open("expenses.csv", "r")
        reader = csv.reader(file)

        print("\nExpense List")
        for row in reader:
            print("Item:", row[0], "Amount:", row[1])

        file.close()

    except FileNotFoundError:
        print("No expenses found.")

def total_expense():
    total = 0

    try:
        file = open("expenses.csv", "r")
        reader = csv.reader(file)

        for row in reader:
            total = total + int(row[1])

        file.close()

        print("Total Expense =", total)

    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
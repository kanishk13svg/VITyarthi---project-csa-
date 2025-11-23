
amounts = []
categories = []
descriptions = []
dates = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Enter category (Food/Travel/Bills etc): ")
    description = input("Enter short description: ")
    date = input("Enter date (DD-MM-YYYY): ")

    amounts.append(amount)
    categories.append(category)
    descriptions.append(description)
    dates.append(date)

    print("Expense added successfully!\n")

def view_expenses():
    if len(amounts) == 0:
        print("No expenses recorded!\n")
        return

    print("\nIndex | Amount   | Category     | Date         | Description")
    print("---------------------------------------------------------------")

    for i in range(len(amounts)):
        print(f"{i:5d} | {amounts[i]:8.2f} | {categories[i]:12} | {dates[i]:10} | {descriptions[i]}")
    print()

def total_expense():
    if len(amounts) == 0:
        print("No expenses to calculate!\n")
        return

    total = sum(amounts)
    print(f"Total Expense = {total:.2f}\n")

def total_by_category():
    if len(amounts) == 0:
        print("No expenses recorded!\n")
        return

    category_totals = {}

    for i in range(len(categories)):
        cat = categories[i]
        amt = amounts[i]

        if cat in category_totals:
            category_totals[cat] += amt
        else:
            category_totals[cat] = amt

    print("\nCategory-wise totals:")
    for cat, total in category_totals.items():
        print(f"{cat} : {total:.2f}")
    print()

def delete_expense():
    if len(amounts) == 0:
        print("No expenses to delete!\n")
        return

    try:
        index = int(input("Enter index to delete: "))
    except ValueError:
        print("Invalid index!\n")
        return

    if index < 0 or index >= len(amounts):
        print("Index out of range!\n")
        return

    amounts.pop(index)
    categories.pop(index)
    descriptions.pop(index)
    dates.pop(index)

    print("Expense deleted successfully!\n")

def view_by_index():
    if len(amounts) == 0:
        print("No expenses recorded!\n")
        return

    try:
        index = int(input("Enter index to view: "))
    except ValueError:
        print("Invalid index!\n")
        return

    if index < 0 or index >= len(amounts):
        print("Index out of range!\n")
        return

    print("\nExpense Details:")
    print("Amount      : ",amounts[index])
    print("Category    : ",categories[index])
    print("Date        : ",dates[index])
    print("Description : ",descriptions[index])

def main():
    while True:
        print("===== Expense Management System =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expense")
        print("4. Total by Category")
        print("5. Delete Expense (by index)")
        print("6. View Expense (by index)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            total_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            view_by_index()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

main()

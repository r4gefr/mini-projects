import json

print("Welcome to Expense Tracker!")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
expenses = []

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        category = input("Enter expense category: ").strip().lower()
        if not category:
            print("Category cannot be empty. Please try again.")
            return
        
        expenses.append({"amount": amount,"category": category})
        save_expenses()
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses():
    if not expenses:
        print("No expenses recorded")
    else:
        print("\nExpenses:")
        for index, exp in enumerate(expenses, start=1):
            print(f"{index}. {exp['category'].capitalize()}: ₹{exp['amount']:.2f}")

def total_spending():
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total spending: ₹{total:.2f}")

def category_spending():
    if not expenses:
        print("No expenses recorded")
        return

    category_totals = {}
    for exp in expenses:
        key = exp['category']
        category_totals[key] = category_totals.get(key, 0) + exp['amount']

    print("\nCategory-wise Spending:")
    for category, total in category_totals.items():
        print(f"{category.capitalize()}: ₹{total:.2f}")
        
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
    else:
        print("\nExpenses:")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['category'].capitalize()}: ₹{exp['amount']:.2f}")

        try:    
            num = int(input("Enter expense number to delete: "))
            if 1 <= num <= len(expenses):
                removed = expenses.pop(num - 1)
                save_expenses()
                print(f"Deleted: {removed['category']} ₹{removed['amount']:.2f}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    load_expenses()

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spending()
        elif choice == '4':
            category_spending()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
import json
import datetime

# File paths
EXPENSE_FILE = "expenses.json"

# Load expenses from file
def load_expenses():
    """Load expenses from the file or create a new file if it doesn't exist."""
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save expenses to file
def save_expenses(expenses):
    """Save the expense list to a file."""
    try:
        with open(EXPENSE_FILE, "w") as file:
            json.dump(expenses, file, indent=4)
    except Exception as e:
        print(f"Error saving expenses: {e}")


# Get a valid amount input
def get_valid_amount(prompt):
    """Get a valid amount input from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Get a valid string input
def get_valid_string(prompt):
    """Get a non-empty string input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value.capitalize()
        print("Input cannot be empty. Please try again.")


# Add a new expense
def add_expense(expenses):
    """Add a new expense."""
    amount = get_valid_amount("Please enter expense amount: ")
    category = get_valid_string("Enter category (e.g., Food, Transport, Entertainment, Shopping): ")
    description = get_valid_string("Please enter description: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expenses.append({"amount": amount, "category": category, "description": description, "date": date})
    save_expenses(expenses)
    print("Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. ${expense['amount']:.2f} - {expense['category']} ({expense['description']}) on {expense['date']}")


# View total spending
def view_total_spending(expenses):
    """Calculate and display total spending."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ${total:.2f}")


# Filter expenses by category
def filter_expenses_by_category(expenses):
    """Filter and display expenses by category."""
    category = get_valid_string("Enter category to filter by: ")
    filtered = [exp for exp in expenses if exp["category"] == category]

    if not filtered:
        print(f"Oops..No expenses found for category '{category}'.")
    else:
        for exp in filtered:
            print(f"${exp['amount']:.2f} - {exp['description']} on {exp['date']}")


# Delete an expense
def delete_expense(expenses):
    """Delete an expense from the list."""
    view_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            del expenses[index]
            save_expenses(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input! Please enter a number.")


# Edit an expense
def edit_expense(expenses):
    """Edit an existing expense."""
    view_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to edit: ")) - 1
        if 0 <= index < len(expenses):
            amount = get_valid_amount("Enter new expense amount: ")
            category = get_valid_string("Enter new category: ")
            description = get_valid_string("Enter new description: ")
            expenses[index] = {"amount": amount, "category": category, "description": description,
                               "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            save_expenses(expenses)
            print("Expense updated successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input! Please enter a number.")


# Main program loop
def main():
    """Main program loop."""
    expenses = load_expenses()

    while True:
        print("\nSmart Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Filter Expenses by Category")
        print("5. Delete an Expense")
        print("6. Edit an Expense")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total_spending(expenses)
        elif choice == "4":
            filter_expenses_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            edit_expense(expenses)
        elif choice == "7":
            print("Goodbye! See you soon!")
            break
        else:
            print("Invalid choice, please try again.")


# Entry point
if __name__ == "__main__":
    main()
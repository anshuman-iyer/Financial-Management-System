# Financial Management Application
# Made by Anshuman Iyer (Apllication No. 25BAC10027), 5

import os

# ---Global Variables---
transactions = []
FILENAME = "transactions.txt"
next_id = 1

# ---Functions---

def display_menu():
    """Prints the main menu to the console."""
    print("\n--- Financial Management Menu ---")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Show Financial Summary")
    print("6. Save and Exit")
    print("---------------------------------")

def get_valid_int(prompt):
    """Utility function to get validated integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_valid_float(prompt):
    """Utility function to get validated non-negative float input."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_transaction():
    """Adds a new transaction to the list."""
    global next_id
    
    print("\n--- Add New Transaction ---")
    
    # Get Type
    type_choice = get_valid_int("Enter Type (1 for Income, 2 for Expense): ")
    if type_choice not in [1, 2]:
        print("\nInvalid type. Returning to menu.")
        return
    
    t_type = "Income" if type_choice == 1 else "Expense"
    
    # Get other details
    t_date = input("Enter Date (YYYY-MM-DD): ")
    t_category = input("Enter Category (e.g., Food, Salary, Bills): ")
    t_amount = get_valid_float("Enter Amount: ")
    t_description = input("Enter Description: ")

    # Create and store the transaction (as a dictionary)
    transaction = {
        "id": next_id,
        "date": t_date,
        "type": t_type,
        "category": t_category,
        "amount": t_amount,
        "description": t_description
    }
    
    transactions.append(transaction)
    next_id += 1
    
    print("\nTransaction added successfully!")
    save_to_file() # Auto-save

def view_transactions():
    """Displays all recorded transactions in a formatted table."""
    print("\n--- All Transactions ---")
    if not transactions:
        print("No transactions recorded yet.\n")
        return

    # Print Header
    print(f"{'ID':<5} {'Date':<15} {'Type':<12} {'Category':<20} {'Amount':<12} {'Description'}")
    print("-" * 80)

    # Print each transaction
    for t in transactions:
        amount_str = f"${t['amount']:.2f}"
        print(f"{t['id']:<5} {t['date']:<15} {t['type']:<12} {t['category']:<20} {amount_str:<12} {t['description']}")
    
    print("-" * 80)

def update_transaction():
    """Finds a transaction by ID and allows the user to update it."""
    try:
        id_to_update = get_valid_int("\nEnter the ID of the transaction to update: ")
    except ValueError:
        print("\nInvalid ID format.")
        return

    transaction_to_update = None
    for t in transactions:
        if t['id'] == id_to_update:
            transaction_to_update = t
            break

    if transaction_to_update:
        print(f"\n--- Updating Transaction ID: {id_to_update} ---")

        # Get new Type
        type_choice = get_valid_int("Enter new Type (1 for Income, 2 for Expense): ")
        if type_choice not in [1, 2]:
            print("\nInvalid type. Update cancelled.")
            return
        
        # Get new details
        transaction_to_update['type'] = "Income" if type_choice == 1 else "Expense"
        transaction_to_update['date'] = input("Enter new Date (YYYY-MM-DD): ")
        transaction_to_update['category'] = input("Enter new Category: ")
        transaction_to_update['amount'] = get_valid_float("Enter new Amount: ")
        transaction_to_update['description'] = input("Enter new Description: ")

        print("\nTransaction updated successfully!")
        save_to_file() # Auto-save
    else:
        print(f"\nTransaction with ID {id_to_update} not found.\n")

def delete_transaction():
    """Finds a transaction by ID and deletes it."""
    try:
        id_to_delete = get_valid_int("\nEnter the ID of the transaction to delete: ")
    except ValueError:
        print("\nInvalid ID format.")
        return

    transaction_to_remove = None
    for t in transactions:
        if t['id'] == id_to_delete:
            transaction_to_remove = t
            break

    if transaction_to_remove:
        transactions.remove(transaction_to_remove)
        print("\nTransaction deleted successfully!")
        save_to_file() # Auto-save
    else:
        print(f"\nTransaction with ID {id_to_delete} not found.\n")

def show_summary():
    """Calculates and displays a summary of finances."""
    if not transactions:
        print("\nNo transactions to summarize.\n")
        return

    total_income = 0.0
    total_expense = 0.0
    expense_by_category = {}

    for t in transactions:
        if t['type'] == "Income":
            total_income += t['amount']
        else:
            total_expense += t['amount']
            # Use .get() to safely handle new categories
            expense_by_category[t['category']] = expense_by_category.get(t['category'], 0) + t['amount']

    balance = total_income - total_expense

    print("\n--- Financial Summary ---")
    print(f"Total Income:    ${total_income:.2f}")
    print(f"Total Expenses:  ${total_expense:.2f}")
    print("-------------------------")
    print(f"Remaining Balance: ${balance:.2f}")
    print("\n--- Expenses by Category ---")

    if not expense_by_category:
        print("No expenses recorded.")
    else:
        for category, amount in expense_by_category.items():
            print(f"{category:<20}: ${amount:.2f}")
    
    print("---------------------------\n")

def save_to_file():
    """Saves all transactions from the list to the data file."""
    try:
        with open(FILENAME, 'w') as f:
            # Save the next ID on the first line
            f.write(f"{next_id}\n")
            
            # Save each transaction
            for t in transactions:
                f.write(f"{t['id']},{t['date']},{t['type']},{t['category']},{t['amount']},{t['description']}\n")
    except IOError as e:
        print(f"Error: Could not open file for writing. {e}")

def load_from_file():
    """Loads transactions from the data file into the list."""
    global next_id
    
    if not os.path.exists(FILENAME):
        # File doesn't exist, not an error.
        return 

    try:
        with open(FILENAME, 'r') as f:
            transactions.clear()
            
            # Load the next ID from the first line
            try:
                next_id = int(f.readline().strip())
            except ValueError:
                # Handle empty or corrupt file
                print("Warning: Could not read next_id from file. Starting from 1.")
                next_id = 1
                return

            # Load each transaction
            for line in f:
                if not line.strip(): # Skip empty lines
                    continue
                
                # Split the line, ensuring description (which may have commas) is last
                parts = line.strip().split(',', 5) 
                
                if len(parts) == 6:
                    try:
                        transaction = {
                            "id": int(parts[0]),
                            "date": parts[1],
                            "type": parts[2],
                            "category": parts[3],
                            "amount": float(parts[4]),
                            "description": parts[5]
                        }
                        transactions.append(transaction)
                    except (ValueError, IndexError):
                        print(f"Warning: Skipping corrupt line in file: {line.strip()}")
                else:
                    print(f"Warning: Skipping malformed line in file: {line.strip()}")

    except IOError as e:
        print(f"Error: Could not open file for reading. {e}")
    except Exception as e:
        print(f"An unexpected error occurred during file load: {e}")


# --- Main Application Logic ---

def main():
    """Main function to run the application loop."""
    load_from_file() # Load existing data
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            show_summary()
        elif choice == '6':
            save_to_file()
            print("\nExiting application. Your data has been saved. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

# Entry point for the script
if __name__ == "__main__":
    main()
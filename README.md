Simple Python Financial Management CLI Application

Author: Anshuman Iyer

📖 Overview
This is a straightforward, console-based Financial Management application written in Python. It allows users to track their income and expenses through a simple command-line interface. All transaction data is saved locally to a transactions.txt file, ensuring data persistence between sessions.

The application provides core functionalities for personal finance tracking, including adding, viewing, updating, and deleting transactions, as well as generating a summary of financial activity.

✨ Features

Add Transaction: Add new income or expense records with details like date, category, amount, and a description.

View All Transactions: Display a neatly formatted table of all recorded transactions.

Update Transaction: Modify the details of an existing transaction by its unique ID.

Delete Transaction: Remove a transaction from the records using its ID.

Financial Summary: Get a quick overview of total income, total expenses, and the remaining balance. It also provides a breakdown of expenses by category.

Data Persistence: Transactions are automatically loaded from and saved to a local file (transactions.txt), so your data is always there when you restart the application.

Input Validation: Includes checks to ensure the user enters valid choices and data formats (e.g., numbers for amounts).

Zero Dependencies: Runs using only standard Python libraries.

🛠️ How to Run
This program is written in standard Python and has no external dependencies.

Prerequisites

Python 3.6 or newer (due to the use of f-strings).

Running the Application

Save the Code: Save the provided source code into a file named financial_management.py.

Open a Terminal or Command Prompt: Navigate to the directory where you saved the file.

Run the Program: Run the following command to start the application:

python financial_management.py


Note: On some macOS or Linux systems, you may need to use the python3 command instead:

python3 financial_management.py


⚙️ How to Use
Once the application is running, you will be presented with the main menu:

--- Financial Management Menu ---
1. Add Transaction
2. View All Transactions
3. Update Transaction
4. Delete Transaction
5. Show Financial Summary
6. Save and Exit
---------------------------------
Enter your choice:


Simply enter the number corresponding to the action you wish to perform and follow the on-screen prompts. The application will automatically save your changes after adding, updating, or deleting a transaction. Choosing option 6 will also save the current state before exiting.

📁 Data Storage
The application stores all financial data in a plain text file named transactions.txt in the same directory as the script.

The first line of the file stores the next_id to ensure new transactions get a unique ID.

Subsequent lines store the transaction data in a comma-separated format:
id,date,type,category,amount,description

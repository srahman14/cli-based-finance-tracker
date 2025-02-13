# cli-based-finance-tracker

A command-line application where users can input expenses, categorize them, and get insights. This tool allows you to:

- Add expenses with specified amounts, categories, and descriptions
- View all recorded expenses in a tabular format
- Visualize expenses with bar and pie charts
- Delete specific expenses based on row number

## Features

- **Add Expense**: Record a new expense with its amount, type, and description.
- **View Expenses**: Display a list of all recorded expenses.
- **Visualize Expenses**: Generate visual representations (bar and pie charts) of your expenses based on category or amount.
- **Delete Expense**: Remove an expense from the list by specifying its row number.

## Usage
The application uses a **command-line interface (CLI)** for interaction. Below are the available commands:

1.) add --amount <amount> --category <category> --description <description>
<amount> -> int, <category> -> str, <description> -> str
# Example
- python src/financeTracker.py add --amount 10 --category food --description "chocolate"
Output: amount, category, description added to CSV file holding related data

2.) view
# Example
- python src/financeTracker.py view
Output: Displays a list of all recorded expenses in a tabular format.

3.) visualise
# Example
- python src/financeTracker.py visualise
Output: display of barchart of expenses (default)

4.) delete --row <row_number>
# Example
- python src/financeTracker.py delete --row 2
--row: The row number of the expense you want to delete. (Row number starts from 0)
Ouput: related row will be dropped from the CSV file

# Dependencies
argparse (for command-line argument parsing)
pandas (for reading and manipulating the expenses CSV)
matplotlib (for generating charts)
os (for file handling)

# File Structure
cli-based-finance-tracker/
├── src/
│   └── financeTracker.py     # Main script for managing expenses
├── expenses.csv              # File to store the expenses data
└── README.md                 # Project documentation

# License
This project is licensed under the MIT License - see the LICENSE file for details.

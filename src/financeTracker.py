import argparse
from csv import writer
import pandas as pd 
import os 
import matplotlib.pyplot as plt

class CLIMenu:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="CLI Finance Tracker")
        subparsers = self.parser.add_subparsers(dest="command")

        add_parser = subparsers.add_parser("add", help="Add a new expense")
        add_parser.add_argument("--amount", type=float, required=True, help="The amount of the expense to be added")
        add_parser.add_argument("--category", type=str, required=True, help="The category of the expense to be added")
        add_parser.add_argument("--description", type=str, required=True, help="The description of the expense to be added")
        view_parser = subparsers.add_parser("view", help="View your expenses")
        vis_parser = subparsers.add_parser("visualise", help="Visualise your expenses")
        vis_parser.add_argument("--p", type=str, required=True, help="Visualise your expenses in a piechart, ordered by cateogry")
        vis_parser.add_argument("--b", type=str, required=True, help="Visualise your expenses as a barchart")
        delete_parser = subparsers.add_parser("delete", help="Delete a row of your expenses")
        delete_parser.add_argument("--row", type=int, required=True, help="Row number of the expense to be deleted")

        self.args = self.parser.parse_args()
        self.expense_manager = ExpenseManager()
        self.report_gen = ReportGenerator()


        if self.args.command:
            self.handle_commands()
        else:
            self.show_menu()

    def handle_commands(self):
        self.expense_manager = ExpenseManager()
        self.report_gen = ReportGenerator()

        if self.args.command == "add":
            self.expense_manager.addExpense(self.args.amount, self.args.category, self.args.description)
            print(f"Added expense: {self.args.amount} for {self.args.category},\nDescription: {self.args.description}")
        elif self.args.command == "view":
            print(self.report_gen.viewExpenses())
        elif self.args.command == "visualise":
            self.report_gen.visualiseGenerator()
        elif self.args.command == "delete":
            self.expense_manager.deleteExpenses(self.args.row)
    
    def show_menu(self):
        print("Welcome to your personal CLI Finance Tracker \n")
        print("CLI Menu: \n 1. Add Expense \n 2. View Expenses \n 3. Visualise Expenses \n 4. Delete Expenses \n 5. Help \n 6. Exit")

        while True:
            option = 0
            try:
                option = int(input("\nEnter option -- 1/2/3/4/5/6: "))
            except ValueError:
                print("\n You must enter 1/2/3/4/5/6 only!")
            except:
                print("\n Enter from options 1/2/3/4/5/6")

            if option < 1 or option > 6:
                print("\n You must enter 1/2/3/4/5/6 only!")
            elif option == 1:
                try:
                    expense = float(input("Enter expense amount: "))
                    if expense <= 0:
                        print("Expense cannot be less than 0")
                        continue
                    expenseType = input("Enter expense type: ")
                    expenseDescription = input("Enter expense description: ")

                    self.expense_manager.addExpense(expense, expenseType, expenseDescription)
                    print(f"Expense of {expense} added successfully.")
                except ValueError:
                    print("Invaliud input. PLease enter a valid number for expense.")
            elif option == 2:
                print(self.report_gen.viewExpenses())
            elif option == 3:
                return self.report_gen.visualiseGenerator()
            elif option == 4:
                try:
                    rowNum = int(input("Enter row number to delete: "))
                except ValueError:
                    print("Input for row number must be a number")
                
                return self.expense_manager.deleteExpenses(rowNum)
            elif option == 6:
                break
            
class ExpenseManager:
    def __init__(self):
        self.csv_path = os.path.join(os.getcwd(), 'expenses.csv')

    def addExpense(self, expense, expenseType, expenseDescription):
        contentToAdd = [expense, expenseType, expenseDescription]
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as f_object:
                writer_obj = writer(f_object)
                writer_obj.writerow(['Amount', 'Type', 'Description'])

        with open(self.csv_path, 'a', newline='') as f_object:
            writer_obj = writer(f_object)
            writer_obj.writerow(contentToAdd)
            print(f"Expense added: {contentToAdd}")  # Debugging line

    
    def deleteExpenses(self, row):
        contentToDelete = row

        if not os.path.exists(self.csv_path):
            print('No such file exists for expenses')
            return

        df = pd.read_csv(self.csv_path)
        if contentToDelete < 0 or contentToDelete >= len(df):
            print(f"Row index out of bounds. Max row: ", len(df))

        df = df.drop(df.index[contentToDelete])
        df.to_csv(self.csv_path, index=False)

        print(f"\nRow {contentToDelete} successfully deleted")
        print(df)



class ReportGenerator:
    def __init__(self):
        pass

    def viewExpenses(self):
        if not os.path.exists('expenses.csv'):
            print('No such file exists for expenses')

        df = pd.read_csv('expenses.csv')
        print(df)
        
    
    def visualiseGenerator(self):#
        # add one for kind="pie", for different categories, and this will be a subcommand -p
        # add one for kind="bar" for different dates and amounts, and this will be subcommand -b
        df = pd.read_csv('expenses.csv')
        df.plot(kind="bar")
        plt.show()

class DatabaseHandler:
    def __init__(self):
        pass

def main():
    CLIMenu()

if __name__ == "__main__":
    main()
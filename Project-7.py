# Budget Tracker
class Transaction:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

class BudgetTracker:
    def __init__(self):
        self.income = []
        self.expenses = []  # Fixed typo from 'expanses' to 'expenses'

    def add_income(self, amount, category):
        self.income.append(Transaction(amount, category))

    def add_expense(self, amount, category):  # Fixed method name from 'add_expenses'
        self.expenses.append(Transaction(amount, category))

    def get_total_income(self):
        return sum(transaction.amount for transaction in self.income)  # Fixed 'Transaction.amount'

    def get_total_expenses(self):
        return sum(transaction.amount for transaction in self.expenses)  # Fixed 'Transaction.amount'

    def display_summary(self):
        print("Income Summary:")
        for transaction in sorted(self.income, key=lambda t: t.category):
            print(f"{transaction.category}: ${transaction.amount:.2f}")
        print("Total Income: ${:.2f}".format(self.get_total_income()))

        print("\nExpenses Summary:")
        for transaction in sorted(self.expenses, key=lambda t: t.category):
            print(f"{transaction.category}: ${transaction.amount:.2f}")
        print("Total Expenses: ${:.2f}".format(self.get_total_expenses()))

        print("\nNet Savings: ${:.2f}".format(self.get_total_income() - self.get_total_expenses()))

# Example Usage
tracker = BudgetTracker()
tracker.add_income(5000, 'Salary')
tracker.add_income(200, 'Freelance')
tracker.add_expense(1500, 'Rent')
tracker.add_expense(200, 'Groceries')
tracker.add_expense(100, 'Utilities')
tracker.display_summary()

class ExpenseTracker:
    def __init__(self):
        self.expenses=[]
    def add_expense(self,expense):
        self.expenses.append(expense)
    def view_expense(self):
        for expense in self.expenses:
            print(expense)
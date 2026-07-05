from expense import Expense as ex
from tracker import ExpenseTracker as et
tracker =et()
exp1=ex(40,"food","milk","29-06-2026")
exp2=ex(50,"food","jalebi","5-07-26")
exp3=ex(60,"food","sutte","5-07-26")
tracker.add_expense(exp1)
tracker.add_expense(exp2)
tracker.add_expense(exp3)
tracker.view_expense()
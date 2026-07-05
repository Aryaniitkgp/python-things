from expense import Expense as ex
from tracker import ExpenseTracker as et
tracker =et()
while(True):
    print("Starting the tracker")
    menu=int(input("Enter the choice : 1/2/3: "))
    if menu==1:
        amount=int(input(" "))
        category=input(" ")
        description=input(" ")
        date=input(" ")
        exp=ex(amount,category,description,date)
        tracker.add_expense(exp)
    elif menu==2 :
        tracker.view_expense()
    elif menu==3 :
        print("Exiting")
        break
    else : 
        print("invalid input")
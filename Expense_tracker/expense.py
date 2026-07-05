class Expense:
    def __init__(self, amount, category, description, date):
        self.amount=amount
        self.category=category
        self.description=description
        self.date=date
    def __str__(self):
        return f"""amount: {self.amount}
                   category: {self.category}
                   description: {self.description}
                   date: {self.date}"""
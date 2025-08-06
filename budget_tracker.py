import os
from datetime import datetime

class Transaction:
    def _init_(self, amount, category, t_type, notes=""):
        self.amount = float(amount)
        self.category = category
        self.type = t_type  # 'income' or 'expense'
        self.notes = notes
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _str_(self):
        return f"{self.date}|{self.type}|{self.amount}|{self.category}|{self.notes}"

    @staticmethod
    def from_string(data_line):
        date, t_type, amount, category, notes = data_line.strip().split("|")
        transaction = Transaction(amount, category, t_type, notes)
        transaction.date = date
        return transaction


class BudgetTracker:
    def _init_(self, filename="transactions.txt"):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def add_transaction(self, amount, category, t_type, notes=""):
        transaction = Transaction(amount, category, t_type, notes)
        self.transactions.append(transaction)
        self.save_transactions()

    def list_transactions(self):
        for t in self.transactions:
            print(t)

    def filter_transactions(self, by_type=None, by_category=None):
        filtered = self.transactions
        if by_type:
            filtered = [t for t in filtered if t.type == by_type]
        if by_category:
            filtered = [t for t in filtered if t.category.lower() == by_category.lower()]
        for t in filtered:
            print(t)

    def view_summary(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        balance = income - expenses
        print(f"Total Income: ₹{income}")
        print(f"Total Expenses: ₹{expenses}")
        print(f"Net Balance: ₹{balance}")

    def save_transactions(self):
        with open(self.filename, "w") as f:
            for t in self.transactions:
                f.write(str(t) + "\n")

    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    self.transactions.append(Transaction.from_string(line))
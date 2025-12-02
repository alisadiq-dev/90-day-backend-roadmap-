from bank_with_errors import BankAccount

if __name__ == "__main__":
    acc = BankAccount("Ali Sadiq", 1000)
    acc.deposit(1000, "Salary")
    acc.withdraw(500, "Shopping")
    acc.withdraw(5000, "Shopping")
    acc.deposit(-1000, "Salary")
    acc.get_balance()
    acc.show_history()
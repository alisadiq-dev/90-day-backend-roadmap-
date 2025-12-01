from typed_bank import BankAccount

if __name__ == "__main__":
    acc = BankAccount("Ali Sadiq", 0)
    acc.deposit(1000, "salary")
    acc.withdraw(500, "shopping")
    acc.show_history()
    acc.get_balance()

class BankAccount:
    def __init__(self, owner, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs. {amount:,} New balance: Rs. {self.balance:,}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Not enough money.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs. {amount:,} Remaining: Rs. {self.balance:,}")

    def get_balance(self):
        print(f"{self.owner}'s balance: Rs. {self.balance:,}")
        return self.balance

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: Rs. {self.balance:,}"

# ... for testing .....
if __name__ == "__main__":
    print("Welcome to the Bank System!")

    # Creating  accounts
    ali = BankAccount("Ali Sadiq", 150_000)
    ehtisham = BankAccount("Ehtisham Sadiq", 80_000)
    dua = BankAccount("Dua Sadiq", 0)

    print("\n initialize balance  ")
    print(ali)
    print(ehtisham)
    print(dua)

    print("\n perform transactions ")
    ali.deposit(50_000)
    ehtisham.withdraw(20_000)
    dua.deposit(1_000_000)

    print("\n final balance ")
    ali.get_balance()
    ehtisham.get_balance()
    dua.get_balance()

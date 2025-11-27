 """
Document design decisions

1. Why I used Inheritance
   - SavingsAccount and CheckingAccount both need deposit, withdraw, balance etc.
   - Instead of copying the same code again, I made them children of BankAccount.
   - So they automatically get all the functions from the parent → less code, easy to maintain.

2. super() 
   - I used super().__init__(owner, balance) so the parent class sets owner and balance first.
   - Without super() those two lines would be missing in child classes.

3. Method overriding
   - In CheckingAccount I rewrote the withdraw() function so it allows overdraft.
   - Same name, different behaviour → that’s overriding.

4. Future plan (Composition)
   - Tomorrow I will create a TransactionHistory class.
   - Every account will keep its own history → Account “has a” history.

That’s it!  
This way my code is clean, easy to understand and works like real bank apps.
Feeling good about Day 04 :)
"""

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


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print("Interest added: Rs.", round(interest, 2))
        print("New balance: Rs.", round(self.balance, 2))


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance: float = 0.0, overdraft_limit: float = 50000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"Cannot withdraw Rs. {amount:,} → Overdraft limit exceeded!")
        else:
            self.balance -= amount
            print(f"Withdrew Rs. {amount:,} (overdraft allowed)")
            print(f"Remaining: Rs. {self.balance:,}")


# ====  COMPOSITION ADDED ===
class TransactionHistory:                    
    def __init__(self):
        self.history = []

    def add(self, message):                   
        self.history.append(message)

    def show(self):
        print("\nTransaction History")
        for message in self.history:
            print(message)


# New Bankaccount with composition 
class BankAccountWithHistory(BankAccount):   
    def __init__(self, owner, balance: float = 0.0):
        super().__init__(owner, balance)
        self.history = TransactionHistory()
        self.history.add(f"Account created - Initial balance: Rs. {balance:,}")

    def deposit(self, amount):
        super().deposit(amount)
        self.history.add(f"Deposited Rs. {amount:,}")

    def withdraw(self, amount):
        if amount <= self.balance:
            super().withdraw(amount)
            self.history.add(f"Withdrew Rs. {amount:,}")
        else:
            print("Insufficient balance!")


# ==== TESTING  
if __name__ == "__main__":
    print("Banking System")

    print("\nTesting Savings Account")
    ali = SavingsAccount("Ali Sadiq", 100000, 0.07)
    ali.deposit(4000)
    ali.withdraw(2000)
    ali.apply_interest()
    ali.get_balance()
    print()

    print("Testing Checking Account")
    shsumail = CheckingAccount("Shsumail", 100000, 50000)
    shsumail.deposit(4000)
    shsumail.withdraw(2000)
    shsumail.get_balance()
    print()

    print("Testing Composition (Account with History)")
    acc = BankAccountWithHistory("Ali Sadiq", 100000)
    acc.deposit(4000)
    acc.withdraw(2000)
    acc.history.show()
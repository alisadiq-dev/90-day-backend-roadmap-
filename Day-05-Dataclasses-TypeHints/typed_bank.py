from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Transaction:
    amount: float
    transaction_type : str 
    timestamp : datetime = field(default_factory=datetime.now)
    note: str | None = None # optional note (if we use this then print string otherwise non)

@dataclass
class BankAccount:
    owner : str
    balance : float = 0.0 
    transactions : list[Transaction] = field(default_factory=list)


    def deposit(self, amount : float, note : str | None = None) -> None:
        self.balance += amount
        self.transactions.append(Transaction(amount, "deposit", note=note))

    def withdraw(self, amount : float, note : str | None = None) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append(Transaction(amount, "withdraw", note=note))
 
    def get_balance(self) -> None:
        print(f"Balance Rs:{self.balance}")

    def show_history(self) -> None:
        print(f"{self.owner} Transaction History")
        for transaction in self.transactions:
            print(f"{transaction.amount} {transaction.transaction_type} {transaction.timestamp} {transaction.note}")

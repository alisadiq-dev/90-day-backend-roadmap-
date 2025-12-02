from dataclasses import dataclass , field
from datetime import datetime
from typing import List
import logging 

 # logging configuration 
logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[logging.FileHandler("bank.log"), logging.StreamHandler()]
)

logger = logging.getLogger("bankapp")  
# Exception stepup 

class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass


# dataclasses 
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
    transactions : List[Transaction] = field(default_factory=list)


    def deposit(self, amount : float, note : str | None = None) -> bool:
        try:
            if amount < 0:
                raise NegativeAmountError("Amount cannot be negative")
            self.balance += amount
            self.transactions.append(Transaction(amount, "deposit", note=note))
            return True
        except NegativeAmountError as e:
            logger.error(f"Error: {e}")
            return False

    def withdraw(self, amount : float, note : str | None = None) -> bool:
        try:
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient balance")
            self.balance -= amount
            self.transactions.append(Transaction(amount, "withdraw", note=note))
            logger.info(f"Withdrawal of Rs:{amount} successful")
            return True
        except InsufficientFundsError as e:
            logger.error(f"Error: {e}")
            return False
 
    def get_balance(self) -> None: 
        logger.info(f"Balance Rs:{self.balance}")
        print(f"Balance Rs:{self.balance}")

    def show_history(self) -> None:
        print(f"{self.owner} Transaction History")
        logger.info(f"{self.owner} Transaction History")
        for transaction in self.transactions:
            print(f"{transaction.amount} {transaction.transaction_type} {transaction.timestamp} {transaction.note}")
            logger.info(f"{transaction.amount} {transaction.transaction_type} {transaction.timestamp} {transaction.note}")

# In this file, we will have ( main code save/load + day6 BankSystem)
# ====== file handling  + jason peristence ====

from dataclasses import dataclass, field, asdict 
from datetime import datetime
from typing import List
import json
import logging 

# logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# custom errors (day6)
class AccountNotFound(Exception):
    pass
class NegativeBalanceError(Exception):
    pass
class InsufficientBalanceError(Exception):
    pass

@dataclass
class Transaction:
    amount : float
    type : str 
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    note: str | None = None

    def get_time(self):
        return datetime.fromisoformat(self.timestamp)

@dataclass
class BankAccount:
    owner : str
    balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)
    
    def deposit(self, amount: float, note: str | None = None):
        try:
            if amount <= 0:
                raise NegativeBalanceError("Deposit amount must be positive")
            self.balance += amount 
            self.transactions.append(Transaction(amount, "deposit", note=note))
            logger.info(f"{self.owner} deposited {amount}")
        except NegativeBalanceError as e:
            logger.error(e)

    def show_history(self):
        print(f"Transaction History for {self.owner}:")
        for t in self.transactions:
            print(f"- {t.type.title()}: {t.amount} ({t.note or 'No note'}) on {t.timestamp}")


    def withdraw(self, amount: float, note: str | None = None) -> None:
        try:
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")
            self.balance -= amount
            self.transactions.append(Transaction(amount, "withdraw", note=note))
            logger.info(f"{self.owner} withdrew {amount}")n
        except InsufficientBalanceError as e:
            logger.error(e)
 

    # save account as a jason file 
    def save_to_file(self, filename: str = "bank_data.json") -> None:
        try:
            data = {
                "owner": self.owner,
                "balance": self.balance,
                "transactions": [asdict(t) for t in self.transactions]
            }
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Account saved to {filename}")
        except Exception as e:
            logger.error(f"Failed to save account: {e}")
            
    # load account form jason file 
    @classmethod
    def load_from_file(cls, filename: str = "bank_data.json") -> "BankAccount":
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            account = cls(owner = data["owner"], balance = data["balance"])
            for t in data["transactions"]:
                account.transactions.append(Transaction(**t))
            logger.info(f"data loaded from {filename}")
            return account
        except FileNotFoundError as e:
            logger.warning("File not found")
            return cls("New User", 0)
        except json.JSONDecodeError as e:
            logger.error("Invalid JSON format")
            return cls("New User", 0)
        except Exception as e:
            logger.error(f"Failed to load account: {e}")
            return cls("New User", 0)
    

        

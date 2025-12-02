from typing import list, dict, Optional
# =========== pyhton data class =========
"""
ye bhut sary methode khud say gnearte karta ha like 
- __init__
- __repr__
- __eq__
- __ne__
- __lt__
- __le__
- __gt__
- __ge__

## simple class 
class students:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
#. data clas 
from dataclasses import dataclass
@dataclass
class students:
    name: str
    age: int
    roll: int

"""
# Example 
from dataclasses import dataclass

@dataclass
class BankAccount():
    owner : str 
    balance : float = 0.0

acc1 = BankAccount("Ali Sadiq", 1500000)
acc2 = BankAccount("ehtisham sadiq", 1500000)

print(acc1)
print(acc2)

"""
str = name : str = "Ali"
int = age : int = 25
float = balance : float = 5000.50
bool = is_active : bool = True
list[str] = names : list[str] = ["Ali", "Ahmed"]
dict[str, int] = marks : dict[str, int] = {"Ali": 90}
Optional[str] = middle_name : Optional[str] = None
"""

# ======= Type hint in pyhton ==========


 def upperCase(value:str):
    print(value)
    return value.upper()

upperCase("ali sadiq")


"""
- code khud batata ha kay kia expect kar rha ha 
- FastAPI automatic validation karta ha 

=== without type hin ====
def deposit(account, amount):
    account.balance += amount   # galti se string daal diya to run-time error

==== with type hint ======
from typing import Any

def deposit(account: Any, amount: float) -> None:   # ← clear hai amount number hona chahiye
    account.balance += amount

= agr code ma koi mistake hu ge tu wo code likhty huve he mil jay ge run time par error nahi ay ga 

========== Now We talk about mypy ========

 pyhton ma hum type hint check karty han  " mypy "
 """
 def sum(a : int , b :int) -> int:
     # ye jou def function ha is ma a variable be int hu ga or b variable be int hu ga or jou ye return kary ga wo be int hu ga
     print("adding tow number")
    return a + b   

sum (12, 68)


import math
from typing import Any

import requests
from rich import print as rprint

# print statements
print("Hello, World!")

# --- first step toword programimg 
# simple loop
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# string data type
phrase = "Punjab univeristy Lahore"
print(phrase)
# concatination of strings
print(phrase + " is a good university")
# modify string using methods
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(phrase.lower().islower())
print(phrase.upper().isupper())
# Length of a string
print(len(phrase))
# Accessing a specific character in a string
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase[5])
print(phrase[6])
print(phrase[7])
print(phrase[8])
# Indexing a string
print(phrase.index("Lahore"))
# Replace a substring in a string
print(phrase.replace("Lahore", "Karachi"))

# working with numbers
my_num = 5
print(my_num)
# type conversion 
print(str(my_num), "this is my favtore number")
# for absulte values use (abs) function 
num = -5 
print(abs(num))
# pow(x, y) returns x**y; with 3 args it does (x**y) % mod efficiently.
base = 2
exp = 5
mod = 3
print(pow(base, exp))         # 2**5 = 32
print(pow(base, exp, mod))    # (2**5) % 3 = 2
# round function 
num = -5 
print(round(3.7))
# floor(x) rounds x down to the nearest whole number (int).
value = 3.7
print(math.floor(value))  # 3
value = -2.3
print(math.floor(value))  # -3 because it rounds down
# math.sqrt(x) returns the square root of x
value = 49
print(math.sqrt(value))  # 7.0

def demo_user_input() -> None:
    name = input("Enter your name: ")
    age = input("Enter your age : ")
    print("hello " + name + " " + "your age is " + age)

    # building a basic calculator
    num1 = float(input("First number: "))
    op = input("Operator (+, -, *, /): ").strip()
    num2 = float(input("Second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(num1 / num2)
    else:
        print("Unknown operator.")


def greet(name: str, age: int) -> str:
    """Type-hinted greeting example."""
    return f"Hello {name}, you are {age} years old!"


def http_status(status: int) -> str:
    """Match/case demo."""
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case _:
            return "Unknown Error"


def fetch_sample_post() -> Any:
    """Fetch sample data with error handling."""
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1", timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        return {"error": str(exc)}


def simple_greet(name: str) -> str:
    """Return a friendly greeting using an f-string."""
    return f"Hi {name}, welcome back!"


def run_demos() -> None:
    # original print/loop demos
    print("Hello, World!")
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a + b

    phrase = "Punjab univeristy Lahore"
    print(phrase)
    print(phrase + " is a good university")
    print(phrase.upper())
    print(phrase.lower())
    print(phrase.isupper())
    print(phrase.islower())
    print(phrase.upper().isupper())
    print(phrase.lower().islower())
    print(phrase.upper().isupper())
    print(len(phrase))
    for idx in range(9):
        print(phrase[idx])
    print(phrase.index("Lahore"))
    print(phrase.replace("Lahore", "Karachi"))

    my_num = 5
    print(my_num)
    print(str(my_num), "this is my favtore number")
    num = -5
    print(abs(num))
    base = 2
    exp = 5
    mod = 3
    print(pow(base, exp))
    print(pow(base, exp, mod))
    print(round(3.7))
    value = 3.7
    print(math.floor(value))
    value = -2.3
    print(math.floor(value))
    value = 49
    print(math.sqrt(value))

    demo_user_input()

    print(greet("Ali", 25))
    print(http_status(404))
    print(http_status(500))

    data = fetch_sample_post()
    print(data)

    print(simple_greet("Alisha"))
    numbers = [2, 4, 6]
    if (total := sum(numbers)) > 10:
        print(f"Walrus says total {total} is greater than 10!")
    else:
        print(f"Total {total} is not greater than 10.")

    rprint("[bold green]Success![/bold green] 🎉")


if __name__ == "__main__":
    run_demos()
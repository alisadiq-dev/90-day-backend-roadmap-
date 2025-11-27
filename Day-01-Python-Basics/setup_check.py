 # backend_journey/day01/setup_check.py

import sys
from rich import print as rprint
import requests

# 1. Print Python version
rprint(f"[bold green]Python Version:[/bold green] {sys.version.split()[0]}")

# 2. Prove requests & rich imported successfully
rprint("[bold cyan]✓ requests & rich imported successfully![/bold cyan]")

# 3. Factorial function with type hints
def factorial(n: int) -> int:
    """Calculate factorial using recursion with type hints"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Using walrus operator once while keeping the value
num = 7
if (result := factorial(num)) > 0:
    rprint(f"[bold yellow]Factorial of {num} = {result:,}[/bold yellow]")
else:
    rprint("[bold yellow]Factorial result is zero[/bold yellow]")

# 4. Save everything to output.txt
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(f"Python Version: {sys.version.split()[0]}\n")
    file.write(f"requests & rich: Successfully imported\n")
    file.write(f"Factorial of {num} = {result:,}\n")
    file.write("Day 01 Completed – Modern Python + venv ready! \n")

rprint("[bold magenta]output.txt created successfully![/bold magenta]")
rprint("[bold red]Day 01 100% DONE! Push to GitHub now 🚀[/bold red]")
# cli.py
# Yeh file terminal ko sundar banayegi – colors, tables, emojis

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from .manager import TaskManager
from .task import Priority, Category

from .export import export_to_csv

console = Console()

def main():
    manager = TaskManager()

    while True:
        console.print("\n[bold magenta]=== My Todo App ===[/bold magenta]")
        console.print("1. Add Task")
        console.print("2. View All Tasks")
        console.print("3. Complete Task")
        console.print("4. Delete Task")
        console.print("5. Export Tasks to CSV")
        console.print("6. Exit")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            title = Prompt.ask("[green]Task title[/green]")
            priority_str = Prompt.ask("[yellow]Priority[/yellow] (high/medium/low)", default="medium")
            priority = Priority.HIGH if priority_str.lower() == "high" else Priority.MEDIUM if priority_str.lower() == "medium" else Priority.LOW
            category_str = Prompt.ask("[cyan]Category[/cyan] (work/personal/health/study/other)", default="other")
            category = Category[category_str.upper()]
            manager.add_task(title, priority, category)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = IntPrompt.ask("[blue]Enter task ID to complete[/blue]")
            manager.complete_task(task_id)

        elif choice == "4":
            task_id = IntPrompt.ask("[red]Enter task ID to delete[/red]")
            manager.delete_task(task_id)

        elif choice == "5":
            export_to_csv(manager.tasks)

        elif choice == "6":
            console.print("[bold green]Goodbye! Have a productive day![/bold green]")
            break

if __name__ == "__main__":
    main()
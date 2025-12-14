
import csv
from .task import Task
from typing import List

def export_to_csv(tasks: List[Task], filename: str = "my_tasks.csv") -> None:
    # Agar koi task nahi to kuch mat karo
    if not tasks:
        print("no task found for export")
        return

    # CSV file ke columns
    fieldnames = [
        "ID", "Title", "Priority", "Category", 
        "Status", "Created At", "Due Date", "Tags"
    ]

    try:
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()  # pehli line mein headings

            for task in tasks:
                writer.writerow({
                    "ID": task.id,
                    "Title": task.title,
                    "Priority": task.priority.name,
                    "Category": task.category.value,
                    "Status": "Completed" if task.completed else "Pending",
                    "Created At": task.created_at.strftime("%Y-%m-%d %H:%M"),
                    "Due Date": task.due_date.strftime("%Y-%m-%d") if task.due_date else "",
                    "Tags": ", ".join(task.tags) if task.tags else ""
                })
        print(f"Tasks exported to {filename} successfully")
    except Exception as e:
        print(f"Export failed: {e}")
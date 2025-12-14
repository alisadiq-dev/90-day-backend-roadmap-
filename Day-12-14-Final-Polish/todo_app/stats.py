

from .task import Task
from typing import List

def show_statistics(tasks: List[Task]) -> None:
    if not tasks:
        print("no task found")
        return

    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    pending = total - completed
    percentage = (completed / total) * 100 if total > 0 else 0
    
    print(f"Total Tasks     : {total}")
    print(f"Completed       : {completed}")
    print(f"Pending         : {pending}")
    print(f"Completion Rate : {percentage:.1f}%")

    # Priority wise count
    for pri in ["HIGH", "MEDIUM", "LOW"]:
        count = sum(1 for t in tasks if t.priority.name == pri)
        print(f"  {pri:6} : {count} tasks")

    # Category wise count
    categories = {}
    for t in tasks:
        cat = t.category.value
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in categories.items():
        print(f"  {cat:10} : {count} tasks")
# storage.py
# Yeh file saare tasks ko "tasks.json" mein save karegi aur load karegi
# Program band karne ke baad bhi data rahega

import json
from .task import Task, Priority, Category
from typing import List
from datetime import datetime

FILENAME = "tasks.json"

def save_tasks(tasks: List[Task]) -> None:
    # Task object ko simple dict mein convert karo
    data = []
    for task in tasks:
        task_dict = {
            "id": task.id,
            "title": task.title,
            "priority": task.priority.name,      # HIGH, MEDIUM, LOW string mein
            "category": task.category.value,     # Work, Personal etc
            "completed": task.completed,
            "created_at": task.created_at.isoformat(),
            "due_date": task.due_date.isoformat() if task.due_date else None,
            "tags": task.tags
        }
        data.append(task_dict)

    try:
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Tasks saved to {FILENAME}")
    except Exception as e:
        print(f"Save failed: {e}")

def load_tasks() -> List[Task]:
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        
        tasks = []
        for item in data:
            # String se wapas Enum banao
            priority = Priority[item["priority"]]
            category = Category(item["category"])

            task = Task(
                title=item["title"],
                priority=priority,
                category=category,
                completed=item["completed"],
                tags=item.get("tags", [])
            )
            task.id = item["id"]
            task.created_at = datetime.fromisoformat(item["created_at"])
            if item["due_date"]:
                task.due_date = datetime.fromisoformat(item["due_date"])
            
            tasks.append(task)
        
        print(f"Loaded {len(tasks)} tasks from {FILENAME}")
        return tasks
    except FileNotFoundError:
        print("No tasks file found – starting fresh!")
        return []
    except Exception as e:
        print(f"Load failed: {e}")
        return []
"""
- This file will load and save data from tasks.json 
"""

import json
from models import Task
from typing import List 

def save_tasks(tasks: List[Task], filename: str = "tasks.json") -> None:

    data = []
    for task in tasks:
        data.append({
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "created_at": task.created_at,
            "updated_at": task.updated_at,
            "note": task.note
        })
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks(filename: str = "tasks.json") -> List[Task]:
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        tasks = []
        for task_data in data:
            task = Task(
                id=task_data["id"],
                title=task_data["title"],
                status=task_data["status"],
                created_at=task_data["created_at"],
                updated_at=task_data["updated_at"],
                note=task_data["note"]
            )
            tasks.append(task)
        # print("Tasks loaded successfully.") # Optional:  
        return tasks
    except FileNotFoundError:
        # print("No tasks found.") # Optional:  
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
    
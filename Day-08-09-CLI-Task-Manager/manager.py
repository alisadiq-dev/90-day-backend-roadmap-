# in this file we have add, delete, update, list, complete, and load tasks

from models import Task
from storage import save_tasks, load_tasks
from typing import List
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = load_tasks()
        self.next_id = self.get_next_id()

    def get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title: str, note: str | None = None) -> None:
        new_task = Task(
            id=self.next_id,
            title=title,
            note=note,
            status="pending",
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.tasks.append(new_task)
        self.next_id += 1
        save_tasks(self.tasks)
        print(f"task added ID: {new_task.id}")

    def list_tasks(self) -> None:
        if not self.tasks:
            print("No tasks found.")
            return
        
        for task in self.tasks:
            print(task)
            if task.note:
                print(f"   Note: {task.note}")

    def complete_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                task.status = "completed"
                task.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(self.tasks)
                print(f"Task {task_id} completed.")
                return
        print(f"Task {task_id} not found.")
                 
    def delete_task(self, task_id: int) -> None:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                removed = self.tasks.pop(i)
                save_tasks(self.tasks)
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")
                 
        
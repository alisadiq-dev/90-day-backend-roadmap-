from .task import Task, Priority, Category
from datetime import datetime
from typing import List, Optional
from .storage import save_tasks, load_tasks

class TaskManager:
    def __init__(self):
        self.tasks : List[Task] = load_tasks()
        self.next_id : int = (max(t.id for t in self.tasks) + 1) if self.tasks else 1

    def add_task(self, title : str, priority : Priority = Priority.MEDIUM, category : Category = Category.OTHER, 
     due_date : Optional[str] = None, tags : List[str] = None) -> None:
        
        task = Task(
            title = title,
            priority = priority,
            category = category,
             
        )
        if due_date:
            task.due_date = datetime.strptime(due_date, '%Y-%m-%d')

        if tags:
            task.tags = tags

        task.id = self.next_id
        self.tasks.append(task) 
        self.next_id += 1
        save_tasks(self.tasks)
        print(f"Task added: {task.id}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return

        for task in sorted(self.tasks):
            print(f"{task.id}. {task}")

    def complete_task(self, task_id : int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                save_tasks(self.tasks)
                print(f"Task {task_id} completed")
                return
        print(f"Task {task_id} not found")



    def delete_task(self, task_id : int):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                removed_task = self.tasks.pop(i)
                save_tasks(self.tasks)
                print(f"Task {removed_task.id} deleted")
                return
        print(f"Task {task_id} not found")

    def filter_tasks(self, priority : Optional[Priority] = None, category : Optional[Category] = None):
        
        result = self.tasks

        if priority:
            result = [task for task in result if task.priority == priority]

        if category:
            result = [task for task in result if task.category == category]

        return result



     

        
        
  
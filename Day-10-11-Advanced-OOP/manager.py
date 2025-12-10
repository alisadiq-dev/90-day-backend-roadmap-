""" 
This file is the "brain" of our todo app.
What it does:
- Keeps all tasks in a list (like a notebook)
- Adds new tasks
- Shows the full list of tasks
- Marks a task as "completed"
- Deletes a task when you don't want it anymore
In short:  
All the main work happens here.  
Without this file, nothing works it controls everything!
"""

from task import Task
from typing import List, Protocol

# for strategy pattern 
class SortStrategy(Protocol):
    def sort(self, tasks: List[Task]) -> List[Task]:
        pass
# sort by pripority 
class SortByPriority():
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks)
# sort by date 
class SortByDate:
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda t: t.created_at, reverse=True)

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
        self.sorter: SortStrategy = SortByPriority()


    def add_task(self, title, priority = 3):
        task = Task(title = title, priority=priority)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        print(f"task added: {title}")

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task marked as completed: {self.tasks[index].title}")

    def  __iter__(self):
        sorted_tasks = self.sorter.sort(self.tasks)
        return iter(sorted_tasks)

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, index):
        return self.tasks[index]

    def set_sorting_strategy(self, sorter: sortStrategy):
        self.sorter = sorter
        print("sorting strategy changed")
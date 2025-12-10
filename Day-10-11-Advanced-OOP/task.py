"""
This file is the blueprint of the Task 
— it defines what a task contains and how it should behave in Python, such as how it sorts, prints, and compares
"""
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(order=True)
class Task:
    sort_index: datetime = field(init=False, repr = False)
    title : str
    priority : int = 3
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    due_date: datetime | None = None
    
    def __post_init__(self):
        self.sort_index = self.created_at

    def __str__(self):
        status = "Done" if self.completed else "pending"
        return f"[{self.priority}] {self.title} {status}"

    def __repr__(self):
        return f"task('{self.title}', priority={self.priority})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.title == other.title

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.created_at < other.created_at
        return self.priority < other.priority
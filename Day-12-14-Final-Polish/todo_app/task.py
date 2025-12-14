from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, List


# Priority levels - HIGH, MEDIUM, LOW
class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

# Categories (type of task)
class Category(Enum):
    WORK = "Work"
    PERSONAL = "Personal"
    SCHOOL = "School"
    HEALTH = "Health"
    STUDY = "Study"
    OTHER = "Other"

# main task class 
"""
1 task anme 
2 default medium 
3 default other 
4 default false 
5 default now 
6 default none 
7 default empty list 
"""

@dataclass
class Task:
    title : str
    id : int = 0
    priority : Priority = Priority.MEDIUM
    category : Category = Category.OTHER
    completed : bool = False
    created_at : datetime = field(default_factory=datetime.now)
    due_date : Optional[datetime] = None
    tags : List[str] = field(default_factory=list)


    def __str__(self):
        status = "Done" if self.completed else "Pending"
        due = f" | due: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else ""
        tags = f" | tags: {', '.join(self.tags)}" if self.tags else ""
        return f"[{self.priority.name}] {self.title} | {status} | {due}{tags}"
    
    def __lt__(self, other):
        return self.priority.value < other.priority.value
  



 
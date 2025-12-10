# Day 10-11 – Advanced OOP Patterns (Magic Methods + Strategy Pattern)

Today I made my Task class and TaskManager **super smart** – just like real Python objects!

### What I Learned & Did
- Added **magic methods** to Task:
  - `print(task)` → shows nice text
  - `task1 < task2` → compares by priority
  - `len(manager)` → tells how many tasks
  - `for task in manager:` → works directly!

- Added **Strategy Pattern**:
  - Can sort tasks by **priority** OR by **date**
  - Just one line change → sorting style changes!

### Files
- `task.py` → Task class with magic methods
- `manager.py` → Controls all tasks + smart sorting
- `main.py` → Test everything

### How to Run
```bash
python main.py
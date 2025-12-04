# CLI Task Manager – My First Real Project

This is a simple **command line todo app** I built in Day 8-9.

### Features
- Add new tasks
- View all tasks
- Mark task as complete
- Delete task
- All tasks saved in `tasks.json` → data never lost even after closing

### How to Run
Open terminal and run these commands:

```bash
# Add task
python main.py add "Buy milk"
python main.py add "Call mom" --note "Evening"

# See all tasks
python main.py list

# Mark task as done
python main.py complete 1

# Delete task
python main.py delete 2
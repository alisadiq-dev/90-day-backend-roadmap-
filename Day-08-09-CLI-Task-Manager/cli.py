import argparse
from manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")

    subparsers = parser.add_subparsers(dest="command")

    # add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--note", "-n", help="Task note")


    #list command 
    subparsers.add_parser("list", help="List all tasks")

    # complete command 
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument("task_id", type=int, help="Task ID")

    # for delete command 

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task ID")

    args = parser.parse_args()

    # start TaskManger 

    manager = TaskManager()

    # add task 

    if args.command == "add":
        manager.add_task(args.title, args.note)
    elif args.command == "list":
        manager.list_tasks()
    elif args.command == "complete":
        manager.complete_task(args.task_id)
    elif args.command == "delete":
        manager.delete_task(args.task_id)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
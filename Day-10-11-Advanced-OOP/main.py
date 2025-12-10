from manager import TaskManager, SortByPriority, SortByDate

manager = TaskManager()
 
# add task 

manager.add_task("Buy Milk", 1)
manager.add_task("Namaz time", 5)
manager.add_task("learn FastAPI", 2)


print("sorted by priority")
for task in manager:
    print(task)

print("sort by date")
manager.set_sorting_strategy(SortByDate())
 for task in manager:
    print(task)
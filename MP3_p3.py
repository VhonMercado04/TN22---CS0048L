ToDoList = []

def add_task(task):
    ToDoList.append(task)
    print("\n",task,"is added to the list.")

def remove_task(task):
    try:
        ToDoList.remove(task)
        print("\n",task,"removed from the list.")
    
    except ValueError:
        print("\n",task,"is not found in the list.")    

def view_task():
    if not ToDoList:
        print("\nYour list is empty.")
    else: 
        print("\n----------------")
        print("Your To-Do list:")
        print("----------------")
        for num_list, list in enumerate(ToDoList):
            
            print((num_list + 1),".", list)
while True:
    print("\n=====================")
    print("-- To-Do list Menu --")
    print("=====================")

    print("  1. Add Task\n  2. Remove Task\n  3. View Task\n  4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("\nExiting program... Thank you\n")
        break
    
    if choice == 1:
        AddTask = input("Enter task to add: ")
        add_task(AddTask) 

    elif choice == 2:       
        RemoveTask = input("Enter task to remove: ")
        remove_task(RemoveTask)

    elif choice == 3:
        view_task()   

    else: 
        print("Invalid input")     
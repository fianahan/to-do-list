import json

tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["completed"] = True
        print("Task marked complete.")
    except:
        print("Invalid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f'Task "{removed["task"]}" deleted.')
    except:
        print("Invalid number.")

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print("Tasks saved.")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

def menu():
    load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Save tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            save_tasks()
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

menu()

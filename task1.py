import json
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

tasks = []

def add_task(title, description):
    task = Task(title, description)
    tasks.append(task)
    return "Task added successfully."

def update_task(title, new_title, new_description):
    for task in tasks:
        if task.title == title:
            task.title = new_title
            task.description = new_description
            return "Task updated successfully."
    return "Task not found."

def complete_task(title):
    for task in tasks:
        if task.title == title:
            task.is_completed = True
            return "Task marked as completed."
    return "Task not found."

def list_tasks():
    return json.dumps([vars(task) for task in tasks], indent=4)

def display_options():
    print("\nOptions:")
    print("1. Add a new task")
    print("2. Update an existing task")
    print("3. Mark a task as completed")
    print("4. List all tasks")
    print("5. Exit")

while True:
    display_options()
    option = input("Enter option (1-5): ")

    if option == '1':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        print(add_task(title, description))

    elif option == '2':
        title = input("Enter current task title: ")
        new_title = input("Enter new task title: ")
        new_description = input("Enter new task description: ")
        print(update_task(title, new_title, new_description))

    elif option == '3':
        title = input("Enter task title to mark as completed: ")
        print(complete_task(title))

    elif option == '4':
        print(list_tasks())

    elif option == '5':
        break

    else:
        print("Invalid option.")

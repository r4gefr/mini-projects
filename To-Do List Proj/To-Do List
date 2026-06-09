print("Welcome to Your To-Do List!")

tasks = []
commands = {
    "1": "Add Task",
    "2": "View Tasks",
    "3": "Toggle Complete",
    "4": "Delete Task",
    "5": "Exit"
}

def show_menu():
    print("\n--- Menu ---")
    for key, value in commands.items():
        print(f"  {key}. {value}")

def display_tasks(show_status=True):
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "❌"
        if show_status:
            print(f"  {i}. {task['task']} [{status}]")
        else:
            print(f"  {i}. {task['task']}")

def get_task_number(prompt):
    """Returns a valid task index or None on failure."""
    try:
        num = int(input(prompt))
        if 1 <= num <= len(tasks):
            return num
        else:
            print(f"Please enter a number between 1 and {len(tasks)}.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

while True:
    show_menu()
    command = input("\nEnter a command (1-5): ").strip()

    if command == "1":
        task = input("Enter the task: ").strip()
        if not task:
            print("Task cannot be empty.")
        else:
            tasks.append({"task": task, "done": False})
            print("✅ Task added successfully!")

    elif command == "2":
        if not tasks:
            print("No tasks to show.")
        else:
            print("\nYour tasks:")
            display_tasks()

    elif command == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            print("\nYour tasks:")
            display_tasks()
            num = get_task_number("Enter task number to toggle: ")
            if num:
                task = tasks[num - 1]
                task["done"] = not task["done"]   # Toggle instead of one-way set
                state = "complete ✔" if task["done"] else "incomplete ❌"
                print(f"Task marked as {state}.")

    elif command == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour tasks:")
            display_tasks()                         # Now shows status consistently
            num = get_task_number("Enter task number to delete: ")
            if num:
                removed = tasks.pop(num - 1)
                print(f"Deleted: '{removed['task']}'")

    elif command == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid command. Please try again.")
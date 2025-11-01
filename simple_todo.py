# simple_todo.py

# --- To-Do List App (Beginner Level) ---

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    try:
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("⚠️  Task cannot be empty.\n")

def delete_task(tasks):
    """Delete a task by number."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️  Deleted task: {removed}\n")
        else:
            print("⚠️  Invalid task number.\n")
    except ValueError:
        print("⚠️  Please enter a valid number.\n")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️  Invalid option.\n")

if __name__ == "__main__":
    main()
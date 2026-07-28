def display_menu():
    print("\n" + "=" * 40)
    print("         TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("=" * 40)


def add_task(tasks):
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        print(f"✅ Task '{task}' added successfully.")
    else:
        print("❌ Task cannot be empty.")


def view_tasks(tasks):
    print("\n------ YOUR TASKS ------")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = []

    while True:
        display_menu()

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            print("\nThank you for using the To-Do List App.")
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
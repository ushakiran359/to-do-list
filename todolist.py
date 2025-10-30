# Simple To-Do List in Python

todo_list = []

while True:
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if not todo_list:
            print("No tasks yet!")
        else:
            print("Your Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == '3':
        if not todo_list:
            print("No tasks to remove!")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(todo_list):
                removed = todo_list.pop(task_no - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")

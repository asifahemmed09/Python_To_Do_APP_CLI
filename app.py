def show_todos(todos):
    print("\nYour To-Do List:")
    if not todos:
        print("No to-do items found.")
    else:
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo}")


def to_do():
    print("---- Welcome to your To-Do List ----")
    todos = []

    try:
        todo_count = int(input("How many to-do's do you have? \n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for i in range(1, todo_count + 1):
        todo = input(f"Enter to-do {i}: ")
        todos.append(todo)

    while True:
        show_todos(todos)

        print("\nChoose an option:")
        print("1. Add a to-do")
        print("2. Update a to-do")
        print("3. Remove a to-do")
        print("4. View to-do's")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo = input("Enter the to-do: ")
            todos.append(todo)
            print(f"{todo} added successfully.")

        elif choice == "2":
            if not todos:
                print("No items to update.")
                continue

            try:
                index = int(input("Enter the index: ")) - 1
                if 0 <= index < len(todos):
                    new_todo = input("Enter updated to-do: ")
                    todos[index] = new_todo
                    print("Updated successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            if not todos:
                print("No items to remove.")
                continue

            try:
                index = int(input("Enter the index: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    print(f"{removed} removed successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            show_todos(todos)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


to_do()
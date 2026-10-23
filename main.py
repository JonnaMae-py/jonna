
from todo import add_todo, view_todos, complete_todo, delete_todo


def main():
    while True:
        print("\n===== TO-DO LIST SYSTEM =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todos()
        elif choice == "3":
            complete_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            print("Thank you for using the To-Do List System!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()

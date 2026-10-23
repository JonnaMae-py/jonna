
from database.database import get_connection


def add_todo():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO todos (title, description)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (title, description))
        connection.commit()

        print("Task added successfully!")

    except Exception as error:
        print("Error adding task:", error)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def view_todos():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, title, description, completed FROM todos ORDER BY id"
        )
        todos = cursor.fetchall()

        print("\n===== YOUR TASKS =====")

        if not todos:
            print("No tasks found.")
            return

        for todo in todos:
            status = "Completed" if todo[3] else "Pending"
            print(f"\nID: {todo[0]}")
            print(f"Title: {todo[1]}")
            print(f"Description: {todo[2] or 'None'}")
            print(f"Status: {status}")

    except Exception as error:
        print("Error viewing tasks:", error)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def complete_todo():
    try:
        task_id = int(input("Enter task ID to complete: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE todos SET completed = TRUE WHERE id = %s",
            (task_id,)
        )
        connection.commit()

        if cursor.rowcount > 0:
            print("Task marked as completed!")
        else:
            print("Task ID not found.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid number.")
    except Exception as error:
        print("Error updating task:", error)


def delete_todo():
    try:
        task_id = int(input("Enter task ID to delete: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM todos WHERE id = %s", (task_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Task deleted successfully!")
        else:
            print("Task ID not found.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid number.")
    except Exception as error:
        print("Error deleting task:", error)

from task_manager import TaskManager
import file_ops
import db_ops  # Import the database operations

def main():
    manager = TaskManager()
    
    # Load tasks from both JSON file and PostgreSQL
    file_ops.load_tasks(manager)
    db_ops.load_tasks_from_db(manager)

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. Mark Task as Undone")
        print("5. List All Tasks")
        print("6. List Completed Tasks")
        print("7. Save and Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            manager.add_task(description)  # Add the task

        elif choice == '2':
            manager.list_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            manager.remove_task(index)

        elif choice == '3':
            manager.list_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            manager.mark_task_done(index)

        elif choice == '4':
            manager.list_tasks()
            index = int(input("Enter task number to mark as undone: ")) - 1
            manager.mark_task_undone(index)

        elif choice == '5':
            manager.list_tasks()

        elif choice == '6':
            manager.list_completed_tasks()

        elif choice == '7':
            # Save tasks to both JSON file and PostgreSQL
            file_ops.save_tasks(manager)  # Save to JSON file
            db_ops.save_tasks_to_db(manager)  # Save to PostgreSQL
            print("Tasks saved to file.")
            print("Tasks saved to database.")
            break

if __name__ == "__main__":
    main()

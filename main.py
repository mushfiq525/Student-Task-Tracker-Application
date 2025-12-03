from task_manager import TaskManager

manager = TaskManager("tasks.json")

while True:
    print("===== Student Task Tracker =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter choice: ").strip()

    if choice == "1":
        title = input("Task Title: ").strip()
        description = input("Task Description: ").strip()

        if title == "":
            print("Title can't be empty. Task not added.")
        else:
            manager.add_task(title, description)
    
    elif choice == "2":
        manager.view_tasks()
    
    elif choice == "3":
        if not manager.tasks:
            print("No tasks available to update. The task list is empty.")
        else:
            # Show all tasks with numbers
            manager.view_tasks()
            
            try:
                idx = int(input("Enter the number of the task to update: ").strip()) - 1
                if 0 <= idx < len(manager.tasks):
                    new_title = input("New Title: ").strip()
                    new_desc = input("New Description: ").strip()
                    
                    if new_title:
                        manager.tasks[idx].title = new_title
                    if new_desc:
                        manager.tasks[idx].description = new_desc
                    
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a numeric value.")

    
    elif choice == "4":
        if not manager.tasks:
            print("No tasks available to delete. The task list is empty.")
        else:
            # Show all tasks with numbers
            manager.view_tasks()
            
            try:
                idx = int(input("Enter the number of the task to delete: ").strip()) - 1  # convert to 0-based index
                if 0 <= idx < len(manager.tasks):
                    confirm = input(f"Are you sure you want to delete '{manager.tasks[idx].title}'? (y/n): ").strip().lower()
                    if confirm == "y":
                        removed = manager.tasks.pop(idx)
                        print(f"Task '{removed.title}' deleted successfully!")
                    else:
                        print("Delete cancelled.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a numeric value.")
    
    elif choice == "5":
        print("Saving tasks and exiting.")
        manager.save_to_file()
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    
    print()
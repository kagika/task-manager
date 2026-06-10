"""
main.py - Entry point for the Task Manager application.
 
Run this script from the project root:
    python main.py
"""
 
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)
 
 
def print_separator(char="─", width=50):
    print(char * width)
 
 
def display_task(index, task):
    status = "Complete" if task["completed"] else "Pending"
    print(f"  {index}. [{status}] {task['title']}")
    print(f"       Description : {task['description']}")
    print(f"       Due Date     : {task['due_date']}")
 
 
def display_menu():
    print_separator()
    print("       TASK MANAGER")
    print_separator()
    print("  1. Add a new task")
    print("  2. Mark a task as complete")
    print("  3. View pending tasks")
    print("  4. View all tasks")
    print("  5. Track progress")
    print("  6. Exit")
    print_separator()
 
 
def handle_add_task(tasks):
    print("\n-- Add New Task --")
    title       = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date    = input("Enter due date (YYYY-MM-DD): ").strip()
 
    success, message = add_task(tasks, title, description, due_date)
    print(f"\n{message}")
 
 
def handle_mark_complete(tasks):
    print("\n-- Mark Task as Complete --")
    if not tasks:
        print("No tasks available.")
        return
 
    title = input("Enter the title of the task to complete: ").strip()
    success, message = mark_task_as_complete(tasks, title)
    print(f"\n{message}")
 
 
def handle_view_pending(tasks):
    print("\n-- Pending Tasks --")
    pending = view_pending_tasks(tasks)
 
    if not pending:
        print("No pending tasks! All done.")
        return
 
    print(f"{len(pending)} pending task(s):\n")
    for i, task in enumerate(pending, start=1):
        display_task(i, task)
 
 
def handle_view_all(tasks):
    print("\n-- All Tasks --")
    if not tasks:
        print("No tasks have been added yet.")
        return
 
    print(f"{len(tasks)} task(s) total:\n")
    for i, task in enumerate(tasks, start=1):
        display_task(i, task)
 
 
def handle_progress(tasks):
    print("\n-- Progress Tracker --")
    percentage = calculate_progress(tasks)
 
    if not tasks:
        print("No tasks yet. Add some tasks to track progress.")
        return
 
    bar_length   = 30
    filled       = int(bar_length * percentage / 100)
    progress_bar = "#" * filled + "-" * (bar_length - filled)
 
    print(f"Progress: [{progress_bar}] {percentage:.1f}%")
 
 
def main():
    tasks = []
 
    print("\nWelcome to the Task Manager!")
 
    while True:
        print()
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
 
        if choice == "1":
            handle_add_task(tasks)
        elif choice == "2":
            handle_mark_complete(tasks)
        elif choice == "3":
            handle_view_pending(tasks)
        elif choice == "4":
            handle_view_all(tasks)
        elif choice == "5":
            handle_progress(tasks)
        elif choice == "6":
            print("\nGoodbye! Stay productive!\n")
            break
        else:
            print("\nInvalid option. Please enter a number between 1 and 6.")
 
 
if __name__ == "__main__":
    main()
 
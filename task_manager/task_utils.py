"""
task_utils.py - Core task management functions for the Task Manager application.
"""

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        return False, str(e)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    return True, f"Task '{title}' added successfully!"


def mark_task_as_complete(tasks, title):
    if not title or not isinstance(title, str):
        return False, "Error: Please provide a valid task title."

    for task in tasks:
        if task["title"].lower() == title.lower():
            if task["completed"]:
                return False, f"Task '{task['title']}' is already marked as complete."
            task["completed"] = True
            return True, f"Task '{task['title']}' marked as complete!"

    return False, f"Error: No task found with the title '{title}'."


def view_pending_tasks(tasks):
    pending = [task for task in tasks if not task["completed"]]
    return pending


def calculate_progress(tasks):
    total = len(tasks)
    if total == 0:
        return 0.0

    completed = sum(1 for task in tasks if task["completed"])
    percentage = (completed / total) * 100
    return percentage